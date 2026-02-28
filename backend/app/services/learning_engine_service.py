SUCCESS_THRESHOLD_FOR_MASTERY = 2


def is_day_unlocked(day_number: int, completed_days: list[int]) -> bool:
    if day_number <= 1:
        return True
    return (day_number - 1) in completed_days


def can_complete_day(challenge_passed: bool) -> bool:
    return challenge_passed


def difficulty_for_day(day_number: int) -> str:
    if day_number <= 35:
        return "Beginner"
    if day_number <= 75:
        return "Intermediate"
    return "Advanced"


def update_concept_tracking(
    progress: dict,
    challenge_concepts: list[str],
    passed: bool,
    concept_success_counter: dict[str, int],
) -> dict:
    learned = set(progress.get("learned_concepts", []))
    weak = set(progress.get("weak_concepts", []))
    mastered = set(progress.get("mastered_concepts", []))

    for concept in challenge_concepts:
        learned.add(concept)
        if passed:
            weak.discard(concept)
            concept_success_counter[concept] = concept_success_counter.get(concept, 0) + 1
            if concept_success_counter[concept] >= SUCCESS_THRESHOLD_FOR_MASTERY:
                mastered.add(concept)
        else:
            weak.add(concept)
            concept_success_counter[concept] = 0

    return {
        "learned_concepts": sorted(learned),
        "weak_concepts": sorted(weak),
        "mastered_concepts": sorted(mastered),
        "concept_success_counter": concept_success_counter,
    }


def adaptive_retry_payload(failed_attempts: int, challenge_concepts: list[str]) -> dict:
    if failed_attempts >= 3:
        return {
            "show_extra_guided_hint": True,
            "micro_drill": {
                "concepts": challenge_concepts,
                "instruction": "Complete this short drill before retry: solve one minimal task per weak concept.",
            },
        }
    return {"show_extra_guided_hint": False, "micro_drill": None}


def validate_workspace_challenge(files: list[dict], requirements: dict) -> dict:
    """Validate challenge outputs from user workspace files without command execution."""
    by_path = {f["path"]: f.get("content", "") for f in files}
    errors = []

    for required_path in requirements.get("required_files", []):
        if required_path not in by_path:
            errors.append(f"missing file: {required_path}")

    for contains_rule in requirements.get("contains", []):
        path = contains_rule["path"]
        expected_values = contains_rule.get("values", [])
        content = by_path.get(path, "")
        for value in expected_values:
            if value not in content:
                errors.append(f"{path} missing value: {value}")

    for schema in requirements.get("schema", []):
        path = schema["path"]
        content = by_path.get(path, "")
        if schema["type"] == "csv":
            headers = content.splitlines()[0] if content else ""
            for col in schema.get("columns", []):
                if col not in headers:
                    errors.append(f"{path} missing csv column: {col}")
        if schema["type"] == "json":
            for key in schema.get("keys", []):
                if f'"{key}"' not in content:
                    errors.append(f"{path} missing json key: {key}")

    return {"passed": len(errors) == 0, "errors": errors}
