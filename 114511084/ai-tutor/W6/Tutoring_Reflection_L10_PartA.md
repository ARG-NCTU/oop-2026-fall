<!-- AI prompt
I just learned Understanding Program Efficiency (Part 1) in today's lecture.

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

**Topic:** Understanding Program Efficiency, Part 1 (MIT 6.0001 Lecture 10)  
**Date:** 2026-10-12  

---

### ① Check My Understanding

* **Questions completed:** 5 / 5
* **Answers revised after AI hints:** 0 / 5  

| 題號 | 主題 | 我的答案 | 結果 |
| :--- | :--- | :--- | :--- |
| Q1 | 在同一台電腦用 `time.time()` 計時，是否是比較演算法效率最可靠的方法 | False | ✅ 一次答對 |
| Q2 | O(n) 的 `1000n + 5` 是否在任何 n 下都比 O(n²) 的 `n²` 快 | False | ✅ 一次答對 |
| Q3 | 兩層巢狀迴圈（內層固定 `range(100)`）是否為 O(n²) | False | ✅ 一次答對 |
| Q4 | 只有一層 `for` 但內含 `x in L2`（list）的函式是否為 O(n) | False | ✅ 一次答對 |
| Q5 | O(n) + O(n²) 的函式，n 從 1000 變 2000 時執行時間是否約變 4 倍 | True | ✅ 一次答對 |

---

### ② My Misconception

**Before: I thought…**  
我知道 Big-O 會忽略常數，也知道 O(n) 比 O(n²) 好，但沒有具體想過這個結論在**什麼輸入大小**下才成立，容易把「O(n) 比較好」當成任何情況都適用的規則。

⸻

**Now: I understand…**  
經過 Q2 的計算，我理解到：

* `1000n + 5` 與 `n²` 的交叉點約在 n = 1000：n ≤ 1000 時 `n²` 反而比較小（例如 n = 1000 時，1,000,000 < 1,000,005），n ≥ 1001 之後 O(n) 才開始領先。
* Big-O 描述的是 **n 很大時的成長趨勢**，常數係數在小輸入時仍可能主導實際執行時間。
* 同理，Q1 中即使在同一台電腦上計時，也只反映**特定輸入與特定實作**的結果，無法說明輸入變大時的成長方式。

---

### ③ Challenge the AI

**One AI-generated question I challenged:**  
Q4：「假設 `L1` 和 `L2` 都是長度 n 的 list。這個函式只有一層 `for` 迴圈，而且找到共同元素就會提早 `return`，所以它的時間複雜度是 O(n)。」

```python
def has_common(L1, L2):
    for x in L1:
        if x in L2:
            return True
    return False
```

⸻

**Why?**

* [ ] Ambiguous
* [ ] Oversimplified
* [x] Technically questionable
* [ ] Too easy
* [ ] Other: 

**Brief explanation:**  
題目只說「時間複雜度是 O(n)」，沒有說明是**最壞情況**；若第一個元素就配對成功，最佳情況其實是 O(1)，判斷依據不夠明確。此外這題和 Q3 測的是同一個觀念（不能只看迴圈層數判斷複雜度，只是方向相反），內容重複。

**改寫建議：**  
改測 list 與 set 的 `in` 成本差異：

```python
def has_common(L1, L2):
    S = set(L2)
    for x in L1:
        if x in S:
            return True
    return False
```

> 假設 `L1`、`L2` 長度都是 n。在最壞情況（沒有共同元素）下，把 `L2` 先轉成 `set` 後，雖然 `set(L2)` 本身要花 O(n)，但整個函式的時間複雜度會從 O(n²) 降到 O(n)。（答案：True）

這樣必須同時考慮轉換成本 O(n)、`set` 的 `in` 平均 O(1)，以及加法法則 O(n) + O(n) = O(n)，測到 Q3 沒有涵蓋的觀念。

---

### ④ One-Minute Reflection

**One thing I am still unsure about:**  
O(log n) 要怎麼判斷？

AI 說明後的理解：

* 關鍵是看控制迴圈的變數**每一輪怎麼變**：
  * 加減常數（`i -= 1`、`i -= 2`）→ 約 n / c 次 → **O(n)**
  * 乘除常數（`i //= 2`、`i *= 2`）→ 約 log n 次 → **O(log n)**
* 直覺：n = 1,000,000 時每次減半約 20 次就到 1（2²⁰ ≈ 1,000,000），輸入變 1000 倍，次數只多約 10 次。
* 常見例子：binary search（每次排除一半範圍）、計算一個數有幾位數（每次 `// 10`）。

小檢查：

```python
def h1(n):
    count = 0
    i = n
    while i > 1:
        i = i // 2
        count += 1
    return count

def h2(n):
    count = 0
    for j in range(n):
        i = n
        while i > 1:
            i = i // 2
            count += 1
    return count
```

我回答 `h1(16)` 回傳 `4`（16 → 8 → 4 → 2 → 1），`h1` 是 O(log n)；`h2` 外層 n 次、每次內層 log n 次，是 O(n log n)。✅

**下一步想釐清：**  
O(n log n) 在實際演算法中出現在哪裡（例如排序），以及它和 O(n)、O(n²) 的成長速度差距有多大。

⸻
