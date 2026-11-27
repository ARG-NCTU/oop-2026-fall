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
**Date:** 2026-10-12  
**Topic:** Understanding Program Efficiency, Part 1 (MIT 6.0001 Lecture 10)  
**Language:** C++17（題目原本用 Python 出，我用 C++ 實作）  

---

### 1. Today's Challenge

**Core concept from today's OCW lecture:**  
巢狀迴圈是 O(n²)（`isSubset`、`intersect`），換個資料結構可以降到 O(n)。

**AI-generated coding challenge title:**  
Count Pairs with Sum

---

### 2. My Initial Approach — Before AI Help

**Before asking AI for hints, briefly describe how you planned to solve the problem.**

**My approach:**  
O(n²) 版本用兩層迴圈。O(n) 版本由左往右掃，用 hash map 記錄每個值出現過幾次，看到 `x` 就加上 `seen[target - x]`。跟最後的方法一樣。

---

### 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

* [ ] No — I solved it independently
* [x] Yes — I received one or more hints

**The most useful hint/question from AI was:**  
掃到某個元素 `x` 的時候，你需要知道前面的什麼資訊，才能馬上知道它能跟幾個元素配對？有什麼資料結構可以用 O(1) 查到這個資訊？

**It helped me realize that:**  
要知道的是「前面出現過幾個 `target - x`」，所以可以用 hash map 記錄每個值出現的次數，掃一遍就算完，不用兩層迴圈。而且要先查詢再把 `x` 記進去，才不會讓元素跟自己配對。

---

### 4. My Revision

**Did you change your approach or code after interacting with AI?**

* [x] No
* [ ] Yes

**What did you change, and why?**  
第一版就通過所有測資，演算法沒有改過。改成 C++ 時，一開始就把型別設成 `long long`，因為 `target - x` 最大可能是 2×10^9，答案最多約 5×10^9，兩個都超過 `int` 的範圍。

---

### 5. Verification

**My final program:**

* [x] Passed the provided examples
* [x] Passed additional edge cases
* [x] Still has unresolved problems

**One edge case I tested:**  
```text
Input: L = {1000000000, 1000000000}, target = 2000000000（target 超過 int 上限）

Expected output: 1
Actual output: 1
```

**Unresolved problems:**  
`unordered_map` 平均是 O(1)，但如果遇到刻意設計、讓所有 key 都碰撞到同一個 bucket 的資料（anti-hash test），每次操作會退化成 O(n)，總共變成 O(n²)。我沒有測這種情況。

---

### 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**  
lecture 分析過 `intersect` 這種巢狀迴圈是 O(n²)。這題先寫 O(n²) 版本，再發現內層迴圈其實只是在「查詢」，換成 hash map 就能把查詢降到 O(1)，整體變成 O(n)。

**One thing I understand better now:**  
分析複雜度時也要分析數值範圍：`target - x` 和配對數都可能超過 `int`。另外，`[1, 1, 1, 1]` 是 6 組，因為題目算的是索引對，不是值的組合。

**One thing I am still unsure about:**  
題目要求「O(n)」，我的解法是**平均** O(n)，不是最壞情況 O(n)。不確定這樣是否符合要求。如果要保證最壞情況，可以先排序再用雙指標，但那樣會變成 O(n log n)。

---
