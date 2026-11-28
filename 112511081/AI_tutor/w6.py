# W6 AI Tutor Part B: Pair Sum (OCW Lec 10: Understanding Program Efficiency, Part 1)
#
# pair_sum_slow(nums, target)  -> True if two different positions add up to target, O(n^2)
# pair_sum_sorted(nums, target)-> same answer, O(n log n): sort, then two pointers
# pair_sum_fast(nums, target)  -> same answer, O(n) using a set
# count_steps_slow(n)          -> worst case number of comparisons of the slow version


def pair_sum_slow(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return True
    return False


def pair_sum_sorted(nums, target):
    """first idea: sort, then move two pointers inward, O(n log n)"""
    s = sorted(nums)                         # sorted() makes a copy, input unchanged
    i, j = 0, len(s) - 1
    while i < j:
        total = s[i] + s[j]
        if total == target:
            return True
        elif total < target:
            i += 1
        else:
            j -= 1
    return False


def pair_sum_fast(nums, target):
    seen = set()
    for x in nums:
        if target - x in seen:               # set lookup is O(1) on average
            return True
        seen.add(x)
    return False


def count_steps_slow(n):
    """worst case comparisons of pair_sum_slow: n(n-1)/2 -> O(n^2)"""
    return n * (n - 1) // 2


if __name__ == "__main__":
    # provided examples
    assert pair_sum_slow([2, 7, 11, 15], 9) is True
    assert pair_sum_fast([2, 7, 11, 15], 9) is True
    assert pair_sum_slow([1, 2, 3], 7) is False
    assert pair_sum_fast([1, 2, 3], 7) is False

    # edge cases
    for f in (pair_sum_slow, pair_sum_sorted, pair_sum_fast):
        assert f([], 0) is False
        assert f([5], 10) is False           # one element cannot pair with itself
        assert f([5, 5], 10) is True         # two positions, same value
        assert f([-3, 4, 1], 1) is True      # negative numbers
    assert count_steps_slow(1) == 0 and count_steps_slow(4) == 6

    # both versions agree on random inputs
    import random
    for _ in range(300):
        nums = [random.randint(-10, 10) for _ in range(random.randint(0, 8))]
        t = random.randint(-20, 20)
        assert pair_sum_slow(nums, t) == pair_sum_sorted(nums, t) == pair_sum_fast(nums, t)

    print("all tests passed")
