**Topic:** Introduction and Optimization Problems  
**Date:** 2026/11/27

### ① Check My Understanding

Questions completed: **5 / 5**

Answers revised after AI hints: **0 / 5**

### ② My Misconception

**Before: I thought…**

Selecting items with the highest value-to-weight ratio would always produce an optimal solution to a knapsack problem. I also thought that algorithms using the same greedy selection criterion would have the same time complexity.

**Now: I understand…**

A greedy algorithm based on value density guarantees global optimality for the fractional knapsack problem but not for the 0/1 knapsack problem. Additionally, algorithms using the same selection criterion may have different time complexities depending on their implementation. Local optimality does not necessarily guarantee global optimality.

### ③ Challenge the AI

**One AI-generated question I challenged:**

Q1: A solution that achieves a higher profit than every feasible solution should be considered optimal, even if it exceeds the budget constraint.

**Why?**

☐ Ambiguous  
☐ Oversimplified  
☐ Technically questionable  
☑ Too easy  
☐ Other

**Brief explanation:**

The question only tests the basic definition of a feasible solution. A more challenging question could involve hard constraints, soft constraints, and penalty functions, requiring a deeper understanding of how constraints and objective functions influence optimization results.

### ④ One-Minute Reflection

**One thing I am still unsure about:**

I am still unsure how to determine whether an optimization problem satisfies the greedy-choice property and optimal substructure. I also want to understand how dynamic programming can exploit overlapping subproblems to find a globally optimal solution to the 0/1 knapsack problem without exhaustively examining all 2ⁿ possible subsets.