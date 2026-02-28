import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.services.workspace_service import (
    build_file_diff,
    create_workspace,
    save_workspace_version,
    update_file,
    workspace_mode_for_day,
)


def test_workspace_initialization_and_versioning():
    workspace = create_workspace(user_id="u1", course_slug="python-for-pentesters")
    assert workspace["files"]["main.py"]
    assert len(workspace["version_history"]) == 1

    update_file(workspace, "main.py", "print('v2')\n")
    snap = save_workspace_version(workspace, "After challenge pass")
    assert snap["version"] == 2
    assert len(workspace["version_history"]) == 2


def test_workspace_diff_and_mode():
    diff = build_file_diff("print('a')\n", "print('b')\n", "main.py")
    assert "a/main.py" in diff and "b/main.py" in diff

    assert not workspace_mode_for_day(10)["project_mode_enabled"]
    assert workspace_mode_for_day(61)["project_mode_enabled"]
    assert workspace_mode_for_day(91)["capstone_locked_mode"]
