# AI Tutor — Part A | Lecture 11

**Topic:** Understanding Program Efficiency: 2 — Complexity Classes, Bisection Search, and Recursion  
**Date:** 2026/11/10  
**Source:** MIT 6.0001 Lecture 11, *Understanding Program Efficiency: 2* (slides 8–17, 21–22, 25–37).  
**Record type:** AI-prepared sample answers and reflections.

## ① Check My Understanding

**Questions completed:** 5 / 5 (AI-written responses)  
**Answers revised after AI hints:** 0 / 5

### Q1 — Constant Complexity

**Statement:** An algorithm that always performs exactly 100 iterations has time complexity O(1), even though it contains a loop, provided each iteration takes constant time.

**Sample answer:** **True.** The number of iterations is fixed at 100 and does not increase with the size of the input. If the work per iteration is also constant, the total work remains constant.

**AI self-check question:** What if the loop still runs 100 times, but each iteration scans all n items of a list?

**Revision:** No change to the answer; the constant-work-per-iteration assumption is essential.

**Concept learned:** A loop does not necessarily imply O(n). Complexity depends on how its work scales with the input.

### Q2 — Bisection Search With Slicing

**Statement:** If a recursive binary search cuts a sorted list in half on each call, it must take O(log n) total time even when every call creates a new list using slicing.

**Sample answer:** **False.** There are O(log n) recursive levels, but creating a slice copies elements. The sizes copied along the recursion path are roughly n/2, n/4, n/8, and so on. Their total is O(n), so this implementation has O(n) total time.

**AI self-check question:** Does halving the number of remaining elements also make the cost of creating a new sublist constant?

**Revision:** No change; the critical distinction is recursive depth versus work within each call.

**Concept learned:** Analyze both the number of calls and the operations performed at each call. Passing low/high indices avoids copying and allows O(log n) time.

### Q3 — Iteration Versus Recursion

**Statement:** The iterative and recursive factorial algorithms can have the same O(n) time complexity, although the recursive version may have additional function-call overhead.

**Sample answer:** **True.** Both versions perform a linear number of multiplication steps under the constant-cost operation model. The recursive version creates more call frames, but the extra constant work per call does not change the asymptotic growth rate.

**AI self-check question:** Does O(n) tell us the exact execution time or the memory needed for recursive calls?

**Revision:** No change. The recursive implementation typically requires O(n) call-stack space, whereas the iterative version can use O(1) auxiliary space.

**Concept learned:** Two algorithms can have the same Big O time complexity while differing in actual overhead and auxiliary space.

### Q4 — Exponential Recursion

**Statement:** For the Towers of Hanoi recurrence T(n) = 2T(n−1) + 1, the total number of moves grows linearly because the problem size decreases by one with each recursive call.

**Sample answer:** **False.** Each non-base case requires solving two smaller problems. Expanding the recurrence gives T(n) = 2^n − 1 moves, so the growth is exponential, O(2^n).

**AI self-check question:** For n = 1, 2, 3, 4, how many moves are required? Is the increase a fixed addition or roughly a doubling?

**Revision:** No change; decreasing the input by one is not enough to guarantee linear time when each call branches into multiple calls.

**Concept learned:** The number of recursive branches matters, not only the amount by which each branch decreases its input.

### Q5 — Recursive Fibonacci

**Statement:** A recursive Fibonacci function that separately evaluates F(n−1) and F(n−2) can perform exponentially many calls, even though both recursive arguments are smaller than n.

**Sample answer:** **True.** The recursion branches and repeatedly recomputes subproblems. The lecture uses O(2^n) as an exponential upper bound.

**AI self-check question:** In the recursion tree for F(5), how many times is F(3) evaluated? Could caching a result avoid this repeated work?

**Revision:** No change; memoization can remove repeated subproblem calculations.

**Concept learned:** Repeated overlapping subproblems make naïve recursive Fibonacci exponentially more expensive than iterative Fibonacci.

---

## ② My Misconception

### Before: I thought…

A recursive algorithm must have O(log n) total time whenever it halves its input at each step, regardless of what happens during each recursive call.

### Now: I understand…

The number of recursive levels and the cost of each level are separate. Binary search with index boundaries has O(log n) time, but using list slicing adds copying work whose total is O(n).

I also understand that a recursion tree with multiple branches can grow exponentially even when each individual argument becomes smaller.

---

## ③ Challenge the AI

### One AI-generated question I challenged:

Q2 — If recursive binary search halves the list on every call, it must take O(log n) total time even when every call uses slicing.

### Why?

* [ ] Ambiguous
* [x] Oversimplified
* [ ] Technically questionable
* [ ] Too easy
* [ ] Other

### Brief explanation:

The question oversimplifies how complexity can be inferred from the number of recursive calls. A complete analysis must account for copying progressively smaller slices.

Multiplying O(log n) by O(n) gives a loose O(n log n) bound, while summing the actual sizes of the slices yields the tighter O(n) bound.

---

## ④ One-Minute Reflection

### One thing I am still unsure about:

How to derive tight bounds from more complicated recursion trees, especially when recursive branches have different sizes or each call performs additional copying.