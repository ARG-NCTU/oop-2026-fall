**Topic:** Understanding Program Efficiency, Part 1  
**Date:** 2026/11/26

### ① Check My Understanding

Questions completed: **5 / 5**

Answers revised after AI hints: **0 / 5**

### ② My Misconception

**Before: I thought…**

The time complexity of nested loops could always be determined by multiplying the maximum number of iterations of each loop. I also associated Big O notation exclusively with worst-case complexity.

**Now: I understand…**

The tightest time complexity depends on the total number of operations across all iterations. Nested loops may have a lower complexity than the product of their maximum iteration counts. Additionally, Big O describes an asymptotic upper bound and can be applied to best-case, average-case, and worst-case running times.

### ③ Challenge the AI

**One AI-generated question I challenged:**

Q5: Since Big O notation describes worst-case complexity, describing an algorithm's average-case running time as O(n) is mathematically incorrect, even though its average number of operations grows linearly.

**Why?**

☐ Ambiguous  
☐ Oversimplified  
☑ Technically questionable  
☐ Too easy  
☐ Other

**Brief explanation:**

The question uses the expression “tightly bounded by O(n),” which is less mathematically precise than using Θ(n). Big O represents an asymptotic upper bound, while Big Theta represents a tight asymptotic bound. Distinguishing these notations would make the question more rigorous.

### ④ One-Minute Reflection

**One thing I am still unsure about:**

I am still unsure how to systematically analyze the time complexity of functions that combine recursion, conditional branches, and Python built-in operations with different computational costs, particularly amortized operations such as `list.append()`.