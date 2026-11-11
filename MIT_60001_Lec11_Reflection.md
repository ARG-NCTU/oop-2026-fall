# MIT 6.0001 Lecture 11 Reflection Log

Topic: Understanding Program Efficiency 2  
Date: 2026-11-10

---

## ① Check My Understanding

Questions completed: 5 / 5  
Answers revised after AI hints: 3 / 5  

---

## ② My Misconceptions

### Misconception 1: 遞迴切片二元搜尋的時間複雜度
* **Before: I thought…**  
  二元搜尋遞迴深度為 $O(\log N)$，且每次遞迴都使用串列切片 `L[:mid]`（複製耗時 $O(N)$），因此總時間複雜度為 $O(N \log N)$。
* **Now: I understand…**  
  每次切片複製的串列長度依次折半（$\frac{N}{2} + \frac{N}{4} + \frac{N}{8} + \dots + 1$），屬於公比為 $\frac{1}{2}$ 的等比級數求和，總和收斂於 $N$ 以內。因此總時間複雜度由切片複製成本主導，應為 **$O(N)$**。

---

### Misconception 2: Python 字典（Dict）查詢時間複雜度
* **Before: I thought…**  
  Python 字典底層採用哈希表（Hash Table），如同指紋般獨一無二，因此不論何種狀況（包含最壞狀況 Worst Case），查詢時間皆嚴格保證為 $O(1)$。
* **Now: I understand…**  
  字典在平均狀況下查詢為 $O(1)$。但由於記憶體空間有限（鴿籠原理），不同的 Key 仍可能發生**哈希碰撞（Hash Collision）**。若所有 Key 皆擠在同一探測鏈上，最壞狀況下的查詢複雜度會退化為 **$O(N)$**。

---

### Misconception 3: 樸素遞迴費氏數列的空間複雜度
* **Before: I thought…**  
  `fib_recur(n)` 的時間複雜度因為呼叫樹爆發為 $O(2^N)$，且會儲存先前計算的狀態，因此記憶體空間複雜度同樣為 $O(2^N)$。
* **Now: I understand…**  
  樸素遞迴完全沒有儲存已計算過的值。然而在空間複雜度方面，呼叫堆疊（Call Stack）採用深度優先搜尋（DFS），同一時間點僅維持單一路徑，樹的最大深度為 $N$。當葉子節點 return 後記憶體便被彈出（Pop）並重複利用，因此最大空間複雜度僅為 **$O(N)$**。

---

## ③ Challenge the AI

One AI-generated question I challenged:  
> 第四題有問題，題目只要求剔除最後一個值，假設 L=[1,2,3,4,5]，L 的子集應該只有 [1,2,3,4] 一個而已，而不是所有元素的排列才對。

Why?
- [x] Ambiguous
- [ ] Oversimplified
- [ ] Technically questionable
- [ ] Too easy
- [ ] Other: Terminology Unclear

**Brief explanation:**  
題目未事先清楚定義「冪集（Power Set）」是指包含**所有 $2^N$ 個可能子集組合**的集合，導致將遞迴呼叫 `genSubsets(L[:-1])` 誤解為僅做一次單純切片取單個子串列，進而混淆了迴圈走訪 $2^{n-1}$ 次造成的 $O(2^N)$ 時間爆發本質。

---

## ④ One-Minute Reflection

**One thing I am still unsure about:**  
為何哈希表會發生 Hash 碰撞？  
* **主要原因：**
  1. **鴿籠原理 (Pigeonhole Principle)**：輸入的 Key 有無限多種可能，但字典分配的記憶體桶子（Buckets）數量是有限的，將無限映射到有限必然產生衝突。
  2. **取餘數空間縮減**：計算出 Hash 值後會對陣列長度取餘數（如 `hash(key) % M`），不同 Hash 值取餘數後可能落在同一個索引位置。
  3. **最壞狀況退化**：碰撞發生時 Python 採用開放定址探測，若極端情況下全部 Key 被分配到同一個桶子鏈，查詢便需逐一比對，退化為 $O(N)$。

---
---

# MIT 6.0001 Lecture 11 Coding Challenge Reflection Log

Name: User  
Date: 2026-11-10  
Topic: Python Practice Challenge — Strictly Greater Element Finder (`find_next_greater`)

---

## 1. Today’s Challenge

* **Core concept from today’s OCW lecture:**  
  二元搜尋法（Bisection Search）與雙指標控制（Pointer Indexing），避免串列切片開銷。
* **AI-generated coding challenge title:**  
  Strictly Greater Element Finder (`find_next_greater`)

---

## 2. My Initial Approach — Before AI Help

Before asking AI for hints, briefly describe how you planned to solve the problem.

* **My approach:**  
  取串列最中間的值與 `target` 比較。若 `target` 較大，則取中間值與最大值之間的中間值繼續與 `target` 比較；反之亦然，層層迭代折半搜尋。

---

## 3. AI Tutor Help

Did you ask the AI Tutor for help?
- [ ] No — I solved it independently
- [x] Yes — I received one or more hints

* **The most useful hint/question from AI was:**  
  使用 `low` 與 `high` 指標夾擠收窄範圍以防範切片開銷，並思考當 `nums[mid] == target` 或 `nums[mid] > target` 時指標該如何移動。
* **It helped me realize that:**  
  利用 `nums[mid] <= target` 統一將 `low` 往右推進（`low = mid + 1`），當迴圈結束（`low > high`）時，`nums[low]` 必為第一個嚴格大於 `target` 的最小元素。

---

## 4. My Revision

Did you change your approach or code after interacting with AI?
- [ ] No
- [x] Yes

* **What did you change, and why?**  
  1. 將條件簡化：將 `nums[mid] == target` 的分支直接合併至 `nums[mid] <= target` 的 `else` 區塊中（`low = mid + 1`）。
  2. 修正邊界回傳值：當不存在嚴格大於 `target` 的元素時（即 `low >= len(nums)`），將原回傳的 `None` 修正為 `-1` 以符合規格需求。

---

## 5. Verification

My final program:
- [x] Passed the provided examples
- [x] Passed additional edge cases
- [ ] Still has unresolved problems

* **One edge case I tested:**  
  * **Input:** `nums = [1, 3, 7, 10]`, `target = 10`  
  * **Expected output:** `-1`  
  * **Actual output:** `-1`  

---

## 6. One-Minute Reflection

* **What idea from the OCW lecture did you transfer to this new problem?**  
  二元搜尋法的折半搜尋邏輯與 `low`/`high` 指標範圍鎖定機制，避免使用 `L[:mid]` 切片以達成嚴格 $O(\log N)$ 時間複雜度。

* **One thing I understand better now:**  
  二元搜尋結束時的數學不變性（Invariant）：迴圈結束時必定滿足 $nums[high] \le target < nums[low]$，因此 `nums[low]` 必然指向第一個嚴格大於 `target` 的位置。

* **One thing I am still unsure about:**  
  二元搜尋法遞迴版（Recursive Approach）的 Call Stack 空間複雜度為何是 $O(\log N)$，以及如何透過傳遞 `low`/`high` 指標實作乾淨的遞迴版本。

```python
def find_next_greater_recur(nums: list[int], target: int) -> int:
    """
    遞迴版二元搜尋：透過傳遞 low/high 指標避免切片開銷。
    時間複雜度：O(log N)
    空間複雜度：O(log N) (來自 Call Stack 深度)
    """
    def helper(low: int, high: int) -> int:
        # Base Case: 當範圍交錯 (low > high)，解答位置鎖定於 low
        if low > high:
            return nums[low] if low < len(nums) else -1
            
        mid = (low + high) // 2
        if nums[mid] > target:
            return helper(low, mid - 1)
        else:
            return helper(mid + 1, high)

    return helper(0, len(nums) - 1)
```