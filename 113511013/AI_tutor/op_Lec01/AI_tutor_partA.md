# AI Tutor — Part A | Optimization Lecture 1

**Topic:** Introduction and Optimization Problems — Knapsack and Greedy Algorithms
**Date:** 2026/11/21
**Record type:** AI-prepared sample answers and reflections.

## ① Check My Understanding

**Questions completed:** 5 / 5 (AI-prepared responses)
**Answers revised after AI hints:** 0 / 5

### Q1 — Objective Functions and Constraints

**Statement:** A solution with the highest objective function value is always the optimal solution, even if it violates one of the constraints.

**Sample answer:** **False.**

An optimal solution must satisfy all constraints. A solution with a higher objective value is not valid if it exceeds the allowed cost or weight.

**AI self-check question:** If a knapsack can carry at most 10 kg, should a combination weighing 12 kg be accepted simply because it has a higher value?

**Concept learned:** Optimization requires finding the best feasible solution rather than simply maximizing the objective function.

### Q2 — The Power Set

**Statement:** A 0/1 knapsack problem containing n items has 2^n possible combinations before applying the capacity constraint.

**Sample answer:** **True.**

Each item has two possible decisions: take it or leave it.

Therefore, the total number of possible combinations is 2^n, including the empty set.

**AI self-check question:** How many possible combinations are added when one more item is introduced?

**Concept learned:** Enumerating all possible subsets leads to exponential growth.

### Q3 — Greedy by Value

**Statement:** Selecting the most valuable available item first always produces an optimal solution to the 0/1 knapsack problem.

**Sample answer:** **False.**

Suppose the knapsack capacity is 10, and there are three items:

| Item | Value | Weight |
|---|---:|---:|
| A | 15 | 10 |
| B | 10 | 5 |
| C | 10 | 5 |

Greedy by value selects A and obtains a total value of 15.

However, selecting B and C produces a total value of 20 without violating the capacity constraint.

**AI self-check question:** Can one locally optimal decision prevent a better combination from being selected later?

**Concept learned:** Local optimality does not necessarily imply global optimality.

### Q4 — Greedy by Density

**Statement:** Selecting items according to their value-to-weight ratio always guarantees the optimal solution to the 0/1 knapsack problem.

**Sample answer:** **False.**

Consider a knapsack with capacity 50.

| Item | Value | Weight | Density |
|---|---:|---:|---:|
| A | 60 | 10 | 6 |
| B | 100 | 20 | 5 |
| C | 120 | 30 | 4 |

Greedy by density selects A and B, obtaining a total value of 160.

However, selecting B and C produces a total value of 220.

**AI self-check question:** What happens when an item cannot be divided into smaller pieces?

**Concept learned:** Greedy by density is not guaranteed to find the optimal solution for the 0/1 knapsack problem.

### Q5 — Greedy Algorithm Complexity

**Statement:** If a greedy algorithm first sorts n items in O(n log n) time and then examines every item once, its total worst-case time complexity is O(n log n).

**Sample answer:** **True.**

The sorting operation requires O(n log n) time.

The subsequent iteration requires O(n) time.

Therefore:

T(n) = O(n log n) + O(n) = O(n log n).

**AI self-check question:** Which operation dominates the total running time as n becomes large?

**Concept learned:** Sequential operations have additive complexities, and the dominant term determines the overall growth rate.

---

## ② My Misconception

### Before: I thought…

Choosing the item with the highest value-to-weight ratio would always produce the optimal solution to a knapsack problem.

### Now: I understand…

A greedy algorithm makes locally optimal decisions, but these decisions do not necessarily produce a globally optimal solution.

For the 0/1 knapsack problem, each item must either be selected completely or not selected at all.

As a result, selecting an apparently efficient item can prevent a better combination of items from being chosen.

---

## ③ Challenge the AI

### One AI-generated question I challenged:

Q4 — Selecting items according to their value-to-weight ratio always guarantees the optimal solution to the knapsack problem.

### Why?

* [ ] Ambiguous
* [x] Oversimplified
* [x] Technically questionable
* [ ] Too easy
* [ ] Other

### Brief explanation:

The answer depends on the type of knapsack problem.

For the 0/1 knapsack problem, greedy by density does not always produce the optimal solution.

However, for the standard fractional knapsack problem, items can be divided, and greedy by density does produce an optimal solution.

Therefore, the type of knapsack problem must be specified clearly.

---

## ④ One-Minute Reflection

### One thing I am still unsure about:

How to determine whether a particular optimization problem can be solved optimally using a greedy algorithm.

I would also like to understand how to prove that a greedy selection rule always leads to a globally optimal solution.