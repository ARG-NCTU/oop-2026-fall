# Week 4 — AI Tutor Learning Record (Part A)

- 學號：112511246
- Topic：Lecture 8 — 物件導向程式設計（Object Oriented Programming）
- 教材：MIT OCW 6.0001 Fall 2016, Lecture 8（講者 Ana Bell），題目依課堂逐字稿內容出題
- 備註：本週僅有影片課程，無上機課。
- 完成方式：直接整理五題概念題與解答，未採逐題提示後修正的流程。
- 格式來源：[AI Tutor for AOOP 2026](https://github.com/ARG-NCTU/oop-python-nycu/blob/main/ai-tutor-2026.md)

## Part A: True or False

### ① Check My Understanding

- Questions completed: 5 / 5
- Answers revised after AI hints: 不適用；未採逐題提示後修正的流程。

### 題目與解答

#### 第 1 題：class 與 instance

**題目：** `class` 和 `instance` 是同一件事，只是講法不同。

**答案：錯。**

課堂用「藍色的車和粉紅色的車來自同一張藍圖」比喻：`class` 是藍圖，定義這個型別有哪些資料屬性與方法；`instance` 是依藍圖造出來的個體。`Coordinate` 這個 class 定義一次，`c = Coordinate(3, 4)` 與 `origin = Coordinate(0, 0)` 則是兩個獨立的 instance，結構相同但 x、y 的值各自不同。

#### 第 2 題：`self` 是不是保留字

**題目：** 方法定義裡的第一個參數必須命名為 `self`，否則程式無法運作。

**答案：錯。**

課堂原話是「it can be named anything you want, but really by convention it's always named self」。真正的機制是：用 `c.distance(origin)` 呼叫時，Python 會自動把 `c` 當成第一個引數傳進去，所以定義時一定要預留這個位置，但名字不是語言規定的。課堂也回答了同學的提問，確認 `self.x` 的 `x` 和參數的 `x` 不必同名。

#### 第 3 題：兩種呼叫方法的寫法

**題目：** `c.distance(origin)` 和 `Coordinate.distance(c, origin)` 是等價的。

**答案：對。**

課堂特別用一張投影片並排這兩種寫法。右邊那種要寫出類別名稱、方法名稱，並把包含 `self` 在內的所有引數都填進去，比較容易理解實際發生什麼事；左邊那種則由 Python 自動查出物件的型別，再把物件當成 `self` 傳入，等價但簡潔得多，所以平常都用左邊的寫法——就像我們一直在用的 `L.append(3)`。

#### 第 4 題：`__str__`

**題目：** 如果沒有在類別裡定義 `__str__`，對該類別的物件呼叫 `print()` 會發生錯誤。

**答案：錯。**

不會錯誤，只是印出來的東西沒有用。課堂示範沒有定義 `__str__` 時 `print(c)` 會印出類似「這是一個位於某記憶體位址的 Coordinate 物件」的訊息，講者形容為 very uninformative。定義 `__str__` 之後就能自己決定印出什麼，課堂選擇印成角括號包起來的 `<3,4>`。注意 `__str__` 必須回傳一個字串。

#### 第 5 題：特殊運算子

**題目：** 只要兩個自訂類別的物件型別相同，就可以直接用 `+` 把它們相加。

**答案：錯。**

課堂說得很明確：如果沒有實作 `__add__`，對兩個 `Coordinate` 物件使用 `+` 會產生錯誤，因為 Python 本來就不知道兩個座標該怎麼相加。要讓 `+`、`-`、`==`、`<`、`len()` 這些運算子能用在自訂型別上，必須自己實作對應的特殊方法，並自行決定語意。課堂的 `Fraction` 例子就實作了 `__add__`、`__sub__`、`__float__`，而且 `__add__` 回傳的是一個新的 `Fraction` 物件，不是數字，因此回傳值還能繼續套用同一套方法。

### ② My Misconception

- **Before（常見誤解）：** 以為 `self` 是 Python 的關鍵字，也以為自訂類別的物件只要型別相同就能直接用 `+` 相加。
- **Now（觀念整理）：** `self` 只是第一個參數的慣用名稱，真正的機制是呼叫方法時自動把物件當第一個引數傳入；運算子要能用在自訂型別上，必須自己實作對應的特殊方法，Python 不會自動推論語意。

### ③ Challenge the AI

- **Question examined：** 第 2 題，關於 `self` 是否為保留字。
- **Why：** Oversimplified。
- **Brief explanation：** 技術上答案是「不是保留字」，但只回答這一句會給人「可以隨便改名」的印象。實際上整個 Python 社群、所有工具與閱讀習慣都預設是 `self`，改名雖然能跑卻等於製造麻煩。題目若改問「`self` 不是保留字，那為什麼仍然不該改名」，會比單純判斷對錯更有價值。

### ④ One-Minute Reflection

- **One thing I am still unsure about：** 我還不確定設計自己的類別時，要怎麼決定哪些資料該放進 `__init__` 當資料屬性、哪些應該在需要時才計算。課堂的 `Coordinate` 很直覺地用 x 和 y，但換成比較抽象的物件我就沒有判斷依據。
- **Further question（延伸思考）：** 特殊方法讓自訂型別能使用內建運算子，但到什麼程度才算合理？例如替一個「學生」類別定義 `__add__`，語意上並不清楚，這種情況該如何判斷要不要實作？
