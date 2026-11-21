# AI Tutor — Part B | Optimization Lecture 2

**Name:** 范芷祺
**Date:** 2026/11/21
**Topic:** Recursive Optimization, Memoization, and Dynamic Programming
**Record type:** AI-prepared example and reference implementation.

## 1. Today's Challenge

### Core concept from today's OCW lecture:

A recursive optimization problem can be solved by exploring different decisions and comparing the optimal results of smaller subproblems.

If these subproblems overlap, their results can be stored using memoization to avoid repeated computation.

### Coding challenge title:

[LeetCode #198 — House Robber](https://leetcode.com/problems/house-robber/)

### Problem Description

You are given an integer array nums, where nums[i] represents the amount of money stored in the ith house.

You cannot rob two adjacent houses because doing so will trigger an alarm.

Return the maximum amount of money that can be obtained without robbing two adjacent houses.

### Examples

| nums | Output |
|---|---:|
| [1,2,3,1] | 4 |
| [2,7,9,3,1] | 12 |
| [5] | 5 |

---

## 2. My Initial Approach — Before AI Help

### My approach (sample):

I considered using recursion to examine two possible decisions for every house.

* Rob the current house and continue from the house after the next one.
* Skip the current house and continue from the next house.

I would compare the total money obtained from both decisions and return the larger result.

### My initial complexity prediction:

The recursive algorithm can generate two branches at each step.

Without memoization, many subproblems will be computed repeatedly.

Therefore, an upper bound on the worst-case time complexity is O(2^n).

---

## 3. AI Tutor Help

### Did you ask the AI Tutor for help?

* [ ] No — I solved it independently
* [x] Yes — AI-generated self-review hint

### The most useful hint/question from AI:

Suppose two different sequences of previous decisions both lead to the same house index.

Does the maximum amount of money obtainable from that house onward depend on how you arrived there?

### It helped me realize that:

The remaining optimization problem only depends on the index of the current available house.

Different recursive paths may reach exactly the same index.

Therefore, I can store the maximum obtainable value for every starting index and reuse it whenever the same subproblem appears again.

---

## 4. My Revision

### Did you change your approach or code after interacting with AI?

* [ ] No
* [x] Yes — illustrative revision

### What did you change, and why?

I added a memoization vector to store previously computed results.

I defined solve(i) as the maximum amount of money that can be obtained from house i onward.

There are two possible decisions:

* Rob house i: nums[i] + solve(i + 2)
* Skip house i: solve(i + 1)

The recurrence relation is:

solve(i) = max(nums[i] + solve(i + 2), solve(i + 1))

Before performing recursion, I check whether the result has already been stored in the memoization vector.

After computing the result, I store it so that future recursive calls can reuse it.

---

## 5. Verification

### My final program (C++ reference implementation):

```cpp
class Solution {
private:
    int solve(vector<int>& nums, int i,
              vector<int>& memo) {
        if (i >= nums.size()) {
            return 0;
        }

        if (memo[i] != -1) {
            return memo[i];
        }

        int take = nums[i] + solve(nums, i + 2, memo);

        int skip = solve(nums, i + 1, memo);

        if (take > skip) {
            memo[i] = take;
        } else {
            memo[i] = skip;
        }

        return memo[i];
    }

public:
    int rob(vector<int>& nums) {
        int n = nums.size();

        vector<int> memo(n, -1);

        return solve(nums, 0, memo);
    }
};
```

### Verification Cases

| Input | Expected Output |
|---|---:|
| [1,2,3,1] | 4 |
| [2,7,9,3,1] | 12 |
| [5] | 5 |
| [2,8] | 8 |
| [0,0,0] | 0 |
| [2,1,1,2] | 4 |
| [10,1,1,10] | 20 |
| [5,5,5,5,5] | 15 |

### Verification Status

* [x] Normal and edge-case expected outputs identified
* [x] Representative examples manually traced
* [ ] LeetCode submission verified

### One edge case:

**Input:** nums = [2,1,1,2]

**Expected output:** 4

The optimal solution selects the first and last houses.

This demonstrates that simply choosing every other house according to a fixed starting position does not always produce the optimal solution.

---

## 6. One-Minute Reflection

### Why does my solution work?

For each house, every valid solution must either include the current house or exclude it.

If I include the current house, I cannot include the next house, so I continue from index i + 2.

If I exclude the current house, I continue from index i + 1.

By comparing the optimal results of these two cases, I obtain the optimal result for the current index.

Memoization guarantees that each distinct subproblem is computed at most once.

### Time Complexity

**Without memoization:** O(2^n) upper bound.

The recursive algorithm repeatedly computes overlapping subproblems.

**With memoization:** O(n)

There are only n possible in-bounds starting indices.

Each state performs a constant amount of work apart from its recursive calls, and each state is computed only once.

**Auxiliary space complexity:** O(n)

The memoization vector requires O(n) space.

The recursive call stack also requires O(n) space in the worst case.

### What idea from the OCW lecture did I transfer to this new problem?

I transferred the take-or-skip decision pattern from the recursive knapsack algorithm.

I also applied the lecture's memoization technique to avoid solving overlapping subproblems repeatedly.

### One thing I understand better now:

Dynamic programming is not simply a different way to write recursion.

The most important step is identifying the information that defines each subproblem and storing its optimal result.

### One thing I am still unsure about:

How to eliminate recursion and reduce the auxiliary space complexity from O(n) to O(1) by using only the results of the two relevant previous states.