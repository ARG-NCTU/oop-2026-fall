# Week 1 — AI Tutor Learning Record (Part A)

- 學號：112511246
- Topic：Lecture 5 — Tuple、List、別名、可變性與複製（Tuples, Lists, Aliasing, Mutability, and Cloning）
- 教材：MIT OCW 6.0001 Fall 2016, Lecture 5（講者 Ana Bell），題目依課堂逐字稿內容出題
- 完成方式：直接整理五題概念題與解答，未採逐題提示後修正的流程。
- 格式來源：[AI Tutor for AOOP 2026](https://github.com/ARG-NCTU/oop-python-nycu/blob/main/ai-tutor-2026.md)

## Part A: True or False

### ① Check My Understanding

- Questions completed: 5 / 5
- Answers revised after AI hints: 不適用；未採逐題提示後修正的流程。

### 題目與解答

#### 第 1 題：只有一個元素的 tuple

**題目：** `('a')` 和 `('a',)` 這兩種寫法代表同一個東西。

**答案：錯。**

課堂在講切片時特別點出這個細節：`('a',)` 後面那個逗號不是筆誤，它才是讓 Python 知道「這是一個 tuple」的關鍵。沒有逗號的 `('a')` 只是一個字串，那對括號在這裡不具任何意義，只是一般的運算優先順序括號。所以單一元素的 tuple 一定要補上逗號。

#### 第 2 題：`sort()` 與 `sorted()`

**題目：** `sorted_warm = warm.sort()` 會讓 `sorted_warm` 變成排序後的 list。

**答案：錯。**

課堂把這兩個放在一起對照。`L.sort()` 會**就地修改**原本的 list，而它的回傳值是 `None`，所以把它指派給變數只會得到 `None`；`sorted(L)` 則**不動原本的 list**，回傳一個排序後的新 list。課堂示範 `warm.sort()` 之後印出 `warm` 是排序過的，但印出 `sorted_warm` 得到的是 `None`。講者也提醒 `append`、`remove`、`extend` 這些會修改 list 的方法，回傳值通常也是 `None`，不能把回傳值當成結果使用。

#### 第 3 題：把 list 指派給另一個變數

**題目：** `hot = warm` 會建立一份 `warm` 的複本，之後修改 `hot` 不會影響 `warm`。

**答案：錯。**

這行只是替同一個 list 取了第二個名字，也就是**別名（alias）**，兩個變數指向記憶體中的同一個物件。課堂示範 `warm = ['red', 'yellow', 'orange']`、`hot = warm`，接著 `hot.append('pink')`，結果透過 `warm` 印出來也會看到 `'pink'`。講者用小賈斯汀當比喻：一個人有很多個綽號，但不管用哪個綽號稱呼，指的都是同一個人，那個人多了一個屬性，所有綽號看到的都是同一個改變後的人。

#### 第 4 題：用 `[:]` 複製

**題目：** 只要用 `chill = cool[:]` 複製一份，之後對任何一邊的修改都不會影響另一邊。

**答案：錯（在有巢狀結構時不成立）。**

`[:]` 確實能解決課堂前半段示範的單層 list 問題——`cool` 和 `chill` 變成兩個獨立的物件，對複本 append 不會動到原本的。但課堂後半段的 `bright_colors` 例子顯示，當 list 的元素本身也是 list 時，複製出來的外層雖然是新的，裡面的元素仍然指向同一批內層 list，修改 `hot` 之後 `bright_colors` 跟著變。所以 `[:]` 只複製一層。

#### 第 5 題：邊走訪邊刪除

**題目：** 用 for 迴圈走訪一個 list，同時在迴圈裡刪除它的元素，程式會照預期運作。

**答案：錯。**

課堂最後一個例子就是這個陷阱：想走訪 `L1`，把同時出現在 `L2` 的元素從 `L1` 刪掉。問題在於 Python 在背後是用索引走訪，一開始就決定了長度與索引，**不會因為你刪掉元素而更新**，結果會跳過元素。課堂給的解法是先複製一份，**走訪複本**（它維持不變），修改原本的 list。

### ② My Misconception

- **Before（常見誤解）：** 以為把 list 指派給另一個變數就等於複製了一份，也以為 `L.sort()` 會回傳排序後的 list 可以直接接住。
- **Now（觀念整理）：** 指派只是建立別名，兩個名字指向同一個物件，要獨立的副本必須明確複製；會修改 list 的方法多半回傳 `None`，想拿到新的 list 要用 `sorted()` 這類不修改原物件的版本。

### ③ Challenge the AI

- **Question examined：** 第 4 題，用 `[:]` 複製是否就能避免 side effect。
- **Why：** Oversimplified。
- **Brief explanation：** 課堂先示範 `[:]` 解決單層 list 的 side effect，給人「複製了就安全」的印象，但緊接著的 `bright_colors` 例子其實推翻了這個結論——巢狀的內層 list 仍然是共用的。如果題目只問「複製之後安不安全」而不區分有沒有巢狀結構，答案會隨情境改變。比較好的問法是直接給一個巢狀 list，問複製之後修改內層會發生什麼事。

### ④ One-Minute Reflection

- **One thing I am still unsure about：** 我還不確定實務上什麼時候該用 tuple、什麼時候該用 list。課堂說 tuple 不可變、list 可變，也示範用 tuple 一次回傳多個值，但如果資料之後不會改，我不知道是否一律該優先選 tuple。
- **Further question（延伸思考）：** 既然 `[:]` 只複製一層，那要怎麼做出「連內層都獨立」的複製？Python 有沒有標準做法，還是必須自己走訪每一層？
