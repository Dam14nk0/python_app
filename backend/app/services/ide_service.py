def run_code_mock(code: str, stdin: str) -> dict:
    return {
        "run_output": "Mock runner output",
        "stdin_echo": stdin,
        "code_size": len(code),
    }


def check_code_mock(expected_behavior: str) -> dict:
    return {
        "passed": False,
        "message": f"Validation placeholder against expected behavior: {expected_behavior}",
    }
