from __future__ import annotations

import json
from pathlib import Path

from flask import Blueprint, jsonify, request

from ..repositories.user_files_repo import get_user_files, save_user_files
from ..services.user_files_service import ensure_defaults, reset_workspace_files, upsert_file

workspace_bp = Blueprint("workspace", __name__)
SEED_PATH = Path(__file__).resolve().parents[2] / "seeds" / "python_for_pentesters_100_days.seed.json"


def _load_fixtures() -> list[dict]:
    if not SEED_PATH.exists():
        return []
    data = json.loads(SEED_PATH.read_text())
    return data.get("fixtures", [])


@workspace_bp.get("/workspace/files")
def workspace_files():
    user_id = request.args.get("user_id", "demo-user")
    course_slug = request.args.get("course_slug", "python-for-pentesters")
    doc = get_user_files(user_id, course_slug)
    doc["files"] = ensure_defaults(doc.get("files", []))
    return jsonify(doc), 200


@workspace_bp.post("/workspace/files")
def save_workspace_file():
    payload = request.get_json(silent=True) or {}
    user_id = payload.get("user_id", "demo-user")
    course_slug = payload.get("course_slug", "python-for-pentesters")
    path = payload.get("path")
    content = payload.get("content", "")

    if not path:
        return jsonify({"error": "path is required"}), 400

    current = get_user_files(user_id, course_slug)
    files = ensure_defaults(current.get("files", []))
    next_files = upsert_file(files, path, content)
    saved = save_user_files(user_id, course_slug, next_files)
    return jsonify(saved), 200


@workspace_bp.post("/workspace/reset")
def reset_workspace():
    payload = request.get_json(silent=True) or {}
    user_id = payload.get("user_id", "demo-user")
    course_slug = payload.get("course_slug", "python-for-pentesters")
    saved = save_user_files(user_id, course_slug, reset_workspace_files())
    return jsonify(saved), 200


@workspace_bp.get("/fixtures")
def fixtures_library():
    tool = request.args.get("tool")
    fixtures = _load_fixtures()
    if tool:
        fixtures = [fixture for fixture in fixtures if fixture.get("tool") == tool]
    return jsonify({"fixtures": fixtures, "count": len(fixtures)}), 200
