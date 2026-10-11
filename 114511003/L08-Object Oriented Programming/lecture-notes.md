# L8 - Object-oriented programming

> 本講介紹 Python 的 object、class、instance、attribute 和 method。核心概念是把資料和操作資料的方法放在同一個 class 中，讓程式容易分工、測試和重複使用。

## 1. 什麼是 object？

Python 中幾乎所有資料都是 object，例如：

```python
1234
3.14159
"Hello"
[1, 5, 7]
{"CA": "California"}
```

每個 object 都有：

1. `type`，表示它的類型。
2. 內部資料表示方式。
3. 可以和它互動的操作或方法。

例如：

```python
values = [1, 2, 3]

type(values)       # list
values.append(4)   # 使用 list 的方法
len(values)        # 取得 list 的長度
```

`values` 是一個 `list` object，也可以說它是 `list` 的 instance。

## 2. OOP 是什麼？

OOP 是 Object-Oriented Programming，中文是物件導向程式設計。

物件導向程式通常把以下兩種東西放在同一個 class 裡：

- 描述物件狀態的資料。
- 操作這些資料的方法。

例如座標需要 `x` 和 `y`，也可以有計算距離的方法：

```python
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx ** 2 + dy ** 2) ** 0.5
```

這個 class 把座標資料和座標操作放在一起：

- 資料是 `x` 和 `y`。
- 方法是 `distance()`。

## 3. class、object 和 instance

```python
class Coordinate:
    pass
```

`Coordinate` 是 class，可以把它想成建立座標物件的規則。

```python
point = Coordinate()
```

`point` 是 object，也是 `Coordinate` 的 instance。

可以記成：

```text
class       定義物件的資料和功能
instance    根據 class 建立的個別物件
object      物件的泛稱
```

建立 class 和使用 class 是兩個不同動作：

```text
建立 class：定義 class 名稱、資料和方法
使用 class：建立 instance，並操作 instance
```

## 4. 定義 class

基本語法：

```python
class ClassName:
    # data attributes and methods
    pass
```

投影片中也使用以下寫法：

```python
class Coordinate(object):
    pass
```

括號裡的 `object` 表示 `Coordinate` 繼承 Python 的基本 `object` 類別。在 Python 3 中，通常可以省略它：

```python
class Coordinate:
    pass
```

## 5. attribute

Attribute 是屬於 object 或 class 的資料和功能。

### 5.1 Data attribute

資料屬性保存 object 的狀態，例如：

```python
self.x
self.y
```

### 5.2 Method

Method 是定義在 class 裡的函式，用來操作 object 的資料，例如：

```python
distance()
```

`distance()` 只對座標 object 有意義。這種設計讓使用者透過公開的方法操作資料，而不必直接修改 class 的內部表示方式。

## 6. `__init__` 和 instance 初始化

`__init__` 是 Python 的特殊方法。建立 instance 時，Python 會自動呼叫它，設定 instance 一開始的資料。

```python
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

建立 instance：

```python
point = Coordinate(3, 4)
```

可以把結果理解成：

```python
point.x = 3
point.y = 4
```

因此：

```python
print(point.x)  # 3
print(point.y)  # 4
```

嚴格來說，`__init__` 的主要工作是初始化 instance。呼叫 class 建立物件時，Python 會負責建立物件，再呼叫 `__init__` 設定資料。

## 7. `self`

`self` 代表目前正在使用的 instance。

```python
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

執行：

```python
point = Coordinate(3, 4)
```

此時：

```text
self 代表 point
x    是傳入的 3
y    是傳入的 4
```

`self.x = x` 的意思是：

> 把參數 `x` 的值存到目前 instance 的 `x` 屬性。

建立另一個 instance 時，每個 instance 有自己的資料：

```python
point1 = Coordinate(3, 4)
point2 = Coordinate(10, 20)

print(point1.x)  # 3
print(point2.x)  # 10
```

`self` 不需要在呼叫時自己傳入。Python 會自動把呼叫 method 的 object 傳給第一個參數。

## 8. method 和 function

Function 可以獨立呼叫：

```python
def add(a, b):
    return a + b

add(2, 3)
```

Method 是寫在 class 裡的 function：

```python
class Coordinate:
    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx ** 2 + dy ** 2) ** 0.5
```

使用 method 時通常使用點號：

```python
point.distance(origin)
```

這等價於：

```python
Coordinate.distance(point, origin)
```

因此：

- `self` 是呼叫 method 的 object。
- `other` 是另一個傳入的座標 object。

## 9. Worked example：Coordinate

```python
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx ** 2 + dy ** 2) ** 0.5

    def __str__(self):
        return f"<{self.x},{self.y}>"


point = Coordinate(3, 4)
origin = Coordinate(0, 0)

print(point.x)                 # 3
print(point.distance(origin)) # 5.0
print(point)                  # <3,4>
```

`distance()` 使用固定數量的運算，所以：

- 時間複雜度：`O(1)`。
- 額外空間複雜度：`O(1)`。

## 10. `__str__` 和 `print`

如果沒有定義 `__str__`：

```python
point = Coordinate(3, 4)
print(point)
```

可能得到類似以下的內容：

```text
<__main__.Coordinate object at 0x...>
```

這是 Python 的預設 object 表示方式，通常不容易讀。

可以自己定義 `__str__`：

```python
def __str__(self):
    return f"<{self.x},{self.y}>"
```

當 Python 執行：

```python
print(point)
```

它會自動使用：

```python
point.__str__()
```

`__str__` 必須回傳字串，不能直接回傳整數、list 或其他型別。

## 11. `type()` 和 `isinstance()`

```python
point = Coordinate(3, 4)

print(type(point))
print(isinstance(point, Coordinate))
```

`type(point)` 會取得 point 的實際類型。

`isinstance(point, Coordinate)` 會檢查 point 是否為 `Coordinate` 的 instance，結果是：

```python
True
```

初學時可以這樣記：

- `type()`：詢問 object 的類型。
- `isinstance()`：檢查 object 是否屬於某個 class。

## 12. 特殊運算子

Python 會把許多運算子轉成特殊方法：

| 寫法 | Python 會呼叫 |
| --- | --- |
| `a + b` | `a.__add__(b)` |
| `a - b` | `a.__sub__(b)` |
| `a == b` | `a.__eq__(b)` |
| `a < b` | `a.__lt__(b)` |
| `len(a)` | `a.__len__()` |
| `print(a)` | `a.__str__()` |

這些方法常被稱為 dunder methods，因為名稱前後都有兩個底線。

如果 class 沒有定義某個操作，Python 不知道該如何處理該操作。

## 13. Worked example：Fraction

Fraction class 可以用兩個整數表示分數：

```python
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __float__(self):
        return self.numerator / self.denominator

    def inverse(self):
        return Fraction(self.denominator, self.numerator)
```

使用：

```python
fraction = Fraction(1, 4)

print(fraction)         # 1/4
print(float(fraction))  # 0.25
print(fraction.inverse())  # 4/1
```

若要支援分數相加，可以定義：

```python
def __add__(self, other):
    numerator = self.numerator * other.denominator
    numerator += self.denominator * other.numerator
    denominator = self.denominator * other.denominator
    return Fraction(numerator, denominator)
```

此時：

```python
a = Fraction(1, 4)
b = Fraction(3, 4)

print(a + b)  # 4/4
```

`__add__()` 的運算數量固定，因此時間複雜度和額外空間複雜度都是 `O(1)`。

## 14. `assert` 和輸入限制

如果 Fraction 只接受整數，可以檢查輸入：

```python
class Fraction:
    def __init__(self, numerator, denominator):
        assert type(numerator) == int
        assert type(denominator) == int
        self.numerator = numerator
        self.denominator = denominator
```

但還需要考慮分母是否為零：

```python
assert denominator != 0
```

這些檢查表達的是 class 的使用條件。實務上，如果錯誤來自外部使用者輸入，通常應該使用明確的例外處理，而不是只依賴 assertion。

## 15. Worked example：整數集合

可以使用 class 表示一個整數集合：

```python
class IntSet:
    def __init__(self):
        self.values = []

    def insert(self, value):
        if value not in self.values:
            self.values.append(value)

    def member(self, value):
        return value in self.values

    def remove(self, value):
        if value not in self.values:
            raise ValueError(f"{value} not found")
        self.values.remove(value)

    def __str__(self):
        return "{" + ",".join(str(value) for value in sorted(self.values)) + "}"
```

使用：

```python
numbers = IntSet()
numbers.insert(3)
numbers.insert(4)
numbers.insert(3)

print(numbers)          # {3,4}
print(numbers.member(3)) # True
```

`insert()` 會先檢查數字是否已經存在，因此同一個數字不會被加入兩次。

若用 list 儲存資料：

- `insert()` 的 membership check 時間複雜度是 `O(n)`。
- `member()` 的時間複雜度是 `O(n)`。
- `remove()` 搜尋並刪除時的時間複雜度是 `O(n)`。
- 儲存 `n` 個不同整數需要 `O(n)` 空間。

## 16. OOP 的優點

### 16.1 封裝資料和方法

把資料和操作資料的 method 放在同一個 class 中，使用者不必直接修改內部資料。

### 16.2 模組化

每個 class 可以獨立設計、測試和除錯。大型程式可以拆成多個較小的 class。

### 16.3 重複使用

定義一次 class 後，可以建立很多 instance：

```python
point1 = Coordinate(3, 4)
point2 = Coordinate(0, 0)
point3 = Coordinate(10, 20)
```

### 16.4 抽象化

使用者只需要知道如何呼叫公開的 method，不需要知道 object 的內部資料結構。

### 16.5 繼承

子類別可以重複使用父類別的資料和方法，也可以重新定義或增加部分行為。繼承會在後續課程進一步介紹。

## 17. 常見錯誤

### 17.1 忘記寫 `self`

錯誤：

```python
class Coordinate:
    def __init__(x, y):
        self.x = x
        self.y = y
```

`__init__` 的第一個參數需要接收目前的 instance。

### 17.2 把 `self.x` 寫成 `x`

錯誤：

```python
def __init__(self, x, y):
    x = x
    y = y
```

這只是在設定區域變數，沒有把資料存到 instance。正確寫法是：

```python
self.x = x
self.y = y
```

### 17.3 呼叫 method 時手動傳入 `self`

通常不要這樣寫：

```python
point.distance(point, origin)
```

正確寫法是：

```python
point.distance(origin)
```

Python 會自動把 `point` 傳給 `self`。

### 17.4 `__str__` 沒有回傳字串

錯誤：

```python
def __str__(self):
    print(self.x)
```

`__str__` 應該使用 `return` 回傳字串：

```python
def __str__(self):
    return str(self.x)
```

### 17.5 class 沒有定義想使用的運算

如果沒有定義 `__add__`，就不能假設兩個自訂 object 可以使用 `+`。

### 17.6 混淆 class 和 instance

```python
Coordinate.x       # class 不一定有 instance attribute x
point.x            # point 的 instance attribute
```

`x` 是在 `__init__` 中透過 `self.x` 建立的，所以它屬於每個 instance。

## 18. 課堂內容的整體流程

```text
定義 class
    ↓
定義 data attributes 和 methods
    ↓
呼叫 class 建立 instance
    ↓
__init__ 初始化 instance
    ↓
使用 self 存取 instance 資料
    ↓
使用點號呼叫 method 或讀取 attribute
```

完整例子：

```python
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx ** 2 + dy ** 2) ** 0.5

    def __str__(self):
        return f"<{self.x},{self.y}>"


point = Coordinate(3, 4)
origin = Coordinate(0, 0)

print(point.x)
print(point.distance(origin))
print(point)
```

## 19. 重點速記

```text
class       定義物件應該有什麼資料和功能
object      Python 中的物件
instance    根據 class 建立的個別 object
attribute   object 或 class 擁有的資料或功能
method      定義在 class 裡的 function
__init__    初始化 instance
self        目前正在使用的 instance
__str__     定義 print(object) 的文字表示
```

最重要的關係是：

> Class 定義規則，instance 是根據規則建立的 object，`self` 指向目前這個 instance。

## 20. Closed-AI check

不看筆記，自己回答以下問題：

1. `class`、`object` 和 `instance` 有什麼差別？
2. 為什麼 `__init__(self, x, y)` 需要 `self`？
3. `self.x = x` 左右兩邊的 `x` 分別代表什麼？
4. `point.distance(origin)` 和 `Coordinate.distance(point, origin)` 有什麼關係？
5. 如果沒有定義 `__str__`，`print(point)` 可能會顯示什麼？
6. `a + b` 會對應到哪個特殊方法？
7. 什麼時候應該使用 `isinstance()`？
8. `IntSet.insert()` 為什麼要先檢查元素是否已經存在？

### 參考答案

1. `class` 定義資料和方法；`object` 是物件的泛稱；`instance` 是根據某個 class 建立的 object。
2. `self` 讓 method 知道目前要操作哪個 instance。
3. 左邊的 `self.x` 是 instance attribute，右邊的 `x` 是傳入的參數。
4. 前者是一般寫法，Python 會自動把 `point` 傳給 `self`；後者是明確傳入 `point` 的等價寫法。
5. 可能顯示包含 class 名稱和記憶體位置的預設表示。
6. `__add__()`。
7. 要檢查某個 object 是否屬於指定 class，或是否是該 class 的 instance 時。
8. 確保集合中的每個整數只出現一次。

## 21. 來源

- [MIT OpenCourseWare Lecture 8 課程頁面](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/lecture-8-object-oriented-programming/)
- [MIT Lecture 8 投影片 PDF](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/7a6f85d03f132dcd9d7592bc4643be1c_MIT6_0001F16_Lec8.pdf)
- [MIT Lecture 8 Python 程式碼](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/0705ac9dcc7e637a0e8e9d97eb258a26_lec8_classes.py)
