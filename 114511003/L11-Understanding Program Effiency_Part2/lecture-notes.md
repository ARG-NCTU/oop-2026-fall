# L11 - Understanding program efficiency, part 2

這份筆記整理 MIT 6.0001 Fall 2016 Lecture 11，主題是不同複雜度類別的特徵，以及如何從程式的迴圈、遞迴呼叫和資料結構操作判斷 Big-O。

## 課程資料

- 影片：[MIT OpenCourseWare - Lecture 11: Understanding Program Efficiency, Part 2](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/lecture-11-understanding-program-efficiency-part-2/)
- 投影片：`C:\Users\YiYu8\Downloads\L11-Understanding Program Effiency-part2.pdf`

## 1. 為什麼要分析效率

複雜度分析要回答三個問題：

1. 當輸入規模變大時，演算法需要多少工作？
2. 不同的演算法設計會如何影響執行時間？
3. 某些問題是否有無法避免的時間成本？

Lecture 11 延續 Lecture 10 的 orders of growth。重點不是預測某台電腦上的精確秒數，而是描述輸入大小增加時，執行步驟如何成長。通常以 worst case 作為分析對象，並保留最主要的成長項。

## 2. 常見複雜度類別

令 `n` 表示輸入大小。下表由成長較慢排到成長較快：

| 複雜度 | 名稱 | 常見特徵 |
|---|---|---|
| `O(1)` | constant | 工作量與 `n` 無關 |
| `O(log n)` | logarithmic | 每一步把問題規模縮小，例如減半 |
| `O(n)` | linear | 掃描一次輸入，或做 `n` 次固定成本的工作 |
| `O(n log n)` | log-linear | 常見於有效率的排序法，例如 merge sort |
| `O(n^c)` | polynomial | `c` 是常數，常見於巢狀迴圈 |
| `O(c^n)` | exponential | 每一層產生多個遞迴分支 |

Big-O 會忽略常數與較低階項。例如：

```text
3n^2 + 5n + 7 = O(n^2)
```

這表示 `n` 很大時，`n^2` 主導成長率，不表示程式永遠剛好執行 `n^2` 個步驟。

## 3. `O(1)`：constant complexity

若程式的工作量不隨輸入大小改變，就是 `O(1)`。程式中可以出現迴圈或遞迴，但前提是迭代次數或遞迴呼叫次數固定，不依賴輸入大小。

例如，對 list 做一次索引存取通常是 `O(1)`：

```python
value = values[index]
```

這裡的 `index` 存取不需要從第一個元素開始逐一尋找。

## 4. `O(log n)`：logarithmic complexity

### 4.1 二分搜尋的想法

對已排序的 list `L` 搜尋元素 `e` 時，可以採用以下步驟：

1. 取目前搜尋範圍的中間位置 `mid`。
2. 若 `L[mid] == e`，搜尋成功。
3. 若 `L[mid] > e`，只搜尋左半部。
4. 若 `L[mid] < e`，只搜尋右半部。

每次呼叫都把搜尋範圍縮小約一半。若原本有 `n` 個元素，經過 `k` 次後剩下：

```text
n / 2^k
```

當剩下一個元素時：

```text
n / 2^k = 1
k = log n
```

因此二分搜尋的遞迴呼叫次數是 `O(log n)`。

### 4.2 會複製 list 的版本

投影片中的第一個版本用 slicing 建立新的 list：

```python
def bisect_search1(values, target):
    if values == []:
        return False
    if len(values) == 1:
        return values[0] == target

    half = len(values) // 2
    if values[half] > target:
        return bisect_search1(values[:half], target)
    return bisect_search1(values[half:], target)
```

表面上看，遞迴深度是 `O(log n)`。但每次 `values[:half]` 或 `values[half:]` 都會建立 list 副本，這項成本不能忽略。

- 若只看遞迴呼叫次數，是 `O(log n)`。
- 若把每次 slicing 的複製成本直接估成 `O(n)`，會得到較鬆的 `O(n log n)` 上界。
- 由於每一層複製的 list 也會縮小一半，總複製成本是幾何級數：`n + n/2 + n/4 + ... = O(n)`。
- 因此這個實作的總時間複雜度可寫成 `O(n)`，複製成本主導了 `O(log n)` 的遞迴控制成本。

這個例子提醒我們：分析遞迴時，除了數遞迴深度，也要分析每次呼叫前後做了哪些工作。

### 4.3 只傳遞索引的版本

第二個版本保留原本的 list，只傳入 `low` 和 `high` 表示搜尋範圍：

```python
def bisect_search2(values, target):
    def helper(values, target, low, high):
        if high == low:
            return values[low] == target

        mid = (low + high) // 2
        if values[mid] == target:
            return True
        if values[mid] > target:
            if low == mid:
                return False
            return helper(values, target, low, mid - 1)
        return helper(values, target, mid + 1, high)

    if len(values) == 0:
        return False
    return helper(values, target, 0, len(values) - 1)
```

每次呼叫只做固定數量的索引、比較和算術運算，沒有複製 list。因此：

- 遞迴深度：`O(log n)`。
- 每次呼叫的額外工作：`O(1)`。
- 時間複雜度：`O(log n)`。
- 遞迴堆疊的額外空間：`O(log n)`。

二分搜尋必須使用已排序的資料。若 list 沒有排序，不能根據中間元素的大小決定要捨棄哪一半。

### 4.4 整數轉字串

```python
def int_to_str(number):
    digits = "0123456789"
    if number == 0:
        return "0"

    result = ""
    while number > 0:
        result = digits[number % 10] + result
        number = number // 10
    return result
```

每次迴圈都把 `number` 除以 10，因此迴圈次數等於數字的位數，也就是 `O(log number)`。這裡的對數來自數值每次縮小十倍，而不是 list 長度。

## 5. `O(n)`：linear complexity

### 5.1 迭代版 factorial

```python
def factorial_iter(number):
    product = 1
    for value in range(1, number + 1):
        product *= value
    return product
```

迴圈執行約 `n` 次，每次做固定成本的乘法與指定，因此時間複雜度是 `O(n)`，額外空間複雜度是 `O(1)`。

### 5.2 遞迴版 factorial

```python
def factorial_recur(number):
    """Assume number >= 0."""
    if number <= 1:
        return 1
    return number * factorial_recur(number - 1)
```

這個版本每次把問題減少 1，因此會建立約 `n` 層函式呼叫：

- 時間複雜度：`O(n)`。
- 遞迴堆疊空間：`O(n)`。

遞迴版通常比迭代版多了函式呼叫的固定成本，但兩者的成長率相同，都是 `O(n)`。

## 6. `O(n log n)`：log-linear complexity

許多實用演算法的複雜度是 `O(n log n)`。Merge sort 是常見例子，下一堂課會再詳細分析。

遇到這種複雜度時，可以把它理解成兩個因素的組合：

- `log n` 層的問題分割或合併流程。
- 每一層總共處理 `O(n)` 個元素。

## 7. `O(n^c)`：polynomial complexity

多數課堂例子中的 polynomial complexity 是 quadratic，也就是 `O(n^2)`。它常出現在：

- 兩層都依輸入大小成長的巢狀迴圈。
- 兩個輸入元素互相比較。
- 每一層遞迴都做另一個與輸入大小相關的工作。

例如：

```python
def print_pairs(values):
    for left in values:
        for right in values:
            print(left, right)
```

外層執行 `n` 次，內層每次也執行 `n` 次，因此總工作量是 `n * n = O(n^2)`。

但「有兩層迴圈」本身不是充分條件。若外層執行 `n` 次、內層只固定執行 10 次，整體仍是 `O(n)`。

## 8. `O(c^n)`：exponential complexity

若每一層遞迴對同一個問題大小產生多個遞迴呼叫，常會得到 exponential complexity。這類演算法在輸入稍微增加時，工作量就可能大幅增加。

### 8.1 Hanoi towers

令 `t_n` 表示移動 `n` 個盤子的時間。Hanoi towers 的遞迴關係是：

```text
t_n = 2t_(n-1) + 1
```

展開後：

```text
t_n = 2^n - 1
```

所以時間複雜度是：

```text
O(2^n)
```

這個結果也代表 Hanoi towers 至少需要移動 `2^n - 1` 次盤子。

### 8.2 Power set

給定一組沒有重複元素的整數，要產生所有子集合，結果稱為 power set。

對大小為 `n` 的集合，每個元素都有兩種選擇：放入子集合，或不放入子集合。因此總共有：

```text
2^n
```

種子集合。例如 `{1, 2, 3}` 的 power set 有 8 個元素，其中包括空集合和完整集合。

可以用遞迴建立 power set：先取得前 `n - 1` 個元素的所有子集合，再對每個子集合建立一個「加入第 `n` 個元素」的版本。

```python
def generate_subsets(values):
    if len(values) == 0:
        return [[]]  # 外層的 list 表示「所有子集合」，內層的空 list 表示「空集合」。
                     # 不能回傳 []，因為那會表示「沒有任何子集合」。 
    
    smaller = generate_subsets(values[:-1]) # 取出最後一個元素以前的部分，遞迴取得所有子集合。
    last = values[-1:] # 取得最後一個元素，但保留成 list。這裡使用 [-1:] 而不是 [-1]，因為後面要把它和其他 list 連接
    with_last = []

    for subset in smaller:
        with_last.append(subset + last)

    return smaller + with_last
```

若輸入大小為 `n`，前一層已有 `2^(n-1)` 個子集合。這一層必須複製並擴充這些結果，因此可用下列遞迴關係表示：

```text
t_n = t_(n-1) + 2^(n-1) + c
```

其中 `c` 是固定成本。展開後，計算 power set 的時間複雜度是 `O(2^n)`。這也符合輸出本身就有 `2^n` 個子集合的事實。

## 9. Fibonacci 的比較

### 9.1 迭代版

```python
def fib_iter(number):
    if number == 0:
        return 0
    if number == 1:
        return 1

    previous = 0
    current = 1
    for _ in range(number - 1):
        previous, current = current, previous + current
    return current
```

在 worst case，迴圈執行 `O(n)` 次，每次只做固定成本的運算：

- 時間複雜度：`O(n)`。
- 額外空間複雜度：`O(1)`。

### 9.2 遞迴版

```python
def fib_recur(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    return fib_recur(number - 1) + fib_recur(number - 2)
```

每個非 base case 都產生兩個遞迴呼叫，呼叫樹會快速增長。投影片以 `O(2^n)` 表示 worst-case 時間複雜度。實際呼叫樹會因右側分支較快抵達 base case 而比完整的二元樹稀疏，但仍屬於 exponential complexity。

這個比較說明，寫成遞迴不一定會改變複雜度。Factorial 的迭代版和遞迴版都是 `O(n)`，但 Fibonacci 的兩個版本分別是 `O(n)` 和 `O(2^n)`，原因在於遞迴分支數量不同。

## 10. 常見 Python 操作的複雜度

以下表格整理投影片中的常見估計。`n` 分別代表 list `L` 或 dictionary `d` 的大小。

### List

| 操作 | 複雜度 |
|---|---:|
| index | `O(1)` |
| store | `O(1)` |
| `len(L)` | `O(1)` |
| `append` | `O(1)` |
| `==` | `O(n)` |
| `remove` | `O(n)` |
| `copy` | `O(n)` |
| `reverse` | `O(n)` |
| iteration | `O(n)` |
| `x in L` | `O(n)` |

### Dictionary

投影片區分 worst case 與 average case：

| 操作 | worst case | average case |
|---|---:|---:|
| index | `O(n)` | `O(1)` |
| store | `O(n)` | `O(1)` |
| length | `O(n)` | 未列出 |
| delete | `O(n)` | `O(1)` |
| iteration | `O(n)` | `O(n)` |

Dictionary 的 average case 為 `O(1)`，建立在 hash function 分布良好、碰撞不嚴重的假設上。若許多 key 發生 hash collision，worst case 可能退化成 `O(n)`。

分析一段程式時，不能只看表面上的迴圈，也要查清楚迴圈內使用的操作。例如：

```python
for value in values:
    if value in result:
        continue
```

如果 `result` 是 list，`in` 可能需要 `O(n)`；如果 `result` 是 dictionary，average case 通常是 `O(1)`。資料結構的選擇會改變整段程式的複雜度。

## 11. 複雜度分析流程

看到一段程式時，可以依照以下順序分析：

1. 定義輸入大小，例如 `n = len(values)`。
2. 找出會隨 `n` 增加而重複執行的迴圈或遞迴呼叫。
3. 分析每次迭代或每次函式呼叫內的成本。
4. 連續執行的區段取成長較快的一項。
5. 巢狀工作通常相乘，遞迴分支則要計算總呼叫數。
6. 移除常數與較低階項，留下 Big-O。
7. 另外檢查是否建立 slicing、複製 list、產生輸出，因為這些工作可能主導成本。

例如，若外層迴圈執行 `n` 次，每次呼叫一個 `O(log n)` 的函式，整體通常是：

```text
O(n) * O(log n) = O(n log n)
```

## 12. 常見誤解

### 誤解一：看到二分搜尋就直接寫 `O(log n)`

要檢查每次是否真的把範圍減半，也要檢查是否複製了資料。第一個二分搜尋版本雖然只有 `O(log n)` 次呼叫，但 slicing 的總成本是 `O(n)`。

### 誤解二：遞迴一定比迭代慢很多，或一定有不同 Big-O

遞迴可能有較高的函式呼叫常數成本，但複雜度要看呼叫數。兩個 factorial 版本都是 `O(n)`；兩個 Fibonacci 版本則因為分支數量不同而有不同成長率。

### 誤解三：兩層迴圈一定是 `O(n^2)`

要先確認兩層迴圈各自執行多少次。內層若只執行固定次數，整體可能仍然是 `O(n)`。若兩個輸入大小不同，也應寫成 `O(nm)`，不要直接寫成 `O(n^2)`。

### 誤解四：輸出有 `2^n` 個結果，複雜度仍可能是線性

若演算法必須產生所有 power set，光是輸出結果就有 `2^n` 個子集合，因此至少需要指數級的工作量。這種成本不只是遞迴寫法造成的。

### 誤解五：average case 和 worst case 可以互換

Dictionary 的平均查找成本可能是 `O(1)`，但 worst case 會因 hash collision 變成 `O(n)`。寫出複雜度時要說明分析的是哪種情況。

## 13. 重點整理

- `O(1)` 不依賴輸入大小。
- `O(log n)` 通常來自每一步把問題規模縮小，例如二分搜尋。
- `O(n)` 常見於單次掃描、迭代 factorial 和迭代 Fibonacci。
- `O(n log n)` 是許多實用排序演算法的複雜度。
- `O(n^c)` 常出現在巢狀迴圈或多層遞迴工作。
- `O(c^n)` 常出現在每層產生多個遞迴呼叫的程式，例如 Hanoi towers 和遞迴 Fibonacci。
- 分析遞迴時要同時看遞迴深度、每次呼叫的成本和分支數量。
- list slicing、複製、membership test 等資料結構操作可能改變整體複雜度。
- Big-O 描述成長率，不是特定機器上的精確執行時間。

## 14. Closed-AI check

請先在沒有筆記、自動補全或 AI 的情況下回答，再自行檢查：

1. `bisect_search2` 為什麼是 `O(log n)`，而 `bisect_search1` 不能只寫成 `O(log n)`？
2. `genSubsets` 為什麼至少需要 `O(2^n)` 的工作量？
3. 迭代版與遞迴版 Fibonacci 的複雜度各是多少？差異來自哪裡？
4. 如果外層迴圈執行 `n` 次，內層每次執行固定 10 次，複雜度是多少？

## Sources

- MIT OpenCourseWare: [Lecture 11: Understanding Program Efficiency, Part 2](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/lecture-11-understanding-program-efficiency-part-2/)
- Local handout: `C:\Users\YiYu8\Downloads\L11-Understanding Program Effiency-part2.pdf`
