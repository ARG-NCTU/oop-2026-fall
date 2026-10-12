# Week 5 — AI Tutor Learning Record (Part A)

- 學號：112511246
- Topic：Lecture 8 / 9 — Python 物件導向與繼承（Classes, Instances, Inheritance）
- 教材：MIT OCW 6.0001 Lecture 8、Lecture 9
- 完成方式：直接整理五題概念題與解答，未採逐題提示後修正的流程。
- 備註：本週同時完成 C++ OOP 的互動版學習單，見同資料夾 `partA-cpp-lab.md`。
- 格式來源：[AI Tutor for AOOP 2026](https://github.com/ARG-NCTU/oop-python-nycu/blob/main/ai-tutor-2026.md)

## Part A: True or False

### ① Check My Understanding

- Questions completed: 5 / 5
- Answers revised after AI hints: 不適用；未採逐題提示後修正的流程。

### 題目與解答

#### 第 1 題：class 與 instance 的差別

**題目：** `class` 和 `instance` 指的是同一件事，只是講法不同。

**答案：錯。**

`class` 是型別的定義，描述這一類物件有哪些屬性與方法，相當於設計圖；`instance` 是依照設計圖實際建立出來的個體。`Dog` 這個 class 只定義一次，`a = Dog()`、`b = Dog()` 則產生兩個獨立的 instance，各自擁有自己的屬性值，改動其中一個不會影響另一個。

#### 第 2 題：`__init__` 的角色

**題目：** `__init__` 會在建立新物件時自動被呼叫，用來設定這個物件的初始屬性。

**答案：對。**

寫下 `d = Dog("小黑")` 時，Python 先配置好新物件，再自動呼叫 `__init__`，把參數交給它來設定初始狀態。`__init__` 的角色相當於其他語言的建構子，差別是它不負責建立物件本身，只負責初始化已經建立好的物件，所以它沒有回傳值。

#### 第 3 題：`self` 的意義

**題目：** 方法定義裡的 `self` 是 Python 的保留字，必須叫這個名字才能正常運作。

**答案：錯。**

`self` 只是第一個參數的慣用名稱，不是保留字，技術上改叫別的名字也能執行。真正的機制是：以 `物件.方法()` 呼叫時，Python 會自動把該物件當作第一個引數傳進去。不過整個社群都用 `self`，換名字只會讓程式難讀，所以實務上視為不可違反的慣例。

#### 第 4 題：Python 的封裝

**題目：** 在屬性名稱前面加底線（例如 `self._level`），Python 就會強制禁止外部程式存取這個屬性。

**答案：錯。**

單底線純粹是命名慣例，意思是「這是內部實作，請不要從外面碰」，但語言不會阻止你寫 `obj._level`。雙底線會觸發名稱改編（name mangling），存取變得比較麻煩，但仍然不是真正的存取控制。這和 C++ 的 `private` 由編譯器強制擋下來不同，Python 採取的是約定而非強制。

#### 第 5 題：覆寫與多型

**題目：** 在 Python 中，子類別要覆寫父類別的方法時，必須像 C++ 那樣在父類別標記 `virtual`，否則呼叫到的會是父類別的版本。

**答案：錯。**

Python 的方法查找本來就在執行時沿著物件的類別往上找，先找到子類別的定義就用子類別的版本，不需要任何關鍵字。換句話說 Python 的方法預設全都是動態繫結的，C++ 那種要靠 `virtual` 才有多型的設計在 Python 不存在。想明確呼叫父類別的版本時，用 `super().方法()`。

### ② My Misconception

- **Before（常見誤解）：** 以為 `self` 是 Python 的關鍵字、底線開頭的屬性真的無法從外部存取，也以為 Python 像 C++ 一樣需要額外標記才會有多型。
- **Now（觀念整理）：** `self` 只是慣例名稱，真正的機制是呼叫時自動把物件當第一個引數傳入；底線是約定而非強制；Python 的方法查找本來就在執行時進行，預設即具備多型，不需要 `virtual` 這類標記。

### ③ Challenge the AI

- **Question examined：** 第 4 題，關於底線與封裝。
- **Why：** Oversimplified。
- **Brief explanation：** 題目只提「加底線」，但單底線與雙底線的行為其實不同：單底線純粹是慣例，雙底線會觸發 name mangling，讓屬性名稱在類別外變成 `_類別名__屬性名`。把兩者混為一談會讓人以為 Python 完全沒有任何機制，或者反過來以為雙底線就等於 private。題目應該分開討論這兩種情況。

### ④ One-Minute Reflection

- **One thing I am still unsure about：** 既然 Python 不強制存取控制，我不確定實務上要用什麼標準決定哪些屬性該加底線、哪些該透過 property 包裝，還是乾脆直接公開。
- **Further question（延伸思考）：** 同樣是物件導向，C++ 用編譯器強制擋下違規存取，Python 選擇只用命名慣例提醒。這兩種取捨各自適合什麼樣的開發情境？
