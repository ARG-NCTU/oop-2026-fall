# AI Tutor for AOOP 2026 - Week 9 Learning Record

## Part A: True or False

**Topic:** Introduction and Optimization Problems (6.0002 Lecture 1)  
**Date:** 2026-11-19

### ① Check My Understanding
* **Questions completed:** 5 / 5
* **Answers revised after AI hints:** 1 / 5 (Revised Question 1 after distinguishing an empty constraint set from an empty feasible region)

### ② My Misconception
* **Before:** I used to think an optimization model must always have at least one constraint, confusing "no constraints" with "no feasible combinations satisfying constraints."
* **Now:** I understand that an optimization model consists of an objective function and a set of constraints that can be empty (unconstrained optimization). I also reinforced why brute-force 0/1 Knapsack requires $O(2^n)$ time to enumerate the power set, whereas greedy approximations run in $O(n \log n)$ time without guaranteeing a global optimum.

### ③ Challenge the AI
* **One AI-generated question I challenged:** Question 1
* **Why?**
  - [x] Ambiguous
  - [ ] Oversimplified
  - [ ] Technically questionable
  - [ ] Too easy
  - [ ] Other: __________________
* **Brief explanation:** The phrasing "constraint set is empty" can easily be misread as "no solution satisfies the constraints" (infeasible problem) rather than an unconstrained optimization problem where no restrictions are placed on the variables.

### ④ One-Minute Reflection
* **One thing I am still unsure about:** How exact optimization methods like Dynamic Programming or Search Trees find the true global optimum for the 0/1 Knapsack problem without enumerating all $2^n$ subsets explicitly.

---

## Part B: LeetCode-style Lecture Code Transfer

**Name:** 112610039  
**Date:** 2026-11-19  
**Topic:** Optimization Models, Greedy Algorithms & Higher-Order Functions (`lambda`)

### 1. Today’s Challenge
* **Core concept from today’s OCW lecture:** Formulating the 0/1 Knapsack optimization problem, encapsulating item attributes in a class, and implementing a flexible $O(n \log n)$ greedy algorithm parameterized by `key_func` and `lambda` expressions.
* **AI-generated coding challenge title:** Flexible Knapsack Greedy Solver (`Item` & `flexible_greedy`)

### 2. My Initial Approach — Before AI Help
* **My approach:** Created the `Item` class with type and value validation (`value >= 0`, `weight > 0`) and methods `get_value`, `get_weight`, and `get_density`. Implemented `flexible_greedy` with `isinstance` and `callable(key_func)` checks, sorted a copy of `items` in descending order, and iterated through items to pack the knapsack.

### 3. AI Tutor Help
* **Did you ask the AI Tutor for help?**
  - [ ] No — I solved it independently
  - [x] Yes — I received one or more hints
* **The most useful hint/question from AI was:** Pointing out that using `break` when an item exceeds `max_weight` prematurely terminates the loop and skips lighter items later in the sorted list that could still fit.
* **It helped me realize that:** A greedy knapsack pass must check every candidate item in sorted order (`if total_weight + item.get_weight() <= max_weight:`) rather than stopping at the first overweight item.

### 4. My Revision
* **Did you change your approach or code after interacting with AI?**
  - [ ] No
  - [x] Yes
* **What did you change, and why?** Removed the `break` statement so the loop skips overweight items and continues checking lighter ones, and fixed the f-string syntax typo `f(...)` to `f"..."` in `Item.__str__`.

### 5. Verification
* **My final program:**
  - [x] Passed the provided examples
  - [x] Passed additional edge cases
  - [ ] Still has unresolved problems
* **One edge case I tested:**
  - **Input:** `max_weight = 500`, `key_func = Item.get_value` on `[wine, beer, pizza, burger, apple]`
  - **Expected output:** `[burger, wine]` with `total_value = 189.0` (skipping `pizza` and `beer`, then fitting `wine`)
  - **Actual output:** `[burger, wine]` with `total_value = 189.0`

### 6. One-Minute Reflection
* **What idea from the OCW lecture did you transfer to this new problem?** Decoupling the greedy selection mechanism from the evaluation metric by passing `key_func` (method references or `lambda` expressions) into `sorted()`.
* **One thing I understand better now:** How inverting a metric with `lambda x: 1 / x.get_weight()` converts a descending sort (`reverse=True`) into a lightest-first greedy heuristic.
* **One thing I am still unsure about:** How to quantify the worst-case approximation ratio of greedy heuristics compared to optimal 0/1 Knapsack solutions.
