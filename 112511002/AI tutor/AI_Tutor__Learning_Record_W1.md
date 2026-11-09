# AI Tutor Learning Record — MIT 6.0001 Lecture 5

**Name:** 劉育麟  
**Date:** 2026/11/09  
**Topic:** Tuples, Lists, Aliasing, Mutability, Cloning

---

# Part A: True or False

## ① Check My Understanding

**Questions completed:** 5 / 5  
**Answers revised after AI hints:** 2 / 5（第 2、4 題）

## ② My Misconception

### Before: I thought…

我原本以為 `b = a[:]` 不只會複製外層 List，也會把內層的 List 一起複製，因此 `a` 和 `b` 應該完全獨立，修改其中一個不會影響另一個。

### Now: I understand…

現在我知道 `a[:]` 只會建立 **shallow copy（淺拷貝）**：外層 List 是新的物件，但其中的元素仍可能參照同一個內層物件。因此，如果 `a[0]` 和 `b[0]` 指向同一個 List，執行 `b[0].append(5)` 時，也會從 `a[0]` 看到新增的 `5`。

## ③ Challenge the AI

### One AI-generated question I challenged:

第 4 題：一邊遍歷 `L`，一邊使用 `L.remove(x)` 刪除偶數的 True/False 題目。

### Why?

- [x] Ambiguous
- [ ] Oversimplified
- [ ] Technically questionable
- [ ] Too easy
- [ ] Other

### Brief explanation:

對題目給定的 `L = [1, 2, 3, 4, 5, 6]`，最終結果確實是 `[1, 3, 5]`。但是題目所給的理由不正確，因為迴圈沒有檢查原本 List 中的所有元素。在刪除元素後，後面的元素會向前移動，但迴圈索引仍繼續增加，因此實際上跳過了 `3` 和 `5`。

如果只判斷最終結果，答案是 True；如果連同「迴圈會依序檢查每個元素」這個理由一起判斷，答案就是 False。我認為這樣的敘述容易讓作答者不清楚判斷範圍，因此有歧義。若將「結果是否正確」和「原因是否正確」拆成兩題，會更清楚。

## ④ One-Minute Reflection

### One thing I am still unsure about:

我還想更熟悉 Tuple 裡面包含可變物件時，**immutability（不可變性）** 的適用範圍。例如：

```python
t = ([1, 2], 3)
```

經過討論後，我知道 `t[0].append(4)` 是合法的，因為它修改的是 `t[0]` 所參照的 List；但 `t[0] = [1, 2, 4]` 不合法，因為這是在嘗試替換 Tuple 的元素。我希望之後能更熟練地區分「修改參照物件的內容」和「重新指定容器內的元素」。

---

# Part B: LeetCode-style Lecture Code Transfer

## 1. Today’s Challenge

### Core concept from today’s OCW lecture:

**List iteration、mutation 與 cloning**。在遍歷 List 時直接刪除其中的元素，可能因為元素往前移動而導致部分元素被跳過。可以先建立副本，遍歷副本並修改原本的 List，避免這個問題。

### AI-generated coding challenge title:

**Remove Blocked Items**

## 2. My Initial Approach — Before AI Help

### My approach:

我原本打算先將 `blocked` 轉成 Set，方便快速判斷某個編號是否被禁止；接著從頭遍歷 `items`，把允許的元素依序放進暫存 List；最後利用整段切片賦值，把暫存結果寫回原本的 `items`。

這個方法可以保留允許元素原本的順序和出現次數，同時修改呼叫者傳入的 List。

## 3. AI Tutor Help

### Did you ask the AI Tutor for help?

- [ ] No — I solved it independently
- [x] Yes — I received one or more hints

### The most useful hint/question from AI was:

AI 提醒我，這次練習需要盡量使用 Lecture 5 已介紹的概念，而我提出的 `set()` 與整段切片賦值並不是這份教材示範的操作。AI 引導我回想課堂中的 `L1_copy = L1[:]`，並思考應該遍歷哪個 List、修改哪個 List，以及如何利用 `in` 和 `remove()` 處理重複元素。

### It helped me realize that:

我發現不必使用 Set 或另外建立結果 List，也能利用 Lecture 5 的 cloning 技巧完成要求。只要遍歷副本、修改原本的 List，就不會因為原 List 被刪除元素而跳過副本中的項目。

## 4. My Revision

### Did you change your approach or code after interacting with AI?

- [ ] No
- [x] Yes

### What did you change, and why?

我改用 `items[:]` 建立原 List 的副本，再遍歷這個副本。每次遇到出現在 `blocked` 中的元素，就對原本的 `items` 呼叫一次 `remove()`。

副本保留每個元素原本的出現次數，所以即使禁止的元素重複出現，也會被逐一移除。由於迴圈讀取的是副本，原 List 的索引即使因刪除而移動，也不會影響迭代順序。

## 5. Verification

### My final program:

```python
def remove_blocked(items, blocked):
    items_copy = items[:]
    for item in items_copy:
        if item in blocked:
            items.remove(item)
```

- [x] Passed the provided examples
- [x] Passed additional edge cases
- [ ] Still has unresolved problems

### One edge case I tested:

**Input:**

```python
items = [1, 1, 1]
blocked = [1]
```

**Expected output:** `[]`  
**Actual output:** `[]`

副本中有三個 `1`，所以迴圈會對原本的 `items` 執行三次 `remove(1)`，最後所有被禁止的元素都會被刪除。

## 6. One-Minute Reflection

### What idea from the OCW lecture did you transfer to this new problem?

我把 Lecture 5 的 **cloning（複製）** 概念應用在 **iteration（迭代）** 和 **mutation（修改）** 的分離：迴圈讀取副本，而刪除動作發生在原本的 List，避免直接修改正在遍歷的 List。

### One thing I understand better now:

我更清楚為什麼遍歷 List 的同時刪除元素可能造成漏檢，也理解如何利用 `[:]` 建立副本來避免這個問題。

這個解法會正確移除全部被禁止的元素：如果某個禁止值在原 List 中出現 `k` 次，副本中就有相同的 `k` 次出現，迴圈因此會對原 List 呼叫 `k` 次 `remove()`，每次刪除一個。其餘元素的相對順序也會保留。

若設 `n = len(items)`、`m = len(blocked)`，複製需要 `O(n)`；使用 `in` 查詢最多花 `O(nm)`；`remove()` 最多執行 `n` 次，且每次可能需要 `O(n)`，因此最壞時間複雜度為 **`O(nm + n²)`**。

### One thing I am still unsure about:

我還想進一步了解：什麼情況適合先複製 List 再修改原 List，什麼情況適合建立新的結果 List；尤其是在必須原地修改資料時，應該如何兼顧正確性與時間複雜度。
