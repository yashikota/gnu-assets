import os
import sys
import pytest
from unittest.mock import patch, MagicMock, call

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))
import release


def test_check_existing_release_true():
    with patch('release.run_gh') as mock_gh:
        mock_gh.return_value = MagicMock(returncode=0)
        assert release.check_existing_release("hello-v2.12.1") is True
        mock_gh.assert_called_once_with(["release", "view", "hello-v2.12.1"], check=False)


def test_check_existing_release_false():
    with patch('release.run_gh') as mock_gh:
        mock_gh.return_value = MagicMock(returncode=1)
        assert release.check_existing_release("hello-v99.99") is False


def test_download_file_success():
    with patch('subprocess.run') as mock_run:
        mock_run.return_value = MagicMock(returncode=0)
        assert release.download_file("https://example.com/file.tar.gz", "file.tar.gz", retries=3) is True
        args = mock_run.call_args[0][0]
        assert args[0] == "curl"
        assert "file.tar.gz" in args
        assert "https://example.com/file.tar.gz" in args


def test_download_file_failure():
    with patch('subprocess.run') as mock_run:
        mock_run.return_value = MagicMock(returncode=1)
        assert release.download_file("https://example.com/file.tar.gz", "file.tar.gz") is False


def test_main_existing_release_skips(capsys):
    test_args = [
        "release.py",
        "--project", "hello",
        "--version", "2.12.1",
        "--assets", "dummy.tar.gz",
        "--download-url", "https://example.com/hello-2.12.1.tar.gz",
        "--tarball-name", "hello-2.12.1.tar.gz",
    ]
    with patch.object(sys, 'argv', test_args):
        with patch('release.check_existing_release', return_value=True):
            with pytest.raises(SystemExit) as exc_info:
                release.main()
            assert exc_info.value.code == 0
            assert "Skipping (immutable releases)" in capsys.readouterr().out


def test_main_creates_release_successfully(tmp_path):
    os.chdir(tmp_path)
    dummy_asset = tmp_path / "hello-2.12.1-linux-amd64.tar.gz"
    dummy_asset.write_text("fake tarball content")

    test_args = [
        "release.py",
        "--project", "hello",
        "--version", "2.12.1",
        "--assets", str(dummy_asset),
        "--download-url", "https://example.com/hello-2.12.1.tar.gz",
        "--tarball-name", "hello-2.12.1.tar.gz",
    ]

    with patch.object(sys, 'argv', test_args):
        with patch('release.check_existing_release', return_value=False):
            with patch('release.download_file', return_value=True):
                with patch('release.run_gh') as mock_gh:
                    mock_gh.return_value = MagicMock(returncode=0)
                    release.main()
                    create_call_args = mock_gh.call_args[0][0]
                    assert create_call_args[0] == "release"
                    assert create_call_args[1] == "create"
                    assert "hello-v2.12.1" in create_call_args
                    assert "hello 2.12.1" in create_call_args


def test_main_tag_format(tmp_path):
    os.chdir(tmp_path)
    dummy_asset = tmp_path / "sed-4.9-linux-amd64.tar.gz"
    dummy_asset.write_text("fake")

    test_args = [
        "release.py",
        "--project", "sed",
        "--version", "4.9",
        "--assets", str(dummy_asset),
        "--download-url", "https://example.com/sed-4.9.tar.gz",
        "--tarball-name", "sed-4.9.tar.gz",
    ]

    with patch.object(sys, 'argv', test_args):
        with patch('release.check_existing_release', return_value=False):
            with patch('release.download_file', return_value=True):
                with patch('release.run_gh') as mock_gh:
                    mock_gh.return_value = MagicMock(returncode=0)
                    release.main()
                    create_call_args = mock_gh.call_args[0][0]
                    assert "sed-v4.9" in create_call_args


def test_main_sig_download_failure_exits(tmp_path):
    os.chdir(tmp_path)
    test_args = [
        "release.py",
        "--project", "hello",
        "--version", "2.12.1",
        "--assets", "dummy.tar.gz",
        "--download-url", "https://example.com/hello-2.12.1.tar.gz",
        "--tarball-name", "hello-2.12.1.tar.gz",
    ]
    with patch.object(sys, 'argv', test_args):
        with patch('release.check_existing_release', return_value=False):
            # tarball DL succeeds, sig DL fails
            with patch('release.download_file', side_effect=[True, False]):
                with pytest.raises(SystemExit) as exc_info:
                    release.main()
                assert exc_info.value.code != 0


def test_main_concurrent_race_treated_as_success(tmp_path):
    os.chdir(tmp_path)
    dummy_asset = tmp_path / "hello-2.12.1-linux-amd64.tar.gz"
    dummy_asset.write_text("fake")

    test_args = [
        "release.py",
        "--project", "hello",
        "--version", "2.12.1",
        "--assets", str(dummy_asset),
        "--download-url", "https://example.com/hello-2.12.1.tar.gz",
        "--tarball-name", "hello-2.12.1.tar.gz",
    ]
    with patch.object(sys, 'argv', test_args):
        with patch('release.check_existing_release', side_effect=[False, True]):
            with patch('release.download_file', return_value=True):
                with patch('release.run_gh') as mock_gh:
                    # release create fails (race), but subsequent view succeeds
                    mock_gh.return_value = MagicMock(returncode=1, stdout="", stderr="already exists")
                    release.main()  # must not raise or exit nonzero
