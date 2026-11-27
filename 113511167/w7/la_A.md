**Topic:** Understanding Program Efficiency, Part 2  
**Date:** 2026/11/26

### ① Check My Understanding

Questions completed: **5 / 5**

Answers revised after AI hints: **0 / 5**

### ② My Misconception

**Before: I thought…**

The time complexity of a recursive algorithm could be determined directly from its recursion depth. I also thought that generating 2ⁿ subsets would require only Θ(2ⁿ) time and space.

**Now: I understand…**

The total time complexity of a recursive algorithm depends on its recursion depth, the number of recursive calls, and the computational cost of each call. Additionally, when analyzing algorithms that generate multiple outputs, I must consider both the number of outputs and the size of each output.

### ③ Challenge the AI

**One AI-generated question I challenged:**

Q1: Given T(n) = 5 log₂(n) + 10, increasing the input size from 1,024 to 2,048 produces the same absolute increase in running time as increasing it from 2,048 to 4,096.

**Why?**

☐ Ambiguous  
☐ Oversimplified  
☐ Technically questionable  
☑ Too easy  
☐ Other

**Brief explanation:**

The question only tests a basic mathematical property of logarithmic functions. A more challenging question could involve recursive algorithms with logarithmic recursion depth but different computational costs at each level, requiring deeper complexity analysis.

### ④ One-Minute Reflection

**One thing I am still unsure about:**

I am still unsure how to systematically analyze complex recurrence relations, especially when recursive calls have different input sizes or branching factors. I want to better understand how to determine whether the total computational cost is dominated by the root, the leaf nodes, or the combined work across all recursion levels.