# L6 - Recursion and Dictionaries

> 主題：用遞迴把問題化成更小的同類問題，再用 dictionary 儲存「鍵和值」以及已計算的中間結果。

## 1. 本講重點

這一講把兩個看似不同的工具連起來：

1. **Recursion（遞迴）**：函式呼叫自己，將問題縮小，直到碰到可以直接回答的 base case。
2. **Dictionary（字典）**：用 key 直接找到 value，適合做查表、計數，以及 memoization。
3. **Divide and conquer（分治）**：把一個較難的問題拆成較容易的同類子問題，再組合子問題的答案。
4. **正確性與效率**：遞迴不只要「能停」，還要能說明 base case 正確、每次遞迴都更接近 base case；若重複計算，可以用 dictionary 保存結果。

本筆記的程式碼集中在 [`examples.py`](examples.py)，測試集中在 [`test_examples.py`](test_examples.py)。

## 2. 遞迴的基本結構

遞迴函式通常包含兩部分：

```python
def solve(problem):
    if is_small_enough(problem):       # base case
        return direct_answer(problem)
    smaller = make_smaller(problem)    # recursive case
    return combine(solve(smaller))
```

- **Base case**：最小問題，可以直接回傳答案，而且不再呼叫自己。
- **Recursive case**：把原問題轉成更小的同類問題，再利用該問題的答案。
- **進展保證**：每次呼叫都必須更接近 base case，否則會無限遞迴並最後觸發 `RecursionError`。

### 2.1 乘法：從迭代到遞迴

對非負整數 `b`，乘法可以看成把 `a` 加上 `b` 次：

```text
a * b = a + a * (b - 1)
```

因此可以寫成：

```python
def multiply_recursive(a, b):
    if b == 0:
        return 0
    return a + multiply_recursive(a, b - 1)
```

講義使用 `b == 1` 作為 base case；使用 `b == 0` 只是把定義延伸到 `b = 0`，兩種寫法的核心相同。

- 時間：`O(b)`
- 額外堆疊空間：`O(b)`
- 注意：若要支援負的 `b`，必須另外處理符號；本筆記的範例直接對負數輸入拋出 `ValueError`。

### 2.2 階乘

階乘的遞迴定義是：

```text
0! = 1
n! = n * (n - 1)!，n > 0
```

所以 `factorial(4)` 的展開為：

```text
factorial(4)
= 4 * factorial(3)
= 4 * 3 * factorial(2)
= 4 * 3 * 2 * factorial(1)
= 4 * 3 * 2 * 1 * factorial(0)
= 24
```

每個呼叫都有自己的 local scope。`factorial(4)` 中的 `n` 不會被下一層 `factorial(3)` 改掉；下一層回傳後，上一層才繼續計算。

- 時間：`O(n)`
- 額外堆疊空間：`O(n)`

### 2.3 迭代與遞迴的比較

迭代通常使用迴圈與狀態變數；遞迴則使用函式呼叫的 stack frame 保存狀態。

遞迴的優點：

- 對樹、巢狀結構、分治問題通常更貼近問題本身。
- 有時候程式較短，也較容易直接對應數學定義。

遞迴的代價：

- 需要額外的 call stack。
- 若每層分支很多，可能重複計算大量相同子問題。
- 遞迴深度太大可能超過 Python 的 recursion limit。

## 3. 用歸納法理解遞迴的正確性

### 3.1 程式中的歸納思維

要相信 `multiply_recursive(a, b)` 正確，可以分兩步想：

1. `b = 0` 時直接回傳 `0`，這是正確的 base case。
2. 假設對較小的 `b - 1` 函式已經正確，則
   `a + multiply_recursive(a, b - 1)` 等於 `a + a(b-1) = ab`，因此對 `b` 也正確。

同時，`b` 每次減少 1，且不會低於 0 才進入遞迴，因此一定會抵達 base case。這同時說明了**正確性**與**終止性**。

### 3.2 數學歸納法

對以整數 `n` 為索引的命題，常見證明結構是：

1. 證明最小值（例如 `n = 0`）成立。
2. 假設命題對某個 `k` 成立。
3. 利用這個假設證明命題對 `k + 1` 成立。

例如：

```text
0 + 1 + 2 + ... + n = n(n + 1) / 2
```

程式的 recursive case 可以看成第 3 步：先相信較小輸入的答案，再加上目前這一層新增的部分。

## 4. Divide and conquer：漢諾塔

漢諾塔有三根柱子與大小不同的圓盤，規則是：一次移動一片，且大盤不能放在小盤上。

要把 `n` 片從 `source` 移到 `target`：

1. 把上面的 `n - 1` 片從 `source` 移到 `spare`。
2. 把最大的第 `n` 片從 `source` 移到 `target`。
3. 把 `n - 1` 片從 `spare` 移到 `target`。

```python
def hanoi_moves(n, source, target, spare):
    if n == 1:
        return [(source, target)]
    return (
        hanoi_moves(n - 1, source, spare, target)
        + [(source, target)]
        + hanoi_moves(n - 1, spare, target, source)
    )
```

移動次數滿足：

```text
T(n) = 2T(n - 1) + 1
T(1) = 1
```

因此 `T(n) = 2^n - 1`。如果函式真的回傳完整 move list，輸出本身就需要 `O(2^n)` 空間；呼叫 stack 則是 `O(n)`。

## 5. 多個 base case：Fibonacci

本講的兔子模型使用：

```text
F(0) = 1
F(1) = 1
F(n) = F(n - 1) + F(n - 2)
```

所以：

```text
F(0), F(1), F(2), F(3), F(4), F(5) = 1, 1, 2, 3, 5, 8
```

這裡要留意索引慣例：有些教科書用 `F(1)=1, F(2)=2`，和上面的定義只是整體平移一格，不要把兩種定義混用。

直接遞迴的 Fibonacci 會重算同樣的子問題：

```text
fib(5)
├─ fib(4)
│  ├─ fib(3)
│  └─ fib(2)
└─ fib(3)  ← 和左邊的 fib(3) 重複
```

其時間複雜度是指數級，常以 `O(2^n)` 表示；堆疊空間為 `O(n)`。

### 5.1 Memoization：用字典保存中間結果

```python
def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {0: 1, 1: 1}
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]
```

流程是：

1. 先查 `n` 是否已存在於 dictionary。
2. 若存在，直接使用已知答案。
3. 若不存在，遞迴計算，完成後把答案存入 dictionary。

對 `n >= 0` 的一次完整計算：

- 時間：`O(n)`，每個 `n` 只計算一次。
- memo 與遞迴 stack：合計 `O(n)`。

這個技巧的前提是函式對相同輸入應該得到相同結果，且不依賴呼叫之間的隱藏 side effect。

## 6. 非數值遞迴：回文

回文是正讀與反讀相同的字串。講義先將字串轉成小寫並移除標點與空白，再判斷：

- 長度 0 或 1：一定是回文。
- 第一個字元不等於最後一個：不是回文。
- 第一個與最後一個相等：問題縮小成中間子字串。

例如：

```text
"Able was I, ere I saw Elba"
→ "ablewasiereisawelba"
→ 比較首尾 a/a，再遞迴檢查中間部分
```

若每次建立 `s[1:-1]` 的新字串，單次呼叫會複製目前片段，整體最壞時間可達 `O(n^2)`；遞迴深度為 `O(n)`。若改用左右指標在同一字串上移動，就能把時間降到 `O(n)`、額外空間降到 `O(n)`（若仍使用遞迴）。

## 7. Dictionary 基本觀念

Dictionary 儲存 `key: value` 配對：

```python
grades = {
    "Ana": "B",
    "John": "A+",
    "Denise": "A",
}
```

### 7.1 Lookup 與基本操作

```python
grades["John"]       # 取值，結果為 "A+"
grades["Katy"] = "A" # 新增或更新
"John" in grades     # 測試 key 是否存在
del grades["Ana"]    # 刪除 key
grades.keys()         # keys 的 view
grades.values()       # values 的 view
```

使用不存在的 key 做 `grades["Unknown"]` 會得到 `KeyError`。若「不存在」是正常情況，可以使用：

```python
grades.get("Unknown")          # 預設得到 None
grades.get("Unknown", "N/A")   # 自訂預設值
```

### 7.2 Keys 與 values 的限制

- key 必須唯一；設定同一個 key 會更新舊 value。
- key 必須是 hashable，例如 `int`、`float`、`str`、`tuple`、`bool`。
- `list`、`dict` 這類 mutable object 不能當 key。
- value 可以重複，也可以是 list 或另一個 dictionary。
- 現代 Python 的 dictionary 會保留插入順序；但不能把它當成「依 key 排序」的資料結構。若需要排序，要明確呼叫 `sorted`。

### 7.3 List 與 dictionary 的選擇

| 特性 | list | dictionary |
| --- | --- | --- |
| 主要關係 | index 對 element | key 對 value |
| 查找方式 | 整數索引 | 任意 hashable key |
| 適合情境 | 有順序的序列 | 依名稱／ID 查資料、計數、查表 |
| 常見風險 | index 對錯資料 | key 不存在或 key 不可 hash |

## 8. 歌詞頻率統計

講義用三個函式示範 dictionary：

### 8.1 建立頻率表

```python
def lyrics_to_frequencies(lyrics):
    frequencies = {}
    for word in lyrics:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies
```

如果 `lyrics = ["hello", "world", "hello"]`，結果是：

```python
{"hello": 2, "world": 1}
```

時間是 `O(n)`，其中 `n` 是單字數量；額外空間是 `O(k)`，其中 `k` 是不同單字數量。

### 8.2 找出最高頻率的單字

最高頻率可能有平手，因此結果要回傳「單字 list」與最高次數，而不是只回傳一個單字：

```python
def most_common_words(frequencies):
    best = max(frequencies.values())
    words = [word for word, count in frequencies.items() if count == best]
    return words, best
```

遍歷 dictionary 需要 `O(k)` 時間；空 dictionary 沒有最高值，因此範例會拋出 `ValueError`。

### 8.3 找出至少出現 `min_times` 次的頻率群組

講義的做法是：找目前最高頻率的單字，記錄後從 dictionary 刪掉，再重複。這會依頻率由高到低產生結果；若同一頻率有多個字，會放在同一組。

範例輸入：

```python
{"a": 4, "b": 4, "c": 2, "d": 1}
```

`min_times=2` 的結果可表示為：

```python
[( ["a", "b"], 4), (["c"], 2)]
```

這個演算法最壞可能重複掃描 dictionary，時間為 `O(k^2)`，額外空間為 `O(k)`。若只需要排序後的結果，也可以先做一次 `sorted`，用較直接的方式處理。

## 9. 常見錯誤

1. 忘記 base case，或 base case 永遠到不了。
2. recursive call 沒有讓輸入變小，例如一直呼叫 `f(n)`。
3. 把上一層與下一層 scope 的區域變數當成同一個變數。
4. Fibonacci 直接遞迴，卻沒有注意到相同子問題被重算。
5. 對不存在的 dictionary key 直接使用 `d[key]`，忽略 `KeyError`。
6. 將 mutable `list` 當成 dictionary key。
7. 在 `for key in d:` 迴圈中直接刪除 key，造成執行期錯誤；若要刪除，先複製 keys 或使用講義中受控的刪除流程。
8. 將「插入順序」誤認成「按照 key 排序」。
9. 回文判斷沒有先定義是否忽略大小寫、空白與標點，導致測試期待不一致。

## 10. Closed-AI self-check

先不看程式或 AI，自己回答，再用範例測試驗證：

1. `hanoi_moves(3, "A", "C", "B")` 應該有幾步？為什麼？
2. 為什麼 `fibonacci_memo(34)` 比直接遞迴有效率？dictionary 儲存了什麼？
3. `d[[1, 2]] = "x"` 會發生什麼事？如何修正？
4. 寫出 `factorial(4)` 的 recursive call stack 展開與返回順序。

參考答案：

- 1：`2^3 - 1 = 7` 步。
- 2：相同的子問題只計算一次，後續用 key 查表取回結果。
- 3：`list` 不可 hash，會得到 `TypeError`；可以改用 `(1, 2)`。
- 4：先進入 `4 → 3 → 2 → 1 → 0`，再依 `0 → 1 → 2 → 6 → 24` 的順序返回。
