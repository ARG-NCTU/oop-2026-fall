# MIT 6.0001 Lecture 9 學習心得日誌 & 實作檢討單

**Topic:** MIT 6.0001 Lecture 9 (資訊隱藏、繼承與類別變數)  
**Date:** 2026-11-09  
**Name:** Wayne  

---

## Part A. 觀念測驗與反思 (Check My Understanding)

### ① Check My Understanding
* **Questions completed:** 5 / 5
* **Answers revised after AI hints:** 1 / 5 *(第 5 題因混淆「綁定」與「非綁定」呼叫而出錯，經引導與程式碼範例後更正)*

### ② My Misconception
* **Before I thought…**  
  我以為只要寫點號呼叫 `Animal.__init__()`，Python 就會自動幫我們傳入 `self` 物件實例。
* **Now I understand…**  
  我明白當使用類別名稱直接呼叫父類別方法時（`Animal.__init__(self, age)`），這屬於**非綁定函式呼叫（Unbound Function Call）**，Python 無法自動判斷要套用在誰身上，因此**必須手動將 `self` 作為第一個參數傳入**。若要讓 Python 自動帶入 `self` 且避免硬編碼類別名稱，應使用現代標準寫法 `super().__init__(age)`。

### ③ Challenge the AI
* **One AI-generated question I challenged:** 第 5 題：非綁定父類別呼叫 (Unbound Parent Constructor Call)
* **Why?**
  - [ ] Ambiguous
  - [x] Oversimplified *(初始觀念容易將「物件呼叫」與「類別呼叫」簡化混為一談)*
  - [ ] Technically questionable
  - [ ] Too easy
  - [ ] Other: __________
* **Brief explanation:**  
  第 5 題點出了初學者最容易忽視的語法細節（點號左邊是「類別名稱」還是「物件實體」）。雖然這題觀念明確，但容易因為習慣 `a.get_age()` 的自動傳參特性而直覺誤判為 False。經由範例程式對比 `Animal.__init__(self, age)` 與 `super().__init__(age)` 後，徹底解開了語法背後的運作邏輯。

### ④ One-Minute Reflection
* **One thing I am still unsure about:**  
  在多重繼承（Multiple Inheritance）的複雜架構下，`super()` 的呼叫順序（MRO - Method Resolution Order）是如何運作與決定的？

---

## Part B. LeetCode 實作挑戰 (Coding Challenge)

### 1. Today’s Challenge
* **Core concept from today’s OCW lecture:** 類別變數（Class Variables）、建構子繼承與鏈結（`super().__init__`）、方法覆寫（Method Overriding）、運算子重載（Operator Overloading）。
* **AI-generated coding challenge title:** RPG 魔物培育與識別系統 (RPG Monster Breeding & Identification System)

### 2. My Initial Approach — Before AI Help
1. 在 `Monster` 類別設定類別變數 `total_monsters = 0`，每次初始化時給予 `self.mid` 並讓 `total_monsters` 加 1。
2. `Dragon` 繼承 `Monster` 並透過 `super().__init__` 初始化名稱與等級。
3. 實作 `__add__` 時，直覺地將 `self.name` 和 `self.level` 直接進行修改（如 `self.name = f"{self.name}-{other.name}"`），並直接 `return self`。

### 3. AI Tutor Help
* **Did you ask the AI Tutor for help?** [x] Yes — I received one or more hints
* **The most useful hint/question from AI was:**  
  AI 指出 `+` 運算子直接修改 `self` 會產生副作用（Side Effect）導致原本的飛龍資料被覆蓋，且 `else` 區塊中產生了變數名稱拼寫錯誤（`child_lement` 漏寫 `e`），以及等級平手時（`>=`）的元素選取邏輯問題。
* **It helped me realize that:**  
  `+` 運算子（`__add__`）應該要**建立並回傳一個全新的物件**（`return Dragon(...)`），而不是修改呼叫者本身；且重新實例化 `Dragon` 會自動觸發父類別建構子，完全不需要手動再寫一次 `Monster.total_monsters += 1`。

### 4. My Revision
* **Did you change your approach or code after interacting with AI?** [x] Yes
* **What did you change, and why?**  
  1. **修正 `__add__` 副作用**：改為計算好 `child_name`, `child_level`, `child_element` 後，直接 `return Dragon(child_name, child_level, child_element)`。
  2. **修正變數拼寫錯誤**：將 `child_lement` 修正為 `child_element`，避免拋出 `UnboundLocalError`。
  3. **修正邊界條件**：將條件判斷從 `>` 改為 `>=`（`if self.level >= other.level:`），確保兩隻飛龍同等級時能正確取得 `self.element`。
  4. **修正輸出格式**：移除 `__str__` 中多餘的尖括號 `<>`。

### 5. Verification
* **My final program:** [x] Passed the provided examples & edge cases
* **One edge case I tested:**  
  - **Input:** 
    ```python
    d1 = Dragon("Ignis", 15, "Fire")
    d2 = Dragon("Pyra", 15, "Ice")
    d3 = d1 + d2
    ```
  - **Expected output:** 兩者等級相同（15 級），應優先繼承 `d1` 的元素屬性 `"Fire"`，且 ID 遞增為 `"003"`。輸出：`Dragon #003: Ignis-Pyra [Fire] (Lvl 15)`
  - **Actual output:** `Dragon #003: Ignis-Pyra [Fire] (Lvl 15)`

### 6. One-Minute Reflection
* **What idea from the OCW lecture did you transfer to this new problem?**  
  利用類別變數 `Monster.total_monsters` 進行全域實體計數，並結合 `super().__init__` 讓子類別建立新實體時能自動完成父類別的全域 ID 分配與初始化。
* **One thing I understand better now:**  
  理解到運算子重載（`__add__`）的核心精神是「產生新實體」而非「修改舊實體」，以及直接呼叫 `Dragon(...)` 產生新物件時，物件導向繼承鏈會自動完成屬性賦值與類別變數累加。
* **One thing I am still unsure about:**  
  在 Big O 表示法中，常數時間運算（如幾次加法與字串拼接）為什麼會被統一簡化標示為 $O(1)$，以及字串拼接在處理超大字串時的時間複雜度計算。