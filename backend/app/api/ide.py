from flask import Blueprint, jsonify, request

from ..services.ide_service import check_code_mock, run_code_mock
from ..services.learning_engine_service import validate_workspace_challenge
from ..services.workspace_service import workspace_mode_for_day

ide_bp = Blueprint("ide", __name__)


@ide_bp.post("/ide/run")
def ide_run():
    payload = request.get_json(silent=True) or {}
    code = payload.get("code", "")
    stdin = payload.get("stdin", "")
    day_number = int(payload.get("day_number", 1))
    project_files = payload.get("project_files", {})

    result = run_code_mock(code=code, stdin=stdin)
    result["workspace"] = workspace_mode_for_day(day_number)
    result["project_files_count"] = len(project_files)

    return jsonify(result), 200


@ide_bp.post("/ide/check")
def ide_check():
    payload = request.get_json(silent=True) or {}
    expected_behavior = payload.get("expected_behavior", "")
    day_number = int(payload.get("day_number", 1))
    project_files = payload.get("project_files", {})
    file_requirements = payload.get("file_requirements", {})

    result = check_code_mock(expected_behavior)
    result["workspace"] = workspace_mode_for_day(day_number)
    result["project_files_count"] = len(project_files)
    if day_number >= 91:
        result["validation_scope"] = "project_files"

    if file_requirements:
        files_payload = [{"path": name, "content": content} for name, content in project_files.items()]
        result["file_validation"] = validate_workspace_challenge(files_payload, file_requirements)

    return jsonify(result), 200
