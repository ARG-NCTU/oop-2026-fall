**Topic:** Searching and Sorting Algorithms  
**Date:** 2026-11-02

### ① Check My Understanding

Questions completed: **5 / 5**

Answers revised after AI hints: **0 / 5**

### ② My Misconception

**Before: I thought…**

I tended to focus mainly on the Big-O complexity of an algorithm without always considering the additional operations involved in the implementation or the characteristics of the input data.

**Now: I understand…**

I understand that when comparing algorithms, I need to consider the total computational cost rather than just the complexity of their main operations. For example, binary search requires a sorted list, so the sorting cost must also be considered. Sorting once and performing multiple searches can make binary search more efficient overall because the sorting cost is shared among searches.

I also understand that merge sort has O(n log n) complexity because each recursion level requires O(n) total merging work, and there are O(log n) levels. Additionally, creating sliced sublists in recursive binary search introduces copying costs that can increase the overall complexity from O(log n) to O(n).

Finally, algorithmic complexity does not necessarily represent the actual running time for every input. Bubble sort can finish in O(n) time when the list is already sorted, even though its worst-case complexity is O(n²).

### ③ Challenge the AI

**One AI-generated question I challenged:**

Question 5 — Comparing merge sort and bubble sort, and whether merge sort must always be faster regardless of the initial ordering of the input list.

**Why?**

☐ Ambiguous  
☐ Oversimplified  
☑ Technically questionable  
☐ Too easy  
☐ Other: __________

**Brief explanation:**

The question compared the worst-case complexity of merge sort and bubble sort but asked whether merge sort must always be faster regardless of the initial ordering.

An already sorted list only requires O(n) comparisons in the given bubble sort implementation because it can terminate after the first pass without making any swaps. Merge sort still requires O(n log n) work.

Therefore, worst-case complexity alone cannot determine which algorithm is faster for every particular input.

### ④ One-Minute Reflection

**One thing I am still unsure about:**

I am still curious about how to determine the actual crossover point when comparing two algorithms with different time complexities. For example, even though merge sort has O(n log n) complexity and bubble sort has O(n²) worst-case complexity, how large does the input need to be before merge sort actually becomes faster? I would also like to understand how implementation overhead and input characteristics affect this comparison.