# AI Tutor Learning Record — W10 / MIT 6.0002 Lecture 2

**Name**　劉育麟  
**Date**　2026/11/09（課表日期）  
**OCW Topic**　Optimization Problems（決策樹與動態規劃）  
**課程教材**　[Lecture 2 投影片，第 4–10、18–30 頁](../material2/MIT6_0002F16_lec2.pdf)

> 初答、提示後的修正與反思採示範作答。Part B 的互動式 Python 範例列出實際執行結果。

---

# Part A: True or False

## ① Check My Understanding

**Questions completed**　5 / 5　｜　**Answers revised after AI hints**　1 / 5（示範第 2 題）

| 題號 | 判斷題 | 初答 → 定稿 | 理由 |
| --- | --- | --- | --- |
| 1 | 0/1 背包決策樹中，若目前物品超過剩餘容量，仍要評估「不取」分支，因為後續可能有較輕的物品。 | T → T | 只有取用目前物品的分支不合法，後綴的其他選擇仍可能有價值。 |
| 2 | 對同一份固定選單做記憶化搜尋，只要記錄「下一個要考慮的物品索引」，便足以重用該位置的最佳值。 | T → F | 即使候選物品相同，剩餘容量不同也會改變能取得的價值。 |
| 3 | 對固定選單的標準 0/1 背包，兩條路若來到相同後綴及相同剩餘容量，能共用「從此處往後最多還可取得多少價值」。 | T → T | 後續可行選項相同。先前累積的價值由各路徑自行加回。 |
| 4 | 子問題彼此重疊時，只要用了遞迴，Python 就會自動重用先前呼叫過的結果。 | F → F | 一般函式呼叫會重新執行，必須明確保存與查詢結果才能省去重算。 |
| 5 | 整數容量為 `B` 時，`O(nB)` 中的 `B` 就是輸入容量所需的二進位位元數。 | F → F | `B` 是容量數值，表示它所需的位元數約為 `log₂(B+1)`。這個上界屬於偽多項式時間。 |

## ② My Misconception

**Before — I thought…**　兩條路剩下的物品相同，我就想把它們合併成同一個子問題。

**Now — I understand…**　若最後只剩一項成本 2、價值 8 的物品，剩餘容量 1 的最佳附加價值是 0，容量 3 時則是 8。把兩者都存成「最後一項」會讓其中一條路讀到錯誤結果。課堂的 `fastMaxVal` 同時用剩餘項目數和可用容量作為鍵。

## ③ Challenge the AI

**選題**　第 3 題　｜　**原因**　☒ Ambiguous

「可以共用結果」必須先定義回傳值。若甲、乙來到同一狀態時分別已累積 4 分和 9 分，而且之後最多再得 6 分，可以共用的是 6。兩條路最後的總分分別是 10 和 15。將回傳值寫成「剩餘項目能取得的最大附加價值」，快取裡該存什麼就明確了。

## ④ One-Minute Reflection

我想練習替新限制選擇狀態。若加入「相鄰兩項不能一起選」，直覺上似乎要多記一個布林值，但也可以在選取第 `i` 項時直接跳到 `i+2`，讓下一個子問題自然代表合法的後續選擇。

---

# Part B: LeetCode-style Lecture Code Transfer

## 1. Today’s Challenge

**Schedule Nonadjacent Scans（選擇不相鄰的掃描通道）**

輸入 `scans` 依通道編號排列，每項為整數 `(cost, score)`。每個通道最多掃描一次，總成本不得超過 `budget`，硬體規格也禁止同時選擇編號相鄰的兩個通道。回傳可取得的最大總分，可以完全不選。通道數為 0 到 100，成本為正整數，分數非負，整數預算介於 0 與 500。

```pycon
>>> max_scan_score([(2, 6), (3, 10), (2, 6)], 4)
12
>>> max_scan_score([(2, 5), (2, 6)], 4)
6
```

第一例選編號 0 與 2，剛好花 4 得 12 分。第二例的預算足以支付兩項，但兩個通道相鄰，所以最多得 6 分。

## 2. My Initial Approach — Before AI Help

我會從左往右建立「選、略過」兩條分支。選取時扣除費用並跳過下一個通道，略過時前進一格。初稿想用 `memo[i]` 保存每個位置的最佳分數。

## 3. AI Tutor Help

**示範提示**　對 `[(2, 3), (5, 1), (2, 8)]` 和預算 `3`，先選通道 0 或先略過它，來到通道 2 時分別還剩多少預算？通道 2 還能貢獻幾分？

選過 0 時只剩 1，最後一項拿不到。若略過前兩項則剩 3，可以拿 8 分。此例讓我找到只用索引當快取鍵的錯誤。

## 4. My Revision

我把鍵改為 `(i, remaining)`，值代表從 `i` 往後能額外得到的最大分數。每次外層呼叫都建立新的字典，避免不同掃描表碰巧有相同索引與預算而讀到舊值。

## 5. Verification

**My final program**

```python
def max_scan_score(scans, budget):
    memo = {}

    def best(i, remaining):
        if i >= len(scans) or remaining == 0:
            return 0

        key = (i, remaining)
        if key in memo:
            return memo[key]

        cost, score = scans[i]
        result = best(i + 1, remaining)
        if cost <= remaining:
            take = score + best(i + 2, remaining - cost)
            result = max(result, take)

        memo[key] = result
        return result

    return best(0, budget)
```

- [x] Passed the provided examples
- [x] Passed additional edge cases

**邊界測試**　涵蓋空輸入、零預算、首項過貴、相同後綴搭配不同剩餘預算，以及更換掃描表後重新計算。

```pycon
>>> max_scan_score([], 5), max_scan_score([(1, 7)], 0)
(0, 0)
>>> max_scan_score([(5, 99), (1, 4)], 1)
4
>>> max_scan_score([(2, 3), (5, 1), (2, 8)], 3)
8
>>> max_scan_score([(2, 8)], 2), max_scan_score([(2, 1)], 2)
(8, 1)
```

## 6. One-Minute Reflection

**正確性**　每個合法方案對通道 `i` 只有兩種選擇。略過它時，其他合法方案都在 `best(i+1, remaining)` 內。選取它時，扣掉成本後跳到 `i+2`，正好滿足相鄰限制。每條合法路徑都屬於其中一支，取兩支較高的分數就得到當前狀態的最佳值。沒有通道或沒有預算時，因成本皆為正，回傳 0 正確。

**複雜度與課程轉用**　索引至多有 `n` 個需要快取的位置，剩餘預算有 `B+1` 種整數值。假設字典操作平均為常數時間，每個狀態至多展開一次，時間上界為 `O(n(B+1))`。快取至多占 `O(n(B+1))`，另有 `O(n)` 遞迴堆疊。講義的決策樹與記憶化都能沿用，新增硬體限制只改變「選取」分支的下一個索引。

**仍想釐清**　如果需要回傳實際選到的通道，我想試著沿快取中的分數重建路徑，並替兩條路同分時訂出一致的選擇規則。
