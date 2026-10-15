# OCW Programming Challenge Reflection

Name: ____________________
Date: ____________________
Topic: Lec4 - Functions, Abstraction, Decomposition, Return vs Print

## 1. Today’s Challenge

### Core concept from today’s OCW lecture:

- Function Decomposition
- Abstraction (Black Box Thinking)
- Using return values instead of relying only on print
- Functions calling other functions

---

### AI-generated coding challenge title:

Range Statistics (Balanced Number Counter)

---

## 2. My Initial Approach — Before AI Help

### My approach:

建立 `is_balanced()` 函式來判斷數字是否符合條件。

在函式內再定義 `is_2()` 與 `is_3()` 作為輔助函式，分別判斷是否可被 2 或 3 整除。

接著遍歷範圍內所有數字，利用 `is_balanced()` 的回傳值累積符合條件的數量。

---

## 3. AI Tutor Help

### Did you ask the AI Tutor for help?

☐ No — I solved it independently

☑ Yes — I received one or more hints

### The most useful hint/question from AI was:

題目要求統計的是「1 到 N」，而不是「0 到 N-1」或「0 到 N」。

AI 要求我檢查迴圈實際遍歷的範圍是否符合題意。

---

### It helped me realize that:

即使核心邏輯正確，邊界條件（boundary conditions）仍然可能造成錯誤。

需要仔細確認迴圈實際檢查的是哪些數值。

---

## 4. My Revision

### Did you change your approach or code after interacting with AI?

☐ No

☑ Yes

### What did you change, and why?

原本使用：

```python
for i in range(N+1)
```

導致檢查到 0。

後來改成：

```python
for i in range(N):
    count += is_balanced(i+1)
```

使程式實際檢查範圍為 1 到 N，符合題目要求。

---

## 5. Verification

### My final program:

☑ Passed the provided examples

☑ Passed additional edge cases

☐ Still has unresolved problems

### One edge case I tested:

Input: 1

Expected output: 0

Actual output: 0

---

## 6. One-Minute Reflection

### What idea from the OCW lecture did you transfer to this new problem?

Black Box（Abstraction）以及 Function Decomposition。

主程式只需要呼叫 `is_balanced()`，不需要知道其內部如何判斷。

另外也練習了在函式內定義函式的概念。

---

### One thing I understand better now:

函式的價值不只是重複使用而已，也能讓主程式更容易閱讀。

return 回傳的值可以被後續程式繼續利用，而不只是顯示結果。

---

### One thing I am still unsure about:

`def` 檔案與 `test.py` 的實際分工，以及在開發流程中的使用方式。
