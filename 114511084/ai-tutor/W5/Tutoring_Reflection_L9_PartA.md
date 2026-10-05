<!-- AI prompt
I just learned Python Classes and Inheritance in today's lecture.

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

**Topic:** Python Classes and Inheritance (MIT 6.0001 Lecture 9)  
**Date:** 2026-10-05  

---

### ① Check My Understanding

* **Questions completed:** 5 / 5
* **Answers revised after AI hints:** 1 / 5  

| 題號 | 主題 | 我的答案 | 結果 |
| :--- | :--- | :--- | :--- |
| Q1 | `self.x` 定義的 instance attribute 是否被所有 instance 共用 | False | ✅ 一次答對 |
| Q2 | 在 method 中寫 `self.tag = 100` 是否會修改 class variable `Rabbit.tag` | False | ✅ T/F 答對，但推算數值時經提示後修正 |
| Q3 | 定義在 `Animal` 的 `introduce()` 中呼叫 `self.speak()`，會執行哪個版本 | False | ✅ 一次答對 |
| Q4 | `Student.__init__` 沒呼叫 `Person.__init__` 時，是否仍擁有 `name`、`age` | False | ✅ 一次答對 |
| Q5 | 直接存取 `a.age` 與透過 `a.get_age()` 是否等價 | False | ✅ 一次答對 |

---

### ② My Misconception

**Before: I thought…**  
在 Q2 中，我知道 `r1.tag = 100` 不會改到 class variable，但在推算以下程式的結果時：

```python
r1 = Rabbit(2)
r2 = Rabbit(3)
r1.tag = 100
```

我原本回答 `r2.tag` 是 `3`、`Rabbit.tag` 是 `4`，把 `r2.tag` 和 `Rabbit.tag` 當成兩個獨立的值，好像每個 instance 都有一份 class variable 的副本。

⸻

**Now: I understand…**  
經過 AI 提示（Python 讀取 attribute 的查找順序：instance → class → parent class），並逐步追蹤 `Rabbit.tag` 的變化（1 → 2 → 3 → 3）後，我理解到：

* `r2` 自己沒有 `tag`，讀取 `r2.tag` 時會往上找到 `Rabbit.tag`，兩者是**同一份值**，所以都是 `3`。
* 對 `self.tag` **賦值**不會修改 class variable，而是在該 instance 身上建立一個同名 attribute，把 class variable **遮蔽（shadow）** 起來，且只對那個 instance 有效。
* 這也是為什麼 Lecture 9 中計數器要寫 `Rabbit.tag += 1`，而不是 `self.tag += 1`。

---

### ③ Challenge the AI

**One AI-generated question I challenged:**  
Q5：「在 Python 裡，直接存取 `a.age`（寫法 A）和透過 `a.get_age()`（寫法 B）本質上是等價的。只要 class 本身改得正確，外部程式碼不管用哪一種寫法都不會壞掉。」

⸻

**Why?**

* [ ] Ambiguous
* [ ] Oversimplified
* [ ] Technically questionable
* [x] Too easy
* [ ] Other: 

**Brief explanation:**  
題目直接秀出改版後的程式碼，`self.age` 明顯被換成 `self.birth_year`，只看表面就能判斷 `a.age` 會壞掉，不需要真正理解 information hiding 的價值，應該改成更全面性的觀念問題。

AI 補充指出這題也有技術爭議：Python 可以用 `@property` 把 `age` 改成計算值，讓 `a.age` 不會壞掉，所以「直接存取 attribute 一定比較脆弱」並不絕對成立。

**改寫建議：**  
> Python 不會阻止外部直接存取 `a.age`，而且可以用 `@property` 事後把 attribute 改成計算值。因此在 Python 中，information hiding 這個設計原則已經沒有意義，class 的作者不需要區分哪些是 interface、哪些是內部實作。（答案：False）

這樣必須理解 information hiding 的重點是「區分對外承諾與內部細節」的設計思維，而不是 getter 這個特定語法。

---

### ④ One-Minute Reflection

**One thing I am still unsure about:**  
多層繼承時，method 的查找順序是怎麼決定的？

AI 說明後的理解：

* **單一繼承鏈**：一條直線往上找，`s 自己 → Student → Person → Animal → object`，找到第一個就停止。
* **多重繼承**：Python 用 MRO（Method Resolution Order，C3 linearization）把繼承圖排成一條線，原則是：
  1. subclass 一定排在 parent 前面
  2. parent 的順序照 class 定義時寫的順序
  3. 共同的祖先排到最後
* 不確定時可用 `ClassName.__mro__` 或 `ClassName.mro()` 直接印出順序。

小檢查：

```python
class A:
    def hello(self): return "A"
class B(A):
    pass  # hello removed
class C(A):
    def hello(self): return "C"
class D(B, C):
    pass

D().hello()  # MRO: D → B → C → A → object
```

我回答 `"C"`，因為 B 找不到後會先找 C，共同祖先 A 最後才找。✅

**下一步想釐清：**  
`super().__init__()` 和 `Animal.__init__(self)` 的差別：`super()` 是照 MRO 找「下一個」class，不一定是直接的 parent。

⸻
