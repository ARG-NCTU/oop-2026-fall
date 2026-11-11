# MIT 6.0001 Lecture 7 Reflection Log

Topic: **MIT 6.0001 Lecture 7: Testing, Debugging, Exceptions, and Assertions**  
Date: **2026-10-18**

---

## ① Check My Understanding

- **Questions completed:** 5 / 5
- **Answers revised after AI hints:** 1 / 5

---

## ② My Misconception

**Before: I thought…**
> 我原先不知道 `finally` 的語法特性（以為包含 `return` 時會被跳過）；同時誤以為 `assert` 是用來捕捉錯誤，且以為 `raise Exception` 是用來「捕捉」而不是「拋出/觸發」錯誤。

**Now: I understand…**
> `finally` 是無論前面有無發生錯誤、甚至包含 `return` 或 `break` 都**必定會執行**的收尾區塊；`assert` 是開發者寫給自己看的內部狀態檢查（觸發/拋出 `AssertionError`）；`raise Exception` 是主動拋出/觸發可預期的錯誤（如使用者輸入不良資料）；而 `try-except` 才是用來攔截與捕捉錯誤的防衛網。

---

## ③ Challenge the AI

**One AI-generated question I challenged:**
> 第 1 題（`finally` 的執行機制）與整體題目難易度設定。

**Why?**
- [ ] Ambiguous
- [x] Oversimplified
- [x] Technically questionable
- [x] Too easy
- [x] Other: **題目說明不夠明確**

**Brief explanation:**
> 第一題在未事前說明 `finally` 語法特性的情況下直接出題，說明不夠明確；且 Lecture 7 整體觀念題偏簡單（屬於偏向規則與慣例的防禦性程式設計觀念）。

---

## ④ One-Minute Reflection

**One thing I am still unsure about:**
> 當 `try` 區塊內部發生了未在 `except` 元組中列出的「未預期 Exception」時，雖然 `finally` 仍會執行，但大型系統該如何設計底層的捕獲機制（例如備用 catch-all Handler），才能既不藏 Bug 又能安全記錄與復原？

---
---

Name: **Student**  
Date: **2026-10-18**  
Topic: **MIT 6.0001 Lecture 7: Robust Ledger Engine**

---

## 1. Today’s Challenge

**Core concept from today’s OCW lecture:**
> 防禦性程式設計（Defensive Programming）、自訂異常類別（Custom Exceptions）、`try-except-else-finally` 流程控制與 `assert` 內部不變量檢查。

**AI-generated coding challenge title:**
> **Robust Ledger Engine (強健型財務帳本處理器)**

---

## 2. My Initial Approach — Before AI Help

**Before asking AI for hints, briefly describe how you planned to solve the problem.**

**My approach:**
> 建立繼承 `Exception` 的自訂類別，並用 `pass` 保留預設行為；在 `process_transaction` 中使用 `isinstance` 與 `.get()` 驗證字典與金額，並用 `assert new_balance >= 0` 驗證餘額；在 `batch_process` 中建立 `try-except-else-finally` 結構來進行批次處理。

---

## 3. AI Tutor Help

**Did you ask the AI Tutor for help?**
- [ ] No — I solved it independently
- [x] Yes — I received one or more hints

**The most useful hint/question from AI was:**
> 提示存款（`deposit`）時不應檢查 `balance < amount`（原程式碼會導致餘額少於存款金額時誤判為餘額不足），以及 Python 中 `bool` 是 `int` 的子類別，需排除 `bool` 型態；並補全 `finally` 區塊中的 `audit_log` 審計日誌寫入邏輯。

**It helped me realize that:**
> 防禦性邏輯檢查需要分清交易類型（僅 `withdraw` 才需驗證餘額）；且 `bool` 型態在 `isinstance(True, int)` 會通過驗證，需額外進行邊界防禦。

---

## 4. My Revision

**Did you change your approach or code after interacting with AI?**
- [ ] No
- [x] Yes

**What did you change, and why?**
> 1. 將餘額不足檢查限制在 `type_ == "withdraw"`，避免存款時誤拋錯誤。
> 2. 將交易類型由 `"withdrawal"` 修正為題目規格要求的 `"withdraw"`。
> 3. 在金額型態檢查加上 `and not isinstance(amount, bool)`，防止布林值混入計算。
> 4. 在 `batch_process` 的 `finally` 區塊補上 `audit_log.append(...)`，確保無論成功與否都記錄交易歷程。

---

## 5. Verification

**My final program:**
- [ ] Passed the provided examples
- [x] Passed additional edge cases
- [ ] Still has unresolved problems

**One edge case I tested:**
- **Input:** `balance = 500.0`, `transaction = {"type": "deposit", "amount": True}`
- **Expected output:** 觸發 `InvalidTransactionError`，紀錄為 `FAILED: Invalid transaction amount`
- **Actual output:** `FAILED: Invalid transaction amount`

---

## 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**
> 「絕不靜默失敗（Fail-Fast）」的原則——當發現不合法輸入時主動 `raise` 顯式異常；以及利用 `finally` 確保無論執行路徑如何（包含異常發生時）都能進行必要的 Audit Log 紀錄。

**One thing I understand better now:**
> `finally` 在系統紀錄與資源清理上的不可替代性、`as` 語法在捕捉 Exception 時綁定錯誤字串物件的作用，以及 `enumerate` 同時取得索引與元素的便利性。

**One thing I am still unsure about:**
> 在複雜的物件導向架構（如即將進入的 Lecture 8 OOP）中，自訂 Exceptions 該如何跨多層 Class 進行傳遞與分層捕捉設計？

---

## 7. Final Source Code

```python
class InsufficientFundsError(Exception):
    pass

class InvalidTransactionError(Exception):
    pass

def process_transaction(balance: float, transaction: dict) -> float:
    # 1. 驗證交易格式與型態
    if not isinstance(transaction, dict):
        raise InvalidTransactionError("Invalid transaction format")

    type_ = transaction.get("type")
    if type_ not in ("deposit", "withdraw"):
        raise InvalidTransactionError("Invalid transaction type")

    amount = transaction.get("amount")
    # 排除 bool 型態，確保 amount 為純數字
    if not isinstance(amount, (int, float)) or isinstance(amount, bool):
        raise InvalidTransactionError("Invalid transaction amount")

    if amount <= 0:
        raise InvalidTransactionError("Transaction amount must be positive")

    # 2. 僅在提款時驗證餘額是否足夠
    if type_ == "withdraw" and balance < amount:
        raise InsufficientFundsError("Insufficient funds for the transaction")

    # 3. 計算新餘額並進行不變量檢查
    if type_ == "deposit":
        new_balance = balance + amount
    else:  # withdraw
        new_balance = balance - amount

    assert new_balance >= 0, "New balance should not be negative"
    return new_balance


def batch_process(initial_balance: float, transactions: list) -> tuple:
    current_balance = initial_balance
    successful_count = 0
    failed_count = 0
    audit_log = []
    
    for idx, tx in enumerate(transactions, 1):
        status = "UNKNOWN"
        try:
            current_balance = process_transaction(current_balance, tx)
        except (InvalidTransactionError, InsufficientFundsError) as e:
            failed_count += 1
            status = f"FAILED: {e}"
        else:
            successful_count += 1
            status = "SUCCESS"
        finally:
            # 確保不論成功與否，每一筆交易嘗試都會記錄進 Audit Log
            audit_log.append(f"Tx #{idx} -> {status}")
            
    return current_balance, successful_count, failed_count