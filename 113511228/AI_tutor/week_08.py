"""AOOP Week 08: First Index Not Smaller Than Target.
Original educational exercise inspired by the course OCW topic.
This file is a worked-example solution; run it to execute its tests.
"""

def first_not_smaller(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] >= target:
            hi = mid
        else:
            lo = mid + 1
    return lo


def _run_self_tests():
    """Execute provided examples and additional edge cases."""
    import copy
    cases = [
        (([1, 2, 2, 4], 2), 1),
        (([1, 2, 2, 4], 3), 3),
        (([], 7), 0),
        (([1, 2, 2, 4], 10), 4),
        (([2, 2, 2], 2), 0),
        (([1, 2, 3], 0), 0),
    ]
    for number, (args, expected) in enumerate(cases, 1):
        given = copy.deepcopy(args)
        actual = first_not_smaller(*given)
        assert actual == expected, (number, actual, expected)
    print("Week 08: PASS ({} test cases)".format(len(cases)))


if __name__ == "__main__":
    _run_self_tests()
