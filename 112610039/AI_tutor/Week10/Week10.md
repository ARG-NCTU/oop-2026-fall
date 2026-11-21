# AI Tutor for AOOP 2026 - Week 10 Learning Record

## Part A: True or False

**Topic:** Optimization Problems — Search Trees & Dynamic Programming (6.0002 Lecture 2)  
**Date:** 2026-11-21

### ① Check My Understanding
* **Questions completed:** 5 / 5
* **Answers revised after AI hints:** 0 / 5 (Answered all 5 correctly on the first attempt!)

### ② My Misconception
* **Before:** I used to think that pruning infeasible branches in a search tree could reduce the worst-case asymptotic complexity from exponential to polynomial, or that the memoization key needed to include the history of already-taken items.
* **Now:** I understand that pruning reduces the practical number of visited nodes, but the worst-case time complexity of a search tree remains exponential ($O(2^{n+1})$). Furthermore, because previously chosen items do not affect the optimal choices for remaining items given the remaining capacity, the memo key only needs `(len(to_consider), avail)`.

### ③ Challenge the AI
* **One AI-generated question I challenged:** Question 1
* **Why?**
  - [ ] Ambiguous
  - [x] Oversimplified
  - [ ] Technically questionable
  - [ ] Too easy
  - [ ] Other: __________________
* **Brief explanation:** While pruning clearly cannot change the worst-case exponential Big-O bound (e.g., when all items are light enough to fit), in practical workloads with tight weight constraints, pruning eliminates massive subtrees early and significantly speeds up execution.

### ④ One-Minute Reflection
* **One thing I am still unsure about:** How bottom-up tabulation (2D DP array) compares in memory overhead and cache locality against top-down recursive memoization when item weights are floating-point numbers rather than integers.

---

## Part B: LeetCode-style Lecture Code Transfer

**Name:** [ 請填寫你的姓名 / 學號 ]  
**Date:** 2026-11-21  
**Topic:** Search Trees, Optimal Substructure & Memoized Dynamic Programming

### 1. Today’s Challenge
* **Core concept from today’s OCW lecture:** Solving the 0/1 Knapsack problem for an exact global optimum by combining a top-down binary decision tree with memoization (`(len(to_consider), avail)` state keys) to eliminate overlapping subproblems.
* **AI-generated coding challenge title:** Exact 0/1 Knapsack Solver with Memoization (`solve_knapsack_dp`)

### 2. My Initial Approach — Before AI Help
* **My approach:** Implemented input validation in both `Item` and `solve_knapsack_dp` (`isinstance` checks and non-negative/positive value constraints). Built an inner recursive helper `fast_max_val` that checks base cases (`len(to_consider) == 0 or avail == 0`), queries `memo[(len(to_consider), avail)]`, prunes items heavier than `avail`, and compares `with_val` vs. `without_val` before caching and returning the optimal tuple.

### 3. AI Tutor Help
* **Did you ask the AI Tutor for help?**
  - [x] No — I solved it independently
  - [ ] Yes — I received one or more hints
* **The most useful hint/question from AI was:** N/A (Solved independently; received a minor style tip to initialize `memo = {}` explicitly in the outer function rather than as a default argument)
* **It helped me realize that:** Explicitly passing a freshly initialized `memo` dictionary from the wrapper function avoids mutable default argument linter warnings while keeping recursion state isolated per call.

### 4. My Revision
* **Did you change your approach or code after interacting with AI?**
  - [x] No
  - [ ] Yes
* **What did you change, and why?** No structural logic revisions were needed as the initial implementation passed all defensive checks, memoization lookups, and optimal value tests.

### 5. Verification
* **My final program:**
  - [x] Passed the provided examples
  - [x] Passed additional edge cases
  - [ ] Still has unresolved problems
* **One edge case I tested:**
  - **Input:** `items = [Item("a", 6, 3), Item("b", 7, 3), Item("c", 8, 2), Item("d", 9, 5)]`, `max_weight = 5`
  - **Expected output:** `best_val = 15`, `[item.name for item in best_items] = ['c', 'b']`
  - **Actual output:** `best_val = 15`, `['c', 'b']`

### 6. One-Minute Reflection
* **What idea from the OCW lecture did you transfer to this new problem?** Exploiting optimal substructure and overlapping subproblems by caching `(len(to_consider), avail)` states in a hash map to avoid re-solving identical suffix-capacity subtrees.
* **One thing I understand better now:** Why dynamic programming guarantees the true global optimum (unlike greedy heuristics) while trading space to collapse an exponential call tree into distinct state evaluations.
* **One thing I am still unsure about:** How to reconstruct or count all tied optimal item combinations when multiple subsets achieve the exact same maximum value.