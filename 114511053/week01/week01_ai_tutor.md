# Week 1 AI Tutor Learning Record

- Student ID: 114511053
- Week: 1
- Topic: Introduction / Tuples, Lists, Aliasing, Mutability, and Cloning
- Original Course Date: 2026-09-07
- Make-up Review Date: 2026-10-06

---

# Part A — Concept Review

## 1. Check My Understanding

這次重新複習 Week 1，完成了 5 題 True / False 題目。

### Question 1 — Aliasing and Mutability

```python
a = [1, 2, 3]
b = a
b[0] = 9
```

Statement:

> 執行完之後，`a` 仍然是 `[1, 2, 3]`，因為程式只透過變數 `b` 修改資料。

My answer: **False**

Reason:

`b = a` 不會複製一份新的 list，而是讓 `a` 和 `b` 指向同一個 list object。

因此：

```python
b[0] = 9
```

是在修改兩個變數共同指向的 object。

最後：

```python
a == [9, 2, 3]
b == [9, 2, 3]
```

---

### Question 2 — Cloning

```python
a = [1, 2, 3]
b = a[:]
b.append(4)
```

Statement:

> 執行完之後，`a` 和 `b` 都會變成 `[1, 2, 3, 4]`。

My answer: **False**

Reason:

`b = a[:]` 會建立新的外層 list object。

所以：

```python
a == [1, 2, 3]
b == [1, 2, 3, 4]
```

`b.append(4)` 只修改 `b` 所指向的 list。

---

### Question 3 — Nested List and Shallow Copy

```python
a = [[1, 2], [3, 4]]
b = a[:]

b[0].append(5)
```

Statement:

> `a` 不會受到影響，因為 `b = a[:]` 已經建立新的 list。

My answer: **False**

Reason:

`b = a[:]` 只複製最外層的 list。

`a[0]` 和 `b[0]` 仍然指向同一個 inner list object。

所以：

```python
a == [[1, 2, 5], [3, 4]]
b == [[1, 2, 5], [3, 4]]
```

這也讓我更清楚 `a[:]` 是 shallow copy，而不是 deep copy。

---

### Question 4 — Mutation vs. Rebinding in Functions

```python
def f(L):
    L.append(4)
    L = [9, 9]

a = [1, 2, 3]
f(a)
```

Statement:

> 執行完之後，`a` 會變成 `[9, 9]`。

My answer: **False**

Reason:

```python
L.append(4)
```

會 mutate `L` 原本指向的 list，因此 caller 的 `a` 也會變成：

```python
[1, 2, 3, 4]
```

但是：

```python
L = [9, 9]
```

只是讓 function 裡面的 local variable `L` 重新指向新的 object。

它不會改變外面的 `a` 指向哪個 object。

最後：

```python
a == [1, 2, 3, 4]
```

---

### Question 5 — `sort()` and Return Value

```python
a = [3, 1, 2]
b = a.sort()
```

Statement:

> `a == [1, 2, 3]` 且 `b == [1, 2, 3]`。

My answer: **False**

Reason:

`a.sort()` 會直接 mutate 原本的 `a`：

```python
a == [1, 2, 3]
```

但是 `sort()` 的 return value 是：

```python
None
```

所以：

```python
b is None
```

這和 `sorted(a)` 不一樣。

`sorted(a)` 會建立並回傳一個新的 sorted list，而不修改原本的 list。

---

## 2. My Misconception

在 Coding Challenge 一開始，我看到：

```python
nums = [x for x in nums if x != target]
```

時，我原本認為它不符合題目要求的原因，是「在迴圈執行時修改 `nums`，可能影響 index 或邊界」。

後來我發現真正的問題不是迴圈。

真正的問題是：

```python
nums = new_list
```

屬於 **rebinding**。

它只是讓 function 裡的 local variable `nums` 指向另一個新的 list object，並沒有修改 caller 原本傳進來的 list。

如果題目要求直接修改原本的 object，可以使用：

```python
nums[:] = new_list
```

這是 slice assignment，會 mutate 原本的 list object。

因此現在我會先區分：

- variable 被重新綁定到另一個 object
- object 本身被修改

而不是只看變數名稱有沒有改變。

---

## 3. Challenge the AI

AI statement:

> Using `a[:]` creates a completely independent copy of `a`, so later changes to either list cannot affect the other.

我認為這個說法是：

**Technically incomplete / oversimplified**

原因是：

```python
a[:]
```

建立的是 **shallow copy**，而不是 deep copy。

新的 outer list 和原本的 outer list 是兩個不同的 object，但是裡面的元素仍然可能 reference 相同的 object。

例如：

```python
a = [[1, 2], [3, 4]]
b = a[:]

b[0].append(5)
```

這時 `a[0]` 和 `b[0]` 指向同一個 mutable inner list，因此修改其中一邊會影響另一邊觀察到的內容。

所以更精確的說法應該是：

> `a[:]` creates a new outer list, but the elements inside are still shallow-copied references. If mutable nested objects are shared, changes to those objects may be visible through both lists.

---

## 4. One-Minute Reflection

這次複習後，我對以下概念比較清楚：

- aliasing
- shallow copy
- mutability
- mutation vs. rebinding
- function argument 和 mutable object
- `sort()` vs. `sorted()`
- slice assignment

我以前看到：

```python
nums[:]
```

主要只知道它可以用來複製 list。

這次 Coding Challenge 讓我第一次真正理解：

```python
copy = nums[:]
```

和：

```python
nums[:] = new_list
```

雖然都有 `[:]`，但是因為一個出現在 assignment 右側、一個出現在左側，所以行為不同。

右側的 slicing 會建立新的 list。

左側的 slice assignment 則會修改原本的 list object。

目前我還比較不熟的是 **資料結構與 Big-O time complexity**。

例如這次我一開始不知道，為什麼在 Python list 中重複從中間 `pop()`，worst case 可能造成 `O(n²)` 的時間複雜度。

之後希望在 Coding Challenge 中同時練習：

- correctness
- edge cases
- data structures
- time complexity

---

# Part B — Coding Challenge

## 1. Today's Challenge

### Core Concepts

- List mutability
- Aliasing
- Cloning
- Mutation vs. rebinding
- Slice assignment

### Challenge Title

**Remove Target In Place**

### Problem

實作：

```python
def remove_target(nums, target):
    ...
```

給定一個整數 list `nums` 和整數 `target`。

Requirements:

1. 移除所有等於 `target` 的元素。
2. 保留其他元素原本的順序。
3. 必須直接修改原本傳入的 `nums` object。
4. 如果其他 variable alias 到同一個 `nums`，也必須看到修改。
5. 回傳總共移除了幾個元素。

Example:

```python
nums = [2, 1, 2, 3, 2, 4]

removed = remove_target(nums, 2)

print(nums)
# [1, 3, 4]

print(removed)
# 3
```

---

## 2. My Initial Approach

我的第一個想法是先複製原本的 list：

```python
num = nums[:]
```

再 iterate `num`。

如果找到 target，就對原本的 `nums` 使用 `pop()`。

初版程式：

```python
def remove_target(nums, target):
    num = nums[:]
    count = 0
    ans = 0

    for n in num:
        if n == target:
            nums.pop(count)
            count -= 1
            ans += 1
        count += 1

    return ans
```

我用副本 `num` 進行 iteration，因此不會直接 iterate 一個正在被刪除元素的 list。

真正被修改的是原本的 `nums`。

---

## 3. Verification of Initial Approach

### Test 1 — Consecutive Targets

```python
nums = [2, 2, 2, 3]
print(remove_target(nums, 2), nums)
```

Output:

```text
3 [3]
```

---

### Test 2 — Remove Everything

```python
nums = [2, 2, 2]
print(remove_target(nums, 2), nums)
```

Output:

```text
3 []
```

---

### Test 3 — Target Does Not Exist

```python
nums = [1, 3, 4]
print(remove_target(nums, 2), nums)
```

Output:

```text
0 [1, 3, 4]
```

初版在 correctness 上可以正常運作。

---

## 4. AI Tutor Help

Did I ask the AI Tutor for help?

- [ ] No
- [x] Yes

AI Tutor 沒有直接提供完整 solution，而是提醒我思考兩件事情。

第一個問題是：

```python
nums = new_list
```

和：

```python
nums[:] = new_list
```

有什麼不同？

我原本只知道：

```python
num = nums[:]
```

可以 copy list。

後來才理解：

```python
nums[:] = new_list
```

是 **slice assignment**。

它會修改 `nums` 原本指向的 list object，而不是讓 local variable `nums` 指向另一個 object。

第二個問題是效率。

我的初版會重複執行：

```python
nums.pop(count)
```

Python list 的底層行為類似 dynamic array。

從 list 中間刪除一個元素時，後面的元素可能需要向前移動。

如果大量元素都需要被刪除，總搬移次數可能接近：

```text
(n - 1) + (n - 2) + ... + 1
```

因此 worst-case time complexity 可能是：

```text
O(n²)
```

---

## 5. My Revision

我後來改成先建立需要保留的元素：

```python
new_list = [x for x in nums if x != target]
```

再計算刪除數量：

```python
ans = len(nums) - len(new_list)
```

最後使用：

```python
nums[:] = new_list
```

修改原本的 list object。

Final solution:

```python
def remove_target(nums, target):
    new_list = [x for x in nums if x != target]
    ans = len(nums) - len(new_list)
    nums[:] = new_list
    return ans
```

這個版本避免了反覆從 Python list 中間刪除元素。

---

## 6. Final Verification

### Normal Case

```python
nums = [2, 1, 2, 3, 2, 4]
print(remove_target(nums, 2), nums)
```

Output:

```text
3 [1, 3, 4]
```

---

### Aliasing Test

```python
nums = [2, 1, 2, 3]
alias = nums

removed = remove_target(nums, 2)

print(removed)
print(nums)
print(alias)
print(nums is alias)
```

Output:

```text
2
[1, 3]
[1, 3]
True
```

`nums is alias` 仍然是 `True`。

這表示程式沒有把 `nums` 改成另一個新的 list object，而是真的修改了原本的 list object。

---

## 7. Complexity Analysis

Final solution 中：

```python
new_list = [x for x in nums if x != target]
```

需要走訪原本的 list 一次，因此 time complexity 是：

```text
O(n)
```

接著：

```python
nums[:] = new_list
```

需要把新的內容寫回原本的 list，因此也需要：

```text
O(n)
```

所以總時間可以寫成：

```text
O(n) + O(n)
```

Big-O 會忽略常數，因此整體 time complexity 是：

```text
O(n)
```

因為另外建立了：

```python
new_list
```

所以 additional space complexity 是：

```text
O(n)
```

相比之下，我原本使用多次 `pop()` 的版本，在最差情況下可能需要反覆搬移 list 中後面的元素，因此 worst-case time complexity 可能到：

```text
O(n²)
```

這次也讓我開始理解 **time-space trade-off**：

新的版本使用額外的 `O(n)` 空間，換取較好的 `O(n)` 執行時間。

---

## 8. Coding Challenge Reflection

這一題把 Week 1 的 lecture concepts 轉移到實際 coding problem。

最重要的概念不是單純把 target 刪掉，而是題目要求：

> 修改 caller 傳入的原本 list object。

因此：

```python
nums = new_list
```

雖然能讓 function 裡面的 `nums` 得到正確內容，但不符合題目要求，因為這只是 rebinding。

最後改成：

```python
nums[:] = new_list
```

才真正完成對原本 list object 的 mutation。

另外，我原本的 `pop()` 版本在 correctness 上沒有問題，但分析資料結構後才發現可能存在 `O(n²)` 的效率問題。

這讓我開始理解：

> 程式可以「答案正確」，但不代表它就是好的演算法。

之後希望除了寫出正確答案，也能逐漸學會分析：

- 使用了什麼資料結構
- 每種 operation 的成本
- time complexity
- space complexity
- 是否有更有效率的解法

---

# Week 1 Summary

這週複習後，我目前比較能分辨：

```text
assignment
vs.
mutation
```

以及：

```text
aliasing
vs.
cloning
```

也可以理解：

```python
b = a
```

和：

```python
b = a[:]
```

不一樣。

前者讓兩個變數 reference 同一個 list object。

後者會建立一個新的 outer list，但仍然只是 shallow copy。

另外，我也學到：

```python
nums[:] = new_list
```

是 slice assignment，會修改原本的 list object。

目前我最需要繼續加強的部分是：

```text
Data Structures
+
Time Complexity
+
Space Complexity
```

之後的 Coding Challenge 希望繼續把這三個部分一起加入練習。