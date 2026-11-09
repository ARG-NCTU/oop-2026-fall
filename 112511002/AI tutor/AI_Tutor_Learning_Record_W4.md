# AI Tutor Learning Record — W4 / MIT 6.0001 Lecture 8

**Name:** 劉育麟  
**Date:** 2026/11/09  
**Topic:** Object-Oriented Programming, Classes, Instances, Methods, Operator Overloading, Encapsulation

---

# Part A: True or False

## ① Check My Understanding

**Questions completed:** 5 / 5  
**Answers revised after AI hints:** 1 / 5

| 題號 | 主題 | 我的最終答案 | 結果 |
| --- | --- | --- | --- |
| 1 | Class、Instance 與 Attributes | False | 最初選 True，提示後修正 |
| 2 | `self` 與 Method Calling | True | 首次答對 |
| 3 | Operator Overloading 與 Object Mutation | False | 首次答對 |
| 4 | `__str__` 與 Side Effects | False | 首次答對 |
| 5 | Data Abstraction 與 Representation Invariants | False | 首次答對 |

**本次測驗的關鍵觀察：**

- 第 1 題：`a = Coordinate(3, 4)` 和 `b = Coordinate(3, 4)` 會建立不同實例。即使初始值相同，執行 `a.x = 10` 後，`a.x` 為 `10`，`b.x` 仍為 `3`；`a is b` 為 `False`。
- 第 2 題：`a.distance(b)` 與 `Coordinate.distance(a, b)` 等價，`self` 都是 `a`，`other` 都是 `b`，距離為 `5.0`。
- 第 3 題：`a + b` 會執行 `a.__add__(b)`，並用 `return Fraction(top, bott)` 建立新物件。`a` 仍為 `1/4`、`b` 為 `3/4`，`c` 的分子與分母為 `16`、`16`，不會自動約分；`c is a` 為 `False`。
- 第 4 題：在 `__str__()` 中使用 `self.vals.sort()` 會直接修改原本的 List，因此印出 `[1, 3]` 後，`s.vals` 也變成 `[1, 3]`。
- 第 5 題：`s.insert(2)` 會避免重複，但直接呼叫 `s.vals.append(2)` 會繞過檢查，最後得到 `[2, 2]`。

## ② My Misconception

### Before: I thought…

我原本以為 `__str__()` 只是把物件轉成字串，所以執行 `print(s)` 不會改變物件的狀態。

### Now: I understand…

第 4 題讓我發現，`__str__()` 雖然需要回傳字串，但裡面的 `self.vals.sort()` 會直接修改原本的串列。因此，印出 `[1, 3]` 後，`s.vals` 也會從 `[3, 1]` 變成 `[1, 3]`。

如果只是希望顯示結果經過排序，可以改用 `sorted(self.vals)` 建立排序後的新 List，再轉成字串，而不修改原本的物件狀態。

另外，第 1 題也讓我修正了對 Instance Attributes 的理解：相同類別與相同初始值，不代表兩個物件共用實例屬性。

## ③ Challenge the AI

**One AI-generated question I challenged:**  
第 4 題：`__str__` and Side Effects。

**Why?**

- [ ] Ambiguous
- [x] Oversimplified
- [ ] Technically questionable
- [ ] Too easy
- [ ] Other

### Brief explanation

我認為原題有些過度簡化。它適合檢查學生是否知道 `list.sort()` 會直接修改串列，但只靠 True／False，無法確認學生是否理解「Python 允許這樣做」和「這樣的設計是否合適」之間的差異。

在題目的例子中，`print(s)` 會印出 `[1, 3]`，同時將 `s.vals` 從 `[3, 1]` 改成 `[1, 3]`。即使集合的成員沒有改變，呼叫者若只是想查看內容，仍可能意外改變之後讀到的串列順序。如果排序只是為了顯示，使用下列方法可以保留原本的順序：

```python
def __str__(self):
    return str(sorted(self.vals))
```

我會將原題拆成兩個問題：

1. 執行 `print(s)` 時會印出什麼？執行後 `s.vals` 的內容與順序為何？
2. 如果希望印出排序後的內容，同時保留 `s.vals` 的原始順序，應如何改寫 `__str__()`？為什麼？

第一問測試程式追蹤與 Side Effects，第二問測試能否將顯示需求與物件狀態分開處理。

## ④ One-Minute Reflection

### One thing I am still unsure about

我還不太確定如何設計介面，讓其他人可以讀取物件的資料，卻不會意外修改內部狀態。

以第 5 題的 `intSet` 為例，如果我想提供方法讓呼叫者查看所有元素，應回傳 List 副本，還是不能直接修改的 Tuple？我想理解這兩種做法適合的情況。

在與 AI Tutor 討論後，我理解回傳 List 副本能讓呼叫者自行修改取得的容器，但不會影響內部 List；回傳由不可變整數或字串構成的 Tuple 則更適合提供唯讀的快照。不過，底線命名（如 `_history`）只是一種內部使用慣例，並非強制禁止外部存取的機制。

---

# Part B: LeetCode-style Lecture Code Transfer

## 1. Today’s Challenge

**Core concept from today’s OCW lecture:**  
Object-Oriented Programming（物件導向程式設計）、Classes、Instances、Instance Attributes、Methods、`__init__`、`__str__`、Data Abstraction 與 Encapsulation。

**AI-generated coding challenge title:**  
**Recent Search History（最近搜尋紀錄）**

**Challenge summary:**  
設計 `RecentSearches` 類別，最多儲存 `limit` 筆搜尋紀錄。最新搜尋應排在最前面，相同關鍵字不可重複；再次搜尋時，將該關鍵字移至最前面。超過容量時，移除最舊紀錄。`get_history()` 必須回傳 Tuple 快照，`__str__()` 應用 ` -> ` 連接紀錄；空紀錄顯示 `(empty)`。

## 2. My Initial Approach — Before AI Help

**My approach:**

我會用一個 List 儲存搜尋紀錄，順序固定為「最新在最前面，最舊在最後面」。

每次搜尋時，先檢查關鍵字是否已存在。如果存在，就先移除舊位置，再插入最前面；如果是新關鍵字，則直接插到最前面。插入後若超過 `limit`，就移除最後一筆。這樣重複搜尋不會增加紀錄筆數，也能保留其他關鍵字的相對順序。

**Core Concept Transfer:**

- `__init__` 與 Instance Attributes：透過 `self` 儲存各實例的容量上限及獨立的空 List。
- Methods：`add()` 集中處理去重、順序與容量規則。
- `__str__`：將現有順序組合成字串，不修改物件；空紀錄則回傳 `(empty)`。
- Encapsulation：`get_history()` 將目前的紀錄轉換成 Tuple 回傳。因為關鍵字是不可變字串，所以呼叫者無法透過回傳的 Tuple 修改原本的 List。

## 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

- [x] No — I solved it independently
- [ ] Yes — I received one or more hints

**The most useful hint/question from AI was:**  
我沒有需要修改演算法的提示。AI Tutor 確認了使用 List、先移除再插入、容量超限時 `pop()`，以及回傳 Tuple 快照的設計，並補充 `_history` 的底線只是 Python 內部使用的命名慣例，不能真正禁止外部直接存取。

**It helped me realize that:**  
封裝除了將規則放進方法，也要考慮公開介面會不會讓呼叫者間接修改物件。`__str__()` 也應盡量避免在單純顯示時產生不必要的 Side Effect。

## 4. My Revision

**Did you change your approach or code after interacting with AI?**

- [x] No
- [ ] Yes

**What did you change, and why?**  
我原先的演算法已經符合題目規格，因此不需要改寫主要設計。實作時使用 `_limit`、`_history` 作為實例屬性，`get_history()` 回傳 Tuple，`__str__()` 只讀取搜尋紀錄，讓公開介面不直接暴露可變的內部 List。

## 5. Verification

**My final program:**

```python
class RecentSearches(object):
    def __init__(self, limit):
        self._limit = limit
        self._history = []

    def add(self, term):
        if term in self._history:
            self._history.remove(term)

        self._history.insert(0, term)

        if len(self._history) > self._limit:
            self._history.pop()

    def get_history(self):
        return tuple(self._history)

    def __str__(self):
        if not self._history:
            return "(empty)"
        return " -> ".join(self._history)
```

- [x] Passed the provided examples
- [x] Passed additional edge cases
- [ ] Still has unresolved problems

**Verification summary:**  
八組測試皆通過：一般新增、重複搜尋、容量超限、`limit = 1`、空紀錄、多次重複搜尋、容量超限後再次搜尋、Tuple 快照不受後續更新影響。

**One edge case I tested:**

**Input:**

```python
history = RecentSearches(1)
history.add("A")
history.add("B")
history.add("B")
history.add("C")
print(history.get_history())
```

**Expected output:**  
`('C',)`

**Actual output:**  
`('C',)` — Pass。

## 6. One-Minute Reflection

### Why my solution works

初始化時，紀錄是空的，符合不重複、最新在最前、筆數不超過 `limit` 三個條件。假設呼叫 `add()` 前三項條件都成立：

1. **不重複**：已存在的關鍵字會先被移除，再插入一次；原本不存在的關鍵字則直接插入一次。
2. **最新在最前**：每次都將本次搜尋的關鍵字插入索引 `0`，其餘關鍵字的相對順序不變。
3. **容量限制**：重複搜尋不增加筆數，新搜尋最多增加一筆；若超過 `limit`，使用 `pop()` 移除最舊的一筆。

因此，每次呼叫 `add()` 後，上述三個 Representation Invariants 仍然成立。

### Time and Space Complexity

令 `n` 為目前紀錄筆數，`C` 為所有已儲存關鍵字的總字元數。

| 方法 | 時間複雜度 | 原因 |
| --- | --- | --- |
| `add()` | `O(n)`（假設字串比較為 `O(1)`） | 查找、移除與從開頭插入最多需要處理 `n` 筆；實際成本也受字串長度影響。 |
| `get_history()` | `O(n)` | 建立 Tuple 並逐一複製字串參照。 |
| `__str__()` | 有紀錄時 `O(n + C)`；空紀錄時 `O(1)` | `join()` 需讀取每個關鍵字與產生分隔字串。 |

物件內部的 List 需要 `O(n)` 個參照位置，最多 `O(limit)`。如果連字串內容一起計入，空間為 `O(n + C)`；`limit` 只限制紀錄筆數，不限制字串長度。

### What idea from the OCW lecture did you transfer to this new problem?

`intSet` 與 `RecentSearches` 都在 `__init__` 中為各實例建立自己的 List，並透過 Methods 維持內部資料的不變條件。`intSet.insert()` 維持元素唯一性；`RecentSearches.add()` 除了維持唯一性，還必須管理搜尋新舊順序與容量上限。

課堂版 `intSet` 的 `vals` 可被外部直接取得，使用者若執行 `s.vals.append(2)`，便能繞過 `insert()` 的檢查。相較之下，`RecentSearches.get_history()` 回傳由不可變字串組成的 Tuple 快照，無法透過該回傳值修改內部 List。

另外，`intSet.__str__()` 會對內部 List 原地排序；`RecentSearches.__str__()` 只依已維護好的順序建立字串，因此顯示紀錄時不會改變物件狀態。

### One thing I understand better now

我更能區分使用 Class 儲存資料與設計良好公開介面的差異。OOP 不只是把功能寫成 Methods，也要維護物件的 Representation Invariants，並考慮讀取資料的介面是否會造成不必要的 Mutation 或 Side Effects。

### One thing I am still unsure about

我想進一步比較提供 List 副本與 Tuple 快照的設計取捨，以及在 Python 中除了底線命名慣例之外，還可以如何降低外部程式誤用內部 Instance Attributes 的風險。

---

*依據 MIT 6.0001 Lecture 8 投影片、`lec8_classes.py` 與本次 AI Tutor 實際問答整理。*
