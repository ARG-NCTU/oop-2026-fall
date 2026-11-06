**Topic:** Introduction and Optimization Problems  
**Date:** 2026-11-06

---

### ① Check My Understanding

**Questions completed:** 5 / 5

**Answers revised after AI hints:** 0 / 5

### ② My Misconception

**Before: I thought…**

I understood that optimization problems involve finding the best solution, but I had not fully distinguished between locally optimal choices and globally optimal solutions.

**Now: I understand…**

An optimization problem consists of an objective function and a set of constraints, which can be empty. The objective function defines what we want to maximize or minimize, while constraints determine which solutions are feasible.

I also understand that greedy algorithms make locally optimal choices, but these choices do not necessarily lead to the global optimum. In contrast, brute-force algorithms can guarantee the optimal solution by examining every possible subset, although their exponential computational complexity makes them inefficient for large problems.

Running multiple greedy algorithms with different criteria and choosing the best result still does not guarantee a globally optimal solution.

---

### ③ Challenge the AI

**One AI-generated question I challenged:**

Question 1 — Whether an optimization problem must always have at least one constraint.

**Why?**

☑ Ambiguous  
☐ Oversimplified  
☐ Technically questionable  
☐ Too easy  
☐ Other: __________

**Brief explanation:**

The question was not particularly ambiguous, but it tested a fundamental distinction that could easily be misunderstood. According to the lecture, an optimization problem requires an objective function and a set of constraints, which may be empty. Therefore, constraints are not necessarily required.

### ④ One-Minute Reflection

**One thing I am still unsure about:**

I would like to understand more about when greedy algorithms can actually guarantee a globally optimal solution. I understand that greedy algorithms do not always work for the general 0/1 knapsack problem, but I am still curious about what characteristics of a problem make a greedy strategy optimal, and how we can prove that it always produces the best solution.