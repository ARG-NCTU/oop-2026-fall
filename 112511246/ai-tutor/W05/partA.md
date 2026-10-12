# Week 5 — AI Tutor Learning Record (Part A)

- 學號：112511246
- Topic：Lecture 9 — Python 類別與繼承（Python Classes and Inheritance）
- 教材：MIT OCW 6.0001 Fall 2016, Lecture 9（講者 Ana Bell），題目依課堂逐字稿內容出題
- 備註：本週另完成 C++ OOP 的互動版學習單，見同資料夾 `partA-cpp-lab.md`。
- 完成方式：直接整理五題概念題與解答，未採逐題提示後修正的流程。
- 格式來源：[AI Tutor for AOOP 2026](https://github.com/ARG-NCTU/oop-python-nycu/blob/main/ai-tutor-2026.md)

## Part A: True or False

### ① Check My Understanding

- Questions completed: 5 / 5
- Answers revised after AI hints: 不適用；未採逐題提示後修正的流程。

### 題目與解答

#### 第 1 題：為什麼要用 getter 和 setter

**題目：** 既然 `a.age` 和 `a.get_age()` 得到的結果一樣，使用哪一種寫法並沒有差別。

**答案：錯。**

課堂用一個很具體的情境說明差別：假設寫這個類別的人後來改了實作，把資料屬性從 `age` 改名成 `years`，`__init__` 裡變成 `self.years = age`。原本直接寫 `a.age` 的人就會壞掉，因為那個屬性已經不存在，Python 會回報找不到屬性；而原本用 `a.get_age()` 的人完全不受影響，因為實作者會同步把 getter 改成回傳 `self.years`。這就是資訊隱藏的價值——使用者不需要知道類別內部怎麼實作。

#### 第 2 題：Python 的資訊隱藏

**題目：** Python 能夠確實阻止外部程式直接存取或修改類別的資料屬性。

**答案：錯。**

課堂原話是「Python's actually not very great at information hiding」，並列出三件 Python 允許、但你不該做的事：從類別外部讀取資料屬性（`a.age`）、從外部寫入資料屬性（例如把 age 設成字串 `'infinite'`，讓原本假設 age 是整數的方法全部壞掉）、以及在類別定義之外替某個 instance 新增資料屬性（例如憑空加一個 `size`）。Python 不會攔你，所以靠的是自律與慣例，不是語言強制。

#### 第 3 題：子類別沒有 `__init__`

**題目：** 子類別如果沒有定義 `__init__`，建立該類別的物件時會發生錯誤。

**答案：錯。**

課堂的 `Cat` 就沒有自己的 `__init__`，講者說這樣完全沒問題。Python 的查找規則是：先看自己的類別定義裡有沒有這個方法，沒有就往父類別找，再沒有就往父類別的父類別找，一路沿著繼承鏈往上追。所以 `Cat` 會直接沿用 `Animal` 的 `__init__`。這個規則對所有方法都成立，不只是 `__init__`。

#### 第 4 題：子類別自己定義 `__init__` 的情況

**題目：** 若子類別自己定義了 `__init__`，而且沒有在裡面呼叫父類別的 `__init__`，父類別 `__init__` 中設定的資料屬性就不會被建立。

**答案：對。**

子類別的 `__init__` 會完全取代父類別的版本，不會自動連帶執行。課堂的 `Person` 因此在自己的 `__init__` 第一行就寫 `Animal.__init__(self, age)`，講者說這等於告訴 Python「你已經知道怎麼初始化一個 animal 了，就幫我做掉」，省下重寫的工夫；`Student.__init__` 同樣先呼叫 `Person.__init__(self, name, age)`。沒有這一行的話，父類別負責初始化的屬性不會存在，之後任何讀取它們的方法都會出錯。

#### 第 5 題：class variable

**題目：** 定義在類別內、但在 `__init__` 之外的變數，由該類別所有 instance 共用。

**答案：對。**

課堂用 `Rabbit` 的 `tag = 1` 示範。`tag` 寫在類別定義內、`__init__` 外，是 class variable，所有 instance 共用同一份。每建立一隻兔子，`__init__` 會先把目前的 `tag` 存成該 instance 的 `rid`，再把 `tag` 加 1，於是 r1、r2、r3 的編號依序是 001、002、003。要注意課堂存取它時寫的是 `Rabbit.tag` 而不是 `self.tag`——用類別名稱存取。相對地 `self.rid` 是 instance variable，每隻兔子各自一份，r2 看不到也改不了 r1 的 rid。

### ② My Misconception

- **Before（常見誤解）：** 以為在屬性前加底線或使用 getter/setter，就代表 Python 真的擋得住外部存取；也以為子類別定義了自己的 `__init__` 之後，父類別的初始化仍會自動執行。
- **Now（觀念整理）：** Python 並不強制資訊隱藏，getter/setter 的價值在於實作改變時不會波及使用者，而不是防止存取；子類別的 `__init__` 會完整取代父類別的版本，父類別那部分必須自己呼叫 `Animal.__init__(self, age)` 補上。

### ③ Challenge the AI

- **Question examined：** 第 5 題，class variable 由所有 instance 共用。
- **Why：** Oversimplified。
- **Brief explanation：** 敘述本身沒錯，但只講了一半。實際寫程式最容易出錯的地方是：透過 instance 指派同名屬性（`r1.tag = 99`）並不會改到 class variable，而是在那個物件上新建一個 instance variable 把它遮蔽掉。課堂示範的是用 `Rabbit.tag` 存取與修改，剛好避開了這個陷阱。題目若加上「透過 `r1.tag = 99` 修改會影響其他 instance 嗎」的對照，才測得出是否真的理解共用的範圍。

### ④ One-Minute Reflection

- **One thing I am still unsure about：** 我還不確定什麼時候該用繼承、什麼時候該用組合。課堂的 Animal → Person → Student 階層很自然，但那是因為現實世界本來就有這層關係；換成沒有明顯「是一種」關係的情況，我就不知道該怎麼判斷。
- **Further question（延伸思考）：** 課堂提到 `Student` 覆寫了 `Person` 的 `speak()`，行為從「hello」變成隨機四句話。如果某個子類別覆寫之後行為已經不符合父類別原本的約定，這樣的繼承還算合理嗎？應該用什麼原則判斷？
