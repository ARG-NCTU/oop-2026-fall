<!-- AI prompt
I just learned Decision Trees, Dynamic Programming, and Memoization (applied to Fibonacci and the 0/1 Knapsack Problem) in today's lecture.

Act as my AI Tutor.

1. Generate 5 True/False questions, one question at a time, to test my conceptual understanding of today's topic.
2. Focus on concepts and reasoning, not memorization or Python syntax.
3. After I answer, do not immediately tell me the correct answer.
4. If my answer or reasoning is incorrect, give me a hint, counterexample, or follow-up question.
5. Let me revise my answer before explaining the concept.
6. Adjust the difficulty based on my responses.
7. After five questions, ask me to identify one question that may be ambiguous, misleading, too easy, or technically questionable.
8. Finish by asking me what misconception I corrected and what I am still unsure about.
-->

# 📝 Learning Reflection & Concept Check — Part A

**Topic:** Decision Trees, Dynamic Programming, Memoization (MIT 6.0002 Lecture 2)  
**Date:** 2026-11-09  

---

### ① Check My Understanding

* **Questions completed:** 5 / 5
* **Hints requested before answering:** 2 / 5  

| 題號 | 主題 | 我的答案 | 結果 |
| :--- | :--- | :--- | :--- |
| Q1 | 對任何遞迴演算法加上 memoization 是否都能大幅加速 | False | ✅ 一次答對 |
| Q2 | `fastMaxVal` 以 `(len(toConsider), avail)` 當 key，同一次呼叫中是否可能撞 key 而回傳錯誤結果 | False | ✅ 看提示後答對 |
| Q3 | 預設參數 `memo = {}` 下，對不同菜單連續呼叫，第二次是否一定正確 | False | ✅ 一次答對 |
| Q4 | 加上 DP 後，`fastMaxVal` 的執行時間是否不論 cost 數值都只和 `n` 成多項式關係 | False | ✅ 看提示後答對 |
| Q5 | `withVal > withoutVal` 改成 `>=`，回傳的總價值是否可能不同 | False | ✅ 一次答對 |

---

### ② My Misconception

**Before: I thought…**  
Q4 看提示前沒有直接作答，也沒想到 memo 能不能命中，取決於 `avail` 可能出現多少種值。

⸻

**Now: I understand…**  
memo 的效率取決於 `avail` 的數值範圍。真正的計算次數最多約為 `(n + 1) × (avail 的不同值個數)`。cost 是小整數時（例如 `maxCost = 750`），`avail` 的可能值有限，memo 很有效；cost 是浮點數或很大的數時，`avail` 幾乎每次都不同，memo 幾乎命中不了，執行時間又退回指數級。這叫 pseudo-polynomial。

---

### ③ Challenge the AI

**One AI-generated question I challenged:**  
Q5：「把 `maxVal` 中的 `if withVal > withoutVal:` 改成 `>=`，其餘不變。對某些輸入，修改後的 `maxVal` 回傳的總價值會和原版不同。」

⸻

**Why?**

* [x] Ambiguous
* [ ] Oversimplified
* [ ] Technically questionable
* [ ] Too easy
* [ ] Other

**Brief explanation:**  
「總價值」和「回傳結果」沒有分開講。`maxVal` 回傳的是 `(value, items)` tuple，題目只問總價值，但沒有說明物品組合可能不同，容易讓人誤以為整個回傳結果都要相同。（具體指出哪一點不清楚時，我從 AI 列出的選項中選了這一項。）

**改寫建議：**  

> 把 `maxVal` 中的 `if withVal > withoutVal:` 改成 `>=`，其餘不變。對任何輸入，修改後 `maxVal` 回傳 tuple 的第一個元素（總價值）都和原版相同，但第二個元素（選到的物品組合）可能不同。（答案：True）

---

### ④ One-Minute Reflection

**One thing I am still unsure about:**  
沒有。

⸻
