# Week 2 — AI Tutor Learning Record (Part B)

- 學號：112511246
- Name：張中愷
- Date：2026-10-13
- Topic：Lecture 6 — 遞迴與字典（Recursion and Dictionaries）
- 程式檔：[w2.py](w2.py)
- 格式來源：[AI Tutor for AOOP 2026](https://github.com/ARG-NCTU/oop-python-nycu/blob/main/ai-tutor-2026.md)

## 1. Today's Challenge

**Core concept from today's OCW lecture:**

字典用 key 查 value。課堂把歌詞整理成「每個字 → 出現次數」的字典：走過每個字，先用 `in` 檢查這個 key 是否已經在字典裡，不在就新增，在就更新它的 value。

**AI-generated coding challenge title:** Group by Grade（依成績分組）

### 題目

給一個「學生 → 成績」的字典 `grades`，寫一個函式 `group_by_grade(grades)`，回傳一個新的字典：

- key 是成績
- value 是拿到這個成績的學生名單（list），依名字的字母順序排序

**規定：原本的 `grades` 不能被改到。**

- 輸入：`grades` 為字典，key 為學生名字（字串，不重複），value 為成績（字串，例如 `'A'`、`'B+'`）；學生人數 0～50，可能為空。
- 輸出：字典，key 為成績，value 為排序後的學生名字 list。

| 範例 | 輸入 | 輸出 |
|---|---|---|
| 1 | `{'Ana': 'B', 'John': 'A', 'Kyle': 'A'}` | `{'B': ['Ana'], 'A': ['John', 'Kyle']}`，且 `grades` 不變 |
| 2 | `{'Zoe': 'C', 'Amy': 'C', 'Max': 'C'}` | `{'C': ['Amy', 'Max', 'Zoe']}` |
| 3 | `{}` | `{}` |

## 2. My Initial Approach — Before AI Help

開一個新的字典，掃過 `grades`，成績不在新字典裡就新增一個 list，已經在就把名字 append 進去。

## 3. AI Tutor Help

- [ ] No — I solved it independently
- [x] Yes — I received one or more hints

**The most useful hint/question from AI was:**

AI 用範例 2 `{'Zoe': 'C', 'Amy': 'C', 'Max': 'C'}` 問我：照我的做法掃完會得到 `['Zoe', 'Amy', 'Max']`，還沒排好，要在什麼時間點排序、排的是哪個東西？另外問我 `for name in grades` 每一輪拿到的是什麼、成績要怎麼拿到。

我的程式寫成 `new_grades.sort()` 出現 `AttributeError: 'dict' object has no attribute 'sort'` 時，AI 提示我要排的不是整個字典，而是字典裡每個成績對應的 list，`new_grades[成績]` 拿到的就是那個 list。

**It helped me realize that:**

字典本身不能排序，`sort()` 是 list 的方法；要先用 key 取出 value（list），再對那個 list 排序。另外 `for name in grades` 拿到的是 key（名字），成績要用 `grades[name]` 查。

## 4. My Revision

- [ ] No
- [x] Yes

**What did you change, and why?**

1. 第一版只做了分組，忘了排序，範例 2 輸出 `['Zoe', 'Amy', 'Max']`，沒有通過。
2. 第二版在 return 前寫 `new_grades.sort()`，因為字典沒有 `sort` 方法而出錯。
3. 第三版改成每次 append 之後就對那個 list 排序。結果正確，但 AI 指出這樣每加一個名字就排一次：如果 50 個人都是 A，會排 49 次，比最後排一次慢。
4. 最終版把排序移到分組完成之後，再用一個 for 走過新字典，對每個成績的 list 各排序一次。

### 最終程式

```python
def group_by_grade(grades):
    new_grades = {}
    for i in grades:
        if grades[i] in new_grades:
            new_grades[grades[i]].append(i)
        else:
            new_grades[grades[i]] = [i]
    for j in new_grades:
        new_grades[j].sort()
    return new_grades
```

## 5. Verification

- [x] Passed the provided examples
- [x] Passed additional edge cases
- [ ] Still has unresolved problems

另外測試的邊界情況（每一項都同時檢查原本的 `grades` 沒有被改到）：

| 測試 | 輸入 | 預期輸出 | 實際輸出 |
|---|---|---|---|
| 全部同成績、需要排序 | `{'Zoe': 'C', 'Amy': 'C', 'Max': 'C'}` | `{'C': ['Amy', 'Max', 'Zoe']}` | `{'C': ['Amy', 'Max', 'Zoe']}` |
| 只有一個學生 | `{'Kyle': 'A'}` | `{'A': ['Kyle']}` | `{'A': ['Kyle']}` |
| 每人成績都不同 | `{'Ana': 'A', 'Bob': 'B', 'Cat': 'C'}` | `{'A': ['Ana'], 'B': ['Bob'], 'C': ['Cat']}` | `{'A': ['Ana'], 'B': ['Bob'], 'C': ['Cat']}` |
| `B` 與 `B+` 要分開 | `{'Dan': 'B+', 'Eve': 'B', 'Fay': 'B+'}` | `{'B+': ['Dan', 'Fay'], 'B': ['Eve']}` | `{'B+': ['Dan', 'Fay'], 'B': ['Eve']}` |
| 兩組都要各自排序 | `{'Tom': 'A', 'Ann': 'B', 'Sam': 'A', 'Bea': 'B'}` | `{'A': ['Sam', 'Tom'], 'B': ['Ann', 'Bea']}` | `{'A': ['Sam', 'Tom'], 'B': ['Ann', 'Bea']}` |
| 名字大小寫混合 | `{'bob': 'A', 'Amy': 'A', 'Ben': 'A'}` | `{'A': ['Amy', 'Ben', 'bob']}` | `{'A': ['Amy', 'Ben', 'bob']}` |
| 空字典 | `{}` | `{}` | `{}` |

**One edge case I tested:**

- Input：`group_by_grade({'Zoe': 'C', 'Amy': 'C', 'Max': 'C'})`
- Expected output：`{'C': ['Amy', 'Max', 'Zoe']}`
- Actual output：`{'C': ['Amy', 'Max', 'Zoe']}`

這組在第一版沒有通過（輸出 `['Zoe', 'Amy', 'Max']`），因為範例 1 的 John、Kyle 剛好本來就照字母順序，所以只看範例 1 發現不了少了排序。

### Why my solution works

`grades` 只被 for 迴圈讀取，沒有被修改；所有資料都放進新的字典 `new_grades`。每個學生用 `grades[i]` 查出成績，成績第一次出現就建立只有這個名字的 list，之後再出現就 append，最後再對每個成績的 list 排序。

### Time complexity

第一個 for 把 n 個學生各看一次是 O(n)。最後排序時，最差情況是所有人同一個成績，等於排一個長度 n 的 list，是 O(n log n)。整體為 **O(n log n)**。

## 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**

字典。課堂數每個字出現幾次時，是「不在就新增、在就更新」；這題用一樣的模式，只是 value 從次數換成名字的 list，不在就建立新 list，在就 append。

**One thing I understand better now:**

`sort()` 是 list 的方法，字典不能直接排序；要先用 key 取出 value 再排。另外，結果一樣的兩種寫法速度可能差很多，每次 append 都排序就比最後排一次慢。

**One thing I am still unsure about:**

範例 1 輸出的字典是 `{'B': [...], 'A': [...]}`，B 排在 A 前面。字典的 key 印出來的順序是怎麼決定的，能不能讓成績也照順序排，我還不確定。
