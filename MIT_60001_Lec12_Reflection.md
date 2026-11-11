# MIT 6.0001 Lecture 12 Reflection Log

Topic: Searching and Sorting Algorithms

Date: 2026-11-10

## ① Check My Understanding

Questions completed: 5 / 5

Answers revised after AI hints: 2 / 5

## ② My Misconceptions

### Misconception 1: Merge Sort 的空間複雜度與切片複製

* **Before: I thought…**

  第四題，Merge Sort 串列拆分為兩個子串列，原本以為複製所有未排序的切片需要 $O(N \log N)$ 的空間。

* **Now: I understand…**

  $O(N)$ 指的是實際產生的陣列資料空間（Data Memory）。因為 Python 採用深度優先（Depth-First）執行，在記憶體最高峰時，所有開著的呼叫堆疊所持有的子串列總長度為 $N + \frac{N}{2} + \frac{N}{4} + \dots < 2N$，因此整體空間複雜度明確為 $O(N)$。

### Misconception 2: Monkey Sort (Bogo Sort) 的最佳狀況時間複雜度

* **Before: I thought…**

  Q5，Monkey Sort 最佳狀況時間複雜度為 $O(1)$。

* **Now: I understand…**

  要確認串列是否已經排序（`is_sorted`），演算法必須走訪並比對相鄰元素，考慮檢查排序最小也要 $O(N)$。

## ③ Challenge the AI

One AI-generated question I challenged:

> 無 (None)

Why?

* [ ] Ambiguous

* [ ] Oversimplified

* [ ] Technically questionable

* [ ] Too easy

* [ ] Other: N/A

**Brief explanation:**

本課是非題測驗敘述嚴謹且貼合 OCW 講義核心觀念，無特殊質疑點。

## ④ One-Minute Reflection

**One thing I am still unsure about / Course Reflection:**

雖然順利完成了 MIT 6.0001 的全部 12 堂課，理解了從基礎語法、遞迴、物件導向到時間/空間複雜度（Big-O）與分治法（Divide-and-Conquer）的核心計算思維；但對於在真實世界大規模資料下，如何根據資料特性（如近乎排序 vs 極度隨機）彈性選擇最佳演算法，以及商業套件底層（如 Python 的 Timsort 混合排序）如何優化開銷，仍期待在後續的進階課程（如 6.0002）中繼續深入探索。

---

# MIT 6.0001 Lecture 12 Coding Challenge Reflection Log

Name: User

Date: 2026-11-10

Topic: Python Practice Challenge — Inversion Counter (`count_inversions`)

## 1. Today’s Challenge

* **Core concept from today’s OCW lecture:**

  Merge Sort 的 Divide-and-Conquer（分治法）與 $O(N)$ 合併（Merge）步驟。

* **AI-generated coding challenge title:**

  Inversion Counter (`count_inversions`)

## 2. My Initial Approach — Before AI Help

Before asking AI for hints, briefly describe how you planned to solve the problem.

* **My approach:**

  想利用 Merge Sort 框架與已排序子串列來計數，當遇到 `left[i] > right[j]` 時，直覺推導出的跨區間逆序對個數公式為 `len(left) - i + 1`；但在如何同時執行 Merge 排序並正確累加傳遞各遞迴層級的逆序對數量上尚無完整想法。

## 3. AI Tutor Help

Did you ask the AI Tutor for help?

* [ ] No — I solved it independently

* [x] Yes — I received one or more hints


* **The most useful hint/question from AI was:**

  將跨區間逆序對公式修正為 `len(left) - i`，並讓 `merge_sort` 與 `count_merge` 函式同時回傳 `(排序好的串列, 逆序對數量)` 的 Tuple。

* **It helped me realize that:**

  當 `left[i] > right[j]` 時，由於 `left` 已由小到大排序，`left[i]` 及其後續所有元素均會與 `right[j]` 構成逆序對；且傳遞排序後的串列不會破壞左右區間元素的空間相對位置關係。

## 4. My Revision

Did you change your approach or code after interacting with AI?

* [ ] No

* [x] Yes


* **What did you change, and why?**

  1. 將 `result = 0` 修正為串列 `result = []`，並採用 `.append()` 與 `.extend()` 處理剩餘元素。

  2. 將逆序對打包計數公式修正為 `len(left) - i`。

  3. 將總逆序對拆為「左內部 + 右內部 + 跨區間」並透過遞迴 Tuple 向上傳遞與累加。

## 5. Verification

My final program:

* [x] Passed the provided examples

* [x] Passed additional edge cases

* [ ] Still has unresolved problems


* **One edge case I tested:**

  * **Input:** `nums = [8, 4, 2, 1]`

  * **Expected output:** `6`

  * **Actual output:** `6`

## 6. One-Minute Reflection

* **What idea from the OCW lecture did you transfer to this new problem?**

  Merge Sort 的分治拆分思維與雙指標合併機制。

* **One thing I understand better now:**

  在合併兩個已排序子串列時，可以利用單調性達成 $O(1)$ 的批量逆序對計算，從而將整體複雜度壓在 $O(N \log N)$。

* **One thing I am still unsure about:**

  **為何可以有一個排序好的版本 (result)？並解釋原因**

  * **原因說明：**

    對 `left` 和 `right` 子串列各自進行排序，完全不會改變「`left` 中所有元素在原始串列中皆位在 `right` 所有元素左側」的空間相對位置關係。因此，將 `left` 與 `right` 排序不僅不會破壞「跨區間逆序對」的判定條件，反而讓兩者具備單調性，能用 $O(1)$ 的公式 `len(left) - i` 一次打包計算跨區間逆序對，從而達成 $O(N \log N)$ 的整體時間複雜度。

```python
def count_inversions(nums: list[int]) -> int:
    """
    基於 Merge Sort 的 O(N log N) 逆序對計數器
    """
    def merge_sort(L):
        if len(L) < 2:
            return L[:], 0
        
        middle = len(L) // 2
        left, left_inv = merge_sort(L[:middle])
        right, right_inv = merge_sort(L[middle:])
        merged, cross_inv = count_merge(left, right)
        
        return merged, left_inv + right_inv + cross_inv

    def count_merge(left, right):
        result = []
        inversions = 0
        i, j = 0, 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                inversions += len(left) - i
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result, inversions

    _, total_inversions = merge_sort(nums)
    return total_inversions
```