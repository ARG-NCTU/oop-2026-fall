# Week 3 — AI Tutor Learning Record (Part A)

- 學號：112511246
- Topic：Lecture 7 — 測試、除錯、例外與斷言（Testing, Debugging, Exceptions, and Assertions）
- 教材：MIT OCW 6.0001 Fall 2016, Lecture 7，題目依課堂逐字稿內容出題
- 完成方式：直接整理五題概念題與解答，未採逐題提示後修正的流程。
- 格式來源：[AI Tutor for AOOP 2026](https://github.com/ARG-NCTU/oop-python-nycu/blob/main/ai-tutor-2026.md)

## Part A: True or False

### ① Check My Understanding

- Questions completed: 5 / 5
- Answers revised after AI hints: 不適用；未採逐題提示後修正的流程。

### 題目與解答

#### 第 1 題：path-complete 的測試是否足夠

**題目：** 如果一組測資走過了程式中每一條可能的路徑（path complete），就不會漏掉 bug。

**答案：錯。**

課堂用絕對值函式示範這個陷阱。那份實作寫的是 `if x < -1: return -x`，`else: return x`。用 `-2` 和 `2` 兩筆測資就已經走過兩條分支，是 path complete，但仍然漏掉 `-1`：程式會把 `abs(-1)` 算成 `-1`，是錯的。所以白箱測試除了涵蓋所有路徑，還必須補上**邊界條件**。

#### 第 2 題：黑箱與白箱測試

**題目：** 黑箱測試依據函式的規格（docstring）設計測資，白箱測試依據程式碼本身設計測資。

**答案：對。**

課堂用 `sqrt(x, epsilon)` 示範黑箱：你看不到實作，只根據 docstring 設計測資，所以不論對方用逼近法還是二分法，測資都一樣，這正是黑箱的好處。白箱則是看著程式碼設計測資，目標是走過所有路徑；課堂也給了迴圈的指引——for 迴圈要測「完全沒進入」「進入一次」「進入多次」，while 迴圈則要涵蓋所有跳出迴圈的方式。

#### 第 3 題：assert 與例外的分工

**題目：** `assert` 是用來處理使用者輸入錯誤的主要機制。

**答案：錯。**

課堂把兩者的分工講得很清楚：例外（exceptions）用於處理使用者提供的錯誤資料，斷言（assertions）則用來確認「函式的輸入與假設是否如預期」，屬於防禦性程式設計。課堂示範把 `assert len(grades) != 0, 'no grades data'` 放在函式開頭，斷言一旦為假函式立刻停止，目的是避免壞值繼續往下傳播，讓你更早、更接近源頭發現問題，而不用從輸出一路回推。

#### 第 4 題：try / except / else / finally

**題目：** `else` 區塊只有在 `try` 區塊沒有發生例外時才執行，而 `finally` 區塊無論如何都會執行。

**答案：對。**

課堂說明 `else` 在 try 區塊順利結束、沒有引發錯誤時執行；`finally` 則不論正常結束、引發例外、引發不同種類的例外或走過 `else`，都一定會執行，通常用來做收尾，例如印出結束訊息或關閉檔案。課堂也提到多個 `except` 可以分別攔截不同錯誤（例如 `ValueError` 與 `ZeroDivisionError`），結構上類似 if / elif / else。

#### 第 5 題：處理錯誤的三種做法

**題目：** 當函式遇到不合法的輸入時，回傳一個特殊值（例如 -1）來表示錯誤，是良好的做法。

**答案：錯。**

課堂列出三種做法並評價：第一種「fail silently」直接把錯誤值換掉，是壞主意，因為使用者會以為輸入被接受卻得到奇怪的結果；第二種就是這題說的回傳錯誤值，課堂明講這也不好，因為之後每次呼叫這個函式都得多寫一次「如果回傳是 -1 就…」的檢查，程式會變得很亂；第三種才是建議做法——用 `raise` 主動丟出例外，例如 `raise ValueError('...')`，讓呼叫端用 try/except 統一處理。

### ② My Misconception

- **Before（常見誤解）：** 以為只要測資走過所有程式路徑就算測夠了，也以為 `assert` 可以直接拿來擋使用者輸入的錯誤資料。
- **Now（觀念整理）：** path complete 不等於沒有漏洞，邊界值必須另外補；`assert` 檢查的是程式自身的前後條件，使用者輸入屬於可預期的狀況，應由例外處理負責，兩者的用途不能互換。

### ③ Challenge the AI

- **Question examined：** 第 2 題，黑箱與白箱測試的定義。
- **Why：** Too easy。
- **Brief explanation：** 這題只是把兩個名詞的定義對應回去，記得住名字就能答對，不需要理解兩者的取捨。改成「某個函式之後換了實作方式，原本的黑箱測資與白箱測資哪一組仍然有效？為什麼？」會更有鑑別度，因為那會逼人想到黑箱測資依附的是規格、白箱測資依附的是實作。

### ④ One-Minute Reflection

- **One thing I am still unsure about：** 我還不確定實務上要怎麼判斷等價類切得夠不夠完整，尤其是輸入有多個參數互相影響的時候。課堂提到沒有自然分界時可以用隨機測試，但沒說要測到什麼程度才算足夠。
- **Further question（延伸思考）：** 課堂提到除錯時可以用二分法插入 print 來縮小範圍，這個做法和用 debugger 設中斷點相比各有什麼取捨？什麼情況下 print 反而比 debugger 有效？
