"""MIT 6.0001 Lecture 10 transfer challenge: Count Target-Sum Pairs.

Use only basic Python concepts from the lecture: lists, indexing,
for loops, comparisons, and a constant-size counter.
"""


def count_target_pairs(numbers, target):
    """Count unordered pairs of distinct indices (i, j), i < j,
    with numbers[i] + numbers[j] == target.

    Assumes numbers is a list of integers and target is an integer.
    """
    count = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                count += 1
    return count


def run_tests():
    cases = [
        ([1, 2, 3, 4], 5, 2),
        ([2, 2, 2], 4, 3),
        ([1, 5, 7], 100, 0),
        ([], 5, 0),
        ([5], 10, 0),
        ([0, 0], 0, 1),
        ([-3, 1, 2, 4], 1, 1),
        ([1, 1, 1, 1], 2, 6),
    ]
    for numbers, target, expected in cases:
        actual = count_target_pairs(numbers, target)
        assert actual == expected, (
            f"numbers={numbers}, target={target}: expected {expected}, got {actual}"
        )
        print(f"PASS numbers={numbers}, target={target} -> {actual}")
    print(f"All {len(cases)} tests passed.")


if __name__ == "__main__":
    run_tests()

