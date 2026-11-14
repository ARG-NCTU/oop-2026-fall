
# ============================================================
# LeetCode-style Challenge: Find the Most Similar Pair
# ============================================================
#
# Given a list of samples, where each sample is represented
# by a list of numerical features, find the two samples
# with the smallest Euclidean distance.
#
# Return their indices as [i, j], where i < j.
#
# If multiple pairs have the same minimum distance,
# return the lexicographically smallest pair of indices.
#
# Constraints:
# - 2 <= number of samples <= 100
# - 1 <= number of features <= 10
# - All samples have the same number of features.
# - Feature values are integers between -100 and 100.
#
# Example 1:
# Input: [[1, 2], [2, 2], [5, 6]]
# Output: [0, 1]
#
# Example 2:
# Input: [[0, 0], [2, 0], [1, 0]]
# Output: [0, 2]
#
# Example 3:
# Input: [[1, 1], [1, 1], [3, 3]]
# Output: [0, 1]
#
# Lecture Concepts:
# - Euclidean Distance
# - Brute Force Search
# - Nested Loops
#
# Time Complexity: O(n^2 * d)
# Space Complexity: O(1)
#
# n = number of samples
# d = number of features
#
# We compare squared distances instead of taking square roots.
# This works because the smallest squared distance also
# corresponds to the smallest Euclidean distance.
# ============================================================


# -------------------------
# My Final Solution
# -------------------------

def mostSimilarPair(samples):
    length = len(samples)
    feat = len(samples[0])

    min_num = float('inf')
    min_loc = []

    for i in range(length):
        for j in range(i + 1, length):
            dis = 0

            for k in range(feat):
                dis += (samples[i][k] - samples[j][k]) * \
                       (samples[i][k] - samples[j][k])

            if dis < min_num:
                min_num = dis
                min_loc = [i, j]

    return min_loc


# -------------------------
# Test Cases
# -------------------------

def run_tests():
    tests = [
        # Test 1: Basic example
        (
            [[1, 2], [2, 2], [5, 6]],
            [0, 1]
        ),

        # Test 2: Equal minimum distances
        (
            [[0, 0], [2, 0], [1, 0]],
            [0, 2]
        ),

        # Test 3: Identical samples
        (
            [[1, 1], [1, 1], [3, 3]],
            [0, 1]
        ),

        # Test 4: Three-dimensional samples
        (
            [[0, 0, 100], [0, 0, 0], [1, 0, 100]],
            [0, 2]
        ),

        # Test 5: One-dimensional samples
        (
            [[0], [9], [2]],
            [0, 2]
        ),

        # Test 6: All identical samples
        (
            [[1, 1], [1, 1], [1, 1], [1, 1]],
            [0, 1]
        ),

        # Test 7: Ten-dimensional samples
        (
            [[0] * 10, [5] * 10, [1] * 10],
            [0, 2]
        ),

        # Test 8: Negative feature values
        (
            [[-2, -3], [1, 1], [-1, -2]],
            [0, 2]
        )
    ]

    for i, (samples, expected) in enumerate(tests, 1):
        actual = mostSimilarPair(samples)

        print(f"Test {i}")
        print(f"Expected: {expected}")
        print(f"Actual:   {actual}")

        assert actual == expected, f"Test {i} failed!"
        print("PASS")
        print("-" * 30)

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
