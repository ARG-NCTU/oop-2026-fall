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
**Date:** 2026-11-16  
**Topic:** Graph-theoretic Models, DFS, BFS (MIT 6.0002 Lecture 3)  
**Language:** C++17（題目原本用 Python 出，我用 C++ 實作）  

---

### 1. Today's Challenge

**Core concept from today's OCW lecture:**  
把問題建成圖，再用 BFS 找最短路徑（`BFS`）。

**AI-generated coding challenge title:**  
Word Ladder

---

### 2. My Initial Approach — Before AI Help

**Before asking AI for hints, briefly describe how you planned to solve the problem.**

**My approach:**  
單字是節點，差一個字母就有一條邊。用 BFS，走到哪裡才找鄰居：把每個位置換成 a–z，在字典裡而且還沒走過的就加入 queue。跟最後的方法一樣。

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
第一版就通過所有測資，演算法沒有改過。改成 C++ 時，從「每次用切片串出新字串」改成「原地改一個字元，檢查完再改回去」，減少字串配置。另外，從 queue 取出元素時用複製（`auto [word, steps] = q.front();`），不用參考，因為下一行就會 `pop()`，參考會失效。

---

### 5. Verification

**My final program:**

* [x] Passed the provided examples
* [x] Passed additional edge cases
* [x] Still has unresolved problems

**One edge case I tested:**  
```text
Input: begin = "abc", end = "abd", words = {"abd"}（begin 不在字典裡）

Expected output: 2
Actual output: 2
```

**Unresolved problems:**  
只測了題目給的小例子，沒有測 N = 5000、L = 10 的大資料，所以 O(N × 26 × L²) 實際跑多快沒有實測過。另外沒有處理「單字長度不一致」的輸入，因為題目保證長度都相同。

---

### 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**  
把單字轉換建模成圖（單字是節點、差一個字母是邊），再用 lecture 的 BFS 找最短路徑。每條邊的權重都是 1，所以 BFS 第一次碰到目標就是最短路徑。

**One thing I understand better now:**  
不一定要先把整張圖建出來：先建圖要兩兩比較，O(N² × L)；走到哪裡才產生鄰居比較快。另外，只存步數比 lecture `BFS` 存整條 `path` 省記憶體。

**One thing I am still unsure about:**  
沒有。

---
