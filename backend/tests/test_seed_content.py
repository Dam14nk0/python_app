import json
from pathlib import Path


def test_seed_dataset_has_100_days_and_required_fields():
    path = Path(__file__).resolve().parents[1] / "seeds" / "python_for_pentesters_100_days.seed.json"
    data = json.loads(path.read_text())

    assert {"categories", "tracks", "courses", "modules", "lessons"}.issubset(data.keys())
    assert len(data["lessons"]) == 100

    required = {
        "title",
        "difficulty",
        "est_minutes",
        "content_blocks",
        "step_by_step_path",
        "tasks",
        "challenge",
        "mini_project",
        "beginner_mode",
        "learning_engine",
    }

    lessons = data["lessons"]
    for lesson in lessons:
        assert required.issubset(lesson.keys())
        assert 3 <= len(lesson["tasks"]) <= 8
        assert {"what", "why", "real_example", "common_mistake"} == {blk["kind"] for blk in lesson["content_blocks"]}
        assert {"description", "starter_code", "expected_behavior", "used_concepts", "pass_required_for_day_completion"}.issubset(
            lesson["challenge"].keys()
        )

    checkpoint_days = [l["day_number"] for l in lessons if l["checkpoint_lab"]]
    integrated_days = [l["day_number"] for l in lessons if l["integrated_mini_project_day"]]
    assert checkpoint_days == [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]
    assert integrated_days == [14, 28, 42, 56, 70, 84, 98]

    capstone_days = [l for l in lessons if l["day_number"] >= 91]
    assert len(capstone_days) == 10
    assert all("capstone" in l["module_key"] for l in capstone_days)
