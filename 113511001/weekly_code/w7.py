"""
AOOP 2026 - Week 7
Lecture 11: Understanding Program Efficiency (Part 2)

Challenge: First Occurrence Finder

Problem Statement:
Given a sorted list of integers nums, which may contain
duplicate values, and a target integer target, write a
function that returns the index of the first occurrence
of target.

If the target does not exist, return -1.

Input:
    nums   - A list of integers sorted in ascending order.
    target - An integer to search for.

Output:
    An integer representing the first index of target,
    or -1 if the target is not found.

Constraints:
    0 <= len(nums) <= 100000
    The list may contain negative numbers and duplicates.
    Do not use the built-in index() method.
    Target time complexity: O(log n).

Examples:
    Input:  nums = [1, 2, 2, 2, 4, 5], target = 2
    Output: 1

    Input:  nums = [1, 3, 5, 7], target = 4
    Output: -1

    Input:  nums = [], target = 3
    Output: -1
"""


def first_occurrence(nums, target):
    low = 0
    high = len(nums) - 1
    index = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            index = mid
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return index


# Test Cases
print(first_occurrence([1, 2, 2, 2, 4, 5], 2))  # 1
print(first_occurrence([1, 3, 5, 7], 4))        # -1
print(first_occurrence([], 3))                  # -1
print(first_occurrence([2, 2, 2, 2], 2))        # 0
print(first_occurrence([1, 2, 3, 4], 4))        # 3