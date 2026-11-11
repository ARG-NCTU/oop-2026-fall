# MIT 6.0002 Lecture 1 Reflection Log

Topic: Introduction and Optimization Problems  
Date: 2026-11-10

---

## ① Check My Understanding

Questions completed: 5 / 5

Answers revised after AI hints: 0 / 5

---

## ② My Misconceptions

* **Before: I thought…**  
  對貪婪演算法（Greedy Algorithm）在不同類型背包問題中的表現邊界不太確定，特別是 0/1 背包與連續背包問題（Continuous Knapsack Problem）的差異。

* **Now: I understand…**  
  連續背包問題因為物品具備「可任意分割性」，不會產生空間浪費，因此每一步挑選最高 CP 值（Density）的貪婪策略恆等於全域最佳解（Globally Optimal Solution）；而 0/1 背包問題因物品不可切割，區域最佳選擇（Locally Optimal Choices）隨時可能錯失全域最佳解。

---

## ③ Challenge the AI

One AI-generated question I challenged:

> 第 4 題（關於單次耗時 $O(N)$ 的 `keyFunction` 對整體 `greedy` 演算法時間複雜度的影響）

Why?

* [ ] Ambiguous
* [ ] Oversimplified
* [ ] Technically questionable
* [x] Too easy
* [ ] Other: __________

**Brief explanation:**  
時間複雜度的「主導項（Dominant Term）」概念較為基礎且直觀，該題轉折較少，難度偏低。

---

## ④ One-Minute Reflection

**One thing I am still unsure about:**  
無（對於 Lecture 1 的 0/1 與連續背包模型、冪集暴力法複雜度 $O(2^N)$、貪婪演算法與 `lambda` 鍵值排序運作機制均已清楚掌握）。

---

# MIT 6.0002 Lecture 1 Coding Challenge Reflection Log

Name: User  
Date: 2026-11-10  
Topic: Flexible Greedy Tasks (`flexible_greedy_tasks`)

---

## 1. Today’s Challenge

* **Core concept from today’s OCW lecture:**  
  最佳化模型（Optimization Model）、0/1 背包問題抽象、彈性貪婪演算法（Flexible Greedy Algorithm）架構與 Python `lambda` 匿名鍵值函式應用。

* **AI-generated coding challenge title:**  
  雲端伺服器任務調度器（Cloud Task Allocation via Flexible Greedy）

---

## 2. My Initial Approach — Before AI Help

Before asking AI for hints, briefly describe how you planned to solve the problem.

**My approach:**  
設計 `Task` 類別封裝任務屬性（`name`, `profit`, `cpu`），並實作 `flexible_greedy_tasks` 函式。使用 Python 的 `sorted(tasks, key=key_function, reverse=True)` 對任務進行排序，再透過 `for` 迴圈檢查 CPU 剩餘容量逐一放入任務。使用 `lambda` 定義多種衡量指標（如 `lambda Task: Task.profit`）。

---

## 3. AI Tutor Help

Did you ask the AI Tutor for help?

* [ ] No — I solved it independently
* [x] Yes — I received one or more hints

* **The most useful hint/question from AI was:**  
  1. 釐清 `lambda` 計算出 Key 值後，搭配 `sorted(..., reverse=True)` 是將 Key 值由高到低排序，因此 `lambda t: 1 / t.cpu` 效果等同於「最低 CPU 消耗優先」。
  2. 釐清 Python 中建立與回傳 Tuple 的核心是「逗號 `,`」而非外層括號 `()`，並指出類別宣告與屬性對接的語法錯誤。

* **It helped me realize that:**  
  Python 語法中的元組打包與解包（Packing / Unpacking）機制，以及類別 `__init__` 建構子的標準定義方式。

---

## 4. My Revision

Did you change your approach or code after interacting with AI?

* [ ] No
* [x] Yes

**What did you change, and why?**  
1. 補全 `class Task:` 宣告與 `__init__` 建構子，統一屬性名稱為 `self.cpu`。
2. 修正 `Task(name: str...)` 偽程式碼寫法為標準 Python 類別實體化語法。
3. 規範 `lambda` 的區域變數命名為小寫 `t`，提高程式碼可讀性。

---

## 5. Verification

My final program:

* [x] Passed the provided examples
* [x] Passed additional edge cases
* [ ] Still has unresolved problems

**One edge case I tested:**

* **Input:** `tasks = [Task("Task_A", 100, 10), Task("Task_B", 90, 5), Task("Task_C", 90, 5)]`, `max_cpu = 10`, `strategy_C` (Highest Density)
* **Expected output:** Selected: `[Task_B, Task_C]`, Total Profit: `180.0`, Total CPU: `10`
* **Actual output:** Selected: `[Task_B, Task_C]`, Total Profit: `180.0`, Total CPU: `10`

---

## 6. One-Minute Reflection

* **What idea from the OCW lecture did you transfer to this new problem?**  
  將講義中的 `Food` 類別封裝與 `greedy(items, maxCost, keyFunction)` 彈性貪婪演算法架構完整轉移至「雲端任務分配」場景中。

* **One thing I understand better now:**  
  貪婪演算法整體時間複雜度為 $O(N \log N)$（排序 $O(N \log N)$ 加上單次走訪 $O(N)$），且在 Python 中傳遞 `return a, b, c` 即可利用逗號完成 Tuple 打包與回傳。

* **One thing I am still unsure about:**  
  在 0/1 背包問題中，當貪婪演算法無法保證全域最佳解、而暴力法又需耗時 $O(2^N)$ 時，實務上如何透過搜尋樹與動態規劃（Dynamic Programming）高效求得全域最佳解。

---

## 7. Final Python Implementation Code

```python
class Task:
    def __init__(self, name: str, profit: float, cpu: int):
        self.name = name
        self.profit = profit
        self.cpu = cpu

    def get_density(self) -> float:
        return self.profit / self.cpu

    def __str__(self):
        return f"{self.name}: <Profit: {self.profit}, CPU: {self.cpu}>"

def flexible_greedy_tasks(tasks, max_cpu, key_function):
    sorted_tasks = sorted(tasks, key=key_function, reverse=True)
    
    total_profit = 0.0
    total_cpu = 0
    selected_tasks = []

    for task in sorted_tasks:
        if total_cpu + task.cpu <= max_cpu:
            selected_tasks.append(task)
            total_profit += task.profit
            total_cpu += task.cpu

    return selected_tasks, total_profit, total_cpu
```