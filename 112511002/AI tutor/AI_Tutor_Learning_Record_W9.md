# AI Tutor Learning Record — W9 / MIT 6.0002 Lecture 1

**Name**　劉育麟  
**Date**　2026/11/02（課表日期）  
**OCW Topic**　Introduction and Optimization Problems  
**課程教材**　[Lecture 1 投影片，第 11–18、21–30 頁](../material2/MIT6_0002F16_lec1.pdf) 與 [lecture1.py](../material2/Lecture1/lecture1.py)

> 初答、提示後的修正與反思採示範作答。Part B 的互動式 Python 範例列出實際執行結果。

---

# Part A: True or False

## ① Check My Understanding

**Questions completed**　5 / 5　｜　**Answers revised after AI hints**　1 / 5（示範第 3 題）

| 題號 | 判斷題 | 初答 → 定稿 | 理由 |
| --- | --- | --- | --- |
| 1 | 在課堂的餐點選擇模型中，挑出的食物只要沒有超過熱量上限，就已經得到最佳解。 | F → F | 滿足熱量限制只能確定這是一個可行解，還要比較可行組合的總價值。 |
| 2 | 課堂的 `greedy` 用 `sorted(items, key=..., reverse=True)` 排出考慮順序，原本選單的排列會保留。 | T → T | 它走訪排序後的新串列，未對傳入的選單原地排序。 |
| 3 | 物品不可分割時，每次選擇放得下且價值密度最高的物品，一定能使總價值最大。 | T → F | 一件高密度物品可能留下無法利用的容量，另外兩件物品的合計價值可能更高。 |
| 4 | 若物品可以任意分割、價值隨取用比例線性增加、重量為正且價值非負，按密度從高到低取用可得到最佳解。 | T → T | 若解中用了低密度物品，而高密度物品還有剩餘，用相同重量換過去不會降低總價值。 |
| 5 | 課堂的 `greedy` 遇到第一個放不下的物品時，可以直接結束並保證得到與原程式相同的選擇。 | F → F | 排序依據可能是價值或密度，後面的物品可能更輕，仍放得下。 |

## ② My Misconception

**Before — I thought…**　我以為把每單位容量用在最有價值的物品上，就能把整個背包用得最好。

**Now — I understand…**　假設容量是 4，三件物品的（重量，價值）分別為 `(3, 5)`、`(2, 3)`、`(2, 3)`。第一件的密度 `5/3` 最高，但拿了後剩 1，總價值只有 5。改拿後兩件，重量恰為 4，價值是 6。物品能否拆分，會直接改變這項策略的保證。

## ③ Challenge the AI

**選題**　第 5 題　｜　**原因**　☒ Oversimplified

我會追問排序鍵是什麼。當候選物品按重量由輕到重排列，若當前最輕的一件都放不下，後面確實可以跳過。但課堂的 `keyFunction` 也接受價值或密度，此時較輕物品仍可能排在後面。例如剩餘容量 2，先看見重 3 的高價物品，再看見重 1 的物品，直接結束就會漏選後者。

## ④ One-Minute Reflection

我想練習判斷哪些貪婪法可以證明最佳。密度策略在 0/1 背包的反例，只要三件物品就能看出來；換成時段安排後，證明的重點則變成能否把最佳解中的第一個選擇安全替換掉。

---

# Part B: LeetCode-style Lecture Code Transfer

## 1. Today’s Challenge

**Book the Most Lab Sessions（安排最多儀器使用時段）**

一臺示波器一次只能接受一個預約。輸入 `sessions` 是最多 10,000 筆 `(name, start, end)`，名稱各異，時間為非負整數且 `start < end`。時段採 `[start, end)`，前一人結束的時刻可交給下一人。每筆預約價值相同，目標是接受最多筆，依使用先後回傳名稱串列。

若多個可接受時段同時最早結束，優先使用輸入中較早出現的一筆。保留輸入原順序。

```pycon
>>> slots = [("long", 0, 6), ("scope", 1, 3), ("probe", 3, 5), ("adc", 5, 7)]
>>> select_sessions(slots)
['scope', 'probe', 'adc']
>>> select_sessions([("B", 2, 5), ("A", 0, 5), ("C", 5, 9)])
['B', 'C']
```

## 2. My Initial Approach — Before AI Help

我先想到優先接受使用時間最短的預約。但 `A = [0, 4)`、`M = [3, 5)`、`B = [4, 8)` 中，最短的 `M` 同時占到 `A` 的尾端與 `B` 的開頭。選 `M` 只能排一筆，選 `A` 接 `B` 可以排兩筆。

## 3. AI Tutor Help

**示範提示**　取一份已經排到最多筆的行程。如果把其中第一筆換成所有候選中最早結束的一筆，原本的第二筆還接得上嗎？

換入的預約結束時間不會更晚，所以後續預約仍然可行。這讓我有理由把「最早結束」作為排序鍵。

## 4. My Revision

我依結束時間排序，逐筆接受開始時間大於等於上一筆結束時間的預約。使用 `sorted` 保留原輸入。Python 的排序具有穩定性，結束時間相同的預約會依輸入次序接受檢查。

## 5. Verification

**My final program**

```python
def select_sessions(sessions):
    ordered = sorted(sessions, key=lambda session: session[2])
    selected = []
    available_from = 0

    for name, start, end in ordered:
        if start >= available_from:
            selected.append(name)
            available_from = end
    return selected
```

- [x] Passed the provided examples
- [x] Passed additional edge cases

**邊界測試**　檢查空輸入、三筆都重疊、首尾相接，以及遇到同時結束但第一筆已衝突時仍會考慮下一筆。

```pycon
>>> select_sessions([])
[]
>>> select_sessions([("A", 0, 9), ("B", 1, 5), ("C", 2, 4)])
['C']
>>> requests = [("B", 4, 8), ("M", 3, 5), ("A", 0, 4)]
>>> select_sessions(requests), [s[0] for s in requests]
(['A', 'B'], ['B', 'M', 'A'])
>>> select_sessions([("first", 0, 3), ("clash", 2, 5), ("fit", 3, 5)])
['first', 'fit']
```

## 6. One-Minute Reflection

**正確性**　取得任一筆數最多的可行排程。以目前最早結束的可行預約取代其第一筆後，剩下的預約仍排得下，總筆數相同。固定這一筆後，從其結束時刻開始，剩餘問題仍是同樣的排程問題。逐步套用這個替換理由，即可得到本程式選出的筆數也是最大值。相同結束時間會留下相同的可用起點。

**複雜度與課程轉用**　沿用課堂 `greedy` 的兩個步驟，先透過排序鍵決定選擇順序，再檢查目前限制是否允許接受。對 `n` 筆預約，排序花 `O(n log n)` 時間，掃描花 `O(n)`，額外空間為 `O(n)`，包括排序副本與結果。

**仍想釐清**　如果貴重的量測時段有更高收益，最多筆未必等於總收益最高。我想找出一個最小反例，觀察上述替換證明從哪一步開始失效。
