import json
from pathlib import Path


def _load_seed():
    path = Path(__file__).resolve().parents[1] / "seeds" / "python_for_pentesters_100_days.seed.json"
    return json.loads(path.read_text())


def test_seed_dataset_multicourse_counts_and_rules():
    data = _load_seed()

    assert len(data["categories"]) == 1
    assert len(data["tracks"]) == 2
    assert len(data["courses"]) == 2
    assert len(data["fixtures"]) >= 20

    lessons = data["lessons"]
    assert len(lessons) == 130

    py_lessons = sorted([l for l in lessons if l["course_slug"] == "python-for-pentesters"], key=lambda x: x["day_number"])
    bash_lessons = sorted([l for l in lessons if l["course_slug"] == "bash-for-pentesters"], key=lambda x: x["day_number"])

    assert len(py_lessons) == 100
    assert [py_lessons[0]["day_number"], py_lessons[-1]["day_number"]] == [1, 100]
    assert len(bash_lessons) == 30

    required = {"required_concepts", "unlocked_concepts", "is_checkpoint", "is_capstone_part", "capstone_stage", "fixtures", "fixtures_used", "workspace_tasks"}

    intro = {
        "python-for-pentesters": {"plain_text": 1, "http_headers": 31, "nmap_normal": 46, "nmap_grepable": 46, "nmap_xml": 47, "gobuster": 46, "ffuf": 46, "dig": 48, "log_file": 15},
        "bash-for-pentesters": {"plain_text": 1, "log_file": 11, "http_headers": 14, "nmap_normal": 21, "nmap_grepable": 22, "nmap_xml": 23, "gobuster": 12, "ffuf": 25, "dig": 26},
    }

    for course_slug, course_lessons in [("python-for-pentesters", py_lessons), ("bash-for-pentesters", bash_lessons)]:
        unlocked = set()
        for lesson in course_lessons:
            assert required.issubset(lesson.keys())
            assert set(lesson["required_concepts"]).issubset(unlocked)
            assert set(lesson["challenge"]["used_concepts"]).issubset(unlocked)
            if lesson["is_checkpoint"]:
                assert len(lesson["challenge"]["used_concepts"]) >= 3
            for fixture in lesson["fixtures"]:
                assert lesson["day_number"] >= intro[course_slug][fixture["type"]]
            unlocked.update(lesson["unlocked_concepts"])


def test_day46_and_bash_day12_examples():
    data = _load_seed()
    day46 = next(l for l in data["lessons"] if l["course_slug"] == "python-for-pentesters" and l["day_number"] == 46)
    assert set(day46["fixtures_used"]) >= {"nmap_basic_scan", "ffuf_api_probe"}
    assert "outputs/ports.json" in day46["challenge"]["file_requirements"]["required_files"]

    day12 = next(l for l in data["lessons"] if l["course_slug"] == "bash-for-pentesters" and l["day_number"] == 12)
    assert "gobuster_dirs_small" in day12["fixtures_used"]
    assert day12["challenge"]["file_requirements"]["required_files"] == ["outputs/report.txt"]
