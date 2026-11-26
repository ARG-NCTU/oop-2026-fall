"""AOOP Week 02: Total All Nested Category Scores.
Original educational exercise inspired by the course OCW topic.
This file is a worked-example solution; run it to execute its tests.
"""

def nested_score_total(tree):
    total = 0
    for value in tree.values():
        if isinstance(value, dict):
            total += nested_score_total(value)
        else:
            total += value
    return total


def _run_self_tests():
    """Execute provided examples and additional edge cases."""
    import copy
    cases = [
        (({'A': {'x': 2, 'y': 3}, 'B': 5},), 10),
        (({'a': {'b': -2}, 'c': 7},), 5),
        (({},), 0),
        (({'x': {'empty': {}, 'neg': -4}, 'y': 1},), -3),
    ]
    for number, (args, expected) in enumerate(cases, 1):
        given = copy.deepcopy(args)
        actual = nested_score_total(*given)
        assert actual == expected, (number, actual, expected)
    print("Week 02: PASS ({} test cases)".format(len(cases)))


if __name__ == "__main__":
    _run_self_tests()
