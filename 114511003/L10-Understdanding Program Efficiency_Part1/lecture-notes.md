# L10 - Understanding program efficiency, part 1

這份筆記整理 MIT 6.0001 Fall 2016 Lecture 10，主題是如何估計程式的效率，以及如何用 Big-O 表示演算法的成長率。

## 1. 為什麼要分析程式效率

同一個問題通常可以有不同的演算法。輸入資料很小時，兩種寫法的差異可能不明顯；輸入規模變大後，效率較差的寫法可能需要非常久才能完成。

Lecture 10 關心的是演算法的成長率，而不是某台電腦上測得的固定秒數。分析成長率可以幫助我們在輸入變大時預測程式的行為，也比較不受硬體與實作環境影響。

分析時要先說明輸入大小。例如：

- 一個 list 的長度是 `n`。
- `L1` 和 `L2` 的長度分別是 `n` 和 `m`。
- 一個整數的數值大小，通常不是演算法分析中的輸入大小；要看儲存或處理它所需的資料量。

## 2. 執行步驟與成長率

我們可以用基本操作的次數，粗略估計程式需要做多少工作。基本操作可以是一次比較、一次指定、一次算術運算，或一次 list 存取。

假設一段程式的操作次數是

```text
3n^2 + 5n + 7
```

當 `n` 很大時，`n^2` 的影響會遠大於 `n` 和常數。因此只保留最高階項，得到 `O(n^2)`。

這不是在說程式一定剛好執行 `n^2` 次，而是用一個簡單的上界描述它隨輸入變大的速度。

常見的成長率如下：

| 成長率 | 名稱 | 直覺 |
|---|---|---|
| `O(1)` | constant | 輸入變大時，工作量大致不變 |
| `O(log n)` | logarithmic | 每一步都大幅縮小剩餘問題 |
| `O(n)` | linear | 大致掃描一次輸入 |
| `O(n log n)` | linearithmic | 常見於較有效率的排序方法 |
| `O(n^2)` | quadratic | 對資料做兩層配對或巢狀掃描 |
| `O(2^n)` | exponential | 輸入每增加一點，可能產生大量新分支 |

本講的重點是常數、線性、對數與二次成長率的比較。

## 3. Big-O 的讀法

Big-O 主要描述輸入規模變大時，執行步驟如何成長。分析時通常遵守以下規則：

1. 忽略常數倍。例如 `5n` 和 `n` 都記為 `O(n)`。
2. 忽略較低階項。例如 `n^2 + n + 1` 記為 `O(n^2)`。
3. 連續執行的兩段程式取較大的成長率。例如 `O(n) + O(n^2)` 是 `O(n^2)`。
4. 巢狀迴圈通常相乘。例如外層做 `n` 次、內層每次做 `m` 次，通常是 `O(nm)`。

Big-O 是近似的複雜度表示法，不是實際秒數，也不代表不同 `O(n)` 程式在真實環境中一定一樣快。

## 4. 最好、最壞與平均情況

同一個演算法在不同輸入上可能執行不同次數，因此要區分：

- **Best case**：最有利的輸入。
- **Worst case**：最不利的輸入。
- **Average case**：依照某個輸入分布計算平均行為。

如果沒有特別說明，課堂上的複雜度討論常以 worst case 為主，因為它提供一個可靠的效能上界。

例如，在已排序的 list 中尋找元素時：

- 目標剛好在第一個位置，可能是 `O(1)`。
- 目標在最後，或目標不存在，可能需要掃描整個 list，為 `O(n)`。

## 5. Lecture 10 的搜尋範例

### 5.1 不提前停止的線性搜尋

```python
def linear_search(values, target):
    found = False
    for value in values:
        if value == target:
            found = True
    return found
```

這個函式即使找到目標，也會繼續掃描剩下的元素。因此：

- 時間複雜度：`O(n)`。
- 最好情況也是 `O(n)`，因為函式不會提前結束。
- 額外空間複雜度：`O(1)`。

### 5.2 利用排序提前停止

若 list 已經按照遞增順序排列，可以在目前元素大於目標時停止：

```python
def search_sorted(values, target):
    for value in values:
        if value == target:
            return True
        if value > target:
            return False
    return False
```

這個版本仍然可能掃描整個 list，所以 worst-case 時間複雜度是 `O(n)`。但在目標很前面，或遇到第一個比目標大的元素時，可以提早結束，因此 best case 是 `O(1)`。

這裡的重點是：排序本身不會自動讓所有搜尋變成 `O(log n)`。這個版本只是利用排序條件提早停止，仍然是逐項掃描。要達到對數複雜度，還需要使用每次把搜尋範圍分半的演算法，例如 binary search。

## 6. 巢狀迴圈與 `isSubset`

Lecture 10 的 `isSubset` 會對 `L1` 的每個元素，掃描一次 `L2`：

```python
def is_subset(left, right):
    for element_left in left:
        matched = False
        for element_right in right:
            if element_left == element_right:
                matched = True
                break
        if not matched:
            return False
    return True
```

若 `len(left) = n`，`len(right) = m`：

- worst-case 時間複雜度：`O(nm)`。
- 若兩個 list 長度都約為 `n`，可寫成 `O(n^2)`。
- 額外空間複雜度：`O(1)`，因為只使用固定數量的變數。

`break` 會改善某些輸入的實際執行時間，但不會改變 worst-case 的 `O(nm)`，因為仍可能每次都掃描到 `right` 的尾端。

## 7. `intersect` 的效率

Lecture 10 的交集範例先比較兩個 list 的所有元素配對：

```python
def intersect(left, right):
    temporary = []
    for element_left in left:
        for element_right in right:
            if element_left == element_right:
                temporary.append(element_left)

    result = []
    for element in temporary:
        if element not in result:
            result.append(element)
    return result
```

第一段巢狀迴圈需要 `O(nm)`。後面的 `element not in result` 若使用 list，最壞也要逐項搜尋 `result`。因此完整程式的 worst-case 可以寫成：

```text
O(nm + k^2)
```

其中 `k` 是 `temporary` 的長度。當兩個輸入長度都約為 `n` 時，整體仍可簡化為 `O(n^2)`。

這個例子也提醒我們，不能只看最外層迴圈。`in` 運算子的成本要依資料結構判斷。對 list 做 membership test 通常需要線性搜尋。

## 8. 時間複雜度與空間複雜度

- **Time complexity**：輸入變大時，演算法需要的基本操作數量如何成長。
- **Space complexity**：輸入本身以外，演算法需要的額外記憶體如何成長。

例如：

```python
def count_positive(values):
    count = 0
    for value in values:
        if value > 0:
            count += 1
    return count
```

這個函式：

- 時間複雜度是 `O(n)`，因為每個元素都檢查一次。
- 額外空間複雜度是 `O(1)`，因為只使用 `count` 和 `value` 等固定數量的變數。

如果改成建立一個與輸入同樣大小的新 list，額外空間就可能是 `O(n)`。

## 9. 常見誤解

### 誤解一：找到元素後，線性搜尋一定是 `O(1)`

只有在函式找到元素後立刻 `return`，而且目標剛好在前面時，才可能出現 `O(1)` 的 best case。若找到後仍繼續掃描，best case 也可能是 `O(n)`。

### 誤解二：兩層迴圈一定是 `O(n^2)`

要看每層迴圈的範圍。如果外層跑 `n` 次、內層跑固定 10 次，複雜度是 `O(n)`。若外層跑 `n` 次、內層跑 `m` 次，則是 `O(nm)`，只有在 `m` 和 `n` 同階時才簡化成 `O(n^2)`。

### 誤解三：Big-O 可以直接比較所有程式的實際速度

Big-O 描述成長率，沒有包含所有常數與實作細節。對小輸入來說，`O(n^2)` 的程式可能比常數很大的 `O(n)` 程式快。當輸入規模變大時，成長率通常才是主要差異。

### 誤解四：已排序就一定是 `O(log n)`

排序只提供額外條件。若演算法仍然逐項檢查，複雜度仍可能是 `O(n)`。必須每次把搜尋範圍縮小，例如 binary search，才會得到 `O(log n)`。

## 10. 複習題

1. `linear_search` 找到目標後仍繼續執行。它的 best case 和 worst case 各是多少？
2. `search_sorted` 為什麼可以提早回傳 `False`？這個條件需要什麼前提？
3. 若 `len(L1) = n`、`len(L2) = m`，`isSubset(L1, L2)` 的 worst-case 時間複雜度是多少？
4. `for` 迴圈執行 `n` 次，每次都呼叫一個 `O(n)` 的函式，整體複雜度是多少？
5. 為什麼 `element in result` 會影響 `intersect` 的複雜度？

### 參考答案

1. Best case 和 worst case 都是 `O(n)`，因為函式不會在找到後停止。
2. 因為 list 已排序；一旦目前元素大於目標，後面的元素也都不可能等於目標。
3. `O(nm)`；若 `n` 和 `m` 同階，則為 `O(n^2)`。
4. `O(n^2)`。
5. `result` 是 list，`in` 需要逐項比較，成本會隨目前結果的長度增加。

## 11. 重點整理

- 先定義輸入大小，再數基本操作的成長率。
- Big-O 通常忽略常數與低階項，保留主導成長率的項目。
- 連續程式區段取較大的複雜度，巢狀迴圈通常相乘。
- `break` 和 `return` 可能改善 best case，但不一定改變 worst case。
- 已排序的資料可以提供提前停止的條件，但不會自動產生 `O(log n)`。
- 分析複雜度時要同時看迴圈、函式呼叫，以及 list 的 `in` 等資料結構操作。

## Sources

- MIT OpenCourseWare: [Lecture 10: Understanding Program Efficiency, Part 1](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/lecture-10-understanding-program-efficiency-part-1/)
- MIT OpenCourseWare: [Lecture 10 slides and code](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/pages/lecture-slides-code/)
- Local handout: `C:\Users\YiYu8\Desktop\L10.pdf`
