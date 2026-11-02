"""Verification runner for the Week 6 binary-search transfer challenge."""

import importlib.util
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent


def load_cases():
    cases = json.loads((HERE / "cases.json").read_text(encoding="utf-8"))
    large = list(range(0, 200000, 2))
    cases.extend([
        dict(name="max_length_first", times=large, target=0, expected=0),
        dict(name="max_length_middle_exact", times=large,
             target=100000, expected=50000),
        dict(name="max_length_middle_gap", times=large,
             target=100001, expected=50001),
        dict(name="max_length_after_all", times=large,
             target=200000, expected=-1),
    ])

    names = set()
    for case in cases:
        name = case["name"]
        times = case["times"]
        target = case["target"]
        expected = case["expected"]
        if not isinstance(name, str) or name in names:
            raise ValueError("Case names must be unique strings")
        names.add(name)
        if not isinstance(times, list) or len(times) > 100000:
            raise ValueError(f"{name}: invalid times list")
        if any(type(value) is not int or not 0 <= value <= 1000000000
               for value in times):
            raise ValueError(f"{name}: invalid timestamp")
        if any(times[index] > times[index + 1]
               for index in range(len(times) - 1)):
            raise ValueError(f"{name}: timestamps are not sorted")
        if type(target) is not int or not 0 <= target <= 1000000000:
            raise ValueError(f"{name}: invalid target")
        if type(expected) is not int or not (
                expected == -1 or 0 <= expected < len(times)):
            raise ValueError(f"{name}: invalid expected index")
        qualifying = [index for index, value in enumerate(times)
                      if value >= target]
        oracle = qualifying[0] if qualifying else -1
        if expected != oracle:
            raise ValueError(
                f"{name}: expected {expected}, oracle gives {oracle}")
    return cases


def main():
    cases = load_cases()
    solution_path = HERE / "solution.py"
    spec = importlib.util.spec_from_file_location(
        "week06_student_solution", solution_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    solve = getattr(module, "first_event_at_or_after", None)
    if not callable(solve):
        print("FAIL: solution.py must define first_event_at_or_after(times, target).")
        return 1

    failures = 0
    for case in cases:
        original = case["times"].copy()
        try:
            actual = solve(case["times"], case["target"])
            if type(actual) is not int or actual != case["expected"]:
                raise AssertionError(
                    f"expected {case['expected']!r}, got {actual!r}")
            if case["times"] != original:
                raise AssertionError("input timestamps were modified")
        except Exception as error:
            failures += 1
            print(f"FAIL {case['name']}: {type(error).__name__}: {error}")
        else:
            print(f"PASS {case['name']}")

    print(f"{len(cases) - failures}/{len(cases)} cases passed.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.dont_write_bytecode = True
    sys.exit(main())
