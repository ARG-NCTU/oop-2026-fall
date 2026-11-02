
# AOOP Week 8 - LeetCode-style Coding Challenge
# Topic: Searching and Sorting Algorithms
#
# Problem: Minimum Pairing Cost
#
# Problem Statement:
# Given a list of integers containing an even number of elements,
# divide all elements into pairs so that the sum of the absolute
# differences between each pair is minimized.
#
# Each element must be used exactly once.
# Return the minimum possible total difference.
#
# Input:
# nums - A list of integers with an even number of elements.
#
# Output:
# An integer representing the minimum total difference.
#
# Constraints:
# 1. 2 <= len(nums) <= 2000
# 2. len(nums) is always even.
# 3. -10000 <= nums[i] <= 10000
# 4. Duplicate values are allowed.
# 5. Do not use Python's built-in sort() or sorted().
#
# Example 1:
# Input: nums = [3, 1, 4, 2]
# Output: 2
# Explanation: Pair (1,2) and (3,4).
# Total = |1-2| + |3-4| = 2
#
# Example 2:
# Input: nums = [8, 1, 5, 6]
# Output: 6
# Explanation: Pair (1,5) and (6,8).
# Total = |1-5| + |6-8| = 6
#
# Example 3:
# Input: nums = [-3, -3, 4, 5, 10, 12]
# Output: 3
# Explanation: Pair (-3,-3), (4,5), and (10,12).
# Total = 0 + 1 + 2 = 3


# Solution:

def bubble_sort(L):
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                L[j-1], L[j] = L[j], L[j-1]


def minimum_pairing_cost(nums):
    bubble_sort(nums)

    total = 0

    for i in range(0, len(nums), 2):
        total += abs(nums[i] - nums[i+1])

    return total


# Test Cases
print(minimum_pairing_cost([3, 1, 4, 2]))       # 2
print(minimum_pairing_cost([8, 1, 5, 6]))       # 6
print(minimum_pairing_cost([-3, -3, 4, 5, 10, 12])) # 3
