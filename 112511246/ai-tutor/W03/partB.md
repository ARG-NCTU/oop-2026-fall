# Week 3 — AI Tutor Learning Record (Part B)

- 學號：112511246
- Name：張中愷
- Date：2026-10-13
- Topic：Lecture 7 — 測試、除錯、例外與斷言（Testing, Debugging, Exceptions, and Assertions）
- 程式檔：[w3.py](w3.py)
- 格式來源：[AI Tutor for AOOP 2026](https://github.com/ARG-NCTU/oop-python-nycu/blob/main/ai-tutor-2026.md)

## 1. Today's Challenge

**Core concept from today's OCW lecture:**

用 `try / except` 接住執行時的錯誤，讓程式不會整個當掉；遇到不合理的情況，用 `raise` 主動丟出一個說明清楚的錯誤。課堂的 `get_ratios` 在遇到除以 0 時用 `except ZeroDivisionError` 接住，改放 `nan` 後繼續執行。

**AI-generated coding challenge title:** Safe Average（安全的平均分數）

### 題目

同學自行輸入的成績是一串文字，可能有亂打的內容。寫一個函式 `average_scores(texts)`：

1. 把每個文字用 `int()` 轉成整數
2. 轉不了的（例如 `"abc"`）算一筆壞資料並跳過，程式不能當掉
3. 轉得了但不在 0～100 之間的（例如 `"150"`）也算壞資料並跳過
4. 用剩下的好資料計算平均
5. 用 tuple 回傳 `(平均, 壞資料筆數)`
6. 如果沒有任何好資料，就 `raise ValueError("沒有有效的成績")`

- 輸入：`texts` 為字串 list，長度 0～50，可能為空。
- 輸出：tuple `(平均, 壞資料筆數)`，平均為小數；沒有好資料時丟出 `ValueError`。

| 範例 | 輸入 | 輸出 |
|---|---|---|
| 1 | `["80", "abc", "90"]` | `(85.0, 1)` |
| 2 | `["100", "-5", "70", "x"]` | `(85.0, 2)` |
| 3 | `["abc", ""]` | `ValueError: 沒有有效的成績`（外面用 `try / except` 接住後印出 `錯誤： 沒有有效的成績`） |

## 2. My Initial Approach — Before AI Help

用 try 把文字轉成 int，失敗就把壞資料計數加 1，成功再檢查範圍，最後如果沒有資料就 raise。

## 3. AI Tutor Help

- [ ] No — I solved it independently
- [x] Yes — I received one or more hints

**The most useful hint/question from AI was:**

AI 問我三件事：轉成功之後的範圍檢查要放在哪裡（提示 try 後面可以接 `else`，只有 try 沒出錯時才執行）；好資料要怎麼存下來算平均；raise 要放在算平均的前面還是後面——如果沒有好資料就先算平均，`總和 / 0` 會發生什麼錯誤。

**It helped me realize that:**

範圍檢查放在 `else` 最自然，因為那時候已經確定轉換成功、手上有整數可以檢查。raise 一定要放在算平均之前，否則沒有好資料時會先發生 `ZeroDivisionError`；自己先檢查、丟出「沒有有效的成績」，錯誤原因會清楚很多。

## 4. My Revision

- [ ] No
- [x] Yes

**What did you change, and why?**

第一版就通過了所有範例和邊界測試，但 `int(i)` 寫了 4 次：try 裡面轉完沒有存起來，後面檢查範圍和 append 時又各轉一次。AI 指出這點後，我改成在 try 裡寫 `score = int(i)`，轉一次就存進 `score`，後面都直接用 `score`，程式比較清楚，也不用重複轉換。

### 最終程式

```python
def average_scores(texts):
    count = 0
    new_texts = []
    for i in texts:
        try:
            score = int(i)
        except ValueError:
            count += 1
        else:
            if score < 0 or score > 100:
                count += 1
            else:
                new_texts.append(score)
    if len(new_texts) == 0:
        raise ValueError("沒有有效的成績")
    else:
        average = sum(new_texts) / len(new_texts)
        return (average, count)
```

## 5. Verification

- [x] Passed the provided examples
- [x] Passed additional edge cases
- [ ] Still has unresolved problems

另外測試的邊界情況：

| 測試 | 輸入 | 預期輸出 | 實際輸出 |
|---|---|---|---|
| 0 和 100 剛好在邊界上 | `["0", "100"]` | `(50.0, 0)` | `(50.0, 0)` |
| -1 和 101 剛好超出邊界 | `["-1", "101", "50"]` | `(50.0, 2)` | `(50.0, 2)` |
| 含小數點 | `["8.5", "70"]` | `(70.0, 1)` | `(70.0, 1)` |
| 前後有空白 | `[" 80 "]` | `(80.0, 0)` | `(80.0, 0)` |
| 只有一筆 | `["75"]` | `(75.0, 0)` | `(75.0, 0)` |
| 平均不是整數 | `["1", "2"]` | `(1.5, 0)` | `(1.5, 0)` |
| 空 list | `[]` | `ValueError: 沒有有效的成績` | `ValueError: 沒有有效的成績` |
| 全部超出範圍 | `["200", "-3"]` | `ValueError: 沒有有效的成績` | `ValueError: 沒有有效的成績` |

**One edge case I tested:**

- Input：`average_scores(["0", "100"])`
- Expected output：`(50.0, 0)`
- Actual output：`(50.0, 0)`

0 和 100 都在範圍內，所以條件寫成 `score < 0 or score > 100` 才算壞資料，邊界值本身算好資料。

### Why my solution works

`"abc"` 這類文字在 `int()` 時會丟出 `ValueError`，被 `except ValueError` 接住後只把計數加 1，程式繼續處理下一筆，不會當掉。轉換成功的才進 `else` 檢查範圍，合格的放進 list。最後先檢查 list 是否為空，空的就自己 raise，避免後面 `sum / len` 變成除以 0。

### Time complexity

for 迴圈把 n 筆資料各看一次是 O(n)，`sum` 走過一次也是 O(n)，`len` 是 O(1)。沒有排序，整體為 **O(n)**。

## 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**

`try / except` 和 `raise`。課堂用 `except` 接住除以 0 讓程式繼續跑；這題用 `except` 接住轉換失敗的文字，並在沒有好資料時自己 raise，而不是讓它自然變成 `ZeroDivisionError`，因為自己 raise 的錯誤訊息比較清楚。

**One thing I understand better now:**

`try` 後面的 `else` 只有在沒出錯時才執行，適合放「轉換成功之後才要做的事」。另外，轉換的結果要存進變數，不然後面每次要用都得重新轉一次。

**One thing I am still unsure about:**

測試時發現 `int(" 80 ")` 前後有空白也轉得過，但 `int("8.5")` 會出錯。如果想讓 `"8.5"` 這種小數成績也算有效，要怎麼改，以及 `int()` 到底接受哪些格式，我還不確定。
