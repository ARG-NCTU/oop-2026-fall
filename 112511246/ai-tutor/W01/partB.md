# Week 1 — AI Tutor Learning Record (Part B)

- 學號：112511246
- Name：張中愷
- Date：2026-10-13
- Topic：Lecture 5 — Tuple、List、別名、可變性與複製（Tuples, Lists, Aliasing, Mutability, and Cloning）
- 程式檔：[w1.py](w1.py)
- 格式來源：[AI Tutor for AOOP 2026](https://github.com/ARG-NCTU/oop-python-nycu/blob/main/ai-tutor-2026.md)

## 1. Today's Challenge

**Core concept from today's OCW lecture:**

list 是可變的（mutable），修改 list 會影響所有指向它的名字（別名）；要保留原本的資料就不能直接改它。另外 `sort()` 會改到原本的 list 並回傳 `None`，`sorted()` 則回傳新的 list；邊走訪 list 邊刪除元素會跳過元素。

**AI-generated coding challenge title:** Pass List（及格名單）

### 題目

寫一個函式 `pass_list(scores, limit)`：

1. 找出所有大於或等於 `limit` 的分數
2. 由小到大排序，放進一個新的 list
3. 計算不及格（被排除）的分數有幾個
4. 用 tuple 回傳 `(及格名單, 不及格人數)`

**規定：函式執行完後，原本的 `scores` 必須完全不變（內容與順序都不能變）。**

- 輸入：`scores` 為整數 list，長度 0～100，可能為空、可能有重複；每個分數 0～100。`limit` 為整數。
- 輸出：tuple `(排好的及格名單, 不及格人數)`

| 範例 | 輸入 | 輸出 |
|---|---|---|
| 1 | `[70, 45, 90, 60]`, 60 | `([60, 70, 90], 1)`，且 `scores` 仍為 `[70, 45, 90, 60]` |
| 2 | `[50, 80, 50]`, 60 | `([80], 2)` |
| 3 | `[]`, 60 | `([], 0)` |

## 2. My Initial Approach — Before AI Help

先把 `scores` 複製一份，再把複製出來的 list 裡小於 `limit` 的分數刪掉，最後用 `sorted` 排序。

## 3. AI Tutor Help

- [ ] No — I solved it independently
- [x] Yes — I received one or more hints

**The most useful hint/question from AI was:**

AI 要我用 `copy = [40, 50, 80]`、`limit = 60` 在腦中跑一次「邊用 for 走訪、邊從同一個 list 刪除」：刪掉位置 0 的 40 之後，50 會往前移到位置 0，下一輪 for 去看位置 1，50 就被跳過了。AI 接著問：除了從 list 裡「刪掉不要的」，能不能改成「開一個空的 list，把要的放進去」？另外也提醒我：`copy = scores` 只是別名，不是複製；以及我的做法還沒處理「不及格人數」要怎麼算。

**It helped me realize that:**

根本不需要複製再刪除。只要開一個新的 list，掃過 `scores` 時把及格的放進去、不及格的就計數，`scores` 從頭到尾只被讀取、沒有被修改，自然不會被改到，也避開了邊走訪邊刪除的陷阱。

## 4. My Revision

- [ ] No
- [x] Yes

**What did you change, and why?**

把做法從「複製一份再刪除」改成「開新的 list，只把及格的 append 進去，不及格的 `count += 1`，最後對新 list 排序」。原因是刪除的做法會遇到邊走訪邊刪除跳過元素的問題，而且還要另外確保複製方式正確；新做法只讀取 `scores`，比較簡單也比較安全。

寫程式時，第一版在 `else` 後面少了冒號，執行出現 `SyntaxError: expected ':'`（第 12 行），看錯誤訊息後自行補上。另外確認了 Python 沒有 `count++`，要寫 `count += 1`；排序用 `passed.sort()`，沒有寫成會得到 `None` 的 `passed = passed.sort()`。

### 最終程式

```python
def pass_list(scores, limit):
    passed = []
    count = 0

    for i in scores:
        if i >= limit:
            passed.append(i)
        else:
            count += 1

    passed.sort()
    return (passed, count)
```

## 5. Verification

- [x] Passed the provided examples
- [x] Passed additional edge cases
- [ ] Still has unresolved problems

另外測試的邊界情況（每一項都同時檢查原本的 `scores` 沒有被改到）：

| 測試 | 輸入 | 預期輸出 | 實際輸出 |
|---|---|---|---|
| 全部剛好等於及格線 | `[60, 60, 60]`, 60 | `([60, 60, 60], 0)` | `([60, 60, 60], 0)` |
| 全部不及格 | `[10, 20, 30]`, 60 | `([], 3)` | `([], 3)` |
| 最大最小值與重複 | `[100, 0, 100, 0]`, 60 | `([100, 100], 2)` | `([100, 100], 2)` |
| 及格線前後各差 1 | `[59, 60, 61]`, 60 | `([60, 61], 1)` | `([60, 61], 1)` |
| 及格線為 0 | `[90, 80, 70]`, 0 | `([70, 80, 90], 0)` | `([70, 80, 90], 0)` |
| 及格線為 100 | `[99, 100]`, 100 | `([100], 1)` | `([100], 1)` |
| 只有一個分數 | `[75]`, 60 | `([75], 0)` | `([75], 0)` |

**One edge case I tested:**

- Input：`pass_list([60, 60, 60], 60)`
- Expected output：`([60, 60, 60], 0)`
- Actual output：`([60, 60, 60], 0)`

剛好等於及格線的分數要算及格，所以條件用 `>=` 而不是 `>`。

### Why my solution works

`scores` 只被 for 迴圈讀取，沒有對它做 append、remove 或 sort，所以它不會被改到。及格的分數放進新的 list `passed`，排序的也是 `passed`，最後用 tuple 一次回傳及格名單和不及格人數。

### Time complexity

for 迴圈把 n 個分數各看一次是 O(n)，排序是 O(n log n)，取較大的，整體為 **O(n log n)**。

## 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**

不要動到原本的 list。課堂講 list 可變、別名和複製，以及邊走訪邊修改 list 會出錯；這題我用「開新的 list、只讀原本的 list」來保證原本的資料不變。

**One thing I understand better now:**

想保留原本的 list 時，不一定要先複製再修改，直接建立新的 list、把需要的元素放進去更簡單，也不會遇到邊走訪邊刪除跳過元素的問題。

**One thing I am still unsure about:**

排序的時間複雜度為什麼是 O(n log n)。這次是照提示知道排序比迴圈慢，但 log n 是怎麼來的、Python 的 `sort()` 實際上怎麼排，我還不清楚。
