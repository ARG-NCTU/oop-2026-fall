# L12 - Searching and sorting

本筆記整理 MIT 6.0001 Fall 2016 Lecture 12，說明搜尋與排序的做法、正確性及效率。中文說明、追蹤例子與自我練習為重新整理，並非影片逐字稿。

## 課程資料與閱讀方式

- 課程頁面：[Lecture 12: Searching and Sorting](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/lecture-12-searching-and-sorting/)，講者為 Prof. Eric Grimson。
- 主要內容來源：MIT 6.0001 Lecture 12 投影片 *Searching and Sorting Algorithms*，共 38 頁。
- 下文頁碼使用 PDF 的實際頁次。合併排序圖的部分頁尾編號與 PDF 頁次不一致。
- 程式範例是供閱讀與執行的整理版，修改處會說明；不是作業要求，也沒有更動任何 starter code。

複雜度分析假設元素比較、索引存取及交換各需 `O(1)`，`append` 採攤提 `O(1)`。令 `n = len(L)`；空間指輸入之外的額外空間。若比較的是很長的字串或複雜物件，還需計入比較本身的成本。

## 1. 搜尋在解決什麼問題？

來源：PDF 第 2–3 頁。

搜尋是在候選集合中，找出滿足條件的項目。集合可以是明確儲存的資料，例如學生名單；也可以是隱含的候選解，例如求平方根時搜尋可能的數值。

這堂課主要處理 list 中是否存在元素 `e`，回傳 `True` 或 `False`。這與回傳索引或找出所有相同元素，是不同的介面。

| 方法 | 前提 | 核心做法 | 最壞時間 |
|---|---|---|---|
| 線性搜尋 | 不要求排序 | 逐一檢查 | `O(n)` |
| 已排序資料的線性搜尋 | 由小到大排序 | 遇到大於目標的值即可停止 | `O(n)` |
| 二分搜尋 | 由小到大排序，且可有效索引 | 每次排除約一半候選 | `O(log n)` |

## 2. 線性搜尋

來源：PDF 第 4–5 頁。

### 2.1 未排序的 list

以下保留投影片「即使找到，也繼續掃描」的行為，僅整理縮排。

```python
def linear_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found
```

對 `[7, 2, 9, 4]` 搜尋 `2` 時，第二次比較就找到，但迴圈仍會檢查 `9` 和 `4`。因此這個版本的最好與最壞時間都是 `Θ(n)`，額外空間為 `O(1)`。

補充：若找到就立即 `return True`，最好時間可變成 `O(1)`，但最壞仍為 `Θ(n)`。目標不存在時，必須檢查所有元素。

### 2.2 已排序的 list

```python
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
```

例如在 `[1, 3, 5, 8]` 搜尋 `4`，遇到 `5` 就能確定後面不會出現 `4`。這個推論依賴排序前提。

最好時間為 `O(1)`，最壞時間為 `Θ(n)`，額外空間為 `O(1)`。提前停止能省下部分比較，但不會把最壞複雜度降成對數。

## 3. 二分搜尋，也稱 bisection 或 binary search

來源：PDF 第 6–8 頁。

### 3.1 每次只保留一半

維護尚未排除的範圍 `low` 到 `high`，兩端都包含。比較中間元素後：

1. 若中間元素等於目標，回傳 `True`。
2. 若中間元素太大，改搜尋左半邊。
3. 若中間元素太小，改搜尋右半邊。
4. 範圍變空時，回傳 `False`。

以下是投影片索引遞迴版的整理。保留外層函式名稱 `bisect_search2(L, e)`，用 `low > high` 統一處理空範圍。

```python
def bisect_search2(L, e):
    def bisect_search_helper(L, e, low, high):
        if low > high:
            return False
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        if L[mid] > e:
            return bisect_search_helper(L, e, low, mid - 1)
        return bisect_search_helper(L, e, mid + 1, high)

    return bisect_search_helper(L, e, 0, len(L) - 1)
    # 如果刪掉最後那行，外層函式就直接結束，回傳預設的 None。
    # 前面那些遞迴呼叫只負責「搜尋開始後，繼續搜尋較小範圍」；最後這行負責「第一次啟動搜尋」。
```

以 `[1, 3, 5, 7, 9, 11, 13]` 搜尋 `11`：

| 步驟 | low | high | mid | L[mid] | 決定 |
|---|---|---|---|---|---|
| 1 | 0 | 6 | 3 | 7 | 搜尋索引 4 到 6 |
| 2 | 4 | 6 | 5 | 11 | 找到 |

正確性的關鍵是：如果目標存在，尚未排除的範圍內一定仍有目標。排序讓我們能安全排除另一半。

### 3.2 時間與空間

經過 `k` 次縮減，候選數量約為 `n / 2^k`。當它降到 1，`k` 約為 `log₂ n`。

- 最好時間 `O(1)`，最壞時間 `Θ(log n)`。
- 此遞迴版最壞額外空間 `O(log n)`，來自呼叫堆疊。
- 補充：改用迴圈更新 `low`、`high`，可把額外空間降為 `O(1)`。

索引只是告訴函式「看哪一段」；切片則真的建立一份新的 list。
傳入同一個 list 與索引，不會複製整份 list。補充：若每次改傳 `L[:mid]` 等切片，Python 會建立新 list，複製元素參照。沿單一路徑的切片成本為 `n/2 + n/4 + ... = O(n)`，最壞時間就不再是 `O(log n)`，峰值額外空間也會達到 `O(n)`。

二分搜尋不會自動檢查輸入是否排序。對未排序輸入，結果不受保證；未拋出例外不代表答案正確。每次搜尋前先檢查排序也需 `O(n)`，會抵銷單次搜尋的對數優勢。

## 4. 要不要先排序再搜尋？

來源：PDF 第 9–10 頁。

### 4.1 只有一次搜尋

若資料原本未排序，只做一次查詢，直接線性搜尋的最壞成本是 `O(n)`。先用 merge sort 排序再二分搜尋，成本則為：

```text
O(n log n) + O(log n) = O(n log n)
```

只為一次查詢而排序，通常不划算。投影片用 Big-O 相減來表達直覺，但 Big-O 是成長率的集合記號，不能當作精確秒數相減求門檻。

### 4.2 多次搜尋與攤提成本

若同一份資料要做 `K` 次查詢，而且期間排序結果可重用：

| 策略 | 總時間 |
|---|---|
| 每次線性搜尋 | `O(Kn)` |
| 排序一次，再做 K 次二分搜尋 | `O(n log n + K log n)` |

排序成本分攤到每次查詢後，平均成本為 `O(n log n / K + log n)`。當查詢次數增加，前處理成本占比會下降。

補充：若忽略常數，以 `n log₂ n + K log₂ n < Kn` 粗估，可得到 `K > n log₂ n / (n - log₂ n)`，對大 `n` 約為 `log₂ n` 的量級。這只是成本模型的估算；實際門檻受常數、資料分布與更新頻率影響。

## 5. Bogo sort，也稱 monkey sort

來源：PDF 第 12–13 頁。

做法是檢查是否排序；若沒有，就隨機打亂後重試。以下補上投影片省略的 `is_sorted`，只用來說明概念。

```python
import random

# 負責檢查順序
def is_sorted(L):
    return all(L[i - 1] <= L[i] for i in range(1, len(L))) 
    # 只要有一對不符合，`all(...)` 就回傳 False
    

def bogo_sort(L):
    while not is_sorted(L):
        random.shuffle(L)
        # `random.shuffle(L)` 會直接改變原本的 list
```
複雜度那段可以這樣理解：
- **最好情況：**一開始就排好了，只需檢查一次。檢查 n 個元素要 Θ(n) 時間。
- **最壞情況：**運氣可能一直很差，不斷洗出錯誤順序，所以沒有固定的次數上限。
- **平均要多久：**若 n 個元素都不同，共有 n! 種排列，只有一種是由小到大。例如 3 個不同元素有 3! = 6 種排列，一次洗對的機率是 1/6。在均勻、獨立洗牌的假設下，平均約需 n! 次嘗試；每次檢查或洗牌約花 n 的工作量，因此是 Θ(n · n!)。
「平均約需 n! 次」不是保證。3 個元素平均約 6 次嘗試，某一次執行仍可能洗 20 次才成功。

這個演算法主要用來展示「隨機嘗試直到成功」可能有多慢；實際排序通常不會選它。

若一開始就排序，對 `n >= 2` 的資料，檢查需要 `Θ(n)`。最壞情況沒有有限的執行次數上限，不能保證在固定步數內完成。

補充：若 `n` 個元素互異，且每次均勻、獨立地產生排列，成功機率為 `1/n!`，期望時間為 `Θ(n · n!)`。這不代表每次都會在期望時間內結束。此實作額外空間為 `O(1)`，測試時不應對任意未排序輸入直接等待它完成。

## 6. Bubble sort，氣泡排序

來源：PDF 第 14–15 頁。

由左到右比較相鄰元素，若順序顛倒就交換。完整掃描一輪稱為一個 pass。第一輪結束，最大值會位於最右端；持續掃描，直到整輪都沒有交換。

以下將投影片中意義較容易混淆的 `swap` 旗標改成 `swapped`。`True` 表示這一輪確實有交換。

```python
def bubble_sort(L):
    swapped = True  # 記錄「這一輪至少交換過一次」，讓外面的 while 知道還要再檢查一輪。
    while swapped:
        swapped = False # 每輪開始，先記錄「目前沒有交換」
        for j in range(1, len(L)):
            if L[j - 1] > L[j]:
                L[j - 1], L[j] = L[j], L[j - 1]
                swapped = True
```

追蹤 `[5, 1, 4, 2]`：

```text
第一輪： [1, 5, 4, 2]  ->  [1, 4, 5, 2]  ->  [1, 4, 2, 5]
第二輪： [1, 2, 4, 5]
第三輪： 沒有交換，結束
```

- 最好時間 `Θ(n)`，已排序時只需一輪確認。
- 平均與最壞時間 `Θ(n²)`，最壞需要線性數量的輪次，每輪做線性數量的比較。
- 額外空間 `O(1)`，直接修改原 list，函式回傳 `None`。

補充：這個版本只在嚴格大於時交換相鄰元素，因此穩定。穩定是指相同排序鍵的項目，排序後仍保留原本的相對順序。也可以每輪縮短右邊界，省去已確定位置的比較，但最壞仍是 `Θ(n²)`。

## 7. Selection sort，選擇排序

來源：PDF 第 16–18 頁。

將 list 分成已完成的前綴與未完成的後綴。每輪找出後綴的最小值，放到後綴的第一個位置。

以下保留第 18 頁的程式行為：每次發現更小的值就立刻交換。它與「整輪找完最小值後，只交換一次」的常見版本，交換次數不同。

```python
def selection_sort(L):
    suffixSt = 0 # 索引
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            # 發現更小的值就立刻交換
            if L[i] < L[suffixSt]: #`L[suffixSt]` 都是那段尚未排序資料中的最小值
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
```

追蹤 `[5, 3, 4, 1]`，每輪完成後為：

```text
第一輪： [1, 5, 4, 3]
第二輪： [1, 3, 5, 4]
第三輪： [1, 3, 4, 5]
第四輪： [1, 3, 4, 5]
```

### 7.1 用 loop invariant 解釋正確性

在每輪開始時，令 `k = suffixSt`：

- `L[:k]` 已排序，且包含目前已放妥的最小 `k` 個元素。
- 前綴的任何元素都不大於後綴 `L[k:]` 的任何元素。

初始時前綴為空，條件成立。內層迴圈結束後，`L[k]` 是後綴最小值，將它納入前綴後仍維持條件。當 `k == n`，前綴就是整份 list，因此排序完成。這裡的切片只是描述範圍，程式沒有建立切片。

### 7.2 複雜度

投影片版本的比較次數為 `n + (n - 1) + ... + 1 = n(n + 1)/2`。即使輸入已排序，仍會做完這些比較，所以最好、平均與最壞時間都是 `Θ(n²)`，額外空間為 `O(1)`。

補充：這種遠距離交換不保證穩定。例如以數字作為排序鍵，`[2a, 2b, 1]` 第一輪交換後成為 `[1, 2b, 2a]`，兩個鍵為 2 的項目順序反轉。

## 8. Merge sort，合併排序

來源：PDF 第 19–30 頁。

### 8.1 分割、遞迴、合併

長度為 0 或 1 的 list 已排序。更長的 list 先分成兩半，各自遞迴排序，再把兩份已排序結果合併。

PDF 第 29 頁的例子可依資料大小整理如下；實際程式先深入完成左分支，再處理右分支。

```text
輸入       [8, 4, 1, 6, 5, 9, 2, 0]
分兩半     [8, 4, 1, 6]       [5, 9, 2, 0]
繼續分割   [8, 4] [1, 6]      [5, 9] [2, 0]
基本情況   [8] [4] [1] [6]    [5] [9] [2] [0]
合併       [4, 8] [1, 6]      [5, 9] [0, 2]
再合併     [1, 4, 6, 8]       [0, 2, 5, 9]
最後       [0, 1, 2, 4, 5, 6, 8, 9]
```

### 8.2 合併兩份已排序資料

`i` 與 `j` 分別指向左右兩邊尚未處理的第一個元素。因為兩邊各自已排序，下一個輸出一定來自這兩個元素中較小者。

以下沿用投影片介面，但把第 26 頁的 `<` 改成 `<=`，讓相等時先取左邊元素，使此版本保持穩定。

```python
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
```

若一邊已用完，另一邊剩餘元素可以直接接上。例如合併 `[1, 5, 12, 18, 19, 20]` 與 `[2, 3, 4, 17]`，選出 `17` 後，直接接上 `[18, 19, 20]`。

令左右長度為 `a`、`b`，每個元素恰好加入結果一次，因此時間為 `Θ(a + b)`，結果空間為 `Θ(a + b)`。兩邊皆非空時，元素間比較最多 `a + b - 1` 次。不要改成反覆 `pop(0)`，Python list 每次刪除首項都需搬移後續元素。

### 8.3 遞迴主程式

```python
def merge_sort(L):
    if len(L) < 2:
        return L[:] # 整個List
    middle = len(L) // 2
    left = merge_sort(L[:middle])
    right = merge_sort(L[middle:])
    return merge(left, right)
```
ps. L = [8, 4, 1, 6]
    L[:2]  # [8, 4]，取索引 0、1

這個版本回傳新的已排序 list，原本的 `L` 不變。基本情況也回傳 `L[:]`，讓空 list 與單元素 list 都遵守回傳新 list 的行為。

實際執行順序是先把左半邊排完，再排右半邊，最後合併兩邊

### 8.4 為什麼是 O(n log n)？

每層所有子問題的元素總數為 `n`，該層切片與合併的總工作量是 `Θ(n)`。每次減半，深度約為 `log₂ n`，所以：

```text
T(n) = 2T(n/2) + Θ(n)
     = Θ(n log n)
```

二分搜尋每次只繼續一半，merge sort 則必須處理兩半；兩者雖然都減半，總工作量不同。

補充：此實作最好、平均與最壞時間皆為 `Θ(n log n)`。峰值額外空間為 `O(n)`，包含切片、合併結果及 `O(log n)` 深度的堆疊。整次執行累計建立的 list 元素槽位可達 `O(n log n)`，但它們不會全部同時存活，不能將累計配置量當成峰值空間。

## 9. 複雜度比較與排序下界

來源：PDF 第 31 頁；最好情況、空間、穩定性及下界條件為補充。

| 排序法 | 最好時間 | 平均時間 | 最壞時間 | 額外空間 | 穩定性 |
|---|---|---|---|---|---|
| Bogo sort | `Θ(n)` | 互異元素下 `Θ(n · n!)` | 無有限上限 | `O(1)` | 不保證 |
| Bubble sort，含提前停止 | `Θ(n)` | `Θ(n²)` | `Θ(n²)` | `O(1)` | 本文版本穩定 |
| Selection sort | `Θ(n²)` | `Θ(n²)` | `Θ(n²)` | `O(1)` | 不保證 |
| Merge sort | `Θ(n log n)` | `Θ(n log n)` | `Θ(n log n)` | `O(n)` | 本文 `<=` 版本穩定 |

表格描述本文實作；bogo sort 的期望值使用均勻、獨立洗牌與互異元素假設。`n log n` 的表示用於 `n >= 2`，空輸入與單元素輸入只需常數工作。

投影片將 `O(n log n)` 稱為最快排序速度，更精確的說法是：一般比較排序在最壞情況需要 `Ω(n log n)` 次比較。對 `n` 個互異元素有 `n!` 種可能順序，二元比較決策樹必須能區分這些排列，因此高度至少為 `log₂(n!) = Θ(n log n)`。

這個下界限定以比較判斷順序的模型。補充例子是 counting sort，若輸入為範圍大小 `k` 的整數，可達 `O(n + k)`，但需要利用值域資訊與額外空間，並不違反比較排序下界。

## 10. 執行範例與驗證

以下為補充測試。先執行前面所有 Python 區塊，再執行本區塊。測試涵蓋空輸入、單元素、重複值、反向順序、負數，以及搜尋失敗。

```python
cases = [[], [1], [3, 1, 2], [2, 2, 1], [5, 4, 3, 2, 1], [-1, 0, -3]]
for original in cases:
    expected = sorted(original)
    for sorter in (bubble_sort, selection_sort):
        values = original[:]
        assert sorter(values) is None
        assert values == expected
    before = original[:]
    result = merge_sort(original)
    assert result == expected
    assert original == before
    assert result is not original

for values in cases:
    ordered = sorted(values)
    for target in (-10, -3, 0, 1, 2, 3, 5, 10):
        expected = target in values
        assert linear_search(values, target) == expected
        assert search(ordered, target) == expected
        assert bisect_search2(ordered, target) == expected

assert merge([], [1, 2]) == [1, 2]
assert merge([1, 2], []) == [1, 2]
assert merge([1, 3], [1, 2]) == [1, 1, 2, 3]

# 前提被破壞的示範：這些函式不會驗證輸入已排序。
assert search([3, 1], 1) is False  # 1 存在，但提前停止造成漏報。
assert bisect_search2([3, 1, 2], 3) is False  # 排除時不再有正確性保證。

# 預期失敗：本筆記假設元素可互相比較。
try:
    merge_sort([1, "a"])
except TypeError:
    pass
else:
    raise AssertionError("Expected TypeError for incomparable elements")

# 只測 bogo sort 已排序的情況，避免不確定的等待時間。
for values in ([], [1], [1, 2, 2]):
    bogo_sort(values)
    assert is_sorted(values)

print("All lecture-note examples passed.")
```

## 11. 課程回顧與自我檢查

來源：PDF 第 32–37 頁；下列問題為補充練習。

課程最後回顧資料結構、迴圈與遞迴、程序與資料抽象、類別與方法、演算法及複雜度。Computational thinking 的 three A's 是 abstraction、automation、algorithms：選擇適當的模型，把操作寫成精確規則，並讓電腦執行。

1. 已排序 list 的線性搜尋，為什麼最壞仍是 `O(n)`？
2. 二分搜尋為何不能任意丟掉一半資料？它需要什麼前提？
3. 為什麼二分搜尋與 merge sort 都減半，時間卻不同？
4. Selection sort 的 loop invariant 是什麼？如何從它推導最終結果？
5. Merge 的三個 while 迴圈，為何總時間仍是線性？
6. 哪些函式直接修改 list，哪些回傳新 list？
7. 相等時先選右邊，對 merge sort 的穩定性有何影響？

參考答案：1. 目標在尾端或大於所有元素時仍需掃描全部。2. 必須由排序關係保證被排除區域不含目標。3. 二分搜尋只走一個子問題，merge sort 要處理兩個子問題並合併。4. 前綴已排序且不大於後綴，每輪將後綴最小值加入前綴。5. 每次加入結果都讓某個索引前進，總共只加入 `a + b` 個元素。6. Bubble、selection、bogo 修改原 list；merge 與 merge_sort 回傳新 list；搜尋回傳布林值。7. 右半部的相等元素可能跑到左半部元素前面，因此投影片 `<` 版本不保證穩定。
