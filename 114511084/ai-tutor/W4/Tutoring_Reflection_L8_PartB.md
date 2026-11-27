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
**Date:** 2026-09-28  
**Topic:** Object Oriented Programming (MIT 6.0001 Lecture 8)  
**Language:** C++17（題目原本用 Python 出，我用 C++ 實作）  

---

### 1. Today's Challenge

**Core concept from today's OCW lecture:**  
自訂 class、`__init__`、`__str__`，以及用 special methods 讓物件支援 `+`、`-`、`==`（`Fraction`）。

**AI-generated coding challenge title:**  
Clock Class

---

### 2. My Initial Approach — Before AI Help

**Before asking AI for hints, briefly describe how you planned to solve the problem.**

**My approach:**  
只存「總分鐘數 mod 1440」，加減就是總分鐘數相加減之後再 mod，比較相等就是比較這個整數。跟最後的方法一樣。

---

### 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

* [ ] No — I solved it independently
* [x] Yes — I received one or more hints

**The most useful hint/question from AI was:**  
時間一定要存成「時」和「分」兩個數字嗎？如果只用一個數字表示，加減和比較會不會比較好寫？再算算看，C++ 的 `-1 % 1440` 會得到多少？

**It helped me realize that:**  
存成「從午夜開始的總分鐘數」，加減、比較都只要一行。但 C++ 的 `%` 遇到負數，結果也是負數，要先加 1440 再 mod 一次，才能保證結果在 0–1439 之間。

---

### 4. My Revision

**Did you change your approach or code after interacting with AI?**

* [ ] No
* [x] Yes

**What did you change, and why?**  
Python 版第一次就通過了。改成 C++ 時，把 mod 的寫法從 `x % 1440` 改成 `(x % 1440 + 1440) % 1440`。原因是 C++ 的 `-1 % 1440` 是 `-1`，不是 Python 的 1439，直接照搬的話，`Clock(0, -1)` 會出錯。這是改寫時就想到的，不是測資沒過。另外，C++17 不會自動用 `==` 產生 `!=`，所以多寫了 `operator!=`。

---

### 5. Verification

**My final program:**

* [x] Passed the provided examples
* [x] Passed additional edge cases
* [ ] Still has unresolved problems

**One edge case I tested:**  
```text
Input: Clock(-1000000, -1000000).str()（題目允許的最小值）

Expected output: "21:20"（−61,000,000 mod 1440 = 1280 分鐘，另外用 Python 驗算過）
Actual output: "21:20"
```

---

### 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**  
跟 lecture 的 `Fraction` 一樣，用 special methods（C++ 是 operator overloading）讓自訂型別支援 `+`、`-`、`==`，而且每次運算都回傳新物件，不修改原本的物件。

**One thing I understand better now:**  
選對內部表示法，所有運算都會變簡單：存總分鐘數時，每個時間只有一種表示方式，`==` 直接比較整數就好。另外，只寫 `==` 時，Python 3 和 C++20 會自動提供 `!=`，C++17 不會。

**One thing I am still unsure about:**  
沒有。

---
