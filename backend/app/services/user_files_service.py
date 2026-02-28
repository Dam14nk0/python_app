from __future__ import annotations

from datetime import datetime, timezone

DEFAULT_WORKSPACE_FILES = [
    {"path": "outputs/.gitkeep", "content": "", "updated_at": ""},
    {"path": "notes/todo.md", "content": "# Workspace tasks\n", "updated_at": ""},
]


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def normalize_files(files: list[dict]) -> list[dict]:
    stamp = now_iso()
    normalized = []
    for entry in files:
        normalized.append(
            {
                "path": entry["path"],
                "content": entry.get("content", ""),
                "updated_at": entry.get("updated_at", stamp),
            }
        )
    return normalized


def ensure_defaults(files: list[dict]) -> list[dict]:
    by_path = {f["path"]: f for f in files}
    for default in DEFAULT_WORKSPACE_FILES:
        if default["path"] not in by_path:
            by_path[default["path"]] = {
                "path": default["path"],
                "content": default["content"],
                "updated_at": now_iso(),
            }
    return list(by_path.values())


def upsert_file(files: list[dict], path: str, content: str) -> list[dict]:
    stamp = now_iso()
    updated = False
    next_files = []
    for file_entry in files:
        if file_entry["path"] == path:
            next_files.append({"path": path, "content": content, "updated_at": stamp})
            updated = True
        else:
            next_files.append(file_entry)
    if not updated:
        next_files.append({"path": path, "content": content, "updated_at": stamp})
    return next_files


def reset_workspace_files() -> list[dict]:
    return normalize_files(DEFAULT_WORKSPACE_FILES)
