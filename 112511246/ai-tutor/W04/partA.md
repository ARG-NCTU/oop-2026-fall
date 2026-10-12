# Week 4 — AI Tutor Learning Record (Part A)

- 學號：112511246
- Topic：Lecture 8 — 物件導向程式設計（Object Oriented Programming）
- 教材：MIT OCW 6.0001 Fall 2016, Lecture 8
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

`class` 是型別的定義，描述這一類物件有哪些資料屬性與方法，相當於設計圖；`instance` 是依設計圖實際建立出來的個體。`Coordinate` 這個 class 只定義一次，`a = Coordinate(1, 2)` 與 `b = Coordinate(3, 4)` 則是兩個獨立的 instance，各自擁有自己的屬性值，改動其中一個不會影響另一個。

#### 第 2 題：`__init__` 的角色

**題目：** `__init__` 會在建立新物件時自動被呼叫，用來設定這個物件的初始屬性。

**答案：對。**

寫下 `c = Coordinate(1, 2)` 時，Python 先配置好新物件，再自動呼叫 `__init__`，把參數交給它設定初始狀態。它的角色相當於其他語言的建構子，差別在於它不負責建立物件本身，只負責初始化已經存在的物件，所以沒有回傳值。

#### 第 3 題：`self` 的意義

**題目：** 方法定義裡的 `self` 是 Python 的保留字，必須叫這個名字才能正常運作。

**答案：錯。**

`self` 只是第一個參數的慣用名稱，不是保留字，技術上改叫別的名字程式照樣能跑。真正的機制是：以 `物件.方法()` 呼叫時，Python 自動把該物件當成第一個引數傳進去，所以定義時一定要預留這個位置。不過整個社群都用 `self`，改名只會讓程式難讀，實務上視為不可違反的慣例。

#### 第 4 題：資訊隱藏

**題目：** 在屬性名稱前面加底線（例如 `self._x`），Python 就會強制禁止外部程式存取這個屬性。

**答案：錯。**

單底線純粹是命名慣例，意思是「這是內部實作，請不要從外面碰」，但語言不會阻止你寫 `obj._x`。雙底線會觸發名稱改編（name mangling），讓屬性在類別外變成 `_類別名__屬性名`，存取比較麻煩但仍然做得到。因此 Python 的資訊隱藏靠的是約定，而不是像 C++ 的 `private` 那樣由編譯器強制擋下。使用 getter 與 setter 的價值在於保留日後加入驗證或改變內部表示法的彈性。

#### 第 5 題：`__str__`

**題目：** 在類別中定義 `__str__` 之後，對該類別的物件呼叫 `print()` 就會顯示你自訂的字串。

**答案：對。**

`print(obj)` 實際上會去呼叫 `str(obj)`，而 `str()` 會找該類別的 `__str__` 方法。沒有定義時會落回預設行為，印出類似 `<__main__.Coordinate object at 0x...>` 的內容，只看得到型別與記憶體位址。自訂 `__str__` 屬於特殊方法的一種，`__add__`、`__eq__`、`__len__` 也是同一類機制，讓自訂型別能和內建運算子與函式自然搭配。

### ② My Misconception

- **Before（常見誤解）：** 以為 `self` 是 Python 的關鍵字，也以為在屬性前面加底線就等於 C++ 的 `private`，外部真的存取不到。
- **Now（觀念整理）：** `self` 只是慣例名稱，真正的機制是呼叫方法時自動把物件當第一個引數傳入；底線是給人看的約定而非語言強制，資訊隱藏在 Python 靠的是共識與 getter/setter 的設計，而不是存取控制。

### ③ Challenge the AI

- **Question examined：** 第 4 題，關於底線與資訊隱藏。
- **Why：** Oversimplified。
- **Brief explanation：** 題目只提「加底線」，但單底線與雙底線的行為其實不同：單底線純粹是慣例，雙底線會觸發 name mangling。把兩者混為一談，容易讓人以為 Python 完全沒有任何機制，或反過來以為雙底線就等於 private。題目應該分開討論這兩種情況。

### ④ One-Minute Reflection

- **One thing I am still unsure about：** 既然 Python 不強制存取控制，我不確定實務上要用什麼標準決定哪些屬性該加底線、哪些該用 getter/setter 包起來、哪些乾脆直接公開。
- **Further question（延伸思考）：** 特殊方法（`__str__`、`__add__` 等）讓自訂型別能使用內建運算子，那要到什麼程度才算合理？例如替一個「學生」類別定義 `__add__` 是否反而會讓程式更難讀？
