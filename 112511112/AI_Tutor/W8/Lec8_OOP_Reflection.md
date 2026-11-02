# Name: 朱昱瑋
Date: ____________________
Topic: OOP、Class、Operator Overloading (__add__)、String Representation (__str__)

## 1. Today’s Challenge

Core concept from today’s OCW lecture:

- Class 設計
- Instance Attributes
- Methods
- Operator Overloading (`__add__`)
- String Representation (`__str__`)
- Object / Instance 與 Reference 的概念

---

AI-generated coding challenge title:

**Library Book Tracker**

---

## 2. My Initial Approach — Before AI Help

Before asking AI for hints, briefly describe how you planned to solve the problem.

### My approach:

建立一個 `book` 類別，使用 `title` 與 `b_c` 紀錄書名及借閱次數。

我知道需要利用 `__add__()` 讓兩本書可以使用 `+` 相加，並利用 `__str__()` 客製化輸出格式。另外建立 `popular()` 方法判斷借閱次數是否大於等於 100。

---

## 3. AI Tutor Help

Did you ask the AI Tutor for help?

☐ No — I solved it independently

☑ Yes — I received one or more hints

### The most useful hint/question from AI was:

為什麼 `__str__()` 不能直接回傳：

```python
(self.title, '(', self.b_c, ')')
```

以及 Python 為什麼要求 `__str__()` 必須回傳字串。

### It helped me realize that:

- `__str__()` 必須回傳 `str` 型態。
- Tuple 與 String 是不同型態。
- `print(obj)` 會自動呼叫 `obj.__str__()`。
- 若沒有定義 `__str__()`，物件通常會顯示類似：

```text
<__main__.book object at 0x...>
```

---

## 4. My Revision

Did you change your approach or code after interacting with AI?

☐ No

☑ Yes

### What did you change, and why?

1. 將 `_init_` 改成 `__init__`。
2. 將 `_add_` 改成 `__add__`。
3. 將 `_str_` 改成 `__str__`。
4. 修正 `popular()` 缺少 `self` 的問題。
5. 將書名相加改為：

```python
self.title + '&' + other.title
```

以符合題目要求。
6. 理解 `__str__()` 必須回傳字串，而非 tuple。

---

## 5. Verification

### My final program:

☑ Passed the provided examples

☑ Passed additional edge cases

☐ Still has unresolved problems

### One edge case I tested:

Input:

```python
a = book('History', 99)
print(a.popular())
```

Expected output:

```text
False
```

Actual output:

```text
False
```

另一個測試：

```python
a = book('A',10)
b = book('B',20)
c = book('C',30)

print((a+b)+c)
```

Expected output:

```text
A&B&C(60)
```

Actual output:

```text
A&B&C(60)
```

---

## 6. One-Minute Reflection

### What idea from the OCW lecture did you transfer to this new problem?

我將 Lec8 中的 Operator Overloading、Class Design、Instance Attributes 與 `__str__()` 的概念轉移到新的 Book 類別設計。

尤其是：

```python
__add__
```

讓物件能使用 `+` 運算。

以及：

```python
__str__
```

控制物件被印出時的格式。

---

### One thing I understand better now:

- `print(obj)` 與 `str(obj)` 都會呼叫 `obj.__str__()`。
- `__str__()` 必須回傳字串。
- `a+b` 本質上是在呼叫：

```python
a.__add__(b)
```

- `a`、`b`、`c` 可以指向不同的 instance。

---

### One thing I am still unsure about:

- `__str__()` 與 `__repr__()` 的差異。
- Python 物件預設顯示方式的實作細節。
- 特殊方法（magic methods）還有哪些常見應用。
