# Name: ____________________
# Date: ____________________
# Topic: Lec7 - Exceptions, Raise, Try/Except

## 1. Today's Challenge

**Core concept from today's OCW lecture:**

- try / except
- raise
- List Traversal
- Edge Case Handling
- Debugging

---

**AI-generated coding challenge title:**

Safe Percentage Change

---

## 2. My Initial Approach — Before AI Help

**My approach:**

使用迴圈逐一檢查相鄰元素，計算百分比變化；若資料不足則報錯；若遇到除以 0 則改輸出 `"undefined"`。

---

## 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

☐ No — I solved it independently  
☑ Yes — I received one or more hints

**The most useful hint/question from AI was:**

我目前計算的是 `new/old`，還是 `(new-old)/old`？

**It helped me realize that:**

我把百分比變化公式寫錯了，而且忽略了運算優先順序與括號的重要性。

---

## 4. My Revision

**Did you change your approach or code after interacting with AI?**

☐ No  
☑ Yes

**What did you change, and why?**

1. 修正百分比變化公式。
2. 將輸入改成 `.split(',')` 後再轉成數字。
3. 修正 `ValueError` 的寫法。
4. 保留 `try/except` 來處理除以 0 的情況。

這些修改讓程式能正確處理正常輸入與邊界案例。

---

## 5. Verification

**My final program:**

☑ Passed the provided examples  
☑ Passed additional edge cases  
☐ Still has unresolved problems

**One edge case I tested:**

Input: `0,10`

Expected output: `['undefined']`

Actual output: `['undefined']`

---

## 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**

使用 `raise` 提前報告不合法輸入，並利用 `try/except` 處理可預期發生的執行期錯誤，而不讓整個程式崩潰。

**One thing I understand better now:**

我更清楚區分了：

- 不合法輸入 → 使用 `raise`
- 執行過程中的例外 → 使用 `try/except`

以及兩者在程式設計上的不同目的。

**One thing I am still unsure about:**

當輸入包含非數字資料（例如 `100,abc,90`）時，應該直接 `raise ValueError`，還是利用例外處理機制繼續執行比較合適？
