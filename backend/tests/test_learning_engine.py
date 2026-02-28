import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.services.learning_engine_service import (
    adaptive_retry_payload,
    can_complete_day,
    difficulty_for_day,
    is_day_unlocked,
    update_concept_tracking,
    validate_workspace_challenge,
)
from app.services.xp_service import calculate_awarded_xp, resolve_level_tag


def test_unlock_and_completion_rules():
    assert is_day_unlocked(1, [])
    assert is_day_unlocked(4, [1, 2, 3])
    assert not is_day_unlocked(4, [1, 2])

    assert can_complete_day(True)
    assert not can_complete_day(False)


def test_difficulty_and_xp_scaling():
    assert difficulty_for_day(5) == "Beginner"
    assert difficulty_for_day(45) == "Intermediate"
    assert difficulty_for_day(90) == "Advanced"

    assert calculate_awarded_xp(task_completed=True, challenge_passed=True, day_completed=True) == 195
    assert resolve_level_tag(0) == "Beginner"
    assert resolve_level_tag(2000) == "Intermediate"
    assert resolve_level_tag(9200) == "Expert"


def test_concept_tracking_and_adaptive_retry():
    progress = {"learned_concepts": [], "weak_concepts": [], "mastered_concepts": []}
    counter: dict[str, int] = {}

    failed = update_concept_tracking(progress, ["loops"], passed=False, concept_success_counter=counter)
    assert "loops" in failed["learned_concepts"]
    assert "loops" in failed["weak_concepts"]

    passed_once = update_concept_tracking(failed, ["loops"], passed=True, concept_success_counter=counter)
    assert "loops" not in passed_once["weak_concepts"]
    assert "loops" not in passed_once["mastered_concepts"]

    passed_twice = update_concept_tracking(passed_once, ["loops"], passed=True, concept_success_counter=counter)
    assert "loops" in passed_twice["mastered_concepts"]

    low_fail = adaptive_retry_payload(2, ["loops"])
    assert not low_fail["show_extra_guided_hint"]

    high_fail = adaptive_retry_payload(3, ["loops"])
    assert high_fail["show_extra_guided_hint"]
    assert high_fail["micro_drill"]["concepts"] == ["loops"]


def test_workspace_file_validation_rules():
    files = [
        {"path": "outputs/ports.json", "content": "{\"open_ports\": [22], \"services\": [\"ssh\"]}"},
        {"path": "outputs/endpoints.csv", "content": "endpoint,status\napi,200\n"},
    ]
    requirements = {
        "required_files": ["outputs/ports.json", "outputs/endpoints.csv"],
        "contains": [{"path": "outputs/endpoints.csv", "values": ["api,200"]}],
        "schema": [
            {"path": "outputs/ports.json", "type": "json", "keys": ["open_ports", "services"]},
            {"path": "outputs/endpoints.csv", "type": "csv", "columns": ["endpoint", "status"]},
        ],
    }
    result = validate_workspace_challenge(files, requirements)
    assert result["passed"]
