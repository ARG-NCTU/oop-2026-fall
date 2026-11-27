<!-- AI prompt
I have just studied the following lecture code from today's OCW programming lecture.

[LECTURE CODE]

Act as my AI Tutor.

Based on the concepts and programming patterns demonstrated in the lecture code, generate ONE new LeetCode-style programming challenge.

Requirements:

1. Test the same core concept as the lecture code.
2. Do not simply ask me to reproduce or slightly modify the lecture example.
3. Create a new problem that requires me to transfer what I learned.
4. Use only programming concepts that have been covered in the course so far.
5. Provide:
    * Problem statement
    * Input/output specification
    * Constraints
    * 2-3 examples
6. Do NOT provide code, pseudocode, or the solution.

Before I write code:

7. Ask me to explain my proposed algorithm.
8. Ask me to identify which concept from the lecture code I am applying.
9. If my reasoning is incorrect, give me a hint or counterexample instead of the answer.

After I write my code:

10. Test my solution using normal and edge cases.
11. If my code fails, help me identify the problem without rewriting the solution for me.
12. Ask me to revise my solution.

Finally, ask me to explain:

* Why my solution works
* Its time complexity
* What idea from the lecture code I transferred to this new problem
-->

# 📝 AI Tutor Learning Record — Coding Challenge

**Name:** Yoei  
**Date:** 2026-10-26  
**Topic:** Searching and Sorting (MIT 6.0001 Lecture 12)  
**Language:** C++17（題目原本用 Python 出，我用 C++ 實作）  

---

### 1. Today's Challenge

**Core concept from today's OCW lecture:**  
merge sort 的「切一半、各自處理、再合併」（`merge_sort`、`merge`），O(n log n)。

**AI-generated coding challenge title:**  
Count Inversions

---

### 2. My Initial Approach — Before AI Help

**Before asking AI for hints, briefly describe how you planned to solve the problem.**

**My approach:**  
用 merge sort，在 merge 時，每次從右半拿元素，就把左半還沒拿的個數加進答案。Python 版每一層都用切片建新的 list。

---

### 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

* [ ] No — I solved it independently
* [x] Yes — I received one or more hints

**The most useful hint/question from AI was:**  
merge 的時候，左右兩半都已經排序好了。當你從右半拿走 `right[j]` 時，左半還沒拿的那些元素跟 `right[j]` 比起來是大還是小？它們在原本陣列裡的位置是在 `right[j]` 的前面還是後面？

**It helped me realize that:**  
從右半拿元素的那一刻，左半剩下的元素全都比它大，而且原本都排在它前面，所以一次就能加上「左半剩下的個數」這麼多個反序對，不用一對一對檢查。整體就是 merge sort 的 O(n log n)。

---

### 4. My Revision

**Did you change your approach or code after interacting with AI?**

* [x] No
* [ ] Yes

**What did you change, and why?**  
第一版就通過所有測資，演算法沒有改過。改成 C++ 時調整了兩點：(1) 不再每層建新的 vector，改成共用一個暫存陣列 `buf`，只傳 `[lo, hi)` 索引範圍，減少記憶體配置；(2) 答案改用 `long long`，因為 10^5 個元素最多有約 5×10^9 個反序對，超過 `int` 的範圍。

---

### 5. Verification

**My final program:**

* [x] Passed the provided examples
* [x] Passed additional edge cases
* [ ] Still has unresolved problems

**One edge case I tested:**  
```text
Input: {100000, 99999, ..., 1}（長度 10^5，完全反序）

Expected output: 100000 × 99999 / 2 = 4999950000
Actual output: 4999950000
```

---

### 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**  
沿用 lecture `merge_sort` 的 divide and conquer，在 `merge` 步驟順便計數，所以計數只多了 O(1) 的工作，整體仍然是 O(n log n)。

**One thing I understand better now:**  
相等的元素要先拿左邊，否則會把不算反序對的相等元素也算進去（例如 `[2, 2, 1]` 會多算）。另外 bubble sort 每次交換剛好讓反序對減少 1，所以 bubble sort 的交換次數就等於反序對的數量。

**One thing I am still unsure about:**  
沒有。

---
