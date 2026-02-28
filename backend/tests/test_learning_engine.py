import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.services.learning_engine_service import can_complete_day, difficulty_for_day, is_day_unlocked
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
