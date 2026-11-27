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
**Date:** 2026-09-14  
**Topic:** Recursion, Dictionaries (MIT 6.0001 Lecture 6)  
**Language:** C++17（題目原本用 Python 出，我用 C++ 實作）  

---

### 1. Today's Challenge

**Core concept from today's OCW lecture:**  
遞迴，加上用 dictionary 做 memoization（`fib_efficient(n, d)`）。

**AI-generated coding challenge title:**  
Climbing Stairs (1, 2, 3 steps)

---

### 2. My Initial Approach — Before AI Help

**Before asking AI for hints, briefly describe how you planned to solve the problem.**

**My approach:**  
用最後一步走 1、2 或 3 階來拆成三個子問題，`ways(n) = ways(n-1) + ways(n-2) + ways(n-3)`，再用 map 記錄算過的結果。跟最後的方法一樣。

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
第一版就通過所有測資，沒有改過。從 Python 改成 C++ 時有兩點不同：(1) 回傳型別改成 `long long`，因為 `count_ways(50) ≈ 1.06×10^13`，用 `int` 會溢位；(2) 查 memo 改用 `find`，不用 `memo[n]`，因為 `operator[]` 遇到不存在的 key 會自動插入 0。

---

### 5. Verification

**My final program:**

* [x] Passed the provided examples
* [x] Passed additional edge cases
* [ ] Still has unresolved problems

**One edge case I tested:**  
```text
Input: n = 0

Expected output: 1（什麼都不走也算一種）
Actual output: 1
```

**Note:**  
如果 n 超過題目限制，從 n = 73 開始 `long long` 也會溢位，但題目限制 n ≤ 50，所以不影響。

---

### 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**  
跟 `fib_efficient` 一樣，把問題拆成更小的同型子問題（最後一步走 1、2 或 3 階），再用 dictionary 存已經算過的結果，從指數時間降到 O(n)。

**One thing I understand better now:**  
Python 的 `memo={}` 預設參數只在定義函式時建立一次，多次呼叫會共用同一個 dict；C++ 的預設參數每次呼叫都會重新求值，最接近 Python 這個行為的是函式裡的 `static` 變數。

**One thing I am still unsure about:**  
沒有。

---
