<!-- AI prompt
I just learned Understanding Program Efficiency (Part 2) in today's lecture.

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

**Topic:** Understanding Program Efficiency, Part 2 (MIT 6.0001 Lecture 11)  
**Date:** 2026-10-19  

---

### ① Check My Understanding

* **Questions completed:** 5 / 5
* **Answers revised after AI hints:** 0 / 5  

| 題號 | 主題 | 我的答案 | 結果 |
| :--- | :--- | :--- | :--- |
| Q1 | 每次遞迴傳入切片的 `bisect_search1` 是否和 `bisect_search2` 一樣是 O(log n) | False | ✅ 一次答對 |
| Q2 | `genSubsets` 每層只遞迴一次，是否最多為 O(n²) | False | ✅ 一次答對 |
| Q3 | `f(n//2) + f(n//2)` 有兩個遞迴分支，是否和 `fib` 一樣是 O(2ⁿ) | False | ✅ 一次答對 |
| Q4 | 以整數值 `i` 為問題大小，`digit_sum(i)` 是否為 O(i) | False | ✅ 一次答對 |
| Q5 | 每次切掉一個元素的 `sum_list` 總複製成本是否和 `bisect_search1` 一樣是 O(n) | False | ✅ 一次答對 |

---

### ② My Misconception

**Before: I thought…**  
我知道切片會複製 list、會增加成本，但沒有仔細區分**每次縮小多少**對總成本的影響，容易以為「有切片複製」的遞迴函式，總複製成本都差不多。

⸻

**Now: I understand…**  
比較 Q1 與 Q5 後，我理解到切片的總成本取決於每次縮小的方式：

* **每次減半**（`bisect_search1`）：n/2 + n/4 + n/8 + … ≈ n，是等比級數，總複製成本 **O(n)**。
* **每次減 1**（`sum_list`）：(n-1) + (n-2) + … + 1 = n(n-1)/2，是等差級數，總複製成本 **O(n²)**。
* 同樣的道理也適用於遞迴呼叫樹（Q3）：分支數 × 深度決定呼叫總數。`f(n//2) + f(n//2)` 深度只有 log n，總呼叫數約 n，是 **O(n)**；`fib(n-1) + fib(n-2)` 深度約 n，才是 **O(2ⁿ)**。

---

### ③ Challenge the AI

**One AI-generated question I challenged:**  
Q4：「`digit_sum` 只有一層 `for` 迴圈，每個字元做常數時間的工作，所以若以輸入的整數 `i` 作為問題大小，它的時間複雜度是 O(i)；也就是說，`i` 從 1,000 變成 1,000,000（放大 1000 倍）時，迴圈次數也會大約放大 1000 倍。」

```python
def digit_sum(i):
    total = 0
    for c in str(i):
        total += int(c)
    return total
```

⸻

**Why?**

* [ ] Ambiguous
* [ ] Oversimplified
* [ ] Technically questionable
* [ ] Too easy
* [x] Other: 題目敘述不完整

**Brief explanation:**  
題目開頭提到「講義的 `intToStr` 用 `i //= 10` 逐位處理」，要我拿 `digit_sum` 跟它比較，卻沒有附上 `intToStr` 的程式碼，只能憑記憶作答，比較基準不清楚。此外，題目說「每個字元做常數時間的工作」，卻沒有說明迴圈開始前 `str(i)` 轉換本身的成本，這個轉換同樣需要逐位處理。

**改寫建議：**  
把兩段程式碼都放進題目：

```python
def intToStr(i):
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i % 10] + result
        i = i // 10
    return result

def digit_sum(i):
    total = 0
    for c in str(i):
        total += int(c)
    return total
```

> 以整數值 `i` 作為問題大小，並假設 `str(i)` 的成本與位數成正比。`intToStr` 用 `while` 迴圈逐位處理，`digit_sum` 用 `for` 迴圈逐字元處理，兩者的時間複雜度都是 O(log i)。（答案：True）

---

### ④ One-Minute Reflection

**One thing I am still unsure about:**  
O(n log n) 是怎麼來的？

AI 說明後的理解：

* 延續 Q3 的遞迴關係比較：
  * T(n) = 2T(n/2) + **c** → 每次拆兩半，但每次呼叫只做常數工作 → **O(n)**
  * T(n) = 2T(n/2) + **n** → 每次拆兩半，且**每一層的總工作都是 n** → 每層 n × 共 log n 層 → **O(n log n)**
* 典型例子：merge sort，每層要把所有元素合併一次（共 n），總共 log n 層。
* 成長速度（n = 1,000,000）：O(n) 約 10⁶、O(n log n) 約 2×10⁷、O(n²) 約 10¹²。O(n log n) 只比 O(n) 多約 20 倍，但比 O(n²) 快約 5 萬倍。

小檢查：

```python
def g(L):
    if len(L) <= 1:
        return 1
    mid = len(L) // 2
    return g(L[:mid]) + g(L[mid:])
```

我回答：每一層所有切片加起來的總複製成本是 O(n)，共 log n 層，所以 `g` 是 O(n log n)。和 Q3 的 `f` 結構相同，差別在於多了切片，讓每層的工作從常數變成 n。✅

**下一步想釐清：**  
merge sort 的 `merge` 實際怎麼在 O(n) 內完成，以及其他排序演算法（例如 selection sort、bubble sort）為什麼是 O(n²)。

⸻
