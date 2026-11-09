# W2 — AI Tutor Learning Record (MIT 6.0001 Lecture 6)

**Name:** 劉育麟  
**Date:** 2026/11/09  
**Topic:** Recursion, Dictionaries, Recursive Scope, Memoization  
**Source:** MIT 6.0001 Lecture 6 (`MIT6_0001F16_Lec6.pdf`) 與 `lec6_recursion_dictionaries.py`

---

# Part A: True or False

## ① Check My Understanding

**Questions completed:** 5 / 5  
**Answers revised after AI hints:** 0 / 5

| 題次 | 主題 | 我的答案 | 結果 |
|---|---|---|---|
| 1 | Recursion 與 Base Case | False | 首次答對 |
| 2 | Recursive Function Scope | False | 首次答對 |
| 3 | Dictionary Mutation | False | 首次答對 |
| 4 | Fibonacci Memoization | True | 首次答對 |
| 5 | Dictionary Keys 與 Membership | False | 首次答對 |

### 作答重點

**Q1 — Base Case：** 每次 `n - 2` 不會改變奇偶性。偶數可沿著 4 → 2 → 0 到達終止條件；奇數如 3 → 1 → -1 → … 會跳過 0，最終因過深遞迴而發生 `RecursionError`。即使是偶數，數值過大也可能先碰到 Python 遞迴深度限制。

**Q2 — Recursive Scope：** `calculate(3)` 最後回傳 `3`。每層遞迴呼叫都有自己的區域變數 `x`；外層沒有使用內層的回傳值，而是回傳自己的 `x`。

**Q3 — Dictionary Mutation：** `counts` 最後是 `{'apple': 3}`。函式中的參數 `freqs` 與外部 `counts` 指向同一個字典；更新字典內容不需要透過 `return` 才能生效。

**Q4 — Memoization：** 記憶化不改變 Fibonacci 的遞迴關係或結果，而是儲存已計算的子問題，避免重複展開。共用快取且字典查詢平均為 O(1) 時，從空快取計算可把時間複雜度由指數級降為 O(n)。

**Q5 — Dictionary Membership：** `2 in freqs` 檢查的是 keys，而不是 values，因此條件為 False，最後結果為 `{'apple': 3, 'banana': 1}`。若要檢查 values，可寫 `2 in freqs.values()`。

## ② My Misconception

### Before: I thought…

我原本以為加上 Memoization 後，像 `fib(3)` 這樣的子問題只會被**呼叫一次**。我把「呼叫函式」與「實際重新計算子問題」當成同一件事。

### Now: I understand…

我理解這兩件事並不相同。如果 `fib` 是進入函式後才查 Dictionary，第二次呼叫 `fib(3)` 時仍然會進入函式，只是可以立即回傳快取結果，不必再發出原本的子遞迴呼叫。因此，Memoization 能避免重複計算，卻不表示相同參數絕不會再次被呼叫。

## ③ Challenge the AI

**One AI-generated question I challenged:** 第 4 題 — Memoization（記憶化）

**Why?**

- [ ] Ambiguous
- [x] Oversimplified
- [ ] Technically questionable
- [ ] Too easy
- [ ] Other

### Brief explanation

我認為原題對「減少函式呼叫次數」的描述有一點過度簡化，因為結果取決於快取檢查的位置。若在函式入口才查快取，快取命中時，這次函式呼叫仍然發生，只是省去之後的遞迴展開；若呼叫端先查快取，才可能連該次函式呼叫都省略。

原題的結論在常見的記憶化實作中仍成立。當所有遞迴呼叫共用同一份字典時，每個子問題最多只需要實際展開計算一次，Fibonacci 的計算量可由指數級降為線性級。題目更精確的說法應區分**函式呼叫**與**子問題的重新計算**。

## ④ One-Minute Reflection

**One thing I am still unsure about:**

我還想更熟悉快取 Dictionary 的作用域安排。例如，先執行 `fib(5)`，再執行 `fib(6)`，要如何讓第二次呼叫沿用先前的結果？我已理解可以在函式外建立字典，再把**同一份字典**傳給不同呼叫（如 `fib_efficient(n, d)`）；接下來希望透過實作，確認何時適合共用快取、何時應為新的計算建立新快取。

---

# Part B: LeetCode-style Lecture Code Transfer

**Name:** 劉育麟  
**Date:** 2026/11/09  
**Topic:** Recursion and Dictionaries

## 1. Today’s Challenge

**Core concept from today’s OCW lecture:**

遞迴處理巢狀資料結構，並利用 Dictionary 的可變性，讓每一層遞迴共同累加統計結果。

**AI-generated coding challenge title:** **Nested Tag Counter（巢狀標籤統計）**

**Challenge:** 輸入一個可包含字串與子 List 的巢狀 List，統計所有層級中每個字串標籤的出現次數，並回傳 Dictionary。

## 2. My Initial Approach — Before AI Help

**My approach:**

我會先建立空 Dictionary，再逐一走訪最外層 List。遇到子 List 時，就遞迴處理子 List 的所有元素；遇到字串時，就更新字典中的計數，第一次出現記為 1，往後每次出現加 1。空 List 不會進入迴圈，因此自然結束。所有遞迴層都共用一份字典，最後由外層函式回傳統計結果。

## 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

- [x] No — I solved it independently
- [ ] Yes — I received one or more hints

**The most useful hint/question from AI was:**

AI 在確認我的演算法後，提醒可以考慮利用 Nested Function 封裝遞迴處理，不過這不是必要條件。我沒有要求額外提示，而是自行寫出使用獨立輔助函式的程式。

**It helped me realize that:**

可以讓主函式負責建立與回傳 Dictionary，遞迴輔助函式負責走訪巢狀 List。只要各層傳遞同一個 `counts`，不論輔助函式是否巢狀定義，都能正確累加計數。

## 4. My Revision

**Did you change your approach or code after interacting with AI?**

- [x] No
- [ ] Yes

**What did you change, and why?**

我的初步演算法已能涵蓋巢狀 List、空 List 與重複字串，因此實作後無須修正。程式使用 `isinstance(item, list)` 判斷是否需要遞迴，若是字串就更新共用的字典。

## 5. Verification

**My final program:**

```python
def count_tags(data):
    counts = {}
    _count_nested_tags(data, counts)
    return counts


def _count_nested_tags(data, counts):
    for item in data:
        if isinstance(item, list):
            _count_nested_tags(item, counts)
        elif item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
```

- [x] Passed the provided examples
- [x] Passed additional edge cases
- [ ] Still has unresolved problems

**Verification summary:** 已核對題目提供的三組範例，另測試空 List、單一標籤、只有巢狀空 List、不同層重複標籤，共 **7 / 7** 組通過。

**One edge case I tested:**

**Input:**

```python
[[], [[], [[]]]]
```

**Expected output:** `{}`  
**Actual output:** `{}`

這個輸入只有空的子 List，沒有任何字串。每一層都不會更新 `counts`，因此回傳空字典。

## 6. One-Minute Reflection

**Why my solution works:**

每層遞迴以 `for` 迴圈走訪當前 List。遇到字串就統計一次；遇到子 List 就遞迴處理其元素，再回到上一層繼續走訪。因此每個字串的每次出現都會被拜訪且計數恰好一次。沒有子 List 時不再往下遞迴；空 List 的迴圈則直接結束。所有呼叫共用同一個 `counts`，不同層的相同標籤會累加在同一筆紀錄。

**Time and space complexity:**

設 `n` 為所有層級中的元素總數（包含作為元素的 List 與字串）、`d` 為最大巢狀深度、`k` 為不同標籤數，並假設字典查詢與更新平均為 O(1)。

| 項目 | 複雜度 | 原因 |
|---|---|---|
| 時間 | O(n) | 每個元素走訪一次，字典操作平均為 O(1)。 |
| 額外空間，不含回傳字典 | O(d) | 遞迴呼叫堆疊深度與最大巢狀深度成正比。 |
| 空間，含回傳字典 | O(d + k) | 除遞迴堆疊外，字典儲存 k 種標籤的計數。 |

**What idea from the OCW lecture did you transfer to this new problem?**

`lyrics_to_frequencies()` 以一層 `for` 迴圈統計平坦 List 中的字詞次數；這題延續相同的 Dictionary 計數方式，並加入 Recursion 以處理不限層數的巢狀 List。例如在 `['red', ['blue', 'red']]` 中，外層迴圈只會看到 `'red'` 與整個子 List；必須進一步遞迴走訪子 List 才能找到 `'blue'` 與第二個 `'red'`。

**One thing I understand better now:**

我更理解如何把遞迴走訪與共用 Dictionary 結合：各層負責自己的 List，但把統計結果寫入同一個可變物件，不需要在遞迴返回時合併多個字典。

**One thing I am still unsure about:**

我希望繼續練習在不同題目中選擇「透過參數傳入共用 Dictionary」或「由每層遞迴回傳結果再合併」的設計方式，並比較其可讀性與效率。
