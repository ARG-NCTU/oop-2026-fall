**Topic:** Searching and Sorting  
**Date:** 2026/11/27

### ① Check My Understanding

Questions completed: **5 / 5**

Answers revised after AI hints: **0 / 5**

### ② My Misconception

**Before: I thought…**

Sorting algorithms with the same time complexity would perform approximately the same number of comparisons and swaps. I also thought that merge sort was inherently stable regardless of its implementation.

**Now: I understand…**

Comparisons and swaps are different operations. Although selection sort and bubble sort both have quadratic worst-case time complexity, selection sort requires significantly fewer swaps. Additionally, merge sort's stability depends on how equal elements are handled during the merging process.

### ③ Challenge the AI

**One AI-generated question I challenged:**

Q1: If the number of search queries is sufficiently large relative to the input size, sorting the list once and performing binary search can have a lower total asymptotic time complexity than repeatedly performing linear search.

**Why?**

☐ Ambiguous  
☐ Oversimplified  
☐ Technically questionable  
☑ Too easy  
☐ Other

**Brief explanation:**

The question directly tests the basic concept of amortizing the initial sorting cost across multiple searches. A more challenging question could involve dynamically inserting or modifying elements between search queries, requiring an analysis of both searching and maintaining sorted order.

### ④ One-Minute Reflection

**One thing I am still unsure about:**

I am still unsure how hybrid sorting algorithms such as Timsort detect naturally ordered runs, determine when to use insertion sort or merging, and maintain sorting stability while achieving efficient performance on different input distributions.