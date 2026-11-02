<!-- AI prompt
I just learned Optimization Problems, the 0/1 Knapsack Problem, and Greedy Algorithms in today's lecture.

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

**Topic:** Optimization Problems, 0/1 Knapsack, Greedy Algorithms (MIT 6.0002 Lecture 1)  
**Date:** 2026-11-02  

---

### ① Check My Understanding

* **Questions completed:** 5 / 5
* **Answers revised after AI hints:** 2 / 5  

| 題號 | 主題 | 我的答案 | 結果 |
| :--- | :--- | :--- | :--- |
| Q1 | greedy by density 的總價值是否一定不低於 by value 和 by cost | False | ✅ 一次答對 |
| Q2 | 遇到放不下就 `break` 的版本，總價值是否一定不高於原版 | False → True | ✅ 看提示後修正 |
| Q3 | 排序順序不同，選出的物品集合是否一定不同 | False | ✅ 一次答對 |
| Q4 | 每個物品 cost 都相同時，greedy by value 是否一定能得到最佳解 | False → True | ✅ 看提示後修正 |
| Q5 | `maxCost` 變大時，greedy by value 的總價值是否一定不會下降 | False | ✅ 一次答對 |

---

### ② My Misconception

**Before: I thought…**  
Q2 第一次回答 False，認為 `break` 版的總價值有可能高於原版（當時未附理由）。

⸻

**Now: I understand…**  
`break` 版的總價值一定不高於原版。以 AI 提示的例子來看（`maxCost = 10`，排序後為 A、B、C，cost 分別是 6、7、3），原版選 A、C，`break` 版只選 A，原版只會多加不會變少。

---

### ③ Challenge the AI

**One AI-generated question I challenged:**  
Q4：「假設 0/1 背包問題中，每個物品的 cost 都相同，value 都是正數，而且 `maxCost >= 0`。在這個特殊情況下，greedy by value 一定能得到最佳解。」

⸻

**Why?**

* [x] Ambiguous
* [ ] Oversimplified
* [ ] Technically questionable
* [ ] Too easy
* [ ] Other

**Brief explanation:**  
沒說明最佳解可能不只一組。（這個質疑方向由 AI 先提議，我選用。）

**改寫建議：**  

> 假設每個物品的 cost 都相同，value 都是正數，而且 `maxCost >= 0`。greedy by value 選出的組合，總價值一定等於所有可行組合中的最大值；但達到這個最大值的組合可能不只一組。（答案：True）

---

### ④ One-Minute Reflection

**One thing I am still unsure about:**  
沒有。

⸻
