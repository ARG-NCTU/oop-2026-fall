# AI Tutor Learning Record — W6 / MIT 6.0001 Lecture 10

**Name**　劉育麟  
**Date**　2026/10/12（課表日期）  
**OCW Topic**　Understanding Program Efficiency, Part 1  
**課程教材**　[Lecture 10 投影片，第 12–22、27–37 頁](../material/MIT6_0001F16_Lec10.pdf) 與 [lec10_complexity_part1.py](../material/lec10_complexity_part1.py)

> 初答、提示後的修正與反思採示範作答。Part B 的互動式 Python 範例列出實際執行結果。

---

# Part A: True or False

## ① Check My Understanding

**Questions completed**　5 / 5　｜　**Answers revised after AI hints**　1 / 5（示範第 1 題）

| 題號 | 判斷題 | 初答 → 定稿 | 理由 |
| --- | --- | --- | --- |
| 1 | 在課堂的 `linear_search(L, e)` 中，若第一個元素就是 `e`，只會做一次元素相等比較。 | T → F | 找到時只把 `found` 設成 `True`。迴圈仍走到最後，一共比較 `len(L)` 次。 |
| 2 | 把未排序的 `[5, 1]` 傳給講義中遇到較大值就停止的 `search`，搜尋 `1` 會得到 `False`。 | T → T | 第一輪看到 `5 > 1` 就提前回傳。這種停止條件需要輸入已排序。 |
| 3 | 完整掃描長度為 `n` 與 `m` 的兩份資料各一次，若每筆工作固定，總時間為 `Θ(n + m)`。 | T → T | 兩次掃描先後執行，操作次數相加。 |
| 4 | `isSubset` 的內圈有 `break`，所以在整次呼叫中，第二份串列的每個位置最多只會讀一次。 | F → F | 換到外圈的下一個元素時，內圈會重新從第二份串列的開頭搜尋。 |
| 5 | 若某演算法的最壞時間為 `Θ(n²)`，把一筆輸入加倍後，實測秒數一定恰為四倍。 | F → F | 成長階描述大規模時的趨勢。特定輸入的分支、常數成本與量測環境都會影響秒數。 |

## ② My Misconception

**Before — I thought…**　我看到 `linear_search` 這個名字，就把「找到立刻回傳」的版本套進題目。

**Now — I understand…**　我用 `L = [7, 2, 9]`、`e = 7` 追一次。`found` 第一輪已經變成 `True`，接下來還是會比較 `2` 和 `9`。若改成在命中時 `return True`，這筆輸入才只需一次比較。兩個版本的最壞時間都是線性，最佳情況卻不同。

## ③ Challenge the AI

**選題**　第 4 題　｜　**原因**　☒ Oversimplified

光知道程式有兩層迴圈或有 `break`，都不足以算出比較次數。以 `isSubset([3, 2], [1, 2, 3])` 為例，搜尋 `3` 需要三次比較，搜尋 `2` 又做兩次，合計五次。若題目進一步要求指出「換外圈元素時，內圈從哪裡開始」，就能分辨內圈重跑和兩個索引只向前移動的寫法。

## ④ One-Minute Reflection

我還想練習為「最佳」或「平均」標清楚條件。例如，若要估算提前回傳版本的平均比較次數，還需要知道搜尋成功的比例，以及命中位置如何分布。

---

# Part B: LeetCode-style Lecture Code Transfer

## 1. Today’s Challenge

**Count Pairs Within Budget（預算內的配對數）**

給定已依非遞減順序排列的非負整數串列 `costs` 和非負整數 `budget`，回傳滿足 `i < j` 且 `costs[i] + costs[j] <= budget` 的索引配對數。相同數值出現在不同位置時，分別計數。長度為 0 到 100,000。輸入已排序，目標為線性時間與常數額外空間。

```pycon
>>> count_pairs_within([1, 2, 3, 4], 5)
4
>>> count_pairs_within([2, 2, 2], 4)
3
```

第一例的四組費用為 `(1, 2)`、`(1, 3)`、`(1, 4)`、`(2, 3)`。第二例的三組則由三個不同的索引組合而成。

## 2. My Initial Approach — Before AI Help

我會固定左邊的項目，往右逐一試配，遇到超出預算就結束內圈。當預算足以接受所有配對時，內圈沒有機會提早結束，仍要檢查 `n(n−1)/2` 組。

## 3. AI Tutor Help

**示範提示**　看 `[1, 2, 3, 4]` 和預算 `5`。既然 `1 + 4` 合格，還需要逐一測試 `1 + 2`、`1 + 3` 嗎？反過來，若最小值搭最大值都超出預算，最大值還能和誰配對？

因為串列有序，兩端的一次比較就能決定一整批配對，也能證明某個端點可以排除。

## 4. My Revision

我用 `left` 與 `right` 表示尚待處理的範圍。若兩端和在預算內，就一次加入 `right - left` 組，再前移左端。若超出預算，就縮回右端一格。每一步都少考慮一個位置。

## 5. Verification

**My final program**

```python
def count_pairs_within(costs, budget):
    left = 0
    right = len(costs) - 1
    pairs = 0

    while left < right:
        if costs[left] + costs[right] <= budget:
            pairs += right - left
            left += 1
        else:
            right -= 1
    return pairs
```

- [x] Passed the provided examples
- [x] Passed additional edge cases

**邊界測試**　空輸入、單一項目、所有組合都超額，以及恰好等於零預算。

```pycon
>>> count_pairs_within([], 10)
0
>>> count_pairs_within([0], 0)
0
>>> count_pairs_within([4, 5, 6], 5)
0
>>> count_pairs_within([0, 0, 0, 5], 0)
3
```

## 6. One-Minute Reflection

**正確性**　若 `costs[left] + costs[right] <= budget`，左端和範圍內其餘每個位置都能配成一組。一次計入後移走左端，這些配對就不會重複。若兩端和超額，任選另一個位置搭配右端，只會使總和相同或更大，故可安全排除右端。剩不到兩個位置時，所有可能配對都已處理。

**複雜度與課程轉用**　對長度 `n ≥ 1` 的串列，初始兩端相距 `n−1`，每輪恰好縮短一格，所以迴圈恰跑 `n−1` 輪。時間為 `Θ(n)`，額外空間為 `O(1)`，以整數運算為常數成本。講義的 `isSubset` 示範了重新掃描的成本，本題利用既有順序省掉了內圈。

**仍想釐清**　如果題目改成列出每一組索引，所有值都很小時就有 `n(n−1)/2` 筆輸出。我想進一步比較「只回傳數量」和「輸出所有解」時，輸出大小如何限制最快能做到的時間。
