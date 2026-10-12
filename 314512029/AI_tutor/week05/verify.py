"""AI-provided test infrastructure; contains no student solution.

Exit codes: 0 = fixtures valid / solution cases passed; 1 = failure;
2 = solution absent. --check-fixtures does not test a student solution.
"""

import argparse
import importlib.util
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent


def load_cases():
    cases = json.loads((HERE / "cases.json").read_text(encoding="utf-8"))
    # Larger boundary inputs are generated here to keep cases.json readable.
    cases.extend([
        dict(name="max_length_equal", readings=[100] * 1000,
             k=1000, limit=100000, expected=-1),
        dict(name="max_length_alert", readings=[100] * 1000,
             k=1000, limit=99999, expected=0),
        dict(name="max_length_last_alert", readings=[0] * 999 + [100],
             k=1, limit=99, expected=999),
    ])
    names = set()
    for case in cases:
        name = case["name"]
        if not isinstance(name, str) or name in names:
            raise ValueError("Case names must be unique strings")
        names.add(name)
        readings, k, limit = case["readings"], case["k"], case["limit"]
        if not isinstance(readings, list) or not 0 <= len(readings) <= 1000:
            raise ValueError(f"{name}: invalid readings length")
        if any(type(value) is not int or not 0 <= value <= 100
               for value in readings):
            raise ValueError(f"{name}: invalid reading")
        if type(k) is not int or not 1 <= k <= 1000:
            raise ValueError(f"{name}: invalid k")
        if type(limit) is not int or not 0 <= limit <= 100000:
            raise ValueError(f"{name}: invalid limit")
        expected = case["expected"]
        if type(expected) is not int or not (
            expected == -1 or 0 <= expected <= len(readings) - k
        ):
            raise ValueError(f"{name}: expected index outside output domain")
    return cases


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-fixtures", action="store_true",
                        help="Validate case format/ranges only, not solution correctness")
    args = parser.parse_args()
    cases = load_cases()
    if args.check_fixtures:
        print(f"PASS: {len(cases)} test fixtures have valid format and ranges.")
        print("This does not validate a student solution or prove expected outputs.")
        return 0

    path = HERE / "solution.py"
    if not path.exists():
        print("PENDING: solution.py is absent; no student tests were run.")
        print("Explain your approach to the tutor before writing your solution.")
        return 2

    spec = importlib.util.spec_from_file_location("student_solution", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    solve = getattr(module, "first_unsafe_window", None)
    if not callable(solve):
        print("FAIL: solution.py must define first_unsafe_window(readings, k, limit).")
        return 1

    failures = 0
    for case in cases:
        readings = case["readings"].copy()
        try:
            actual = solve(readings, case["k"], case["limit"])
            if type(actual) is not int or actual != case["expected"]:
                raise AssertionError(
                    f"expected {case['expected']!r}, got {actual!r}")
            if readings != case["readings"]:
                raise AssertionError("input readings were modified")
        except Exception as error:
            failures += 1
            print(f"FAIL {case['name']}: {type(error).__name__}: {error}")
        else:
            print(f"PASS {case['name']}")
    print(f"{len(cases) - failures}/{len(cases)} cases passed.")
    print("Record actual results; discuss failures with the tutor before revising.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.dont_write_bytecode = True
    sys.exit(main())
