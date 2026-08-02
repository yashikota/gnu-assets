import os
import sys
import textwrap
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
import check


@pytest.fixture
def projects_file(tmp_path):
    data = {
        "projects": [
            {"name": "sed", "binary_names": "sed"},
            {"name": "src-highlite", "binary_names": "source-highlight", "tarball_prefix": "source-highlight"},
            {"name": "coreutils", "binary_names": "ls cat", "configure_args": "--without-gmp"},
        ]
    }
    f = tmp_path / "projects.yml"
    f.write_text(yaml.dump(data))
    return str(f)


def test_load_project_found(projects_file):
    p = check.load_project(projects_file, "sed")
    assert p["binary_names"] == "sed"


def test_load_project_not_found(projects_file):
    with pytest.raises(SystemExit):
        check.load_project(projects_file, "nonexistent")


def test_get_latest_ftp_version_force():
    result = check.get_latest_ftp_version("sed", "sed", force_version="4.9")
    assert result == "4.9"


def test_get_latest_ftp_version_parses_html():
    html = textwrap.dedent("""\
        sed-4.8.tar.xz
        sed-4.9.tar.xz
        sed-4.7.tar.gz
    """)

    mock_resp = MagicMock()
    mock_resp.read.return_value = html.encode()
    mock_resp.__enter__ = lambda s: s
    mock_resp.__exit__ = MagicMock(return_value=False)

    with patch("urllib.request.urlopen", return_value=mock_resp):
        result = check.get_latest_ftp_version("sed", "sed")
    assert result == "4.9"


def test_get_latest_ftp_version_returns_none_when_empty():
    mock_resp = MagicMock()
    mock_resp.read.return_value = b"<html>no tarballs here</html>"
    mock_resp.__enter__ = lambda s: s
    mock_resp.__exit__ = MagicMock(return_value=False)

    with patch("urllib.request.urlopen", return_value=mock_resp):
        result = check.get_latest_ftp_version("sed", "sed")
    assert result is None


def test_resolve_tarball_url_first_match():
    call_count = [0]

    def fake_urlopen(req, timeout=None):
        call_count[0] += 1
        if "tar.xz" in req.full_url:
            return MagicMock(__enter__=lambda s: s, __exit__=MagicMock(return_value=False))
        raise Exception("not found")

    with patch("urllib.request.urlopen", side_effect=fake_urlopen):
        url, name = check.resolve_tarball_url("sed", "sed", "4.9")
    assert "tar.xz" in name
    assert "4.9" in url


def test_resolve_tarball_url_fallback():
    def fake_urlopen(req, timeout=None):
        if "tar.gz" in req.full_url:
            return MagicMock(__enter__=lambda s: s, __exit__=MagicMock(return_value=False))
        raise Exception("not found")

    with patch("urllib.request.urlopen", side_effect=fake_urlopen):
        url, name = check.resolve_tarball_url("sed", "sed", "4.9")
    assert "tar.gz" in name


def test_resolve_tarball_url_not_found():
    with patch("urllib.request.urlopen", side_effect=Exception("not found")):
        url, name = check.resolve_tarball_url("sed", "sed", "4.9")
    assert url is None
    assert name is None


def test_get_latest_github_release_parses_tags():
    with patch("subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(
            returncode=0,
            stdout="sed-v4.8\nsed-v4.9\nsed-v4.7\n",
        )
        result = check.get_latest_github_release("sed")
    assert result == "4.9"


def test_get_latest_github_release_ignores_other_projects():
    with patch("subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(
            returncode=0,
            stdout="grep-v3.11\nsed-v4.9\n",
        )
        result = check.get_latest_github_release("sed")
    assert result == "4.9"


def test_get_latest_github_release_returns_none_on_empty():
    with patch("subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(returncode=0, stdout="")
        result = check.get_latest_github_release("sed")
    assert result is None


def test_get_latest_github_release_raises_on_gh_failure():
    with patch("subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(returncode=1, stdout="", stderr="API error")
        with pytest.raises(RuntimeError, match="gh release list failed"):
            check.get_latest_github_release("sed")


def test_main_has_new(projects_file, tmp_path):
    output_file = tmp_path / "github_output"
    output_file.write_text("")

    with patch("check.get_latest_ftp_version", return_value="4.9"), \
         patch("check.resolve_tarball_url", return_value=("https://example.com/sed-4.9.tar.xz", "sed-4.9.tar.xz")), \
         patch("check.get_latest_github_release", return_value="4.8"), \
         patch.dict(os.environ, {"GITHUB_OUTPUT": str(output_file)}):
        check.main(["--project", "sed", "--projects-file", projects_file])

    content = output_file.read_text()
    assert "has_new=true" in content
    assert "latest_version=4.9" in content
    assert "binary_names=sed" in content


def test_main_already_up_to_date(projects_file, tmp_path):
    output_file = tmp_path / "github_output"
    output_file.write_text("")

    with patch("check.get_latest_ftp_version", return_value="4.9"), \
         patch("check.resolve_tarball_url", return_value=("https://example.com/sed-4.9.tar.xz", "sed-4.9.tar.xz")), \
         patch("check.get_latest_github_release", return_value="4.9"), \
         patch.dict(os.environ, {"GITHUB_OUTPUT": str(output_file)}):
        check.main(["--project", "sed", "--projects-file", projects_file])

    content = output_file.read_text()
    assert "has_new=false" in content


def test_main_print_flag(projects_file, capsys):
    with patch("check.get_latest_ftp_version", return_value="4.9"), \
         patch("check.resolve_tarball_url", return_value=("https://example.com/sed-4.9.tar.xz", "sed-4.9.tar.xz")), \
         patch("check.get_latest_github_release", return_value="4.8"):
        check.main(["--project", "sed", "--projects-file", projects_file, "--print"])

    out = capsys.readouterr().out
    assert "has_new=true" in out
    assert "binary_names=sed" in out


def test_main_configure_args_included(projects_file, tmp_path):
    output_file = tmp_path / "github_output"
    output_file.write_text("")

    with patch("check.get_latest_ftp_version", return_value="9.5"), \
         patch("check.resolve_tarball_url", return_value=("https://example.com/coreutils-9.5.tar.xz", "coreutils-9.5.tar.xz")), \
         patch("check.get_latest_github_release", return_value=None), \
         patch.dict(os.environ, {"GITHUB_OUTPUT": str(output_file)}):
        check.main(["--project", "coreutils", "--projects-file", projects_file])

    content = output_file.read_text()
    assert "configure_args=--without-gmp" in content
