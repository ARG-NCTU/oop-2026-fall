# AI Tutor Learning Record — W3 / MIT 6.0001 Lecture 7

**Name:** 劉育麟  
**Date:** 2026/11/09  
**Topic:** Testing, Debugging, Exceptions, Assertions

---

# Part A: True or False

## ① Check My Understanding

**Questions completed:** 5 / 5  
**Answers revised after AI hints:** 0 / 5

| 題號 | 主題 | 我的答案 | 結果 |
| --- | --- | --- | --- |
| 1 | Glass Box Testing 與 Boundary Cases | False | 正確，首次答對 |
| 2 | `try`、`except`、`else`、`finally` | True | 正確，首次答對 |
| 3 | Unit Testing 與 Regression Testing | True | 正確，首次答對 |
| 4 | Assertions 與 Exceptions | True | 正確，首次答對 |
| 5 | Exception Handling 與 `raise` | True | 正確，首次答對 |

## ② My Misconception

### Before: I thought…

我原本以為，在 `except` 裡引發新的例外後，原本的例外就會消失，呼叫者只能看到新引發的例外。

### Now: I understand…

做完第 5 題後，我才知道，外層雖然會收到 `ValueError`，原本的 `TypeError` 仍會保留在例外鏈中。如果沒有捕捉 `ValueError`，我可以從錯誤追蹤看到是哪個例外先發生，以及程式後來引發了哪個例外。

## ③ Challenge the AI

**One AI-generated question I challenged:**  
第 5 題：Exception Handling 與 `raise`。

**Why?**

- [ ] Ambiguous
- [x] Oversimplified
- [ ] Technically questionable
- [ ] Too easy
- [ ] Other

### Brief explanation

原題正確指出，呼叫者可以用 `except ValueError` 捕捉向外傳遞的例外。不過，在處理 `TypeError` 時引發新的 `ValueError`，Python 也會把原本的 `TypeError` 保留為新例外的上下文。如果外層沒有捕捉 `ValueError`，預設的錯誤追蹤會顯示兩個例外。

我會把題目改成分別問：「外層要用哪個 `except` 才能捕捉這次呼叫拋出的例外？」以及「如果外層沒有捕捉它，錯誤追蹤會顯示哪些例外？」這樣就能同時檢驗例外傳遞與例外鏈的理解。

## ④ One-Minute Reflection

### One thing I am still unsure about

我還想更熟悉直接寫 `raise ValueError(...)` 與寫 `raise ValueError(...) from e` 時，錯誤追蹤有什麼差別，以及什麼情況下適合用 `from e` 明確標示原因。

經過 AI Tutor 的補充後，我知道一般在處理舊例外的過程中引發新例外，Python 會以 `__context__` 保留原始例外；而 `raise ... from e` 會明確指定直接原因 `__cause__`。我希望繼續透過實際案例熟悉兩種寫法。

---

# Part B: LeetCode-style Lecture Code Transfer

## 1. Today’s Challenge

**Core concept from today’s OCW lecture:**  
Defensive Programming、Exception Handling、Testing，並結合先前課程的 Dictionary Mutation 與 Cloning。

**AI-generated coding challenge title:**  
**Safe Inventory Transactions（安全庫存更新）**

**Challenge summary:**  
給定記錄商品庫存的字典 `stock` 和交易清單 `transactions`，依序處理每筆進貨或銷售。交易後若庫存小於零，應引發 `ValueError`；若所有交易成功，則回傳更新後的新字典。無論成功或失敗，都不可修改原始 `stock`。

## 2. My Initial Approach — Before AI Help

**My approach:**

我會先複製 `stock`，再按照交易清單的順序更新副本。每筆交易都以副本中的最新庫存為準，讓同一商品的下一筆交易能接續前一筆的結果。副本裡沒有的商品，庫存就從 `0` 算起。

每次都先算出交易後的庫存。若結果小於 `0`，就立即引發 `ValueError`。先前成功的交易都只更新了副本，因此即使做到一半失敗，原始 `stock` 也不會受影響。全部交易成功後，才回傳副本。交易清單為空時，也會回傳一份內容相同的新字典。

**Testing plan:**

| 測試情況 | 預期結果 |
| --- | --- |
| 同一商品先進貨再銷售 | 後一筆交易使用前一筆更新後的庫存 |
| 庫存為 `1`，賣出 `1` 件 | 成功，庫存剛好為 `0` |
| 庫存為 `1`，連續兩筆各賣 `1` 件 | 第二筆引發 `ValueError`，原始庫存仍是 `1` |
| 對不存在的商品進貨或銷售 | 進貨能建立商品，直接銷售會引發 `ValueError` |
| 交易清單為空 | 回傳內容相同、可獨立修改的新字典 |

## 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

- [x] No — I solved it independently
- [ ] Yes — I received one or more hints

**The most useful hint/question from AI was:**  
我沒有需要修改演算法的提示。AI Tutor 確認了先複製字典、依序更新副本、庫存不足時引發例外的設計，並提醒我檢查空交易、剛好歸零，以及中途失敗後原始資料是否仍然不變。

**It helped me realize that:**  
正確性不只包含成功時的回傳值，也必須驗證失敗情況是否符合規格，以及原始字典在所有情況下都未被修改。

## 4. My Revision

**Did you change your approach or code after interacting with AI?**

- [x] No
- [ ] Yes

**What did you change, and why?**  
原先設計已符合題目要求，因此不需要修改演算法或程式碼。我在驗證階段額外確認了例外發生時 `stock` 仍保持原樣，以及空交易時回傳的是獨立的新字典。

## 5. Verification

**My final program:**

```python
def apply_transactions(stock, transactions):
    updated_stock = stock.copy()

    for product, change in transactions:
        current_quantity = updated_stock.get(product, 0)
        new_quantity = current_quantity + change

        if new_quantity < 0:
            raise ValueError("Insufficient stock for " + product)

        updated_stock[product] = new_quantity

    return updated_stock
```

- [x] Passed the provided examples
- [x] Passed additional edge cases
- [ ] Still has unresolved problems

**Verification summary:**  
七組案例通過：正常交易、第二筆交易失敗、新商品進貨、庫存剛好歸零、銷售不存在商品、空交易、同一商品連續交易。也驗證了原始 `stock` 不被修改；成功情況下回傳的字典與原始字典不是同一個物件。

**One edge case I tested:**

**Input:**

```python
stock = {'pen': 1}
transactions = [['pen', -1], ['pen', -1]]
```

**Expected output:**  
第二筆交易引發 `ValueError`，而原始 `stock` 仍是 `{'pen': 1}`。

**Actual output:**  
引發 `ValueError("Insufficient stock for pen")`；原始 `stock` 仍是 `{'pen': 1}`。**Pass**。

## 6. One-Minute Reflection

### Why my solution works

`stock.copy()` 建立一個獨立的字典。庫存值都是整數，因此淺拷貝就足夠。程式只會寫入副本，所以即使前幾筆交易已成功、後來某筆交易引發 `ValueError`，原始 `stock` 也保持原樣。

迴圈依照清單順序處理交易。每筆交易都從副本讀取庫存，再把成功的結果寫回同一份副本。因此，處理第 `i` 筆交易時，副本已反映前 `i-1` 筆交易的結果。

### Time and Space Complexity

- **時間：`O(n + m)`**。`stock.copy()` 複製 `n` 筆庫存資料，需要 `O(n)`；每筆交易的查詢與更新平均為 `O(1)`，最多處理 `m` 筆，因此為 `O(m)`。若中途失敗，迴圈會提前停止。
- **空間：`O(n + u)`**。其中 `u` 是實際新增的商品種類數。複製原字典需要 `O(n)`，每個新商品再多一筆；因為 `u ≤ m`，最壞情況可寫成 `O(n + m)`。
- 即使交易清單為空，也需要 `O(n)` 的時間與空間建立獨立副本。

### What idea from the OCW lecture did you transfer to this new problem?

和 Lecture 7 的 `get_ratios()` 一樣，這題用 `raise ValueError(...)` 將失敗回報給呼叫者，讓呼叫者可以用 `except ValueError` 處理。不同的是，這題由程式主動檢查交易後的庫存是否會低於 `0`，並在違反條件時引發例外。

**Cloning（複製）** 提供一份獨立的工作副本，**Dictionary Mutation（字典修改）** 則讓每筆成功的交易直接累積到副本。全部交易通過後，才將更新後的字典回傳給呼叫者。

### One thing I understand better now

我更清楚如何結合防禦式程式設計與資料複製：先檢查交易結果是否合法，再修改工作副本；當中途發生例外時，原始資料仍能維持一致。測試時也不能只確認成功結果，還需要檢查失敗情況的例外類型與副作用。

### One thing I am still unsure about

我希望繼續練習不同層級的例外處理方式，特別是何時直接使用 `raise ValueError(...)`，以及何時應用 `raise ... from e` 保留底層例外的原因關係。

---

*依照 MIT 6.0001 Lecture 7 投影片、`lec7_debug_except.py`，以及本次 AI Tutor 實際問答整理。*
