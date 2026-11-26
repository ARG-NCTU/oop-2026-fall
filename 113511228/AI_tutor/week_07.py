"""AOOP Week 07: Longest Affordable Consecutive Segment.
Original educational exercise inspired by the course OCW topic.
This file is a worked-example solution; run it to execute its tests.
"""

def longest_affordable_segment(costs, budget):
    left = 0
    total = 0
    best = 0
    for right, value in enumerate(costs):
        total += value
        while total > budget:
            total -= costs[left]
            left += 1
        best = max(best, right - left + 1)
    return best


def _run_self_tests():
    """Execute provided examples and additional edge cases."""
    import copy
    cases = [
        (([1, 1, 2, 1], 4), 3),
        (([5, 6], 4), 0),
        (([], 10), 0),
        (([1, 1, 1], 3), 3),
        (([4, 5], 0), 0),
        (([1, 2, 3], 6), 3),
    ]
    for number, (args, expected) in enumerate(cases, 1):
        given = copy.deepcopy(args)
        actual = longest_affordable_segment(*given)
        assert actual == expected, (number, actual, expected)
    print("Week 07: PASS ({} test cases)".format(len(cases)))


if __name__ == "__main__":
    _run_self_tests()
