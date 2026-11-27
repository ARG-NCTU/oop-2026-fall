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
**Date:** 2026-09-21  
**Topic:** Testing, Debugging, Exceptions, Assertions (MIT 6.0001 Lecture 7)  
**Language:** C++17（題目原本用 Python 出，我用 C++ 實作）  

---

### 1. Today's Challenge

**Core concept from today's OCW lecture:**  
用 `try/except` 處理可預期的錯誤輸入（`get_ratios`），用 `assert` 檢查前提條件（`avg`）。

**AI-generated coding challenge title:**  
Parse Scores

---

### 2. My Initial Approach — Before AI Help

**Before asking AI for hints, briefly describe how you planned to solve the problem.**

**My approach:**  
逐一處理每個元素，嘗試轉成整數，失敗就把無效數量 +1，成功的再檢查是不是 0–100。Python 版直接用 `int()` 加上 `try/except`。

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

* [ ] No
* [x] Yes

**What did you change, and why?**  
Python 版第一次就通過了。改成 C++ 時，想法有變：如果直接把 `int()` 換成 `std::stoi`，結果會是錯的，因為 `stoi("3.5")` 會回傳 3，不會拋出例外，`"3.5"` 就會被誤判成有效分數。這是在查 `stoi` 的行為時發現的，不是測資沒過。所以改成用 `pos` 參數檢查後面只剩空白，另外也加上 `catch (std::out_of_range)`，處理太大的數字。

---

### 5. Verification

**My final program:**

* [x] Passed the provided examples
* [x] Passed additional edge cases
* [x] Still has unresolved problems

**One edge case I tested:**  
```text
Input: {"3.5", nullopt, "85 ", "99999999999"}

Expected output: ({85}, 3)：「3.5」不是整數、nullopt 對應 None、「85 」後面有空白但有效、「99999999999」超出 int 範圍
Actual output: ({85}, 3)
```

**Unresolved problems:**  
(1) 題目說元素「可能是任何型別」，但我的 C++ 版只能表示「字串或 None」，不能表示 Python 裡的 `5`、`5.9`、`True` 這類元素。C++ 的 vector 只能放同一種型別，要完整支援就得用 `std::variant` 或 `std::any`，我沒有做。(2) 有一些字串的轉換結果跟 Python 的 `int()` 不一樣，例如 Python 接受 `"1_000"` 和全形數字，我的 `to_int` 不接受。這些情況沒有測。

---

### 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**  
「正常情況下就會遇到」的錯誤資料用 `try/except`（C++ 是 `try/catch`）處理後繼續執行，像 `get_ratios`；「呼叫的人不應該違反」的前提條件用 `assert` 讓程式立刻失敗，像 `avg`。

**One thing I understand better now:**  
同樣是「把字串轉成整數」，Python 的 `int()` 和 C++ 的 `stoi` 行為不同：`stoi` 只讀開頭的數字，後面多出來的字元不會讓它拋出例外，要自己用 `pos` 檢查。另外 C++ 的 `assert` 在 `NDEBUG` 時會被移除，不能拿來處理正常流程中的錯誤。

**One thing I am still unsure about:**  
用 `vector<optional<string>>` 來表示「可能是 None 的輸入」，以及「輸入不是 list」改成靠編譯器擋下、不用 `assert`，不確定這兩個設計是否符合這題想考的重點（`assert` 的用法）。

---
