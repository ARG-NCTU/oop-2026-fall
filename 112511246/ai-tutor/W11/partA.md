# Week 11 — AI Tutor Learning Record (Part A)

- 學號：112511246
- Topic：MIT 6.0002 Lecture 3 — Graph-theoretic Models（圖、DFS、BFS、最短路徑）
- 教材：MIT OCW 6.0002 Fall 2016, Lecture 3，題目依課堂內容出題
- 完成方式：直接整理五題概念題與解答，未採逐題提示後修正的流程。
- 格式來源：[AI Tutor for AOOP 2026](https://github.com/ARG-NCTU/oop-python-nycu/blob/main/ai-tutor-2026.md)

## Part A: True or False

### ① Check My Understanding

- Questions completed: 5 / 5
- Answers revised after AI hints: 不適用；未採逐題提示後修正的流程。

### 題目與解答

#### 第 1 題：無向圖的實作

**題目：** 課堂的 `Graph`（無向圖）繼承 `Digraph`（有向圖），只覆寫 `addEdge`：每加一條邊 A → B，就再加一條反方向的 B → A。

**答案：對。**

`Digraph` 用字典 `self.edges` 存成鄰接串列，key 是點，value 是從這個點可以直接到達的點的 list；`addEdge` 只把終點加進起點的 list，所以邊是單向的。`Graph` 覆寫 `addEdge`，先呼叫 `Digraph.addEdge(self, edge)` 加上 A → B，再建立反方向的 `Edge(dest, src)` 加上 B → A。無向圖因此可以看成「每條邊都有兩個方向的有向圖」，其他方法（例如 `childrenOf`）都直接沿用父類別。

#### 第 2 題：DFS 第一個找到的路線

**題目：** 用深度優先搜尋（DFS）從起點找終點時，第一個找到的路線一定是邊數最少的路線。

**答案：錯。**

DFS 會沿著一條路一直走到底，走不通才退回上一個岔路。第一個碰到終點的路線，只是剛好先被走到的那一條，不一定最短。以課堂的城市圖為例，從 Boston 到 Phoenix，如果先走 Providence，第一條找到的是 Boston → Providence → New York → Chicago → Denver → Phoenix（5 趟），但最短的是 Boston → New York → Chicago → Phoenix（3 趟）。所以課堂的 `DFS` 找到一條路線後不會停，而是繼續搜尋，遇到更短的就更新 `shortest`，並把已經不比 `shortest` 短的分支剪掉。

#### 第 3 題：BFS 與最少邊數

**題目：** 在沒有權重的圖中，廣度優先搜尋（BFS）第一個到達終點的路線，一定是邊數最少的路線。

**答案：對。**

課堂的 `BFS` 用一個佇列 `pathQueue` 存放還沒處理的路線：每次用 `pop(0)` 從最前面拿出一條路線，延伸出多一條邊的新路線後用 `append` 排到最後面。因為是先進先出，所有 k 條邊的路線都會比 k + 1 條邊的路線先被拿出來，路線長度只會越來越長。所以第一條走到終點的路線一定是邊數最少的，找到就可以直接回傳，不必像 DFS 一樣試完所有路線。如果把 `pop(0)` 改成 `pop()`（後進先出），就會變成深度優先。

#### 第 4 題：避免繞圈

**題目：** 課堂的 DFS 和 BFS 在延伸路線前都會檢查 `if node not in path`；如果拿掉這個檢查，在有環（cycle）的圖中搜尋可能永遠不會結束。

**答案：對。**

城市圖中 Boston 和 Providence 互相都有航班，形成一個環。如果不檢查下一個點是否已經在目前的路線上，DFS 會在 Boston → Providence → Boston → Providence …… 之間無限遞迴；BFS 則會不斷產生越來越長、在環上繞圈的路線，佇列永遠不會清空（如果終點根本到不了，就永遠不會結束）。檢查 `node not in path` 保證每條路線不會重複經過同一個點，路線長度最多就是點的數量，搜尋才一定會結束。

#### 第 5 題：有權重的最短路徑

**題目：** 即使每條邊有不同的權重（例如飛行時間），BFS 第一個到達終點的路線仍然是總權重最小的路線。

**答案：錯。**

BFS 保證的是「邊數最少」，不是「總權重最小」。例如 A → C 直飛要 10 小時，A → B → C 兩段各 1 小時：BFS 會先找到只有 1 條邊的 A → C，但總時間最短的是 A → B → C（2 小時）。課堂指出 DFS 比較容易改成處理權重：DFS 本來就會比較所有路線，只要把比較的標準從 `len(path)` 換成路線的總權重即可。BFS 則因為找到就停，沒有比較其他路線的機會。

### ② My Misconception

- **Before（常見誤解）：** 以為 DFS 和 BFS 只是走的順序不同，最後找到的路線都一樣；也以為 BFS 找到的「最短路徑」在任何圖中都是最快的。
- **Now（觀念整理）：** DFS 第一個找到的路線不一定最短，必須試完所有路線（加上剪枝）才能確定；BFS 一層一層往外找，第一個找到的就是邊數最少的。但 BFS 的「最短」是指邊數最少，邊有權重時就不一定是總權重最小的。

### ③ Challenge the AI

- **Question examined：** 第 4 題，`if node not in path` 的作用。
- **Why：** Incomplete。
- **Brief explanation：** 題目的答案「對」沒有問題，但只說了這個檢查能讓搜尋結束，沒有說它的限制。`node not in path` 只禁止「同一條路線」重複經過同一個點，不同的路線仍然可以各自經過同一個點，所以同一個點會被不同的路線重複處理很多次，在點多的圖中路線數量仍可能非常多。另外，`in` 查 list 是 O(n)，每次延伸路線還要用 `path + [node]` 複製整條路線。如果只需要最短距離，可以改用一個字典記錄「已經看過的點」，每個點只處理一次，這就是我在 Part B 用的做法。

### ④ One-Minute Reflection

- **One thing I am still unsure about：** 邊有權重時，DFS 雖然可以比較總權重，但要試完所有路線，圖一大就會很慢。有沒有像 BFS 一樣「找到就能停」、又能處理權重的方法，我還不清楚。
- **Further question（延伸思考）：** 課堂的城市圖中，Los Angeles 可以飛到別的城市，但沒有任何城市飛得到 Los Angeles。如果想一次找出「從某個城市出發，所有到得了的城市」，應該用 DFS 還是 BFS？兩種方法找出來的城市會不會不一樣？
