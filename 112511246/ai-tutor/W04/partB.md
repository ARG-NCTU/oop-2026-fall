# Week 4 — AI Tutor Learning Record (Part B)

- 學號：112511246
- Name：張中愷
- Date：2026-10-14
- Topic：Lecture 8 — 物件導向程式設計（Object Oriented Programming）
- 程式檔：[w4.py](w4.py)
- 格式來源：[AI Tutor for AOOP 2026](https://github.com/ARG-NCTU/oop-python-nycu/blob/main/ai-tutor-2026.md)

## 1. Today's Challenge

**Core concept from today's OCW lecture:**

用 class 自己定義一種新的型別：`__init__` 和 `self` 存下物件的資料，方法定義物件能做的事，特殊方法（`__str__`、`__add__`、`__eq__`）讓自訂的物件可以用 `print`、`+`、`==`。課堂的 `Fraction` 就是自己做一個「分數」型別，`__add__` 回傳一個新的 Fraction。

**AI-generated coding challenge title:** Duration（時間長度）

### 題目

做一個 class `Duration`，代表「幾分幾秒」：

| 名稱 | 要做什麼 |
|---|---|
| `__init__(self, minutes, seconds)` | 存下分鐘和秒數 |
| `to_seconds(self)` | 回傳總秒數，例如 3 分 5 秒 → `185` |
| `__str__(self)` | 印成 `分:秒`，秒數固定兩位數，例如 `3:05` |
| `__add__(self, other)` | 兩段時間相加，回傳新的 Duration，秒數超過 60 要進位 |
| `__eq__(self, other)` | 總秒數相同就算相等 |

- 限制：`minutes`、`seconds` 為非負整數；建立時 `seconds` 在 0～59；相加後的結果秒數也必須在 0～59。

| 範例 | 程式 | 輸出 |
|---|---|---|
| 1 | `a = Duration(3, 5)`；`print(a)`；`print(a.to_seconds())` | `3:05`、`185` |
| 2 | `b = Duration(1, 58)`；`print(a + b)`；`print(a)` | `5:03`、`3:05`（a 不變） |
| 3 | `print(a + b == Duration(5, 3))`；`print(a == b)` | `True`、`False` |

## 2. My Initial Approach — Before AI Help

`__add__` 先把兩段時間都換成總秒數相加，再用除法換回分和秒。

## 3. AI Tutor Help

- [ ] No — I solved it independently
- [x] Yes — I received one or more hints

**The most useful hint/question from AI was:**

AI 用 303 秒為例，說明一般除法 `303 / 60` 會得到小數 5.05，而要拿到「5 分 3 秒」兩個整數，要用整數除法 `//` 取分鐘、取餘數 `%` 取秒數（303 ÷ 60 = 5 …… 3）。另外提示 `__str__` 的秒數補兩位可以用 W5 Rabbit 用過的 `zfill`，`__eq__` 可以直接用 `to_seconds()` 比較。

**It helped me realize that:**

Python 的 `/` 一定得到小數，跟 C++ 兩個 int 相除不一樣，要整數結果就要用 `//`。而且 class 裡已經寫好的 `to_seconds()` 可以在 `__add__` 和 `__eq__` 裡重複使用，不用再算一次 `分 × 60 + 秒`。

我也問了「限制條件」是不是要自己防呆。AI 說明限制條件是保證輸入一定在這個範圍內，不用自己檢查；真正要我負責的是「相加後的秒數也要在 0～59」，也就是進位。

## 4. My Revision

- [ ] No
- [x] Yes

**What did you change, and why?**

`__str__` 我用 f-string `f"{self.minutes}.{self.seconds:02d}"` 來補兩位數，但分和秒中間放了點 `.`，所以印出 `3.05`，不是題目要求的 `3:05`，三個範例中有三行沒過。原因是我把 AI 解釋除法時的例子 `303 / 60 = 5.05`（5.05 分鐘，小數）看成了時間格式。AI 承認這個例子舉得不好，數字剛好跟「5 分 05 秒」長得很像，並說明 `5.05` 是小數分鐘、`5:03` 才是 5 分 3 秒。我把點改成冒號後，所有範例都通過。

### 最終程式

```python
class Duration:
    def __init__(self, minutes, seconds):
        self.minutes = minutes
        self.seconds = seconds

    def to_seconds(self):
        return self.minutes * 60 + self.seconds

    def __str__(self):
        return f"{self.minutes}:{self.seconds:02d}"

    def __add__(self, other):
        total_sec = self.to_seconds() + other.to_seconds()
        sum_min = total_sec // 60
        sum_sec = total_sec % 60
        return Duration(sum_min, sum_sec)

    def __eq__(self, other):
        return self.to_seconds() == other.to_seconds()
```

## 5. Verification

- [x] Passed the provided examples
- [x] Passed additional edge cases
- [ ] Still has unresolved problems

另外測試的邊界情況：

| 測試 | 輸入 | 預期輸出 | 實際輸出 |
|---|---|---|---|
| 零 | `Duration(0, 0)` | `0:00`，總秒數 `0` | `0:00`，`0` |
| 剛好進位成整分 | `Duration(0, 30) + Duration(0, 30)` | `1:00` | `1:00` |
| 差 1 秒進位 | `Duration(0, 59) + Duration(0, 1)` | `1:00` | `1:00` |
| 兩邊秒數都最大 | `Duration(0, 59) + Duration(0, 59)` | `1:58` | `1:58` |
| 不用進位 | `Duration(2, 10) + Duration(1, 20)` | `3:30` | `3:30` |
| 分鐘很大 | `Duration(120, 45) + Duration(0, 15)` | `121:00` | `121:00` |
| 秒數本來就是兩位數 | `Duration(3, 15)` | `3:15` | `3:15` |
| 加上零 | `Duration(4, 7) + Duration(0, 0)` | `4:07` | `4:07` |
| 組合不同、總秒數相同 | `(Duration(1, 0) + Duration(0, 30)) == (Duration(0, 59) + Duration(0, 31))` | `True` | `True` |
| 相加後 a、b 不變，結果是新物件 | `a = Duration(3, 5)`，`b = Duration(1, 58)`，`a + b` | a、b 不變 | a、b 不變，`a + b` 是新物件 |

**One edge case I tested:**

- Input：`print(Duration(0, 59) + Duration(0, 1))`
- Expected output：`1:00`
- Actual output：`1:00`

剛好湊滿 60 秒時，`60 // 60 = 1`、`60 % 60 = 0`，正確進位成 1 分 0 秒，秒數也補成 `00`。

### Why my solution works

`__add__` 先用 `to_seconds()` 把兩段時間換成總秒數相加，再用 `//` 取分鐘、`%` 取剩下的秒數，所以秒數一定在 0～59，進位自動完成。它回傳的是新的 Duration，沒有修改 `self` 或 `other`，所以 `a + b` 之後 a 不變。`__eq__` 比較總秒數，所以只要時間長度一樣就相等。

### Time complexity

沒有迴圈，每個方法都只做固定幾次加減乘除，跟數字大小無關，所以每個方法都是 **O(1)**。

## 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**

class 和特殊方法。照課堂 Fraction 的做法，自己定義一個 Duration 型別，用 `__str__` 決定印出的樣子、`__add__` 回傳新的物件、`__eq__` 定義什麼叫相等。

**One thing I understand better now:**

`__add__` 要回傳新的物件才不會改到原本的值；class 裡寫好的方法（`to_seconds()`）可以在其他方法裡用 `self.` 重複呼叫。另外 `/`、`//`、`%` 的差別：`/` 得到小數，`//` 只留整數，`%` 是餘數。

**One thing I am still unsure about:**

我在 `__str__` 用的是 f-string 的 `:02d` 來補兩位數，效果跟 `zfill(2)` 一樣，但 f-string 冒號後面還能寫哪些格式（例如小數要留幾位），我還不清楚。
