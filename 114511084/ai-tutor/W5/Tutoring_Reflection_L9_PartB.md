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
**Date:** 2026-10-05  
**Topic:** Python Classes and Inheritance (MIT 6.0001 Lecture 9)  
**Language:** C++17（題目原本用 Python 出，我用 C++ 實作）  

---

### 1. Today's Challenge

**Core concept from today's OCW lecture:**  
父類別與子類別、覆寫（override）方法、用 class variable 產生唯一 id（`Rabbit.tag`）。

**AI-generated coding challenge title:**  
Bank Account Hierarchy

---

### 2. My Initial Approach — Before AI Help

**Before asking AI for hints, briefly describe how you planned to solve the problem.**

**My approach:**  
用 class variable 當作 id 計數器。`CheckingAccount` 本來打算整個覆寫 `withdraw`，後來改成把「最低餘額」抽成一個方法，讓子類別只要覆寫這個規則。`SavingsAccount` 覆寫 `withdraw`，先檢查次數，再呼叫父類別的版本。

---

### 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

* [ ] No — I solved it independently
* [x] Yes — I received one or more hints

**The most useful hint/question from AI was:**  
`SavingsAccount` 和 `CheckingAccount` 的 `withdraw` 跟父類別比起來，真正不一樣的只有哪一條規則？能不能只把那一條規則抽出來給子類別覆寫？另外，提款失敗的時候，次數應該在什麼時候 +1？

**It helped me realize that:**  
可以把「最低餘額」抽成一個 `virtual` 方法，`CheckingAccount` 只要覆寫它，不用重寫整個 `withdraw`。次數要在呼叫父類別的 `withdraw` 成功之後才 +1，失敗的提款才不會用掉次數。

---

### 4. My Revision

**Did you change your approach or code after interacting with AI?**

* [ ] No
* [x] Yes

**What did you change, and why?**  
有兩處：(1) 寫完檢查程式碼時，發現建構子初始化列表的順序（`id`、`owner_`、`balance_`）跟成員宣告的順序不一樣。C++ 是依照宣告順序初始化的，雖然這裡不會造成錯誤，但會觸發 `-Wreorder` 警告，所以改成跟宣告順序一致（`id`、`balance_`、`owner_`）。(2) 「失敗的提款是否算一次」是我額外考慮到的，所以在測試裡補了一個先失敗、再成功 3 次的例子。所有自我檢查第一次就通過了。

---

### 5. Verification

**My final program:**

* [x] Passed the provided examples
* [x] Passed additional edge cases
* [x] Still has unresolved problems

**One edge case I tested:**  
```text
Input: SavingsAccount("Ben", 1050); 依序 withdraw(100000)、withdraw(1) × 4

Expected output: 第 1 次拋出例外（餘額不足，不算次數），接著 3 次成功，第 5 次拋出例外（超過 3 次），最後餘額是 1047.00
Actual output: ValueError ok ok ok ValueError，餘額 1047.00
```

**Unresolved problems:**  
金額用 `double` 存，會有浮點數誤差（例如 `0.1 + 0.2 != 0.3`）。在餘額剛好等於下限的情況，`balance_ - amount < min_balance()` 有可能判斷錯誤。實務上應該用整數「分」來存金額，但題目要求顯示到小數點後兩位，而且範例都是整數，所以我沒有改，也沒有測小數金額的邊界情況。

---

### 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**  
跟 lecture 的 `Rabbit.tag` 一樣，用 class variable（C++ 是 `static` 成員）產生唯一 id；子類別重用父類別的建構子，只覆寫真正不一樣的行為，像 `Student` 繼承 `Person`。

**One thing I understand better now:**  
C++ 要加 `virtual` 才會動態分派，Python 的方法預設就是。另外，Python 寫成 `self.next_id += 1` 會在物件上建立新的 instance variable，class variable 不會改變，每個帳戶的 id 都會是 1。

**One thing I am still unsure about:**  
題目說「最多只能成功提款 3 次」，我的解讀是**失敗的提款不算次數**。不確定出題者的意思是不是這樣，還是「嘗試 3 次」就不能再提了。

---
