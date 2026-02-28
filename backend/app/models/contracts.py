from dataclasses import dataclass


@dataclass
class ChallengeResult:
    passed: bool
    message: str
    run_output: str
