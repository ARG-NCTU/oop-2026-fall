# Name: 朱昱瑋
# Date: 2026/10/15
# Topic: AOOP Lec2 - While Loop、Counter Pattern、Accumulator Pattern

---

## 1. Today’s Challenge

**Core concept from today’s OCW lecture:**

- While Loop
- Counter Pattern
- Accumulator Pattern
- Conditional Branching
- Loop Termination Condition

**AI-generated coding challenge title:**

Digit Balance Detector

---

## 2. My Initial Approach — Before AI Help

**My approach:**

使用 k 作為計數器，使用 total 作為累加器。
透過 while 迴圈持續累加 1+2+...+k，直到總和大於等於 n。
最後判斷 total 是否恰好等於 n，決定輸出 BALANCED 或 OVER。

---

## 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

- [ ] No — I solved it independently
- [x] Yes — I received one or more hints

**The most useful hint/question from AI was:**

A. total 永遠跟著 k 一起變化
B. total 只是在當下複製 k 的值

**It helped me realize that:**

Python 的 Assignment 是將當下的值指定給變數，而不是建立永久連動關係。
因此 total = k 之後，k 再改變時不會影響 total。

---

## 4. My Revision

**Did you change your approach or code after interacting with AI?**

- [x] No
- [ ] Yes

**What did you change, and why?**

沒有修改主要演算法，原始解法已能正確通過測試。
但透過討論更加理解 Assignment 與 Re-binding 的概念。

---

## 5. Verification

**My final program:**

- [x] Passed the provided examples
- [x] Passed additional edge cases
- [ ] Still has unresolved problems

**One edge case I tested:**

Input:

20

Expected output:

OVER 6

Actual output:

OVER 6

---

## 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**

While Loop。
利用迴圈反覆更新狀態，直到滿足終止條件後離開迴圈。

**One thing I understand better now:**

當 total 達到或超過 n 時，while 條件不再成立，因此程式會自動離開迴圈，而不是額外再執行一次。

**One thing I am still unsure about:**

如何更精確分析迴圈執行次數與 Time Complexity。
目前知道此題不是 O(n)，因為 1+2+...+k 約等於 n，因此 k 約為 sqrt(2n)，時間複雜度接近 O(sqrt(n))。
