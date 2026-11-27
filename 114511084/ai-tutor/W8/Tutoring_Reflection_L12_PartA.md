<!-- AI prompt
I just learned Searching and Sorting (linear search, bisection search, amortized cost of sorting, bubble sort, selection sort, merge sort and their complexity) in today's lecture.

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

**Topic:** Searching and Sorting (MIT 6.0001 Lecture 12)  
**Date:** 2026-10-26  

---

### ① Check My Understanding

* **Questions completed:** 5 / 5
* **Hints requested before answering:** 0 / 5  

| 題號 | 主題 | 我的答案 | 結果 |
| :--- | :--- | :--- | :--- |
| Q1 | 已排序輸入時 `bubble_sort` 外層只跑一次，最佳情況是否為 O(n) | True | ✅ 一次答對 |
| Q2 | `selection_sort` 每個 `suffixSt` 內層是否最多只交換一次 | False | ✅ 一次答對 |
| Q3 | 已排序輸入時 `merge_sort` 是否會提早結束、最佳情況為 O(n) | False | ✅ 一次答對 |
| Q4 | 只搜尋一次時，先排序再二分搜尋是否比線性搜尋有效率 | False | ✅ 一次答對 |
| Q5 | `bubble_sort` 外層 `while` 是否最多執行 n − 1 次 | False | ✅ 一次答對 |

---

### ② My Misconception

**Before: I thought…**  
5 題都一次答對，沒有明顯的誤解。不過原本只想到「每跑一輪，最大值就會冒泡到定位」，所以直覺上覺得 n − 1 輪就夠了。

⸻

**Now: I understand…**  
`bubble_sort` 只能靠「某一輪完全沒有交換」來判斷已經排好。以 `[3, 2, 1]` 為例，第 2 輪結束時已經排好，但還要再跑第 3 輪確認沒交換才會結束，所以最壞情況外層要跑 n 次。這跟 Q1 已排序時只跑一次是同一個機制：結束條件靠的是 `swap`，不是靠計數。

---

### ③ Challenge the AI

**One AI-generated question I challenged:**  
Q2：「在這個 `selection_sort` 中，`suffixSt` 每固定一個值，內層 `for` 迴圈最多只會做一次交換，因為選擇排序的做法是先找出剩下部分的最小值，再把它跟 `L[suffixSt]` 交換一次。」

⸻

**Why?**

* [x] Ambiguous
* [ ] Oversimplified
* [ ] Technically questionable
* [ ] Too easy
* [ ] Other

**Brief explanation:**  
題目沒有講清楚是在問「選擇排序演算法」還是「這段程式碼」。標準的選擇排序每輪確實只交換一次，照概念回答就是 True；但 `code.txt` 的寫法只要遇到更小的值就交換，針對程式碼答案是 False。題目裡還附了一段「看起來正確」的理由，懂演算法但沒仔細讀程式碼的人很容易被誤導。這題測到的是有沒有發現程式碼跟課本不一樣，不是對選擇排序的理解。（題號是採用 AI 建議的 Q2。）

**改寫建議：**  

> 已知以下程式碼：
> ```python
> def selection_sort(L):
>     suffixSt = 0
>     while suffixSt != len(L):
>         for i in range(suffixSt, len(L)):
>             if L[i] < L[suffixSt]:
>                 L[suffixSt], L[i] = L[i], L[suffixSt]
>         suffixSt += 1
> ```
> 對 `L = [5, 4, 3]` 呼叫 `selection_sort(L)`，在 `suffixSt = 0` 那一輪，內層 `for` 只會交換一次。（答案：False）

---

### ④ One-Minute Reflection

**One thing I am still unsure about:**  
沒有。

⸻
