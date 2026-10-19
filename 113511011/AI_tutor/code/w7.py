"""MIT 6.0001 Lecture 11 transfer challenge: Find Target Range.

Find the first and last positions of a target in a sorted list using
binary search without list slicing. Python 3, standard library only.
"""


def lower_bound(numbers, target):
    """Return the first index i such that numbers[i] >= target.

    If no such index exists, return len(numbers).
    """
    low, high = 0, len(numbers)  # search interval [low, high)
    while low < high:
        mid = (low + high) // 2
        if numbers[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low


def upper_bound(numbers, target):
    """Return the first index i such that numbers[i] > target."""
    low, high = 0, len(numbers)
    while low < high:
        mid = (low + high) // 2
        if numbers[mid] <= target:
            low = mid + 1
        else:
            high = mid
    return low


def find_target_range(numbers, target):
    """Return (first_index, last_index), or (-1, -1) if absent.

    Assumes numbers is sorted in nondecreasing order.
    Worst-case time: O(log n); auxiliary space: O(1).
    """
    first = lower_bound(numbers, target)
    if first == len(numbers) or numbers[first] != target:
        return (-1, -1)
    last = upper_bound(numbers, target) - 1
    return (first, last)


def run_tests():
    cases = [
        ([1, 2, 2, 2, 3, 4], 2, (1, 3)),
        ([1, 3, 5, 7], 4, (-1, -1)),
        ([5, 5, 5, 5], 5, (0, 3)),
        ([], 2, (-1, -1)),
        ([8], 8, (0, 0)),
        ([8], 5, (-1, -1)),
        ([1, 2, 3], 1, (0, 0)),
        ([1, 2, 3], 3, (2, 2)),
        ([-3, -1, -1, 0, 2], -1, (1, 2)),
        ([1, 1, 2, 2, 3, 3], 4, (-1, -1)),
    ]
    for numbers, target, expected in cases:
        actual = find_target_range(numbers, target)
        assert actual == expected, (
            f"numbers={numbers}, target={target}: "
            f"expected {expected}, got {actual}"
        )
        print(f"PASS numbers={numbers}, target={target} -> {actual}")
    print(f"All {len(cases)} tests passed.")


if __name__ == "__main__":
    run_tests()

