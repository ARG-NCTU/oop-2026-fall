# W2 AI Tutor Part B: Broken Staircase (OCW Lec 6: Recursion and Dictionaries)
#
# A staircase has n steps (numbered 1..n). You start on the ground (step 0)
# and may climb 1 or 2 steps at a time. Some steps are broken and cannot be
# stepped on. Return the number of distinct ways to reach step n exactly.


def count_ways(n, broken, memo=None):
    """Number of ways to reach step n from step 0 using moves of 1 or 2,
    never landing on a step in `broken`."""
    if memo is None:
        memo = {}
        broken = set(broken)

    if n < 0 or n in broken:      # fell off the bottom / landed on a broken step
        return 0
    if n == 0:                    # standing on the ground: one way (do nothing)
        return 1
    if n in memo:
        return memo[n]

    memo[n] = count_ways(n - 1, broken, memo) + count_ways(n - 2, broken, memo)
    return memo[n]


if __name__ == "__main__":
    # provided examples
    assert count_ways(4, []) == 5
    assert count_ways(4, [2]) == 1        # 0 -> 1 -> 3 -> 4
    assert count_ways(5, [3]) == 2        # 0-1-2-4-5, 0-2-4-5
    # edge cases
    assert count_ways(0, []) == 1
    assert count_ways(1, [1]) == 0        # destination itself is broken
    assert count_ways(5, [2, 3]) == 0     # two broken steps in a row block the way
    assert count_ways(3, [1, 2]) == 0
    assert count_ways(60, []) == 2504730781961   # only feasible with the memo
    print("all tests passed")
