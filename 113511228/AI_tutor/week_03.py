"""AOOP Week 03: Sum Valid Integer Scores.
Original educational exercise inspired by the course OCW topic.
This file is a worked-example solution; run it to execute its tests.
"""

def sum_valid_scores(tokens):
    total = 0
    invalid = []
    for index, token in enumerate(tokens):
        try:
            total += int(token)
        except ValueError:
            invalid.append(index)
    return total, invalid


def _run_self_tests():
    """Execute provided examples and additional edge cases."""
    import copy
    cases = [
        ((['10', 'bad', '-3'],), (7, [1])),
        (([' 5 ', '2.5', '+7'],), (12, [1])),
        (([],), (0, [])),
        (([' -2 ', '+5', 'two', ''],), (3, [2, 3])),
    ]
    for number, (args, expected) in enumerate(cases, 1):
        given = copy.deepcopy(args)
        actual = sum_valid_scores(*given)
        assert actual == expected, (number, actual, expected)
    print("Week 03: PASS ({} test cases)".format(len(cases)))


if __name__ == "__main__":
    _run_self_tests()
