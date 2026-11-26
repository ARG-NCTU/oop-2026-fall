"""AOOP Week 01: Non-Destructive Inventory Updates.
Original educational exercise inspired by the course OCW topic.
This file is a worked-example solution; run it to execute its tests.
"""

def update_inventory(rows, updates):
    result = [row[:] for row in rows]
    for item, change in updates:
        for row in result:
            if row[0] == item:
                row[1] += change
                break
    return result


def _run_self_tests():
    """Execute provided examples and additional edge cases."""
    import copy
    cases = [
        (([['pen', 5], ['book', 2]], [['pen', -2]]), [['pen', 3], ['book', 2]]),
        (([['A', 1], ['B', 4]], [['B', 1], ['B', -3]]), [['A', 1], ['B', 2]]),
        (([], []), []),
        (([['A', 0]], [['A', 2], ['A', -1]]), [['A', 1]]),
    ]
    for number, (args, expected) in enumerate(cases, 1):
        given = copy.deepcopy(args)
        actual = update_inventory(*given)
        assert actual == expected, (number, actual, expected)
        assert given == args, "Input inventory was mutated"
        if args and args[0]:
            assert all(x is not y for x, y in zip(args[0], actual)), "Inner rows were not independently allocated"
    print("Week 01: PASS ({} test cases)".format(len(cases)))


if __name__ == "__main__":
    _run_self_tests()
