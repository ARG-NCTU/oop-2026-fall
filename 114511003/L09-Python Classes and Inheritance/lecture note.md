# Lecture 9：Python classes and inheritance

課程：MIT 6.0001 Introduction to Computer Science and Programming in Python，Fall 2016。

本筆記依 Lecture 9 投影片整理，另標示 Python 行為的補充說明。程式片段用於說明概念；同名類別的不同片段不應直接視為一份完整程式。

來源：

- [MIT 課程與影片](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/lecture-9-python-classes-and-inheritance/)
- 使用者提供的 `L9-Python Classes and Inheritance.pdf`，共 26 頁。

## 1. Class 與 instance

Class 定義一種物件的資料與行為。Instance 是依據 class 建立的個別物件。

| 名詞 | 意義 | 例子 |
|---|---|---|
| Class 類別 | 定義物件的資料與行為 | `Animal` |
| Instance 實例 | 某個具體物件 | `a = Animal(3)` 中的 `a` |
| Data attribute 資料屬性 | 物件儲存的資料 | `a.age` |
| Method 方法 | 物件提供的操作 | `a.get_age()` |

```python
class Animal:
    def __init__(self, age):
        self.age = age
        self.name = None

a = Animal(3)
b = Animal(5)
```

`a` 與 `b` 都是 `Animal`，但各自儲存自己的 `age`。

- `__init__` 在實例建立後負責初始化資料。
- `self` 指向目前操作的實例。
- `self.age = age` 把參數 `age` 存進該實例。

補充：Python 3 中，這裡的 `class Animal:` 與投影片的 `class Animal(object):` 效果相同。

## 2. self 與方法呼叫

對一般實例方法而言：

```python
a.get_age()
```

可以理解為：

```python
Animal.get_age(a)
```

Python 自動把 `a` 傳給第一個參數 `self`。定義方法時要寫 `self`，透過實例呼叫時不用再傳一次。

```python
def get_age(self):
    return self.age
```

補充：`self` 是慣用名稱，並非 Python 關鍵字。

## 3. Getter、setter 與資料隱藏

Getter 讀取資料，setter 修改資料。

```python
class Animal:
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, newage):
        self.age = newage

    def set_name(self, newname=""):
        self.name = newname

    def __str__(self):
        return f"animal:{self.name}:{self.age}"

a = Animal(3)
a.set_name("Fluffy")
print(a.get_age())   # 3
print(a)             # animal:Fluffy:3
```

投影片建議透過方法存取資料，讓外部程式依賴穩定的介面。

假設內部把 `self.age` 改成 `self.years`，只要同步修改 getter，外部的 `a.get_age()` 就能繼續使用；直接讀取 `a.age` 的程式則可能失效。

補充：Python 不會因為類別提供 getter、setter，就禁止直接存取屬性。本課透過這種寫法說明介面與實作的分離；Python 程式也常使用公開屬性或 `@property`。

## 4. 預設參數與 None

```python
def set_name(self, newname=""):
    self.name = newname
```

```python
a.set_name("Fluffy")  # name 變成 "Fluffy"
a.set_name()          # name 變成 ""
```

沒有傳入引數時，才使用預設值。

`None` 表示沒有值；`""` 是長度為零的字串。初始化時的 `name = None` 與呼叫 `set_name()` 後的結果不同。

## 5. 繼承 inheritance

本課的類別關係：

```text
Animal
├── Cat
├── Rabbit
└── Person
    └── Student
```

子類別可以使用父類別的方法，也可以增加或覆寫方法。

```python
class Cat(Animal):
    def speak(self):
        print("meow")

    def __str__(self):
        return f"cat:{self.name}:{self.age}"

c = Cat(2)
c.set_name("Mimi")
print(c.get_age())   # 2
c.speak()            # meow
print(c)             # cat:Mimi:2
```

| 方法 | 行為 |
|---|---|
| `__init__`、`set_name`、`get_age` | 沿用 `Animal` 的方法 |
| `speak` | `Cat` 新增的方法 |
| `__str__` | `Cat` 覆寫父類別的方法 |

`Cat` 沒有自己定義 `__init__`，因此使用繼承的初始化方法。

繼承具有方向性。`Cat` 可以使用 `Animal` 的方法，但 `Animal` 實例不會因此擁有 `Cat.speak()`。

## 6. 方法查找與覆寫

在本課的單一繼承例子中，先找物件所屬的類別，找不到再往父類別查找。

對 `Student` 實例呼叫 `get_age()` 時，查找順序是：

```text
Student → Person → Animal
```

若 `Student` 定義了 `speak()`，就使用該版本，不會自動把 `Person.speak()` 也執行一次。

補充：多重繼承時，Python 使用 method resolution order，簡稱 MRO，決定查找順序。

## 7. 子類別的初始化

投影片的 `Person`：

```python
class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []

    def get_friends(self):
        return self.friends

    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        print("hello")

    def age_diff(self, other):
        diff = self.age - other.age
        print(abs(diff), "year difference")

    def __str__(self):
        return f"person:{self.name}:{self.age}"
```

建立 `Person("Amy", 20)` 時：

1. `Animal.__init__` 建立 `age` 與 `name`。
2. `set_name` 設定姓名。
3. 建立這個人的 `friends` 串列。

子類別自己定義 `__init__` 後，Python 不會自動再執行父類別的 `__init__`。

補充：本例的父類別初始化也可以寫成 `super().__init__(age)`。`super()` 依 MRO 呼叫下一個類別的方法。

`self.friends = []` 放在 `__init__` 裡，讓每個人有自己的串列。如果改成類別層級的 `friends = []`，實例可能共用同一份朋友名單。

補充：此處 `get_friends()` 回傳原本的串列，外部仍能直接修改它。需要避免這種行為時，可以考慮回傳副本。

## 8. Student 新增資料與覆寫行為

`Student` 繼承 `Person`，新增 `major`，並覆寫 `speak()` 與 `__str__()`。

```python
import random

class Student(Person):
    def __init__(self, name, age, major=None):
        super().__init__(name, age)
        self.major = major

    def change_major(self, major):
        self.major = major

    def speak(self):
        r = random.random()
        if r < 0.25:
            print("i have homework")
        elif r < 0.5:
            print("i need sleep")
        elif r < 0.75:
            print("i should eat")
        else:
            print("i am watching tv")

    def __str__(self):
        return f"student:{self.name}:{self.age}:{self.major}"
```

這裡改用 `super()`，並省略已由前面分支排除的區間下界，保留投影片的行為。

```python
s = Student("Amy", 20, "EE")
s.add_friend("Bob")       # 繼承 Person
s.set_age(21)             # 繼承 Animal
s.change_major("CS")      # Student 自己的方法
```

## 9. Class variable 與 instance variable

`Rabbit` 使用類別變數產生流水號：

```python
class Rabbit(Animal):
    tag = 1

    def __init__(self, age, parent1=None, parent2=None):
        super().__init__(age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1

    def get_rid(self):
        return str(self.rid).zfill(3)

    def get_parent1(self):
        return self.parent1

    def get_parent2(self):
        return self.parent2
```

| 變數 | 儲存位置與用途 |
|---|---|
| `Rabbit.tag` | 類別上的共用計數器，記錄下一個編號 |
| `self.rid` | 各實例自己的編號 |
| `self.age` | 各實例自己的年齡 |

假設從全新的 `Rabbit` 類別開始執行：

```python
r1 = Rabbit(3)
r2 = Rabbit(4)
print(r1.get_rid())  # 001
print(r2.get_rid())  # 002
print(Rabbit.tag)   # 3
```

建立 `r2` 時，計數器增加，但 `r1.rid` 仍然是 `1`。

補充：本例若改寫為 `self.tag += 1`，會建立或更新實例上的屬性，無法達到同樣的共用計數效果。

## 10. 特殊方法與運算子

| 語法 | 本課對應的特殊方法 |
|---|---|
| `str(r)`、`print(r)` | `__str__` |
| `r1 + r2` | `__add__` |
| `r1 == r2` | `__eq__` |

在 `Rabbit` 類別內加入：

```python
def __add__(self, other):
    return Rabbit(0, self, other)
```

執行 `baby = r1 + r2` 會建立一隻新兔子，年齡為 `0`，兩個親代分別指向 `r1` 與 `r2`，並在初始化時取得新的編號。

`+` 的意義由類別定義。在此模型中，它代表產生後代。

## 11. 相等比較與物件身分

本課把兩隻兔子的相等定義為擁有相同的兩個親代，順序不影響結果。

在 `Rabbit` 類別內加入投影片的比較邏輯：

```python
def __eq__(self, other):
    parents_same = (
        self.parent1.rid == other.parent1.rid
        and self.parent2.rid == other.parent2.rid
    )
    parents_opposite = (
        self.parent2.rid == other.parent1.rid
        and self.parent1.rid == other.parent2.rid
    )
    return parents_same or parents_opposite
```

```python
baby1 = r1 + r2
baby2 = r2 + r1
print(baby1 == baby2)  # True，依本課定義
print(baby1 is baby2)  # False，是兩個不同物件
```

- `==` 比較類別所定義的相等關係。
- `is` 判斷是否為同一個物件。

投影片的 `__eq__` 假設雙方都是 `Rabbit`，而且兩個親代都不是 `None`。拿沒有親代資料的兔子比較，會因存取 `None.rid` 而產生 `AttributeError`。

比較親代的 `rid`，可以避免再次呼叫親代兔子的 `__eq__`，把比較一路遞迴到更早的世代。

補充：若要把這段程式用在完整專案，還需定義未知親代如何比較，以及如何處理其他型別。這些規則不是本投影片提供的完整規格。

## 12. 複習問題

1. 為什麼 `a.get_age()` 不用傳入 `self`？
2. `Cat` 沒有 `__init__`，為什麼仍能建立年齡？
3. 子類別寫了自己的 `__init__` 後，父類別初始化會自動執行嗎？
4. 為什麼 `friends` 放在 `self` 上，而 `tag` 放在類別上？
5. 為什麼兩個物件可以 `== True`，但 `is False`？
6. `Rabbit.__eq__` 對沒有親代資料的兔子有什麼問題？

### 參考答案

1. Python 會把呼叫方法的實例自動傳給 `self`。
2. 它繼承了 `Animal.__init__`。
3. 不會，需要明確呼叫，例如 `super().__init__(...)`。
4. 每個人需要自己的朋友名單；兔子編號需要共用的計數器。
5. `==` 依自訂規則比較內容，`is` 比較物件身分。
6. 親代可能是 `None`，讀取其 `rid` 會產生 `AttributeError`。
