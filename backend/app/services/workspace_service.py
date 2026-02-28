from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from datetime import datetime, timezone
from difflib import unified_diff


DEFAULT_FILES = {
    "main.py": "def main():\n    print('CodePath workspace ready')\n\nif __name__ == '__main__':\n    main()\n",
    "modules/__init__.py": "",
    "utils/__init__.py": "",
    "config.json": "{\n  \"target\": \"127.0.0.1\",\n  \"timeout\": 5\n}\n",
}


@dataclass
class WorkspaceSnapshot:
    version: int
    label: str
    created_at: str
    files: dict[str, str]


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def create_workspace(user_id: str, course_slug: str) -> dict:
    return {
        "user_id": user_id,
        "course_slug": course_slug,
        "files": deepcopy(DEFAULT_FILES),
        "version_history": [
            {
                "version": 1,
                "label": "Workspace initialized",
                "created_at": utc_now_iso(),
                "files": deepcopy(DEFAULT_FILES),
            }
        ],
        "last_modified": utc_now_iso(),
    }


def save_workspace_version(workspace: dict, label: str) -> dict:
    next_version = len(workspace["version_history"]) + 1
    snapshot = {
        "version": next_version,
        "label": label,
        "created_at": utc_now_iso(),
        "files": deepcopy(workspace["files"]),
    }
    workspace["version_history"].append(snapshot)
    workspace["last_modified"] = snapshot["created_at"]
    return snapshot


def update_file(workspace: dict, filename: str, content: str) -> None:
    workspace["files"][filename] = content
    workspace["last_modified"] = utc_now_iso()


def build_file_diff(previous: str, current: str, filename: str) -> str:
    return "\n".join(
        unified_diff(
            previous.splitlines(),
            current.splitlines(),
            fromfile=f"a/{filename}",
            tofile=f"b/{filename}",
            lineterm="",
        )
    )


def workspace_mode_for_day(day_number: int) -> dict:
    return {
        "project_mode_enabled": day_number >= 61,
        "capstone_locked_mode": day_number >= 91,
    }
