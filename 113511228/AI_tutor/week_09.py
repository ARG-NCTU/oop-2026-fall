"""AOOP Week 09: Count Exact-Budget Item Selections.
Original educational exercise inspired by the course OCW topic.
This file is a worked-example solution; run it to execute its tests.
"""

def count_exact_budget(prices, target):
    def visit(index, total):
        if index == len(prices):
            return 1 if total == target else 0
        return (visit(index + 1, total) +
                visit(index + 1, total + prices[index]))
    return visit(0, 0)


def _run_self_tests():
    """Execute provided examples and additional edge cases."""
    import copy
    cases = [
        (([2, 3, 5], 5), 2),
        (([1, 1], 1), 2),
        (([], 0), 1),
        (([0, 0], 0), 4),
        (([0, 0], 0), 4),
        (([1, 1, 1], 2), 3),
    ]
    for number, (args, expected) in enumerate(cases, 1):
        given = copy.deepcopy(args)
        actual = count_exact_budget(*given)
        assert actual == expected, (number, actual, expected)
    print("Week 09: PASS ({} test cases)".format(len(cases)))


if __name__ == "__main__":
    _run_self_tests()
