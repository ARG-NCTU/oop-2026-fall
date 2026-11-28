# AI Tutor Learning Record — W7 / MIT 6.0001 Lecture 11

**Name**　劉育麟  
**Date**　2026/10/19（課表日期）  
**OCW Topic**　Understanding Program Efficiency, Part 2  
**課程教材**　[Lecture 11 投影片，第 9–17、21–22、28–32 頁](../material/MIT6_0001F16_Lec11.pdf) 與 [lec11_complexity_part2.py](../material/lec11_complexity_part2.py)

> 初答、提示後的修正與反思採示範作答。Part B 的互動式 Python 範例列出實際執行結果。

---

# Part A: True or False

## ① Check My Understanding

**Questions completed**　5 / 5　｜　**Answers revised after AI hints**　1 / 5（示範第 1 題）

| 題號 | 判斷題 | 初答 → 定稿 | 理由 |
| --- | --- | --- | --- |
| 1 | 二分搜尋每輪把串列切成一半並複製該切片，最壞總時間仍是 `O(log n)`。 | T → F | 比較次數是對數級，但沿搜尋路徑建立的切片共複製約 `n/2 + n/4 + …` 個元素，最壞時間為 `Θ(n)`。 |
| 2 | 講義的 `bisect_search2([], e)` 可以直接得到 `False`。 | T → T | 外層先檢查長度，空串列會在讀取索引之前結束。 |
| 3 | 對已排序且含重複值的串列，課堂的 `bisect_search2` 一旦命中，中點必定是目標第一次出現的位置。 | F → F | 它只需判斷存在性。例如 `[4, 4, 4]` 第一輪就命中索引 1，但第一次出現在索引 0。 |
| 4 | 對 `n` 個相異元素執行 `genSubsets`，空集合也要算入；新增一個相異元素後，子集合數量會加倍。 | T → T | 每個舊子集合各有保留原樣、加入新元素兩種選擇。起點是 `[[]]`，含一個子集合。 |
| 5 | 在乘法視為固定成本的模型下，迭代與一般遞迴階乘都做線性次運算，但遞迴版本還要保留線性層數的呼叫堆疊。 | T → T | 遞迴呼叫須等內層回傳才能完成外層乘法，迭代只需保存目前的乘積與計數。 |

## ② My Misconception

**Before — I thought…**　我原本只數比較次數。看到長度從 16 變成 8、4、2、1，就直接寫下對數時間。

**Now — I understand…**　同樣四次縮小範圍，若每輪配置切片，光複製這四段就可能搬動約 `8 + 4 + 2 + 1 = 15` 個參照。把原串列和兩個索引傳下去時，每輪才只需固定的存取和比較成本。

## ③ Challenge the AI

**選題**　第 1 題　｜　**原因**　☒ Ambiguous

若題目只寫「二分搜尋需要 `O(log n)`」，我會追問是在數鍵值比較，還是在算整個 Python 實作的執行時間。也要確認成本上界是否夠精確。對每層都複製剩餘一半的版本，`O(n log n)` 雖然是上界，但把每層都當成複製 `n` 個元素會高估。把各層的實際長度加起來才能得到緊確的 `Θ(n)`。

## ④ One-Minute Reflection

我想進一步練習遇到遞迴時分別寫出「每次呼叫的工作量」和「共有多少次呼叫」。二分搜尋只往其中一半走，產生冪集合卻必須保留指數量的輸出，光看遞迴深度不足以推斷總時間。

---

# Part B: LeetCode-style Lecture Code Transfer

## 1. Today’s Challenge

**Count ADC Codes in a Band（計算區間內的 ADC 輸出碼數）**

`codes` 是一份已依非遞減順序排列的 12-bit ADC 整數輸出碼，值域為 0 到 4095，可有重複值，長度為 0 到 100,000。給定兩個整數 `low`、`high`，回傳落在閉區間 `[low, high]` 的筆數。界限可超出輸出碼值域，若 `low > high` 則回傳零。要求查詢時不複製或逐筆掃描串列。

```pycon
>>> count_in_band([1, 2, 2, 4, 4, 4, 9], 2, 4)
5
>>> count_in_band([3, 7, 11], 4, 6)
0
```

## 2. My Initial Approach — Before AI Help

我打算先二分搜尋 `low` 和 `high` 並相減，但同一個輸出碼可能佔好幾格。若第一次命中就停止，可能漏掉左右兩端的重複值。另一個問題是兩個界限本身都可能沒有出現在串列中。

## 3. AI Tutor Help

**示範提示**　若已知第一個 `≥ low` 的位置和第一個 `> high` 的位置，即使這兩個界限都沒出現在資料裡，你能直接由索引算出數量嗎？

滿足條件的元素連在一起。第一個符合的位置包含在區間中，右方第一個超界的位置排除在外，它們的索引差就是筆數。

## 4. My Revision

我改寫一個尋找「第一個大於等於目標」的函式。找不到時回傳 `len(codes)`，這個位置也能參與相減。輸出碼與界限都是整數，因此用 `high + 1` 作為第二次查詢的目標，就能找到第一個嚴格大於 `high` 的位置。

## 5. Verification

**My final program**

```python
def count_in_band(codes, low, high):
    if low > high:
        return 0

    def first_at_least(target):
        left = 0
        right = len(codes)
        while left < right:
            mid = (left + right) // 2
            if codes[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    return first_at_least(high + 1) - first_at_least(low)
```

- [x] Passed the provided examples
- [x] Passed additional edge cases

**邊界測試**　以下包含空串列、低高界相同、涵蓋整份資料、界限顛倒，以及上界落在最後一筆。

```pycon
>>> count_in_band([], 0, 4095)
0
>>> count_in_band([7, 7, 7], 7, 7)
3
>>> count_in_band([0, 17, 4095], -1, 5000)
3
>>> count_in_band([1, 2], 2, 1)
0
>>> count_in_band([0, 4095, 4095], 4095, 4095)
2
```

## 6. One-Minute Reflection

**正確性**　每輪開始時，索引小於 `left` 的值都小於目標，索引大於等於 `right` 的已知區段都大於等於目標。若中點的值太小，就連同它左側一起排除。否則中點可能正好是第一個符合者，故保留此邊界並向左找。當兩端相遇，該索引就是所求的分界點。

**複雜度與課程轉用**　兩次查詢都沿用 `bisect_search2` 傳遞索引的概念，每一輪只縮小索引範圍。對 `n ≥ 2`，最壞時間為 `O(log n)`，迭代實作使用 `O(1)` 額外空間。空串列直接得到兩個零索引。

**仍想釐清**　如果輸入改成類比電壓的浮點量測值，`high + 1` 就會把許多高於上限的電壓也算進去。我會保留相同的搜尋範圍，改為直接尋找第一筆 `> high` 的資料。
