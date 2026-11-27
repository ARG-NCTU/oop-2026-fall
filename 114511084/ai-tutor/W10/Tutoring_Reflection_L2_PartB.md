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
**Date:** 2026-11-09  
**Topic:** Decision Trees, Dynamic Programming (MIT 6.0002 Lecture 2)  
**Language:** C++17（題目原本用 Python 出，我用 C++ 實作）  

---

### 1. Today's Challenge

**Core concept from today's OCW lecture:**  
子問題重疊時用 memo 避免重算（`fastMaxVal(toConsider, avail, memo)`、`fastFib`）。

**AI-generated coding challenge title:**  
Minimum Coins

---

### 2. My Initial Approach — Before AI Help

**Before asking AI for hints, briefly describe how you planned to solve the problem.**

**My approach:**  
由小到大填表，`best[a] = min(best[a - c] + 1)`。湊不出來的保持 INF，最後回傳 -1。跟最後的方法一樣。

---

### 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

* [ ] No — I solved it independently
* [x] Yes — I received one or more hints

**The most useful hint/question from AI was:**  
先用 `{1, 3, 4}` 湊 6 試試看「每次拿最大面額」的做法，答案對嗎？接著想：湊出金額 a 的最少硬幣組合裡，最後一枚硬幣如果是 c，前面那些硬幣湊出的是多少錢？那部分也要是最少的嗎？

**It helped me realize that:**  
貪婪法會出錯（4+1+1 是 3 枚，但 3+3 只要 2 枚）。正確的關係是 `best[a] = min(best[a - c] + 1)`，從小金額往大金額填表，每個金額只要算一次。

---

### 4. My Revision

**Did you change your approach or code after interacting with AI?**

* [ ] No
* [x] Yes

**What did you change, and why?**  
解法第一版就通過所有測資，沒有改過。改成 C++ 時，一開始就加上 `best[a - c] != INF` 的檢查，因為 Python 的 `inf + 1` 還是 inf，但 C++ 的 `INT_MAX + 1` 會溢位。**我改過的是測試程式**：一開始寫的暴力解對照組沒有 memo，是指數時間，而且外面包的那層 memo 其實沒有作用，所以改成真正的 top-down memo 遞迴，再拿來跟 bottom-up 的答案比對。

---

### 5. Verification

**My final program:**

* [x] Passed the provided examples
* [x] Passed additional edge cases
* [ ] Still has unresolved problems

**One edge case I tested:**  
```text
Input: coins = {1, 3, 4}, amount = 6（貪婪法的陷阱）

Expected output: 2（3 + 3；貪婪法會拿 4 + 1 + 1，得到 3）
Actual output: 2
```

---

### 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**  
跟 `fastFib`、`fastMaxVal` 一樣，子問題重疊時每個子問題只算一次。lecture 用 top-down memo，這題改用 bottom-up 填表，沒有遞迴深度的問題。

**One thing I understand better now:**  
memo 的 key 要能完整描述子問題：硬幣數量不限，所以只需要「剩下的金額」；0/1 背包（`fastMaxVal`）每樣東西只能用一次，所以還要記錄 `len(toConsider)`。

**One thing I am still unsure about:**  
思考題「沒有 memo 要算多久」，我用「湊出 500 的排列數約有 116 位數」來估計遞迴樹的大小。這是數量級的估計，不是精確的呼叫次數。

---
