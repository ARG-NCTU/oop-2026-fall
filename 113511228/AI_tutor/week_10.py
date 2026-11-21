"""AOOP Week 10: Maximum Workshop Satisfaction.
Original educational exercise inspired by the course OCW topic.
This file is a worked-example solution; run it to execute its tests.
"""

def maximize_satisfaction(durations, values, budget):
    dp = [0] * (budget + 1)
    for duration, value in zip(durations, values):
        for b in range(budget, duration - 1, -1):
            dp[b] = max(dp[b], dp[b - duration] + value)
    return dp[budget]


def _run_self_tests():
    """Execute provided examples and additional edge cases."""
    import copy
    cases = [
        (([2, 3, 4], [4, 5, 10], 5), 10),
        (([1, 2, 3], [5, 6, 8], 3), 11),
        (([], [], 7), 0),
        (([5], [100], 4), 0),
        (([1], [5], 2), 5),
        (([1], [5], 0), 0),
    ]
    for number, (args, expected) in enumerate(cases, 1):
        given = copy.deepcopy(args)
        actual = maximize_satisfaction(*given)
        assert actual == expected, (number, actual, expected)
    print("Week 10: PASS ({} test cases)".format(len(cases)))


if __name__ == "__main__":
    _run_self_tests()
