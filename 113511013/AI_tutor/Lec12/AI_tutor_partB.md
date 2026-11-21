# AI Tutor — Part B | Lecture 12

**Name:** 范芷祺  
**Date:** 2026/11/10  
**Topic:** Merging Sorted Lists, Divide and Conquer, and Sorting Efficiency  
**Record type:** AI-prepared example and reference implementation.

## 1. Today's Challenge

### Core concept from today's OCW lecture:

The merge stage of Merge Sort combines two already sorted sublists in linear time by comparing the next unprocessed values.

The full Merge Sort uses O(log n) levels of splitting and O(n) work per level, leading to O(n log n) time complexity.

### Coding challenge title:

[LeetCode #88 — Merge Sorted Array (Easy)](https://leetcode.com/problems/merge-sorted-array/)

### Problem Description

Given two integer arrays nums1 and nums2, sorted in non-decreasing order, merge nums2 into nums1 as one sorted array.

The length of nums1 is m + n, where the first m elements are meaningful values and the remaining n positions are reserved for merging.

The length of nums2 is n.

The result must be stored directly in nums1.

### Examples

| nums1 | m | nums2 | n | Expected nums1 |
|---|---:|---|---:|---|
| [1,2,3,0,0,0] | 3 | [2,5,6] | 3 | [1,2,2,3,5,6] |
| [1] | 1 | [] | 0 | [1] |
| [0] | 0 | [1] | 1 | [1] |

---

## 2. My Initial Approach — Before AI Help

### My approach (sample):

I initially considered using the lecture's merging strategy from left to right, reading from the front of both arrays and writing directly into nums1.

The algorithm compares the current elements of both arrays and places the smaller element into the result.

### My initial complexity prediction:

A correct two-pointer merge should take O(m+n) time.

However, writing from the front directly into nums1 may overwrite values that have not yet been read. The straightforward version is unsafe without extra storage or shifting elements.

---

## 3. AI Tutor Help

### Did you ask the AI Tutor for help?

* [ ] No — I solved it independently
* [x] Yes — AI-generated self-review hint

### The most useful hint/question from AI:

If you are required to reuse nums1, which end of the array already contains empty buffer positions?

Would filling those positions first allow you to compare meaningful values without destroying them?

### It helped me realize that:

The available buffer is at the end of nums1, so I should reverse the direction used in the lecture's merge function.

Instead of comparing the smallest remaining elements, I should compare the largest remaining elements.

Writing from right to left allows me to merge both arrays without overwriting unprocessed values.

---

## 4. My Revision

### Did you change your approach or code after interacting with AI?

* [ ] No
* [x] Yes — illustrative revision

### What did you change, and why?

I used three indices:

* `i`: The last meaningful element in nums1.
* `j`: The last element in nums2.
* `write`: The last available destination position in nums1.

I compare nums1[i] and nums2[j], place the larger element into nums1[write], and decrement the corresponding index.

After every iteration, I also decrement write.

When nums2 is exhausted, any remaining elements from nums1 are already in their correct positions.

This approach avoids creating an additional array.

---

## 5. Verification

### My final program (reference implementation):

```python
class Solution:
    def merge(self, nums1: list[int], m: int,
              nums2: list[int], n: int) -> None:
        i = m - 1
        j = n - 1
        write = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[write] = nums1[i]
                i -= 1
            else:
                nums1[write] = nums2[j]
                j -= 1

            write -= 1
```

### Verification Status

* [x] Passed the provided examples in local execution
* [x] Passed additional edge cases in local execution
* [ ] Still has unresolved problems in the tested cases

| nums1 | m | nums2 | n | Expected | Actual |
|---|---:|---|---:|---|---|
| [1,2,3,0,0,0] | 3 | [2,5,6] | 3 | [1,2,2,3,5,6] | [1,2,2,3,5,6] |
| [1] | 1 | [] | 0 | [1] | [1] |
| [0] | 0 | [1] | 1 | [1] | [1] |
| [1,2,2,0,0] | 3 | [2,3] | 2 | [1,2,2,2,3] | [1,2,2,2,3] |
| [-3,0,0] | 1 | [-5,2] | 2 | [-5,-3,2] | [-5,-3,2] |
| [0,0,0] | 1 | [-1,2] | 2 | [-1,0,2] | [-1,0,2] |
| [5,6,0,0] | 2 | [1,2] | 2 | [1,2,5,6] | [1,2,5,6] |
| [1,2,0,0] | 2 | [5,6] | 2 | [1,2,5,6] | [1,2,5,6] |

### One edge case I tested:

**Input:**

nums1 = [0,0,0]  
m = 1  
nums2 = [-1,2]  
n = 2

**Expected output:** [-1,0,2]

**Actual output:** [-1,0,2]

This case checks that zero can be a legitimate meaningful value in nums1 and should not automatically be treated as an empty placeholder.

Only m determines how many entries in nums1 are meaningful.

---

## 6. One-Minute Reflection

### Why does my solution work?

Both input arrays are already sorted.

Therefore, the largest remaining element must be either nums1[i] or nums2[j].

By comparing these two elements and placing the larger one at the last available position, I ensure that the sorted suffix grows correctly after every iteration.

Since the algorithm starts writing from the end of nums1, it does not overwrite any elements that still need to be processed.

### Time Complexity

**Time complexity:** O(m+n)

Each iteration fills one destination position and decreases at least one source index. There are at most m+n iterations.

**Space complexity:** O(1)

The algorithm only uses three integer indices and does not require an additional array.

### What idea from the OCW lecture did I transfer to this new problem?

I transferred the two-pointer comparison strategy from the merge step of Merge Sort.

However, instead of merging from left to right into a new array, I merged from right to left into the original array to reduce auxiliary space complexity.

### One thing I understand better now:

When two arrays are already sorted, they can be merged in linear time without performing another complete sorting process.

I also understand that choosing the correct traversal direction can prevent overwriting unprocessed elements and reduce memory usage.

### One thing I am still unsure about:

How to merge two sorted arrays in place when the first array does not contain additional buffer positions, and how to optimize the tradeoff between time complexity and space complexity.