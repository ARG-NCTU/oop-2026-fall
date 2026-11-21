"""AOOP Week 06: Smallest Gap Between Equal Values.
Original educational exercise inspired by the course OCW topic.
This file is a worked-example solution; run it to execute its tests.
"""

def smallest_equal_gap(nums):
    last = {}
    answer = len(nums) + 1
    for i, value in enumerate(nums):
        if value in last:
            answer = min(answer, i - last[value])
        last[value] = i
    return -1 if answer == len(nums) + 1 else answer


def _run_self_tests():
    """Execute provided examples and additional edge cases."""
    import copy
    cases = [
        (([3, 1, 3, 1, 1],), 1),
        (([4, 5, 6],), -1),
        (([8, 8],), 1),
        (([],), -1),
        (([],), -1),
        (([7, 7],), 1),
    ]
    for number, (args, expected) in enumerate(cases, 1):
        given = copy.deepcopy(args)
        actual = smallest_equal_gap(*given)
        assert actual == expected, (number, actual, expected)
    print("Week 06: PASS ({} test cases)".format(len(cases)))


if __name__ == "__main__":
    _run_self_tests()
