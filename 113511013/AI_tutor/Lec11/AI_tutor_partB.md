# AI Tutor — Part B | Lecture 11

**Name:** 范芷祺  
**Date:** 2026/11/10  
**Topic:** Bisection Search, Divide and Conquer, and O(log n) Complexity  
**Record type:** AI-prepared example and reference implementation.

## 1. Today's Challenge

### Core concept from today's OCW lecture:

Binary search repeatedly eliminates half the search interval of a sorted list. The lecture contrasts slicing, which copies data, with passing the original list and boundary indices, which keeps each search step O(1).

### Coding challenge title:

[LeetCode #35 — Search Insert Position (Easy)](https://leetcode.com/problems/search-insert-position/)

### Problem Description

Given a strictly increasing array of integers and a target value, return the index if the target is found. Otherwise, return the index where it would be inserted to preserve the sorted order.

The required time complexity is O(log n).

### Examples

| nums | target | Output |
|---|---:|---:|
| [1,3,5,6] | 5 | 2 |
| [1,3,5,6] | 2 | 1 |
| [1,3,5,6] | 7 | 4 |

---

## 2. My Initial Approach — Before AI Help

### My approach (sample):

I first considered repeatedly taking the left or right half of the array, similar to the lecture's first recursive binary-search implementation.

The algorithm would stop when I found the target or reached a one-element range and then decide where to insert the target.

### My initial complexity prediction:

The number of levels is O(log n), but copying each slice is not free. The total copied element count follows a geometric series and can make the slicing implementation O(n) in time.

That would not satisfy LeetCode's required O(log n) time complexity.

---

## 3. AI Tutor Help

### Did you ask the AI Tutor for help?

* [ ] No — I solved it independently
* [x] Yes — AI-generated self-review hint

### The most useful hint/question from AI:

If you can represent the current candidate range with just two integer indices, why create a new list at every step?

At termination, can the left boundary identify the first element that is not smaller than the target?

### It helped me realize that:

I can avoid slicing entirely. Binary search maintains an interval of possible insertion positions, so I do not need a separate final scan or an extra list.

---

## 4. My Revision

### Did you change your approach or code after interacting with AI?

* [ ] No
* [x] Yes — illustrative revision

### What did you change, and why?

I replaced the idea of creating sublists with a half-open search interval [low, high).

I update `low = mid + 1` only when the middle value is smaller than the target and update `high = mid` otherwise.

This avoids copying and yields a correct insertion position even when the target is absent.

---

## 5. Verification

### My final program (reference implementation):

```python
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums)

        while low < high:
            mid = (low + high) // 2

            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid

        return low
```

### Verification Status

* [x] Passed the provided examples in local execution
* [x] Passed additional edge cases in local execution
* [ ] Still has unresolved problems in the tested cases

| Input | Target | Expected | Actual |
|---|---:|---:|---:|
| [1,3,5,6] | 5 | 2 | 2 |
| [1,3,5,6] | 2 | 1 | 1 |
| [1,3,5,6] | 7 | 4 | 4 |
| [1,3,5,6] | 0 | 0 | 0 |
| [4] | 4 | 0 | 0 |
| [4] | 2 | 0 | 0 |
| [4] | 9 | 1 | 1 |
| [-5,-2,1,7] | -3 | 1 | 1 |

### One edge case I tested:

**Input:** `nums = [4], target = 9`

**Expected output:** `1`

**Actual output:** `1`

This checks that the algorithm correctly returns an index beyond the final element instead of trying to access an invalid array position.

---

## 6. One-Minute Reflection

### Why does my solution work?

At every step, indices before low refer to values smaller than the target, while indices from high onward refer to values greater than or equal to the target.

The middle comparison safely discards positions that cannot be the first value greater than or equal to the target.

When low equals high, their shared value is exactly the target's location or valid insertion position.

### Time Complexity

**Time complexity:** O(log n)

Every iteration reduces the remaining search interval by approximately half. Each iteration performs O(1) work.

**Space complexity:** O(1)

Only a fixed number of integer variables are required.

### What idea from the OCW lecture did I transfer to this new problem?

I transferred binary search's divide-and-conquer strategy and index-based range tracking to a problem that returns an insertion position rather than a Boolean search result.

### One thing I understand better now:

The stopping condition and boundary invariant are just as important as choosing the middle index.

The same two indices can represent both a search range and a potential insertion point.

### One thing I am still unsure about:

How to modify binary search to find the last value less than or equal to a target, especially when the array contains duplicate elements.