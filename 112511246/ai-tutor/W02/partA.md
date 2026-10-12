# Week 2 — AI Tutor Learning Record (Part A)

- 學號：112511246
- Topic：Lecture 6 — 遞迴與字典（Recursion and Dictionaries）
- 教材：MIT OCW 6.0001 Fall 2016, Lecture 6（講者 Eric Grimson），題目依課堂逐字稿內容出題
- 完成方式：直接整理五題概念題與解答，未採逐題提示後修正的流程。
- 格式來源：[AI Tutor for AOOP 2026](https://github.com/ARG-NCTU/oop-python-nycu/blob/main/ai-tutor-2026.md)

## Part A: True or False

### ① Check My Understanding

- Questions completed: 5 / 5
- Answers revised after AI hints: 不適用；未採逐題提示後修正的流程。

### 題目與解答

#### 第 1 題：遞迴的終止條件

**題目：** 一個函式只要在自己的函式本體裡呼叫自己，就構成正確的遞迴。

**答案：錯。**

課堂強調遞迴的定義是「把問題化約成同一個問題的較小版本」，而且必須有 base case 才能停止展開。課堂用 `fact(4)` 逐層展開示範：每次呼叫都建立一個新的 frame，`n` 從 4、3、2 一路降到 1，碰到 `n == 1` 回傳 1 之後再一層層收回去。少了 base case，或每次呼叫沒有讓問題變小，展開就不會停。講者也用換燈泡的笑話描述這個結構：已經轉好就回答 0，否則轉一次、再問我一次、把答案加 1。

#### 第 2 題：Towers of Hanoi 與 Fibonacci 的遞迴結構

**題目：** Towers of Hanoi 和 Fibonacci 都有兩個遞迴呼叫，所以兩者的遞迴結構是相同的。

**答案：錯。**

課堂特別把這兩個例子對照。Towers of Hanoi 是「移動 n-1 層到備用柱、移動最底層、再把 n-1 層移過去」，兩個遞迴呼叫處理的是**同樣大小**的子問題，而且只需要一個 base case。Fibonacci 則是 `fib(n-1) + fib(n-2)`，兩個遞迴呼叫的**引數不同**，因此需要**兩個** base case（`n == 0` 與 `n == 1`，課堂的版本兩者都回傳 1）。

#### 第 3 題：字典的鍵

**題目：** 字典的值（value）可以是任何型別、也可以重複，但鍵（key）必須唯一且不可變（immutable）。

**答案：對。**

課堂列出的規則正是如此。值可以是任何型別、可變或不可變、可以重複，甚至可以是 list 或另一個字典；鍵則必須唯一（否則查找時無法判斷要哪一個）且不可變（否則存進去之後鍵被改掉就找不回來），因此只能是 int、float、string、tuple、Boolean 這類型別。講者另外補充不建議用 float 當鍵，因為必須剛好是同一個浮點數才找得到。

#### 第 4 題：字典的順序

**題目：** 字典沒有順序，走訪 `keys()` 時元素出現的順序無法預期。

**答案：課堂的說法是「對」，但以現行 Python 版本來說已不精確。**

課堂明確說「notice that there's no order to the keys or the values，它們只是被任意存放」，示範跑 `lyrics_to_frequencies` 時也說「What's the order? You don't care. You don't know.」。不過這份教材錄於 2016 年；從 CPython 3.7 起，字典保留插入順序已經寫進語言規格。即使如此，字典的用途仍是鍵值查找而非序列操作，需要排序時應明確使用 `sorted()`。

#### 第 5 題：memoization

**題目：** 用字典把算過的結果記下來，可以大幅減少 Fibonacci 的遞迴呼叫次數。

**答案：對。**

樸素的 `fib` 會重複計算同樣的子問題，課堂畫出呼叫樹說明右半邊幾乎都算過一次了。改成把 n 與結果存進字典，每次先檢查「這個值我算過了嗎」，算過就直接回傳。課堂給的數字是：`fib(34)` 用原本的寫法需要一千一百萬次以上的遞迴呼叫，加上字典之後只要 **65 次**。這個以空間換時間的技巧稱為 memoization。

### ② My Misconception

- **Before（常見誤解）：** 以為只要函式呼叫自己就會自動停止，也以為「有兩個遞迴呼叫」的問題結構都一樣，需要的 base case 數量相同。
- **Now（觀念整理）：** 終止靠的是 base case 加上每次呼叫讓問題變小；需要幾個 base case 取決於遞迴呼叫的引數形態，Hanoi 的兩個呼叫大小相同只需一個 base case，Fibonacci 的兩個呼叫引數不同因此需要兩個。

### ③ Challenge the AI

- **Question examined：** 第 4 題，字典是否沒有順序。
- **Why：** Technically questionable。
- **Brief explanation：** 題目把「字典無序」當成絕對事實，這是 2016 年錄製教材時的語言行為。CPython 3.7 之後字典保證保留插入順序並寫入語言規格，所以這個敘述在今天的 Python 已經不成立。題目應該標明討論的版本，或改問「是否應該依賴字典的順序來設計程式」，才問得出真正該掌握的觀念。

### ④ One-Minute Reflection

- **One thing I am still unsure about：** 我還不確定遇到新問題時，要用什麼標準判斷該寫遞迴還是迴圈。課堂舉手調查時講者說他偏好遞迴版的 factorial，理由是比較清楚，但也提到遞迴要額外配置 frame，我不知道實務上這個成本什麼時候會變成問題。
- **Further question（延伸思考）：** memoization 成立的前提是同樣輸入一定得到同樣輸出，那如果函式有副作用（例如會修改傳進來的 list），還能安全套用這個技巧嗎？
