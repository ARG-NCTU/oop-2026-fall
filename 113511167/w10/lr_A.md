**Topic:** Optimization Problems and Dynamic Programming  
**Date:** 2026/11/27

### ① Check My Understanding

Questions completed: **5 / 5**

Answers revised after AI hints: **0 / 5**

### ② My Misconception

**Before: I thought…**

An optimization problem with optimal substructure could always be solved using a greedy algorithm. I also thought that a dynamic programming algorithm with O(nW) time complexity was necessarily a polynomial-time algorithm.

**Now: I understand…**

Optimal substructure alone does not guarantee the correctness of a greedy algorithm. The greedy-choice property is also required. Furthermore, O(nW) is a pseudo-polynomial time bound because the numerical value of W can grow exponentially relative to its binary encoding length.

### ③ Challenge the AI

**One AI-generated question I challenged:**

Q1: If a recursive algorithm for the 0/1 knapsack problem stops exploring branches whenever their total weight exceeds the capacity, the algorithm is guaranteed to have polynomial worst-case time complexity.

**Why?**

☐ Ambiguous  
☐ Oversimplified  
☐ Technically questionable  
☑ Too easy  
☐ Other

**Brief explanation:**

The question can be answered using a simple counterexample in which the total weight of all items does not exceed the knapsack capacity. A more challenging question could combine pruning and memoization, requiring an analysis of the number of explored branches and distinct subproblems.

### ④ One-Minute Reflection

**One thing I am still unsure about:**

I am still unsure how to design efficient dynamic programming states when the knapsack capacity is extremely large or item weights are non-integer values. I also want to better understand how to choose between weight-based dynamic programming, value-based dynamic programming, and alternative strategies such as meet-in-the-middle based on the input constraints.