# AI Tutor Learning Record — W5 / MIT 6.0001 Lecture 9

**Name**　劉育麟  
**Date**　2026/10/05（課表日期）  
**OCW Topic**　Python Classes and Inheritance  
**課程教材**　[Lecture 9 投影片，第 16–24 頁](../material/MIT6_0001F16_Lec9.pdf) 與 [lec9_inheritance.py](../material/lec9_inheritance.py)

> 初答、提示後的修正與反思採示範作答。Part B 的互動式 Python 範例列出實際執行結果。

---

# Part A: True or False

## ① Check My Understanding

**Questions completed**　5 / 5　｜　**Answers revised after AI hints**　1 / 5（示範第 2 題）

| 題號 | 判斷題 | 初答 → 定稿 | 理由 |
| --- | --- | --- | --- |
| 1 | 課堂的 `Cat` 沒有寫 `__init__`，建立 `Cat(5)` 後仍可用 `get_age()` 讀到 5。 | T → T | 初始化與讀取年齡的方法都可沿著繼承關係在 `Animal` 找到。 |
| 2 | 若替 `Cat` 新寫一個 `__init__`，即使裡面只指定毛色，Python 也一定會先執行 `Animal.__init__`。 | T → F | 建構時會找到子類別自己的初始化方法。若它需要父類別設定年齡，就得在裡面呼叫父類別的初始化方法。 |
| 3 | 在課堂的 `Person` 中，對 `p.get_friends()` 的回傳值執行 `append("Jo")`，下次讀取時會看到 `"Jo"`。 | T → T | Getter 回傳 `self.friends`，兩邊都能取得同一份串列。 |
| 4 | 每建立一隻 `Rabbit` 都會增加 `Rabbit.tag`，先前所有兔子的 `rid` 也跟著增加。 | F → F | `self.rid` 在建立當下取得整數編號。之後更新類別上的 `tag`，舊實例仍保有原編號。 |
| 5 | 若 `a`、`b` 是兩隻兔子，依課堂的 `Rabbit.__eq__`，`(a + b) == (b + a)` 為真。 | T → T | 加法各產生一隻有雙親的新兔子。比較會檢查兩組雙親的編號，也考慮相反順序。 |

## ② My Misconception

**Before — I thought…**　我以為只要宣告 `class Cat(Animal)`，每次建立貓時就會自動執行兩層的初始化。

**Now — I understand…**　我可以用 `get_age()` 查出差別。若子類別只設定 `self.color`，它仍繼承 `get_age()`，但呼叫時會因缺少 `self.age` 而得到 `AttributeError`。課程中的 `Person` 在自己的 `__init__` 裡明確呼叫 `Animal.__init__(self, age)`，因此有年齡可以讀。

## ③ Challenge the AI

**選題**　第 5 題　｜　**原因**　☒ Oversimplified

「兩隻兔子可以用 `==` 比較雙親」需要限定比較對象。題中的兩個運算結果都有 `parent1` 與 `parent2`。若直接比較兩隻建立時未指定雙親的兔子，課堂程式會嘗試讀取 `None.rid`，進而引發 `AttributeError`。我會把題目拆成「交換雙親順序的兩隻後代會相等嗎？」和「比較兩隻沒有雙親資料的兔子，會發生什麼事？」。

## ④ One-Minute Reflection

我還想釐清「繼承一個方法」對資料有哪些要求。現在我會先看方法實際讀了哪些 `self` 屬性，再回到初始化流程，檢查每種子類別是否都建好了這些欄位。

---

# Part B: LeetCode-style Lecture Code Transfer

## 1. Today’s Challenge

**High Samples and Rising Edges（高電位與上升緣計數）**

同一串數位訊號可以有兩種計數方式。設計 `HighCounter` 逐筆累計值為 `1` 的樣本，再用子類別 `RisingEdgeCounter` 累計相鄰樣本由 `0` 變 `1` 的次數。兩類別共用 `observe(bit)` 和 `count()` 介面，子類別只覆寫判斷條件。

每次輸入保證是整數 `0` 或 `1`。`observe` 回傳處理當筆後的累計值，`count` 回傳目前值。新物件從零開始，第一筆資料沒有前一筆可供比較。各實例能交錯使用。

```pycon
>>> high = HighCounter()
>>> [high.observe(bit) for bit in [1, 1, 0, 1]]
[1, 2, 2, 3]
>>> edge = RisingEdgeCounter()
>>> [edge.observe(bit) for bit in [1, 1, 0, 1]]
[0, 0, 0, 1]
```

## 2. My Initial Approach — Before AI Help

我想在父類別保留「上一筆」與「累計值」，並先把上一筆設成 `0`。每次收到樣本時，先呼叫可覆寫的方法判斷是否計數，再把樣本存起來給下一次使用。

## 3. AI Tutor Help

**示範提示**　如果儀器啟動後只收到一筆 `1`，它真的量到一次從低到高的變化了嗎？

只收到一筆時，可以確定電位是高的，卻無法知道它之前是高或低。若上一筆預設為 `0`，上升緣計數器會多算一次。

## 4. My Revision

我把初始的上一筆改成 `None`。每次都在判斷之後才更新上一筆，即使判斷結果為假也要更新，這樣 `0, 1` 中的 `0` 才能留到下一次比較。

## 5. Verification

**My final program**

```python
class HighCounter:
    def __init__(self):
        self._previous = None
        self._count = 0

    def matches(self, previous, current):
        return current == 1

    def observe(self, bit):
        if self.matches(self._previous, bit):
            self._count += 1
        self._previous = bit
        return self._count

    def count(self):
        return self._count


class RisingEdgeCounter(HighCounter):
    def matches(self, previous, current):
        return previous == 0 and current == 1
```

- [x] Passed the provided examples
- [x] Passed additional edge cases

**邊界測試**　以下依序檢查空紀錄、首次輸入高電位、兩個實例交錯使用，以及同一個實例累計兩次上升緣。

```pycon
>>> a, b = RisingEdgeCounter(), RisingEdgeCounter()
>>> (a.count(), b.count())
(0, 0)
>>> (a.observe(0), b.observe(1), a.observe(1), b.count())
(0, 0, 1, 0)
>>> [a.observe(bit) for bit in [1, 0, 1]]
[1, 1, 2]
```

## 6. One-Minute Reflection

**正確性與複雜度**　每次呼叫前，`_previous` 保存上一筆，`_count` 保存前面已符合規則的次數。`observe` 用舊值和當前輸入判斷一次，再保存這次的值，所以每個樣本或相鄰轉換都恰好判斷一次。單次更新為 `O(1)` 時間，每個實例只使用 `O(1)` 額外空間。

**從講義移用的概念**　`Student.speak()` 讓學生實例對同名方法有自己的行為。本題讓父類別的 `observe` 呼叫 `self.matches`，呼叫端即使一律寫 `counter.observe(1)`，也會套用該物件的計數規則。

**仍想釐清**　若新增「連續三筆為高才觸發」的計數器，單憑前一筆已不足夠。我想練習如何增加子類別自己的狀態，同時沿用既有的計數介面。
