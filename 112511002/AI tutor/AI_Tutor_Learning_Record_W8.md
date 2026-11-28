# AI Tutor Learning Record — W8 / MIT 6.0001 Lecture 12

**Name**　劉育麟  
**Date**　2026/10/26（課表日期）  
**OCW Topic**　Searching and Sorting（課表註記為補假、期中考週）  
**課程教材**　[Lecture 12 投影片，第 3–10、14–18、25–30 頁](../material/MIT6_0001F16_Lec12.pdf) 與 [lec12_sorting.py](../material/lec12_sorting.py)

> 初答、提示後的修正與反思採示範作答。Part B 的互動式 Python 範例列出實際執行結果。

---

# Part A: True or False

## ① Check My Understanding

**Questions completed**　5 / 5　｜　**Answers revised after AI hints**　1 / 5（示範第 4 題）

| 題號 | 判斷題 | 初答 → 定稿 | 理由 |
| --- | --- | --- | --- |
| 1 | 對同一份不再改動的資料做 `q` 次查詢，若先用合併排序，再逐次二分搜尋，排序成本只需付一次。 | T → T | `n ≥ 2` 時，總成本可寫成 `O(n log n + q log n)`。 |
| 2 | 課堂的 `bubble_sort` 收到已排序的 `n ≥ 2` 個數時，第一趟仍會做 `n−1` 次相鄰比較。 | T → T | 整趟都沒有交換，才知道可以停止。 |
| 3 | 課堂的 `selection_sort` 每完成一輪外圈，已排好的前綴會增加一格，後綴當時仍可能無序。 | T → T | 該輪會把剩餘區段的最小值移到前綴之後的第一個位置。 |
| 4 | 課堂的 `merge` 只在 `left[i] < right[j]` 時取左側，所以鍵值相等時仍保留左半部元素優先的順序。 | T → F | 相等使條件為假，會取右側。若元素帶有身分標記，相同鍵值的原始相對順序可能改變。 |
| 5 | 對長度大於 1 的數字串列呼叫課堂的 `merge_sort(L)`，即使忽略回傳值，原本的 `L` 仍會被排好。 | F → F | 這份實作遞迴處理切片並建立合併結果，呼叫端需要接住回傳的串列。 |

## ② My Misconception

**Before — I thought…**　我把「結果依鍵值遞增」和「相同鍵值維持原順序」視為同一項保證。

**Now — I understand…**　設兩筆資料的鍵值都是 `2`，左邊那筆來自較早的樣本。課堂的 `<` 遇到平手時先取右邊。結果的鍵值仍然是 `[2, 2]`，但若查看樣本編號，較晚的樣本已排到前面。要讓這個合併步驟穩定，相等時就應先取左邊。

## ③ Challenge the AI

**選題**　第 2 題　｜　**原因**　☒ Oversimplified

「已排序資料的泡沫排序只需一趟」要看外圈如何停止。課堂版本會用旗標記錄是否交換，第一趟零交換就結束。若換成固定執行 `n−1` 趟的版本，輸入相同，趟數也會改變。我會請作答者同時指出停止條件與第一趟比較次數，便能檢查他實際追蹤的是哪個版本。

## ④ One-Minute Reflection

我想練習估算排序的前置成本何時值得。如果只查一個值，從頭找一次就能完成。若對同一份資料反覆查詢，每次搜尋節省的工作才有機會攤回第一次排序的成本。

---

# Part B: LeetCode-style Lecture Code Transfer

## 1. Today’s Challenge

**Count Out-of-Order Samples（計算順序顛倒的樣本配對）**

串列 `samples` 依接收順序記錄樣本的整數序號。回傳有多少組索引 `i < j` 滿足 `samples[i] > samples[j]`。相同序號不計，輸入可能為空，長度最多 100,000。函式必須保留原始接收順序，最壞時間要求 `O(n log n)`。

```pycon
>>> count_inversions([3, 1, 2, 1])
4
>>> count_inversions([2, 2, 1])
2
```

第一例中，開頭的 `3` 與後面三筆各形成一組，`2` 和最後的 `1` 又形成一組。

## 2. My Initial Approach — Before AI Help

我先想到枚舉所有 `i < j`，方法直接，但 100,000 筆資料就有近五十億組候選。若只把序號排序再看結果，接收時的先後關係也會消失。我需要在排序過程中把這項資訊記下來。

## 3. AI Tutor Help

**示範提示**　合併兩個已排序區段 `[2, 4, 7]` 和 `[3]` 時，先取出 `2`。接著輪到右側的 `3`，這一步能確定它和左側的幾筆資料構成逆序？

剩餘的 `4`、`7` 原本都比 `3` 更早收到，又都比 `3` 大。這次取右側就能一次計入兩組。

## 4. My Revision

每層遞迴回傳「已排序區段、該區段內的逆序數」。合併時，只有右側元素嚴格小於左側目前元素，才加上左側剩餘長度。相等時先取左側，以免把平手算進去。

## 5. Verification

**My final program**

```python
def count_inversions(samples):
    def sort_and_count(values):
        if len(values) < 2:
            return values, 0

        middle = len(values) // 2
        left, left_count = sort_and_count(values[:middle])
        right, right_count = sort_and_count(values[middle:])
        total = left_count + right_count
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                total += len(left) - i
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, total

    _, total = sort_and_count(samples)
    return total
```

- [x] Passed the provided examples
- [x] Passed additional edge cases

**邊界測試**　空或單筆輸入、全相等、已排序與完全反序。最後一例也檢查呼叫後的輸入內容。

```pycon
>>> count_inversions([]), count_inversions([8])
(0, 0)
>>> count_inversions([4, 4, 4]), count_inversions([1, 2, 3])
(0, 0)
>>> received = [4, 3, 2, 1]
>>> count_inversions(received), received
(6, [4, 3, 2, 1])
```

## 6. One-Minute Reflection

**正確性**　每對樣本只屬於三種情況之一：兩者同在左半、同在右半、或左右各一。遞迴已處理前兩種。對跨區段的一對，右側較小值被取出時，左側所有尚未輸出的值都比它大。它們被一次計入，該右側值之後也不會再參與計數。

**複雜度與課程轉用**　這題沿用講義 `merge` 的兩個索引。每層切片與合併合計 `O(n)`，共 `O(log n)` 層，總時間為 `O(n log n)`。同時存活的區段與合併結果合計為 `O(n)`，其中遞迴堆疊深度為 `O(log n)`。此處計算資料操作，程式沒有輸出各輪排序的除錯訊息。

**仍想釐清**　若題目改成列出每一對顛倒的原始索引，完全反序時就必須輸出 `n(n−1)/2` 筆。我想比較計數時能合併處理的資訊，在需要列出配對時哪些必須保留下來。
