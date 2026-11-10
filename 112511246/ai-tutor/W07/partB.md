# Week 7 — AI Tutor Learning Record (Part B)

- 學號：112511246
- Name：張中愷
- Date：2026-11-10
- Topic：Lecture 11 — 理解程式效率（二）（Understanding Program Efficiency, Part 2）
- 程式檔：[w7.py](w7.py)
- 格式來源：[AI Tutor for AOOP 2026](https://github.com/ARG-NCTU/oop-python-nycu/blob/main/ai-tutor-2026.md)

## 1. Today's Challenge

**Core concept from today's OCW lecture:**

二分搜尋每次看中間的元素、丟掉一半的範圍，是 O(log n)。課堂的 `bisect_search1` 用 `L[:half]` 複製 list，每次複製是 O(n)，反而讓整體變成 O(n)；`bisect_search2` 改用 `low`、`high` 兩個位置記住目前的範圍，不複製 list，才是真正的 O(log n)。

**AI-generated coding challenge title:** First Passing Score（第一個及格的位置）

### 題目

成績已由小到大排好。寫兩個函式：

| 函式 | 要做什麼 |
|---|---|
| `first_at_least(L, x)` | 回傳 L 中第一個 ≥ x 的位置；若全部都比 x 小，回傳 `len(L)` |
| `count_pass(L, limit)` | 回傳 ≥ limit 的人數，必須使用 `first_at_least` 計算 |

- 規定：`first_at_least` 必須是 O(log n)，不能用 `L[a:b]` 切片複製、不能用 `in`、不能用 for 走完整個 list。
- 限制：L 已由小到大排序，可能有重複、可能為空，長度最多 100 萬。

| 呼叫（`scores = [45, 60, 60, 72, 90]`） | 結果 | 說明 |
|---|---|---|
| `first_at_least(scores, 60)` | `1` | 第一個 60 在位置 1，不是 2 |
| `first_at_least(scores, 61)` | `3` | 第一個 ≥ 61 的是 72 |
| `first_at_least(scores, 0)` | `0` | 全部都 ≥ 0 |
| `first_at_least(scores, 100)` | `5` | 沒有 ≥ 100 的，回傳 `len(L)` |
| `first_at_least([], 60)` | `0` | 空 list |
| `count_pass(scores, 60)` | `4` | 60、60、72、90 |

## 2. My Initial Approach — Before AI Help

`count_pass` 用「list 長度減掉第一個及格的位置」計算。二分搜尋時，如果中間的數 ≥ x 就往左找，因為前面可能還有同樣的分數（例如兩個 60），所以看到 60 不能直接回傳。

## 3. AI Tutor Help

- [ ] No — I solved it independently
- [x] Yes — I received one or more hints

**The most useful hint/question from AI was:**

AI 要我先定義範圍的意思：「答案一定在 low 到 high 之間（包含兩端）」，而且 `high` 要從 `len(L)` 開始而不是 `len(L) - 1`，因為「全部都不及格時回傳 `len(L)`」本身也是可能的答案。接著用 `[45, 60, 60, 72, 90]` 找 60 為例：如果 mid 剛好是 1，`L[1] = 60` 就是正確答案，所以往左縮時不能寫 `high = mid - 1`，否則會把答案丟掉。

**It helped me realize that:**

兩種情況縮範圍的方式不對稱：`L[mid] >= x` 時 mid 可能就是答案，要寫 `high = mid` 把它留著；`L[mid] < x` 時 mid 一定不是答案，寫 `low = mid + 1` 丟掉。範圍縮到 low 和 high 碰在一起就停，所以條件是 `while low < high`。

## 4. My Revision

- [ ] No
- [x] Yes

**What did you change, and why?**

一開始我只想到「≥ x 就往左找」，沒有想清楚 mid 本身要不要留、`< x` 時要怎麼縮、什麼時候停。經過 AI 的提示後，我決定：`L[mid] >= x` 時 `high = mid`，`L[mid] < x` 時 `low = mid + 1`，迴圈條件 `while low < high`，`high` 從 `len(L)` 開始。程式碼由 AI 依照這三個決定寫出。

用範例手動追蹤（找 60）：

| 輪 | low | high | mid | L[mid] | 判斷 | 結果 |
|---|---|---|---|---|---|---|
| 開始 | 0 | 5 | | | | |
| 1 | 0 | 5 | 2 | 60 | ≥ 60 | high = 2 |
| 2 | 0 | 2 | 1 | 60 | ≥ 60 | high = 1 |
| 3 | 0 | 1 | 0 | 45 | < 60 | low = 1 |
| 結束 | 1 | 1 | | | low == high | 回傳 1 |

第 1 輪先碰到位置 2 的 60，但沒有停下來，繼續往左，最後找到位置 1 的第一個 60。

### 最終程式

```python
def first_at_least(L, x):
    low = 0
    high = len(L)
    while low < high:
        mid = (low + high) // 2
        if L[mid] >= x:
            high = mid
        else:
            low = mid + 1
    return low


def count_pass(L, limit):
    return len(L) - first_at_least(L, limit)
```

## 5. Verification

- [x] Passed the provided examples
- [x] Passed additional edge cases
- [ ] Still has unresolved problems

另外測試的邊界情況：

| 測試 | 輸入 | 預期輸出 | 實際輸出 |
|---|---|---|---|
| 只有一個數字，剛好等於 | `first_at_least([60], 60)` | `0` | `0` |
| 只有一個數字，不及格 | `first_at_least([59], 60)` | `1` | `1` |
| 全部一樣 | `first_at_least([60, 60, 60], 60)` | `0` | `0` |
| 答案在最後一個 | `first_at_least([10, 20, 30], 30)` | `2` | `2` |
| 全部不及格 | `first_at_least([10, 20, 30], 31)` | `3` | `3` |
| 隨機測資 | 2000 組長度 0～12 的已排序 list，與 Python 內建 `bisect.bisect_left` 及直接計數比對 | 全部一致 | 全部一致 |

**One edge case I tested:**

- Input：`first_at_least([60, 60, 60], 60)`
- Expected output：`0`
- Actual output：`0`

三個都是 60 時，必須回傳第一個的位置 0。如果看到 `L[mid] == 60` 就直接回傳，會回傳中間的位置 1，答案就錯了。

### 執行時間

| n | 搜尋 1000 次 |
|---|---|
| 1,000 | 0.0008 秒 |
| 1,000,000 | 0.0016 秒 |

資料變大 1000 倍，時間只變約 2 倍：1000 砍一半約 10 次就剩一個，100 萬約 20 次，符合 O(log n)。

### Why my solution works

範圍 `[low, high]` 一直保持「答案一定在裡面」。`L[mid] >= x` 時，mid 可能是答案，而 mid 右邊的位置都不會比 mid 更早，所以縮成 `high = mid`；`L[mid] < x` 時，mid 和它左邊的數都比 x 小，都不是答案，所以縮成 `low = mid + 1`。每一輪範圍至少縮小一格，最後 low 和 high 相等時，那個位置就是第一個 ≥ x 的位置；如果全部都比 x 小，low 會一路被推到 `len(L)`。`count_pass` 則利用 list 已排序：第一個及格的位置之後全部都及格，所以人數是 `len(L)` 減去那個位置。

### Time complexity

每一輪把範圍砍一半，總共約 log n 輪；每一輪只做比較和整數運算，是 O(1)，而且沒有複製 list，所以 `first_at_least` 是 **O(log n)**。`count_pass` 呼叫一次 `first_at_least` 再做一次減法，也是 **O(log n)**。

## 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**

課堂 `bisect_search2` 的做法：用 `low`、`high` 記住搜尋範圍，不用 `L[:half]` 複製 list，才能保持 O(log n)。這題把「有沒有」改成「第一個在哪裡」，所以找到相同的值也不能停，要繼續往左縮。

**One thing I understand better now:**

二分搜尋最容易錯的地方是邊界：範圍的兩端代表什麼、mid 本身要不要留、迴圈什麼時候停。先把「答案一定在 low 到 high 之間」這句話定好，三個邊界就都能推出來。

**One thing I am still unsure about:**

如果要找的是「最後一個 ≤ x 的位置」，`high` 的起始值和兩種情況的縮法要怎麼改，我還沒有把握一次寫對。
