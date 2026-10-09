"""W3 submitted solution with verification checks added by Codex."""

import sys


def import_scores(raw_scores):
    valid = []
    rejected = []
    for i, text in enumerate(raw_scores):
        try:
            score = int(text)
        except ValueError:
            rejected.append((i, text, "not_integer"))
            continue
        if 0 <= score <= 100:
            valid.append(score)
        else:
            rejected.append((i, text, "out_of_range"))
    return {"valid": valid, "rejected": rejected}


def run_checks():
    cases = [
        ("example 1", ["80", " 100 ", "bad", "-1"],
         {"valid": [80, 100], "rejected": [(2, "bad", "not_integer"), (3, "-1", "out_of_range")]}),
        ("example 2", [], {"valid": [], "rejected": []}),
        ("example 3", ["0", "101", "3.5"],
         {"valid": [0], "rejected": [(1, "101", "out_of_range"), (2, "3.5", "not_integer")]}),
        ("normal scores", ["50", "75", "+90"], {"valid": [50, 75, 90], "rejected": []}),
        ("boundaries", ["-1", "0", "100", "101"],
         {"valid": [0, 100], "rejected": [(0, "-1", "out_of_range"), (3, "101", "out_of_range")]}),
        ("invalid integer text", ["", " ", "1e2", "abc"],
         {"valid": [], "rejected": [(0, "", "not_integer"), (1, " ", "not_integer"),
                                    (2, "1e2", "not_integer"), (3, "abc", "not_integer")]}),
    ]
    for name, raw_scores, expected in cases:
        snapshot = raw_scores.copy()
        actual = import_scores(raw_scores)
        assert actual == expected, (name, actual, expected)
        assert raw_scores == snapshot, (name, "input changed")
        print(f"PASS: {name}; output and input preservation verified")

    invalid_type = [None]
    snapshot = invalid_type.copy()
    try:
        import_scores(invalid_type)
    except TypeError:
        pass
    else:
        raise AssertionError("TypeError was not propagated")
    assert invalid_type == snapshot, "out-of-contract input changed"
    print("PASS: out-of-contract None raises TypeError; input unchanged")
    print("ALL 7 CHECKS PASSED")


if __name__ == "__main__":
    print(f"Python {sys.version.split()[0]}")
    run_checks()
