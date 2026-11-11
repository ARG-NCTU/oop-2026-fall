# Optimization Problems

**Topic:** Optimization Problems\
**Date:** November 11, 2026

## ① Check My Understanding

**Questions completed:** 5 / 5

**Answers revised after AI hints:** 0 / 5

## ② My Misconception

**Before: I thought…**

I understood that greedy algorithms are efficient but may not find the optimal solution. However, I had not fully understood the relationship between optimal substructure, overlapping subproblems, and the actual complexity reduction achieved by dynamic programming.

---

**Now: I understand…**

I understand that optimal substructure and overlapping subproblems serve different purposes in dynamic programming. Optimal substructure allows a globally optimal solution to be constructed from optimal solutions to smaller subproblems, while overlapping subproblems allow memoization to avoid redundant calculations

Additionally, pruning invalid branches in brute-force search can improve practical performance without changing its worst-case exponential complexity.

## ③ Challenge the AI

**One AI-generated question I challenged:**

Question 5: Whether introducing memoization into the 0/1 Knapsack problem automatically changes its time complexity from exponential to polynomial.

**Why?**

☐ Ambiguous\
☐ Oversimplified\
☑ Technically questionable\
☐ Too easy\
☐ Other: —

**Brief explanation:**

The question could lead to the misconception that memoization always guarantees polynomial-time complexity.

Although memoization ensures that each distinct subproblem is solved only once, the number of distinct subproblems can still be exponential. In the 0/1 Knapsack problem, the available capacity can have many distinct values depending on the combinations of item weights.

Therefore, we need to consider the number of distinct states rather than simply counting how many times each state is solved.

## ④ One-Minute Reflection

**One thing I am still unsure about:**

I am still unsure how to determine the time complexity of a dynamic programming algorithm by counting its distinct subproblems. In particular, I want to understand more clearly how the possible values of the remaining capacity affect the complexity of the 0/1 Knapsack problem, and under what conditions dynamic programming can achieve polynomial-time performance.
