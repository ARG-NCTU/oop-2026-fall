# W7 AI Tutor Part B: Bisection Helpers (OCW Lec 11: Understanding Program Efficiency, Part 2)
#
# first_at_least(L, x) -> smallest index i with L[i] >= x in a sorted list, len(L) if none, O(log n)
# int_sqrt(n)          -> largest integer r with r*r <= n, O(log n)
# count_halvings(n)    -> how many times n can be halved before reaching 1 (log2 n)


def first_at_least(L, x):
    low, high = 0, len(L)                    # answer is always in [low, high]
    while low < high:
        mid = (low + high) // 2
        if L[mid] < x:
            low = mid + 1
        else:
            high = mid
    return low


def int_sqrt(n):
    assert n >= 0, "n cannot be negative"
    low, high = 0, n + 1                     # r in [low, high)
    while high - low > 1:
        mid = (low + high) // 2
        if mid * mid <= n:
            low = mid
        else:
            high = mid
    return low


def count_halvings(n):
    steps = 0
    while n > 1:
        n //= 2
        steps += 1
    return steps


if __name__ == "__main__":
    # provided examples
    assert first_at_least([1, 3, 5, 7], 4) == 2
    assert first_at_least([1, 3, 5, 7], 5) == 2
    assert int_sqrt(10) == 3
    assert int_sqrt(16) == 4

    # edge cases
    assert first_at_least([], 3) == 0
    assert first_at_least([1, 3, 5], 99) == 3        # bigger than everything
    assert first_at_least([1, 3, 5], -99) == 0       # smaller than everything
    assert first_at_least([2, 2, 2, 2], 2) == 0      # duplicates -> first one
    assert int_sqrt(0) == 0 and int_sqrt(1) == 1
    assert int_sqrt(10**12) == 10**6
    assert count_halvings(1) == 0 and count_halvings(1024) == 10

    import bisect, math
    for n in range(2000):
        assert int_sqrt(n) == math.isqrt(n)
    L = [0, 1, 1, 4, 4, 4, 9]
    for x in range(-1, 11):
        assert first_at_least(L, x) == bisect.bisect_left(L, x)

    try:
        int_sqrt(-1)
    except AssertionError:
        pass
    else:
        assert False, "expected AssertionError"

    print("all tests passed")
