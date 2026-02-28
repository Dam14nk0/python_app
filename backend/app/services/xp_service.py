XP_TASK_COMPLETION = 15
XP_CHALLENGE_PASS = 60
XP_DAY_COMPLETION = 120

LEVEL_THRESHOLDS = [
    (0, "Beginner"),
    (1500, "Intermediate"),
    (4500, "Advanced"),
    (9000, "Expert"),
]


def calculate_awarded_xp(task_completed: bool = False, challenge_passed: bool = False, day_completed: bool = False) -> int:
    xp = 0
    if task_completed:
        xp += XP_TASK_COMPLETION
    if challenge_passed:
        xp += XP_CHALLENGE_PASS
    if day_completed:
        xp += XP_DAY_COMPLETION
    return xp


def resolve_level_tag(xp: int) -> str:
    level = "Beginner"
    for threshold, tag in LEVEL_THRESHOLDS:
        if xp >= threshold:
            level = tag
    return level
