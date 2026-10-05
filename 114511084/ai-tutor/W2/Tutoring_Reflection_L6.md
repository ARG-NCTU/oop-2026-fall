# 📝 AI Tutor Learning Record — Coding Challenges (Double Session)

**Name:** Yoei  
**Date:** 2026-09-14  
**Topic:** Recursion, Dictionaries & Memoization (MIT 6.0001 Lecture 6)  

---

# 🧩 Part I: 第一題（遞迴分治與字典記憶化）

### 1. Today’s Challenge

**Core concept from today’s OCW lecture:**  
* 非數值字串遞迴分治（對應 `isPalindrome` 與字串切片 `[:]`）。
* 樹狀多分支遞迴（對應 `fib(n)`）。
* 字典記憶化快取 (Memoization) 消除指數級重複計算（對應 `fib_efficient`）。

**AI-generated coding challenge title:**  
Token Concatenation Count (標記拼詞計數器)

---

### 2. My Initial Approach — Before AI Help

**Before asking AI for hints, briefly describe how you planned to solve the problem.**

**My approach:**  
以有沒有湊齊 `target` 或是 token 是否找到最後一個為 Base Case。其餘狀況則是回傳 `target` 字串減掉當前 token 後是否成功。子字串是否成功可以用 Dictionary 儲存已經確認過的 `True` 或 `False`。  
後續修正思路時，認為每次比對到一個 token 時，核心累加邏輯是 `1 + (子字串有幾種組合)`。

---

### 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

* [ ] No — I solved it independently
* [x] Yes — I received one or more hints

**The most useful hint/question from AI was:**  
1. **反例辨析**：以極簡案例 `target = "ab"`, `tokens = ["a", "b"]` 為例，若每步都加 1，單一路徑就會被算成 2 種，點出「1」不應該在每次遞迴加，而應該是抵達終點線時的貢獻。
2. **走迷宮比喻**：走到終點（`target == ""`）代表成功走出 1 條完整路線（Base Case 回傳 1）；走進死胡同無 token 可用則回傳 0；路口有多條分支時，總路線數應為各分支「相加」。
3. **字串切片複習**：詳細複習了 `target[:len(token)]` 與 `target.startswith(token)` 的前綴檢查，以及用 `target[len(token):]` 切除已用 token 取得剩餘子字串。

**It helped me realize that:**  
求「總組合數」與求「是否可行 (True/False)」本質不同，決策樹的各條分支必須用加法合計。此外，利用字典紀錄「子字串 $\to$ 組合數」能避免同一子字串被重複搜索，大幅將指數級複雜度降低為多項式級。

---

### 4. My Revision

**Did you change your approach or code after interacting with AI?**

* [ ] No
* [x] Yes

**What did you change, and why?**  
1. **修正 Base Case 回傳值**：當 `target == ""` 時回傳 `1`，若查表命中則回傳 `memo[target]`。
2. **修正分支合併方式**：改用累加器 `total_ways += count_construct(remaining, tokens, memo)` 遍歷所有可行的 token 分支。
3. **應用切片與字典記錄**：利用 `remaining = target[len(token):]` 縮小子問題，並在回傳前將算出的答案存入 `memo[target]`。

---

### 5. Verification

**My final program:**

* [x] Passed the provided examples
* [x] Passed additional edge cases
* [ ] Still has unresolved problems

**One edge case I tested:**  
```python
Input:
target = "apple"
tokens = ["ap", "app", "ple", "le"]

Expected output: 2
Actual output: 2

# 額外重疊子字串測試：
target = "aaaa"
tokens = ["a", "aa"]
Expected output: 5
Actual output: 5
```

---

### 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**  
結合了 `isPalindrome` 的字串切片分治思維與 `fib_efficient` 的字典查表快取，成功將指數級爆炸的字串組合問題轉化為高效的記憶化搜尋。

**One thing I understand better now:**  
釐清了決策樹中「終止條件回傳 1」與「分支結果相加」的計數本質，並找回了 Python 切片 `[start:stop]`「包頭不包尾」的觀念。

**One thing I am still unsure about:**  
當 `target` 長度達到數千以上時，遞迴深度可能會觸發 Python 預設的 `RecursionError`，此時如何將記憶化遞迴改寫為由底向上的迭代迴圈 (Bottom-up Dynamic Programming)？

---
---

# 🧩 Part II: 第二題（字典特性與詞頻反轉分組）

### 1. Today’s Challenge

**Core concept from today’s OCW lecture:**  
* 字典 (Dictionary) 核心操作與約束：Key 必須為不可變型別 (Immutable / Hashable)，Value 可為任意型別（含 List）。
* 詞頻統計標準模式：`lyrics_to_frequencies`。
* 字典反向分組與頻率聚合（延伸自 `most_common_words` 與 `words_often`）。

**AI-generated coding challenge title:**  
Frequency Inversion & Grouping (詞頻反轉分組器)

---

### 2. My Initial Approach — Before AI Help

**Before asking AI for hints, briefly describe how you planned to solve the problem.**

**My approach:**  
先建立一個字典 `dic` 走訪 `words` 計算每個單字出現的次數（如果單字在字典中就 `+= 1`，否則設為 `1`）。接著建立另一個字典來存放反轉後的結果，走訪 `dic` 的鍵值，把次數當成新字典的 Key，若次數已存在就用 `.append()` 加進 List，不存在就建立包含該單字的新 List。最後再用第三個迴圈判斷次數是否大於門檻，並用 `print` 印出結果。

---

### 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

* [ ] No — I solved it independently
* [x] Yes — I received one or more hints

**The most useful hint/question from AI was:**  
1. **邊界條件修正**：題目要求「小於門檻不保留」，代表大於或等於門檻都必須保留，判斷式應為 `>=` 而非 `>`。
2. **函式規格要求**：LeetCode / 模組化函式必須使用 `return` 回傳字典物件給呼叫者，而非直接 `print` 字串（若未 `return` 外部呼叫會拿到 `None`）。
3. **命名與結構優化**：字典變數命名為 `list = {}` 會覆蓋 Python 內建的 `list()` 函式；此外，門檻過濾可直接在反轉迴圈中完成，不需額外跑第三個迴圈。

**It helped me realize that:**  
在實務與評測系統中，函式的輸入輸出規格（`return` vs `print`）和邊界條件（`>=` vs `>`）至關重要。同時更清楚掌握了 Python 字典反轉時「以不可變整數當 Key、以可變串列當 Value」的資料結構特性。

---

### 4. My Revision

**Did you change your approach or code after interacting with AI?**

* [ ] No
* [x] Yes

**What did you change, and why?**  
1. **修正變數名稱**：將覆蓋內建關鍵字的 `list = {}` 改名為語意明確的 `result = {}`。
2. **合併邏輯與修正邊界**：將過濾與反轉邏輯整併至同一迴圈，並將條件改為 `if count >= min_count:`，確保剛好達到門檻的單字不會被誤刪，同時省去一個迴圈開銷。
3. **改為標準回傳**：移除終端機 `print` 輸出，於函式結尾明確寫出 `return result`。

---

### 5. Verification

**My final program:**

* [x] Passed the provided examples
* [x] Passed additional edge cases
* [ ] Still has unresolved problems

**One edge case I tested:**  
```python
# 測試剛好達到門檻 (count == min_count) 以及高於門檻的混合案例
Input: 
words = ["she", "loves", "you", "yeah", "yeah", "yeah", "she", "loves", "you"]
min_count = 2

Expected output: 
{2: ['she', 'loves', 'you'], 3: ['yeah']}

Actual output: 
{2: ['she', 'loves', 'you'], 3: ['yeah']}
```

---

### 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**  
遷移了 Lecture 6 中 `lyrics_to_frequencies` 的字典累加技巧，並結合課堂講述的 Key / Value 特性，成功實作出將 `{單字: 次數}` 反轉為 `{次數: [單字清單]}` 的分組架構。

**One thing I understand better now:**  
完全理解了為什麼字典的 Key 必須不可變（因此整數次數可以當 Key），而 Value 可以任意容納 List；並且掌握了寫 LeetCode 時 `return` 與正確邊界條件 `>=` 的重要性。

**One thing I am still unsure about:**  
在面對海量資料時，若需要將反轉後的字典同時依照「次數由大到小」以及「字母由 A 到 Z」雙重排序輸出，如何寫出時間複雜度最佳且最優雅的 Pythonic 語法？
