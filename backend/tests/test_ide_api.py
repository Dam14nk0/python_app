import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app import create_app


def test_ide_run_and_check_return_workspace_metadata():
    app = create_app()
    client = app.test_client()

    run_resp = client.post(
        "/api/ide/run",
        json={"day_number": 92, "code": "print('x')", "stdin": "", "project_files": {"main.py": "print('x')"}},
    )
    assert run_resp.status_code == 200
    run_json = run_resp.get_json()
    assert run_json["workspace"]["project_mode_enabled"]
    assert run_json["workspace"]["capstone_locked_mode"]

    check_resp = client.post(
        "/api/ide/check",
        json={"day_number": 92, "expected_behavior": "ok", "project_files": {"main.py": "print('x')"}},
    )
    assert check_resp.status_code == 200
    check_json = check_resp.get_json()
    assert check_json["validation_scope"] == "project_files"
