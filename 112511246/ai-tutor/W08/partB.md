# Week 8 — AI Tutor Learning Record (Part B)

- 學號：112511246
- Name：張中愷
- Date：2026-11-10
- Topic：Lecture 12 — 搜尋與排序（Searching and Sorting）
- 程式檔：[w8.py](w8.py)
- 格式來源：[AI Tutor for AOOP 2026](https://github.com/ARG-NCTU/oop-python-nycu/blob/main/ai-tutor-2026.md)

## 1. Today's Challenge

**Core concept from today's OCW lecture:**

merge sort 的合併步驟：兩個已經排好的 list，用兩個位置 `i`、`j` 各自往前走，每次只比較兩邊最前面的元素 `left[i]` 和 `right[j]`，把比較小的放進結果。因為兩邊都已排好，最前面的就是各自剩下的最小值，每個元素只看一次，所以合併是 O(n)。

**AI-generated coding challenge title:** Common Students（兩門課都有修的學生）

### 題目

兩門課的修課名單，學號都已由小到大排好，同一份名單內不重複。寫一個函式 `common_students(A, B)`，回傳兩門課都有修的學號，結果也要由小到大。

- 規定：必須是 O(n + m)（n、m 為兩份名單的長度）；不能用 `in`、字典、`sort()`、`sorted()`，也不能用兩層迴圈。
- 限制：兩份名單都已排序、各自沒有重複，可能為空，長度各自最多 10 萬。

| 呼叫 | 結果 | 說明 |
|---|---|---|
| `common_students([3, 5, 8, 10], [1, 5, 6, 10, 12])` | `[5, 10]` | 5 和 10 兩邊都有 |
| `common_students([1, 2, 3], [4, 5])` | `[]` | 沒有共同的 |
| `common_students([], [1, 2])` | `[]` | 一邊是空的 |
| `common_students([2, 4, 6], [2, 4, 6])` | `[2, 4, 6]` | 完全一樣 |

## 2. My Initial Approach — Before AI Help

用 `i`、`j` 分別指著兩份名單，比較 `A[i]` 和 `B[j]`：相等就加進結果，兩邊都往前；不相等就讓比較小的那邊往前；任一邊走完就停止。

## 3. AI Tutor Help

- [ ] No — I solved it independently
- [x] Yes — I received one or more hints

**The most useful hint/question from AI was:**

AI 在出題時提醒：Lecture 10 的 `intersect` 因為用了 `in` 而是 O(n²)，這題可以利用「兩邊都已經排好」來降低複雜度；並問我：如果 `A[i]` 比 `B[j]` 小，它在 B 裡還有可能出現嗎？

**It helped me realize that:**

B 從 `B[j]` 往後只會越來越大，所以比 `B[j]` 小的 `A[i]` 不可能出現在 B 的後面，可以直接丟掉、讓 i 往前。有了這個提示後，演算法的三種情況和停止條件是我回答出來的，AI 確認正確，沒有需要修正的地方。

## 4. My Revision

- [x] No
- [ ] Yes

**What did you change, and why?**

演算法第一次回答就正確，沒有修改。程式碼由 AI 依照我的演算法寫出，一次就通過所有測試。

這題跟課堂的 `merge` 幾乎一樣，差別在於：

| | 課堂的 `merge` | 這題 |
|---|---|---|
| 比較小的那個 | 放進結果，往前 | 丟掉，往前 |
| 相等的時候 | 放一個進結果 | 放進結果，兩邊都往前 |
| 一邊走完之後 | 另一邊剩下的全部接上 | 直接停止 |

用範例手動追蹤（`A = [3, 5, 8, 10]`、`B = [1, 5, 6, 10, 12]`）：

| 比較 | 結果 | 做什麼 |
|---|---|---|
| 3 vs 1 | 3 > 1 | j 往前 |
| 3 vs 5 | 3 < 5 | i 往前 |
| 5 vs 5 | 相等 | 加入 5，兩邊都往前 |
| 8 vs 6 | 8 > 6 | j 往前 |
| 8 vs 10 | 8 < 10 | i 往前 |
| 10 vs 10 | 相等 | 加入 10，兩邊都往前 |
| A 走完 | | 停止，回傳 `[5, 10]` |

### 最終程式

```python
def common_students(A, B):
    result = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            result.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return result
```

## 5. Verification

- [x] Passed the provided examples
- [x] Passed additional edge cases
- [ ] Still has unresolved problems

另外測試的邊界情況：

| 測試 | 輸入 | 預期輸出 | 實際輸出 |
|---|---|---|---|
| 兩邊都空 | `[]`, `[]` | `[]` | `[]` |
| 各一個且相同 | `[5]`, `[5]` | `[5]` | `[5]` |
| 交錯但沒有共同 | `[1, 3, 5]`, `[2, 4, 6]` | `[]` | `[]` |
| 共同的在最後 | `[1, 2, 3, 100]`, `[100]` | `[100]` | `[100]` |
| 共同的在最前 | `[1]`, `[1, 2, 3, 4]` | `[1]` | `[1]` |
| 隨機測資 | 2000 組隨機已排序、不重複的名單，與集合交集的結果比對 | 全部一致 | 全部一致 |

**One edge case I tested:**

- Input：`common_students([1, 2, 3, 100], [100])`
- Expected output：`[100]`
- Actual output：`[100]`

B 只有一個很大的數，j 會一直停在 100，i 必須一路往前走到 A 的最後才遇到相等，確認迴圈不會太早停止。

### 執行時間（與 Lecture 10 兩層迴圈的 `intersect` 比較，兩邊無共同元素的情況）

| n | `intersect`（兩層迴圈） | `common_students` |
|---|---|---|
| 1,000 | 0.0124 秒 | 0.00023 秒 |
| 2,000 | 0.0512 秒 | 0.00052 秒 |
| 4,000 | 0.4413 秒 | 0.00117 秒 |
| 1,000,000 | （未執行） | 0.243 秒 |

`intersect` 的 n 變 2 倍、時間變 4 倍以上（O(n²)）；`common_students` 的 n 變 2 倍、時間約變 2 倍（O(n)）。

### Why my solution works

兩份名單都已由小到大排好。比較 `A[i]` 和 `B[j]` 時：相等代表找到一個共同學號，加入結果後兩邊都往前；如果 `A[i] < B[j]`，B 中 `B[j]` 以後的數都比 `B[j]` 大，而 `B[j]` 之前的數已經比過了，所以 `A[i]` 不可能出現在 B 裡，可以丟掉、i 往前；`A[i] > B[j]` 時同理 j 往前。任一邊走完後，另一邊剩下的數都沒有對象可以配，所以可以停止。結果依照遇到的順序加入，而兩邊都是由小到大，所以結果自然也是由小到大。

### Time complexity

每一輪迴圈 i 或 j 至少有一個往前一格，i 最多走 n 步、j 最多走 m 步，所以迴圈最多執行 n + m 次，每次只做比較和加一，複雜度為 **O(n + m)**。

## 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**

merge sort 的合併技巧：兩個已排序的 list 用兩個位置同時往前走，每次只比最前面的元素。原本用在把兩個 list 合成一個，這裡改成找共同的元素。

**One thing I understand better now:**

資料是否已經排好，會直接影響能用什麼演算法。同樣是找兩個 list 的共同元素，沒排好時 Lecture 10 的 `intersect` 是 O(n²)；排好之後用合併的方式只要 O(n + m)。

**One thing I am still unsure about:**

如果兩份名單本來沒有排好，要先排序（各 O(n log n)）再用這個方法，還是直接用字典查詢（O(n + m)）比較好？我還不確定實際上該怎麼選。
