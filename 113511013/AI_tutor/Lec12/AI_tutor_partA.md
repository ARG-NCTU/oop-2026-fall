# AI Tutor — Part A | Lecture 12

**Topic:** Searching and Sorting Algorithms — Amortized Cost, Bubble Sort, Selection Sort, and Merge Sort  
**Date:** 2026/11/10  
**Source:** MIT 6.0001 Lecture 12, Searching and Sorting Algorithms  
**Record type:** AI-prepared sample answers and reflections.

## ① Check My Understanding

**Questions completed:** 5 / 5 (AI-written responses)  
**Answers revised after AI hints:** 0 / 5

### Q1 — Sort Then Search

**Statement:** For one search in an initially unsorted list, sorting the list with an O(n log n) algorithm and then using binary search is asymptotically faster than simply doing one linear search.

**Sample answer:** **False.** Sorting once and searching once takes O(n log n) + O(log n) = O(n log n), whereas a single linear search takes O(n).

Sorting first does not give a better asymptotic bound for one search.

**AI self-check question:** Are you counting the sorting cost as well as the final binary-search cost?

**Revision:** No change; the input is initially unsorted, so the preprocessing cost cannot be ignored.

**Concept learned:** Analyze the entire workflow, not just the fastest individual operation inside it.

### Q2 — Repeated Searches and Amortized Cost

**Statement:** If many searches will be performed on the same list without changing its contents, the one-time sorting cost can become worthwhile even though it is not worthwhile for a single search.

**Sample answer:** **True.** With k queries, repeated linear search requires O(kn), while sorting once and then performing binary searches requires O(n log n + k log n).

For sufficiently many queries, the upfront sorting cost can be shared across the searches.

**AI self-check question:** How does the comparison change when k = 1 versus when k grows much larger than log n?

**Revision:** No change; the conclusion depends on how many future searches occur and on the actual implementation constants.

**Concept learned:** Paying an upfront preprocessing cost may reduce total work over a long sequence of operations.

### Q3 — Bubble Sort Versus Selection Sort

**Statement:** With the early-stop Bubble Sort shown in the slides, an already sorted list requires only one comparison pass, while Selection Sort still examines the remaining unsorted portion on every pass.

**Sample answer:** **True.** Bubble Sort uses a flag to stop after a complete pass with no swaps, so a sorted list needs O(n) comparisons.

Selection Sort still performs O(n²) comparisons because it checks the remaining elements for every position.

**AI self-check question:** Does one pass mean a single comparison, or does it mean n−1 adjacent comparisons?

**Revision:** No change; one comparison pass is not O(1) work. It still scans adjacent pairs across the list.

**Concept learned:** An early-termination condition can improve best-case time without changing worst-case complexity.

### Q4 — Selection Sort Invariant

**Statement:** After the first two passes of Selection Sort, the first two elements are guaranteed to be the two smallest elements in sorted order, even if the rest of the list remains unsorted.

**Sample answer:** **True.** Every pass selects the minimum from the remaining unsorted portion and moves it to the beginning of that portion.

After two passes, the first two positions contain the two smallest values in order.

**AI self-check question:** After placing the minimum in position 0, what is guaranteed about every element remaining to its right?

**Revision:** No change; the invariant holds after each completed pass.

**Concept learned:** A loop invariant can prove the correctness of a sorting algorithm, not just estimate its running time.

### Q5 — Merge Sort Analysis

**Statement:** Because Merge Sort halves the input on each recursive level, its full running time is O(log n), even though merging the sorted pieces requires additional work.

**Sample answer:** **False.** Merge Sort has O(log n) recursive levels, but merging all sublists at a given level takes O(n) work in total.

Therefore, the complete running time is O(n log n).

**AI self-check question:** At one recursive level, how many total elements are copied into merged lists across all subproblems?

**Revision:** No change; we must multiply the O(n) work per level by O(log n) levels.

**Concept learned:** Divide-and-conquer depth alone does not determine total complexity. The amount of work at each level also matters.

---

## ② My Misconception

### Before: I thought…

Merge Sort should take only O(log n) because it repeatedly divides the list in half, just like Binary Search.

I overlooked the additional merging operations.

### Now: I understand…

Binary Search keeps only one half of a search range, but Merge Sort sorts both halves and combines them.

Even though the recursion depth is O(log n), each level processes O(n) elements during merging, so the total complexity is O(n log n).

I also understand why one-time sorting can be worthwhile when a list will be searched many times.

---

## ③ Challenge the AI

### One AI-generated question I challenged:

Q3 — An already sorted list requires only one comparison pass in the lecture's Bubble Sort implementation.

### Why?

* [x] Ambiguous
* [ ] Oversimplified
* [ ] Technically questionable
* [ ] Too easy
* [ ] Other

### Brief explanation:

The phrase "one comparison pass" could be mistaken for one comparison.

In fact, the pass still compares each adjacent pair, so it performs n−1 comparisons and takes O(n) time.

The important distinction is between the number of passes and the number of comparisons within a pass.

---

## ④ One-Minute Reflection

### One thing I am still unsure about:

How to prove the O(n log n) complexity of Merge Sort using a recursion tree, and how specialized sorting algorithms can achieve better complexity than comparison-based sorting algorithms.