# MIT 6.0001 Lecture 8 Reflection Log

Topic: **MIT 6.0001 Lecture 8: Object-Oriented Programming (物件導向程式設計)**  
Date: **2026-10-18**

---

## ① Check My Understanding

- **Questions completed:** 5 / 5
- **Answers revised after AI hints:** 1 / 5

---

## ② My Misconception

**Before: I thought…**
> 我原先對於 `c.distance(zero)` 與 `Coordinate.distance(c, zero)` 的呼叫機制不夠清楚[cite: 14]；不確定是否能隨意自創前後帶有雙底線 `__...__` 的自訂方法名稱[cite: 10, 18]；且不確定 `class Vector2D(object)` 括號中的 `object` 代表什麼[cite: 8]。

**Now: I understand…**
> - **呼叫機制（Call Mechanism）**：`c.distance(zero)` 是透過物件實例（Instance）呼叫綁定方法（Bound Method），Python 會自動將 `c` 傳入第一個參數 `self`[cite: 11, 14]；而 `Coordinate.distance(c, zero)` 是透過類別（Class）直接呼叫非綁定函式，必須手動將物件實例 `c` 作為第一個參數傳入[cite: 14]。兩者在執行結果上完全等價[cite: 14]。
> - **特種方法（Special / Dunder Methods）**：前後帶有雙底線（Double Underscore）的名稱是 Python 官方預留的語言特種名稱，用來實現運算子重載（Operator Overloading，如 `__add__` 對應 `+`）與內建功能對接（如 `__str__` 對應 `print()`），不應隨意自創此類名稱[cite: 15, 18]。
> - **基底類別（Base Class）**：`object` 是 Python 中所有類別最頂層的內建基底類別（Base Class）[cite: 8]。在類別名稱後寫 `(object)` 代表繼承其基礎特性[cite: 8]。

---

## ③ Challenge the AI

**One AI-generated question I challenged:**
> 題目中關於 OOP 名詞標示的嚴謹度與統一性。

**Why?**
- [ ] Ambiguous
- [ ] Oversimplified
- [x] Technically questionable
- [ ] Too easy
- [x] Other: **名詞標示與中英文對照需更統一**

**Brief explanation:**
> Lecture 8 包含大量新抽象概念，題目與討論中應全面統一並提供中英文雙語對照（例如：類別 Class、物件實例 Instance、綁定方法 Bound Method、特種方法 Special / Dunder Methods），有助於觀念架構的建立。

---

## ④ One-Minute Reflection

**One thing I am still unsure about:**
> 當子類別（Subclass）繼承父類別（Superclass）時，若兩者都定義了相同的雙底線方法（如 `__str__` 或 `__add__`），子類別該如何優雅地調用父類別的實作進行延伸（如使用 `super()`），這將在 Lecture 9 深入探索。

---
---

Name: **Student**  
Date: **2026-10-18**  
Topic: **MIT 6.0001 Lecture 8: Vector2D Engine**

---

## 1. Today’s Challenge

**Core concept from today’s OCW lecture:**
> 類別定義（Class Definition）、實體屬性（Instance Attributes）、綁定方法（Bound Methods）與特種方法/運算子重載（Dunder Methods / Operator Overloading）[cite: 8, 10, 12, 18]。

**AI-generated coding challenge title:**
> **Vector2D Engine (二維向量運算器)**

---

## 2. My Initial Approach — Before AI Help

**Before asking AI for hints, briefly describe how you planned to solve the problem.**

**My approach:**
> 使用 `self.x = x` 與 `self.y = y` 綁定實體屬性[cite: 10]；使用 `str.format()` 傳回格式化座標[cite: 16]；在 `__add__` 與 `__sub__` 中建立並傳回新的 `Vector2D` 物件實例[cite: 18]；在 `__eq__` 中使用 `isinstance` 進行型態檢查與座標比對[cite: 17, 18]；並使用 `math.sqrt` 與乘法實現 `magnitude` 與 `dot`。

---

## 3. AI Tutor Help

**Did you ask the AI Tutor for help?**
- [ ] No — I solved it independently
- [x] Yes — I received one or more hints

**The most useful hint/question from AI was:**
> 提醒 Python 單行註解應使用 `#` 而非 `//`；說明 `->` 為型態標示（Type Hints）；並提示需在 `__init__` 與算術方法補上 `TypeError` 防禦性檢查（如檢查傳入型態是否為數字或 `Vector2D` 實例，且需排除 `bool` 型態）。

**It helped me realize that:**
> 註解語法（`#`）在 Python 中的正確使用，以及在類別方法入口處進行型態驗證以確保程式碼強健度的重要性。

---

## 4. My Revision

**Did you change your approach or code after interacting with AI?**
- [ ] No
- [x] Yes

**What did you change, and why?**
> 1. 將 `//` 註解修改為符合 Python 語法的 `#`。
> 2. 在 `__init__` 加入 `isinstance(..., (int, float))` 檢查且排除 `bool`，不符合時拋出 `TypeError`。
> 3. 在 `__add__`、`__sub__` 與 `dot` 加入對 `other` 是否為 `Vector2D` 實例的檢查，不符合時拋出 `TypeError`。

---

## 5. Verification

**My final program:**
- [ ] Passed the provided examples
- [x] Passed additional edge cases
- [ ] Still has unresolved problems

**One edge case I tested:**
- **Input:** `v1 = Vector2D(3, 4)`, `v1 + "invalid_vector"`
- **Expected output:** 觸發 `TypeError("加法運算子右側必須為 Vector2D 物件實例")`
- **Actual output:** 成功拋出 `TypeError`

---

## 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**
> 「將資料與處理資料的方法封裝在一起」的物件導向抽象化思想[cite: 4, 6]，以及透過定義 `__add__` 與 `__eq__` 等特種方法（Dunder Methods），讓自訂類別物件能直覺地使用 `+` 與 `==` 等運算子[cite: 18]。

**One thing I understand better now:**
> 物件呼叫 `v.magnitude()` 與類別呼叫 `Vector2D.magnitude(v)` 的底層等價性[cite: 14]、`object` 基底類別（Base Class）的繼承含義[cite: 8]，以及特種方法（Dunder Methods）在運算子重載上的觸發機制[cite: 18]。

**One thing I am still unsure about:**
> 在繼承（Inheritance）架構下，若多個子類別各自重載了運算子，Python 是如何決定執行哪一個類別的 `__add__` 方法（如 `__radd__` 反向運算子機制）。
