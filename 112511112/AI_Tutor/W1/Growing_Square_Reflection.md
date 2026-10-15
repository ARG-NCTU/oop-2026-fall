# Name: 朱昱瑋
# Date: 2026/10/15
# Topic: AOOP Lec1 - Variables、Assignment 與 Re-binding

---

## 1. Today’s Challenge

**Core concept from today’s OCW lecture:**

- Variable（變數）
- Assignment（指定）
- Re-binding（重新綁定）
- Imperative Thinking（以步驟描述解法）

---

**AI-generated coding challenge title:**

**Growing Square**

---

## 2. My Initial Approach — Before AI Help

**My approach:**

使用 `side` 代表目前邊長，利用迴圈重複計算面積，並在每次計算後更新邊長。

---

## 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

- [ ] No — I solved it independently
- [x] Yes — I received one or more hints

---

**The most useful hint/question from AI was:**

> 題目要求回傳所有面積結果，而不是逐行印出結果，因此需要思考如何保留先前計算出的面積。

---

**It helped me realize that:**

除了儲存目前邊長外，還需要使用一個 list 將每次計算出的面積保存起來，否則最後無法輸出完整結果。

---

## 4. My Revision

**Did you change your approach or code after interacting with AI?**

- [ ] No
- [x] Yes

---

**What did you change, and why?**

一開始使用：

```python
print(area)
```

逐行輸出面積。

後來改用：

```python
area.append(side**2)
```

將所有結果存入 list，最後一次輸出完整結果。

因為題目要求回傳所有面積，而不是逐行顯示。

---

## 5. Verification

**My final program:**

- [x] Passed the provided examples
- [x] Passed additional edge cases
- [ ] Still has unresolved problems

---

**One edge case I tested:**

Input:

```text
side = 10
growth = 3
n = 1
```

Expected output:

```text
[100]
```

Actual output:

```text
[100]
```

---

## 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**

Assignment 與 Re-binding。

例如：

```python
side = side + growth
```

利用重新綁定變數的方式更新狀態，讓下一次迴圈能使用新的邊長。

---

**One thing I understand better now:**

程式中的變數並不是數學上的符號，而是一個可以隨著 Assignment 不斷改變內容的儲存空間。

---

**One thing I am still unsure about:**

在較複雜程式中，如何判斷哪些資料應該只保留目前值，哪些資料需要額外使用 list 儲存所有歷史結果。
