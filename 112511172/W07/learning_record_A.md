---

**Topic:** Understanding Program Efficiency: 2  
**Date:** 2026/10/19

## ① Check My Understanding

**Questions completed:** 5 / 5

**Answers revised after AI hints:** 0 / 5

## ② My Misconception

**Before: I thought…**

I was unsure about the difference between the complexity of a problem itself and the complexity of a particular algorithm. I needed to understand how the running time of an algorithm relates to the best possible solution for a problem.

⸻

**Now: I understand…**

The complexity of an algorithm describes the resources required by that particular algorithm, while the complexity of a problem concerns the best achievable resource bounds among all algorithms that solve it. Knowing the complexity of one algorithm does not establish a lower bound for every possible algorithm. To conclude that a problem has complexity \(\Theta(n)\), we need both an \(O(n)\) upper bound and an \(\Omega(n)\) lower bound. Follow-up questions also help me build a more solid understanding of these concepts.

⸻

## ③ Challenge the AI

**One AI-generated question I challenged:**

The question about whether an algorithm with \(O(n^2)\) running time and a proven \(\Omega(n)\) lower bound means that the problem has complexity \(\Theta(n)\).

⸻

**Why?**

☐ Ambiguous  
☐ Oversimplified  
☐ Technically questionable  
☐ Too easy  
☑ Other: Needed further reasoning

**Brief explanation:**

I initially answered yes because there was a proven lower bound. However, the upper bound was still \(O(n^2)\), so the two bounds did not establish \(\Theta(n)\). After a follow-up question, I realized that we also need an \(O(n)\) upper bound to conclude that the problem has \(\Theta(n)\) complexity.

⸻

## ④ One-Minute Reflection

**One thing I am still unsure about:**

I still want to develop a clearer understanding of how to determine the complexity of a problem itself, especially how to prove lower bounds and establish that no faster algorithm can solve the problem under a given computational model.