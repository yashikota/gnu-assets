import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
import watcher


@pytest.fixture
def projects_file(tmp_path):
    data = {"projects": [{"name": "sed"}, {"name": "grep"}]}
    f = tmp_path / "projects.yml"
    f.write_text(yaml.dump(data))
    return str(f)


def test_get_latest_github_release_filters_by_project():
    mock_res = MagicMock(returncode=0, stdout="sed-v4.9\ngrep-v3.11\nsed-v4.8\n")
    with patch("watcher.run_gh", return_value=mock_res):
        result = watcher.get_latest_github_release("yashikota/gnu-assets", "sed")
    assert result == "4.9"


def test_get_latest_github_release_uses_limit_1000():
    mock_res = MagicMock(returncode=0, stdout="sed-v4.9\n")
    with patch("watcher.run_gh", return_value=mock_res) as mock_gh:
        watcher.get_latest_github_release("yashikota/gnu-assets", "sed")
        args = mock_gh.call_args[0][0]
        assert "--limit" in args
        assert "1000" in args


def test_main_dispatch_failure_exits_nonzero(tmp_path, monkeypatch):
    monkeypatch.setenv("GITHUB_REPOSITORY", "yashikota/gnu-assets")
    monkeypatch.setattr(sys, "argv", ["watcher.py"])

    data = {"projects": [{"name": "sed"}]}
    pf = tmp_path / "projects.yml"
    pf.write_text(yaml.dump(data))

    with patch("watcher.get_latest_ftp_version", return_value="4.9"), \
         patch("watcher.get_latest_github_release", return_value="4.8"), \
         patch("watcher.run_gh", return_value=MagicMock(returncode=1, stderr="API error")), \
         patch("os.path.join", return_value=str(pf)):
        with pytest.raises(SystemExit) as exc_info:
            watcher.main(dry_run=False)
        assert exc_info.value.code != 0


def test_main_dry_run_does_not_dispatch(tmp_path, monkeypatch):
    monkeypatch.setenv("GITHUB_REPOSITORY", "yashikota/gnu-assets")
    monkeypatch.setattr(sys, "argv", ["watcher.py"])

    data = {"projects": [{"name": "sed"}]}
    pf = tmp_path / "projects.yml"
    pf.write_text(yaml.dump(data))

    with patch("watcher.get_latest_ftp_version", return_value="4.9"), \
         patch("watcher.get_latest_github_release", return_value="4.8"), \
         patch("watcher.run_gh") as mock_gh, \
         patch("os.path.join", return_value=str(pf)):
        watcher.main(dry_run=True)
        mock_gh.assert_not_called()
