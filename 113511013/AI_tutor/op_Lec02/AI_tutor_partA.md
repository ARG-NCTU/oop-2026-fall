# AI Tutor — Part A | Optimization Lecture 2

**Topic:** Optimization Problems — Search Trees, Memoization, and Dynamic Programming
**Date:** 2026/11/21
**Record type:** AI-prepared sample answers and reflections.

## ① Check My Understanding

**Questions completed:** 5 / 5 (AI-prepared responses)
**Answers revised after AI hints:** 0 / 5

### Q1 — Recursive Search Trees

**Statement:** A recursive search tree for the 0/1 knapsack problem can have exponential time complexity even if branches violating the capacity constraint are removed.

**Sample answer:** **True.**

Each item can generate two branches: taking the item or not taking it.

If the capacity is sufficiently large, most or all branches remain feasible.

For n items, a complete search tree contains:

1 + 2 + 4 + ... + 2^n = 2^(n+1) - 1 nodes.

Therefore, the worst-case complexity remains O(2^n) under the lecture's node-count model.

**AI self-check question:** What happens if the knapsack capacity is large enough to contain every item?

**Concept learned:** Pruning can reduce actual computation without necessarily improving worst-case complexity.

### Q2 — Optimal Substructure

**Statement:** A problem has optimal substructure if its globally optimal solution can be constructed from optimal solutions to smaller subproblems.

**Sample answer:** **True.**

For the knapsack problem, the optimal solution can be determined by comparing two possibilities:

* The optimal solution when the current item is selected.
* The optimal solution when the current item is not selected.

The better feasible result becomes the optimal solution of the current problem.

**AI self-check question:** Why do we need to compare both decisions instead of always selecting the current item?

**Concept learned:** Optimal substructure allows a larger optimization problem to be solved recursively.

### Q3 — Overlapping Subproblems

**Statement:** Two recursive calls must represent different subproblems if they are reached through different previous decisions.

**Sample answer:** **False.**

In the knapsack problem, two different decisions may result in the same remaining items and remaining capacity.

Although the previously selected items may be different, the remaining optimization problem is identical.

For example, choosing either of two different items with the same weight can lead to the same remaining capacity.

**AI self-check question:** Does the best additional value depend on the identities of previously selected items if the available capacity and remaining items are identical?

**Concept learned:** Different recursion paths can lead to overlapping subproblems.

### Q4 — Memoization State

**Statement:** In the knapsack problem, using only the remaining capacity as the memoization key is always sufficient.

**Sample answer:** **False.**

The optimal result depends not only on the remaining capacity but also on which items are still available.

Two recursive calls may have the same remaining capacity but different remaining items.

Their optimal values may therefore be different.

The memoization key should include both the remaining capacity and the position of the next item.

**AI self-check question:** Would a remaining capacity of 5 produce the same result when the remaining items have different values?

**Concept learned:** A dynamic programming state must contain enough information to uniquely determine the subproblem.

### Q5 — Dynamic Programming Complexity

**Statement:** Memoization always converts an exponential recursive algorithm into a polynomial-time algorithm.

**Sample answer:** **False.**

Memoization prevents the same subproblem from being solved repeatedly.

However, its running time still depends on the number of distinct subproblems.

For a 0/1 knapsack problem with n items and integer capacity W, an index-based dynamic programming implementation can have O(nW) states.

This is pseudo-polynomial because W is a numerical value rather than the number of bits required to represent that value.

**AI self-check question:** What happens if W itself grows exponentially with the input encoding length?

**Concept learned:** Memoization improves efficiency by eliminating duplicate calculations, but its complexity depends on the number of unique states.

---

## ② My Misconception

### Before: I thought…

Adding a memoization table to any recursive algorithm would automatically reduce its time complexity from exponential to polynomial.

I also thought that the remaining capacity alone was sufficient to identify a knapsack subproblem.

### Now: I understand…

Dynamic programming is particularly useful when a problem contains optimal substructure and overlapping subproblems.

Memoization stores previously computed results so that identical subproblems do not need to be solved again.

However, the number of distinct states still determines the overall computational complexity.

For the knapsack problem, both the remaining items and the remaining capacity must be included in the state.

---

## ③ Challenge the AI

### One AI-generated question I challenged:

Q5 — Memoization always converts an exponential recursive algorithm into a polynomial-time algorithm.

### Why?

* [ ] Ambiguous
* [x] Oversimplified
* [x] Technically questionable
* [ ] Too easy
* [ ] Other

### Brief explanation:

Memoization reduces repeated calculations but does not necessarily reduce the number of distinct subproblems.

If a problem still contains exponentially many unique states, memoization cannot guarantee polynomial-time complexity.

For the integer 0/1 knapsack problem, an O(nW) dynamic programming algorithm is pseudo-polynomial rather than polynomial in the encoded input length.

Therefore, both the number of states and the cost of computing each state must be considered.

---

## ④ One-Minute Reflection

### One thing I am still unsure about:

How to systematically identify the minimum amount of information required to represent a dynamic programming state.

I would also like to understand how to convert recursive memoization into an iterative dynamic programming implementation and reduce its space complexity.