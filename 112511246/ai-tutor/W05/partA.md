# Week 5 — AI Tutor Learning Record (Part A)

- 學號：112511246
- Topic：Lecture 9 — Python 類別與繼承（Python Classes and Inheritance）
- 教材：MIT OCW 6.0001 Fall 2016, Lecture 9
- 備註：本週另完成 C++ OOP 的互動版學習單，見同資料夾 `partA-cpp-lab.md`。
- 完成方式：直接整理五題概念題與解答，未採逐題提示後修正的流程。
- 格式來源：[AI Tutor for AOOP 2026](https://github.com/ARG-NCTU/oop-python-nycu/blob/main/ai-tutor-2026.md)

## Part A: True or False

### ① Check My Understanding

- Questions completed: 5 / 5
- Answers revised after AI hints: 不適用；未採逐題提示後修正的流程。

### 題目與解答

#### 第 1 題：繼承要寫多少

**題目：** 子類別必須把父類別所有的方法都重新寫一遍，才能使用那些功能。

**答案：錯。**

繼承的用意正是重用。寫下 `class Cat(Animal):` 之後，`Cat` 自動擁有 `Animal` 所有的屬性與方法，不需要重寫。子類別只需要做兩件事：新增父類別沒有的功能，以及覆寫行為需要改變的方法。沒有被覆寫的方法會沿用父類別的版本。

#### 第 2 題：覆寫需不需要特別標記

**題目：** 子類別要覆寫父類別的方法時，必須先在父類別加上類似 `virtual` 的標記，否則呼叫到的會是父類別的版本。

**答案：錯。**

Python 的方法查找在執行時沿著物件的類別往上找，先在子類別找到同名方法就用子類別的版本，不需要任何關鍵字。也就是說 Python 的方法預設全都是動態繫結，C++ 那種要靠 `virtual` 才有多型的設計在 Python 不存在。需要明確呼叫父類別版本時使用 `super().方法()`。

#### 第 3 題：類別變數

**題目：** 定義在類別內、但不在任何方法裡的變數，由該類別的所有 instance 共用。

**答案：對。**

這種變數稱為 class variable，屬於類別本身而不屬於個別物件，所有 instance 看到的是同一份。常見用途是計數器，例如 `Rabbit` 類別用一個 class variable 記錄總共生成了幾隻。要注意的是，透過某個 instance 指派同名屬性會在那個物件身上建立一個 instance variable 並遮蔽掉 class variable，這是很容易踩到的陷阱。

#### 第 4 題：`isinstance` 與繼承

**題目：** 若 `Cat` 繼承自 `Animal`，`c = Cat()`，則 `isinstance(c, Animal)` 的結果是 `True`。

**答案：對。**

`isinstance` 會沿著繼承鏈判斷，只要物件屬於該類別或其任何子類別就回傳 `True`，這正好對應「Cat 是一種 Animal」的語意。相對地 `type(c) == Animal` 會是 `False`，因為它只比對最精確的型別。需要考慮繼承關係時應該用 `isinstance`，而不是直接比較 `type`。

#### 第 5 題：子類別的 `__init__`

**題目：** 子類別如果自己定義了 `__init__`，但沒有呼叫 `super().__init__(...)`，父類別 `__init__` 裡設定的屬性就不會被設定。

**答案：對。**

子類別的 `__init__` 會完全覆蓋父類別的版本，不會自動連帶執行。父類別 `__init__` 裡負責初始化的屬性因此不會存在，之後任何讀取這些屬性的父類別方法都會丟出 `AttributeError`。正確做法是在子類別的 `__init__` 裡先呼叫 `super().__init__(...)` 完成父類別那部分的初始化，再設定子類別自己的屬性。

### ② My Misconception

- **Before（常見誤解）：** 以為 Python 的繼承也需要像 C++ 一樣用 `virtual` 之類的標記才會有多型，也以為子類別定義了 `__init__` 之後父類別的初始化仍會自動執行。
- **Now（觀念整理）：** Python 的方法查找在執行時沿繼承鏈進行，預設即具備多型；子類別的 `__init__` 會完整取代父類別的版本，父類別那部分的初始化必須自己用 `super().__init__()` 補上。

### ③ Challenge the AI

- **Question examined：** 第 3 題，關於類別變數由所有 instance 共用。
- **Why：** Oversimplified。
- **Brief explanation：** 敘述本身沒錯，但只講了一半。透過 instance 指派同名屬性時並不會改到 class variable，而是在那個物件上新建一個 instance variable 遮蔽它，這才是實際寫程式最容易出錯的地方。題目若加上「透過 `obj.x = 1` 修改會影響其他 instance 嗎」這樣的對照，才測得出是否真正理解共用的範圍。

### ④ One-Minute Reflection

- **One thing I am still unsure about：** 我還不確定什麼時候該用繼承、什麼時候該用組合。看起來很多情況兩種都做得到，但我沒有判斷的標準。
- **Further question（延伸思考）：** 如果一個子類別覆寫方法之後，行為已經不符合父類別原本的約定（例如 `Square` 繼承 `Rectangle` 但限制長寬必須相等），這樣的繼承還算合理嗎？應該用什麼原則判斷？
