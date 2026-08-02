import os
import sys
import tarfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
import build


def test_resolve_tarball_picks_first_available():
    def fake_urlopen(req, timeout=None):
        if "tar.xz" in req.full_url:
            return MagicMock(__enter__=lambda s: s, __exit__=MagicMock(return_value=False))
        raise Exception("not found")

    with patch("urllib.request.urlopen", side_effect=fake_urlopen):
        url, name = build.resolve_tarball("sed", "sed", "4.9")
    assert "tar.xz" in name
    assert "sed-4.9" in url


def test_resolve_tarball_raises_when_not_found():
    with patch("urllib.request.urlopen", side_effect=Exception("not found")):
        with pytest.raises(RuntimeError, match="No tarball found"):
            build.resolve_tarball("sed", "sed", "99.99")


def test_verify_gpg_skips_when_no_sig(tmp_path, capsys):
    tarball = tmp_path / "sed-4.9.tar.xz"
    tarball.write_bytes(b"fake")
    build.verify_gpg(tarball)
    assert "skipping GPG" in capsys.readouterr().out


def test_verify_gpg_fails_on_bad_sig(tmp_path):
    tarball = tmp_path / "sed-4.9.tar.xz"
    tarball.write_bytes(b"fake")
    sig = tmp_path / "sed-4.9.tar.xz.sig"
    sig.write_bytes(b"bad sig")

    with patch("build.run") as mock_run:
        mock_run.return_value = MagicMock(returncode=1)
        with pytest.raises(RuntimeError, match="GPG verification FAILED"):
            build.verify_gpg(tarball)


# --- verify_binary ---

def test_verify_binary_linux_unexpected_ldd_failure_raises(tmp_path):
    binary = tmp_path / "myscript"
    binary.write_bytes(b"#!/bin/sh\necho hi")

    with patch("platform.system", return_value="Linux"), \
         patch("build.run", return_value=MagicMock(
             returncode=1,
             stdout="",
             stderr="ldd: ./myscript: No such file or directory\n",
         )):
        # returncode != 0 but no "not a dynamic executable" diagnostic → should raise
        with pytest.raises(RuntimeError, match="ldd failed unexpectedly"):
            build.verify_binary(binary)


def test_verify_binary_linux_static(tmp_path):
    binary = tmp_path / "sed"
    binary.write_bytes(b"ELF fake")

    with patch("platform.system", return_value="Linux"), \
         patch("build.run", return_value=MagicMock(
             returncode=1,
             stdout="not a dynamic executable\n",
             stderr="",
         )):
        build.verify_binary(binary)  # should not raise


def test_verify_binary_linux_musl_dynamic_raises(tmp_path):
    binary = tmp_path / "sed"
    binary.write_bytes(b"ELF fake")

    ldd_output = (
        "linux-vdso.so.1 => (0x...)\n"
        "/lib/ld-musl-x86_64.so.1 (0x...)\n"
    )
    with patch("platform.system", return_value="Linux"), \
         patch("build.run", return_value=MagicMock(returncode=0, stdout=ldd_output, stderr="")):
        with pytest.raises(RuntimeError, match="NOT fully static"):
            build.verify_binary(binary)


def test_verify_binary_linux_dynamic_raises(tmp_path):
    binary = tmp_path / "sed"
    binary.write_bytes(b"ELF fake")

    ldd_output = (
        "linux-vdso.so.1 => (0x...)\n"
        "libpcre.so.3 => /lib/x86_64-linux-gnu/libpcre.so.3\n"
        "libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6\n"
    )
    with patch("platform.system", return_value="Linux"), \
         patch("build.run", return_value=MagicMock(returncode=0, stdout=ldd_output, stderr="")):
        with pytest.raises(RuntimeError, match="NOT fully static"):
            build.verify_binary(binary)


def test_verify_binary_macos_system_only(tmp_path):
    binary = tmp_path / "sed"
    binary.write_bytes(b"Mach-O fake")

    otool_output = (
        "sed:\n"
        "\t/usr/lib/libSystem.B.dylib (compatibility ...)\n"
        "\t/usr/lib/libiconv.2.dylib (compatibility ...)\n"
    )
    with patch("platform.system", return_value="Darwin"), \
         patch("build.run", return_value=MagicMock(returncode=0, stdout=otool_output, stderr="")):
        build.verify_binary(binary)  # should not raise


def test_verify_binary_macos_unexpected_dep_raises(tmp_path):
    binary = tmp_path / "sed"
    binary.write_bytes(b"Mach-O fake")

    otool_output = (
        "sed:\n"
        "\t/usr/lib/libSystem.B.dylib (compatibility ...)\n"
        "\t/usr/local/lib/libpcre.dylib (compatibility ...)\n"
    )
    with patch("platform.system", return_value="Darwin"), \
         patch("build.run", return_value=MagicMock(returncode=0, stdout=otool_output, stderr="")):
        with pytest.raises(RuntimeError, match="unexpected libraries"):
            build.verify_binary(binary)


# --- package ---

def test_package_missing_binary_raises(tmp_path):
    install_dir = tmp_path / "_install" / "bin"
    install_dir.mkdir(parents=True)
    # "hello" binary is not created — should raise

    src_dir = tmp_path / "hello-2.12"
    src_dir.mkdir()

    with pytest.raises(RuntimeError, match="not found in install tree"):
        build.package("hello", "2.12", "hello", tmp_path / "_install", tmp_path, src_dir, verify=False)


def test_package_creates_tarball(tmp_path):
    install_dir = tmp_path / "_install" / "bin"
    install_dir.mkdir(parents=True)
    (install_dir / "sed").write_bytes(b"fake binary")

    src_dir = tmp_path / "sed-4.9"
    src_dir.mkdir()
    (src_dir / "COPYING").write_text("GPL")

    asset_path = build.package("sed", "4.9", "sed", tmp_path / "_install", tmp_path, src_dir, verify=False)

    assert asset_path.exists()
    with tarfile.open(asset_path) as t:
        names = t.getnames()
    assert any("sed" in n for n in names)
    assert any("COPYING" in n for n in names)


def test_package_writes_github_output(tmp_path, monkeypatch):
    install_dir = tmp_path / "_install" / "bin"
    install_dir.mkdir(parents=True)
    (install_dir / "sed").write_bytes(b"fake")

    src_dir = tmp_path / "sed-4.9"
    src_dir.mkdir()

    output_file = tmp_path / "github_output"
    output_file.write_text("")
    monkeypatch.setenv("GITHUB_OUTPUT", str(output_file))

    build.package("sed", "4.9", "sed", tmp_path / "_install", tmp_path, src_dir, verify=False)

    content = output_file.read_text()
    assert "asset_name=" in content
    assert "asset_path=" in content


def test_package_calls_verify(tmp_path):
    install_dir = tmp_path / "_install" / "bin"
    install_dir.mkdir(parents=True)
    (install_dir / "sed").write_bytes(b"fake")

    src_dir = tmp_path / "sed-4.9"
    src_dir.mkdir()

    with patch("build.verify_binary") as mock_verify:
        build.package("sed", "4.9", "sed", tmp_path / "_install", tmp_path, src_dir, verify=True)
        mock_verify.assert_called_once()


# --- main ---

def test_main_src_dir_from_tarball_stem(tmp_path):
    """Source directory is derived from the tarball stem, not a glob that could match stale dirs."""
    with patch("build.install_deps"), \
         patch("build.download"), \
         patch("build.verify_gpg"), \
         patch("build.run"), \
         patch("build.build") as mock_build, \
         patch("build.package") as mock_package:

        mock_package.return_value = tmp_path / "hello-2.12-linux-amd64.tar.gz"
        # Stale dir from a previous run — must NOT be picked
        stale = tmp_path / "hello-2.10"
        stale.mkdir()
        # Correct dir matching the requested version
        correct = tmp_path / "hello-2.12"
        correct.mkdir()
        (tmp_path / "hello-2.12.tar.gz").write_bytes(b"fake")

        build.main([
            "--project", "hello",
            "--version", "2.12",
            "--binary-names", "hello",
            "--work-dir", str(tmp_path),
            "--tarball-url", "https://example.com/hello-2.12.tar.gz",
        ])

        call_src_dir = mock_build.call_args[0][0]
        assert call_src_dir.name == "hello-2.12"


def test_main_uses_tarball_url(tmp_path):
    with patch("build.install_deps"), \
         patch("build.download"), \
         patch("build.verify_gpg"), \
         patch("build.run"), \
         patch("build.build") as mock_build, \
         patch("build.package") as mock_package:

        mock_package.return_value = tmp_path / "sed-4.9-linux-amd64.tar.gz"
        src_dir = tmp_path / "sed-4.9"
        src_dir.mkdir()
        (tmp_path / "sed-4.9.tar.xz").write_bytes(b"fake")

        build.main([
            "--project", "sed",
            "--version", "4.9",
            "--binary-names", "sed",
            "--work-dir", str(tmp_path),
            "--tarball-url", "https://example.com/sed-4.9.tar.xz",
        ])

        mock_build.assert_called_once()
        mock_package.assert_called_once()


def test_main_skip_verify_passes_flag(tmp_path):
    with patch("build.install_deps"), \
         patch("build.download"), \
         patch("build.verify_gpg"), \
         patch("build.run"), \
         patch("build.build"), \
         patch("build.package") as mock_package:

        mock_package.return_value = tmp_path / "sed-4.9-linux-amd64.tar.gz"
        src_dir = tmp_path / "sed-4.9"
        src_dir.mkdir()
        (tmp_path / "sed-4.9.tar.xz").write_bytes(b"fake")

        build.main([
            "--project", "sed",
            "--version", "4.9",
            "--binary-names", "sed",
            "--work-dir", str(tmp_path),
            "--tarball-url", "https://example.com/sed-4.9.tar.xz",
            "--skip-verify",
        ])

        _, kwargs = mock_package.call_args
        assert kwargs.get("verify") is False
