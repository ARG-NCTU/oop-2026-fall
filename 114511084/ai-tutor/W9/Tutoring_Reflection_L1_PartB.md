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
**Date:** 2026-11-02  
**Topic:** Optimization Problems, Greedy Algorithms (MIT 6.0002 Lecture 1)  
**Language:** C++17（題目原本用 Python 出，我用 C++ 實作）  

---

### 1. Today's Challenge

**Core concept from today's OCW lecture:**  
貪婪演算法：依照某個 key 排序，能放就放（`greedy(items, maxCost, keyFunction)`）。key 選得好不好，決定結果是不是最佳解。

**AI-generated coding challenge title:**  
Activity Selection

---

### 2. My Initial Approach — Before AI Help

**Before asking AI for hints, briefly describe how you planned to solve the problem.**

**My approach:**  
依照結束時間排序（平手時比開始時間），能選就選，條件是 `start >= last_end`。跟最後的方法一樣。

---

### 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

* [x] No — I solved it independently
* [ ] Yes — I received one or more hints

**The most useful hint/question from AI was:**  
—（沒有使用 AI 提示）

**It helped me realize that:**  
—

---

### 4. My Revision

**Did you change your approach or code after interacting with AI?**

* [x] No
* [ ] Yes

**What did you change, and why?**  
第一版就通過所有測資，沒有改過。改成 C++ 時用 `stable_sort`，讓 start 和 end 都相同的活動保留原本的順序，跟 Python `sorted` 的行為一致。

---

### 5. Verification

**My final program:**

* [x] Passed the provided examples
* [x] Passed additional edge cases
* [ ] Still has unresolved problems

**One edge case I tested:**  
```text
Input: {{"x", 1, 3}, {"y", 3, 5}}（x 的結束時間剛好等於 y 的開始時間）

Expected output: {"x", "y"}（end == start 不算衝突）
Actual output: {x, y}
```

---

### 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**  
跟 lecture 的 `greedy` 一樣「依照 key 排序，能選就選」，而且 key 的選擇決定是不是最佳解。這題用「結束時間最早」當 key。

**One thing I understand better now:**  
要用反例來檢查 key：「開始時間最早」的反例是 `{A,0,10}, {B,1,2}, {C,3,4}`，「活動時間最短」的反例是 `{A,0,5}, {B,4,7}, {C,6,11}`。「結束時間最早」可以用交換論證說明一定是最佳解：結束得越早，留給後面的時間就越多。

**One thing I am still unsure about:**  
如果有兩個活動的 start 和 end 完全相同，只會選其中一個（排在前面的那個）。題目沒有說這種情況要選哪一個，我照原本的輸入順序選，不確定這是不是出題者預期的結果。

---
