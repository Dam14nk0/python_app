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
