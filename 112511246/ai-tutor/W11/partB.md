# Week 11 — AI Tutor Learning Record (Part B)

- 學號：112511246
- Name：張中愷
- Date：2026-11-17
- Topic：MIT 6.0002 Lecture 3 — Graph-theoretic Models（圖、DFS、BFS）
- 程式檔：[w11.py](w11.py)
- 格式來源：[AI Tutor for AOOP 2026](https://github.com/ARG-NCTU/oop-python-nycu/blob/main/ai-tutor-2026.md)

## 1. Today's Challenge

**Core concept from today's OCW lecture:**

圖由點和邊組成，課堂用字典存成鄰接串列：key 是點，value 是從這個點可以直接到達的點的 list，`childrenOf(node)` 就是查這個字典。BFS 用佇列（先進先出）一層一層往外搜尋：短的路線一定比長的路線先排進隊伍、也先被拿出來，所以在沒有權重的圖中，第一個走到終點的路線一定是邊數最少的。DFS 則是一條路先走到底，第一個找到的不一定最短，必須全部試完才能確定。

**AI-generated coding challenge title:** Degrees of Separation（幾度分隔）

### 題目

社群網站上，朋友是 1 度，朋友的朋友是 2 度，以此類推。給一份朋友名單（字典，朋友關係是雙向的），寫一個函式 `degrees(friends, a, b)`，回傳 a 和 b 之間最少隔幾度；a 就是 b 時回傳 `0`，連不到時回傳 `-1`。

- 規定：只回傳度數，不用回傳路線；不能像課堂一樣用 `nextNode not in tmpPath` 檢查走過的點（`in` 查 list 是 O(n)，而且每條路線都要複製）。
- 限制：最多 1 萬人。

```python
friends = {
    "Amy":   ["Ben", "Cat"],
    "Ben":   ["Amy", "Dan"],
    "Cat":   ["Amy", "Dan"],
    "Dan":   ["Ben", "Cat", "Eve"],
    "Eve":   ["Dan"],
    "Frank": [],
}
```

| 呼叫 | 結果 | 說明 |
|---|---|---|
| `degrees(friends, "Amy", "Ben")` | `1` | 直接是朋友 |
| `degrees(friends, "Amy", "Dan")` | `2` | Amy → Ben → Dan |
| `degrees(friends, "Amy", "Eve")` | `3` | Amy → Ben → Dan → Eve |
| `degrees(friends, "Amy", "Amy")` | `0` | 自己 |
| `degrees(friends, "Amy", "Frank")` | `-1` | 連不到 |

## 2. My Initial Approach — Before AI Help

用 BFS，因為要找最少的度數，而 BFS 一層一層往外找，第一次碰到 b 就是最少的。隊伍裡排「人和度數」，例如 `("Dan", 2)`，不用排整條路線。用字典記錄已經看過的人，查詢是 O(1)。

## 3. AI Tutor Help

- [ ] No — I solved it independently
- [x] Yes — I received one or more hints

**The most useful hint/question from AI was:**

AI 問我：什麼時候要把人記成「看過」，是從隊伍拿出來的時候，還是放進隊伍的時候？並用例子說明：Ben 和 Cat 的朋友裡都有 Dan，如果拿出來才記，處理 Ben 和 Cat 時 Dan 都還沒被拿出來，就會被放進隊伍兩次。

**It helped me realize that:**

要在放進隊伍的時候就記成看過，每個人才只會排隊一次。這樣不會算錯度數，因為 BFS 第一次碰到某個人時，用的就是最少的度數。另外，看到朋友就是 b 時可以直接回傳 `d + 1`，不用等 b 被拿出來，可以少跑一層。

## 4. My Revision

- [ ] No
- [x] Yes

**What did you change, and why?**

我原本的想法只有「用字典記看過的人」，沒有想到記錄的時間點會影響效率。修改後決定：放進隊伍時就記成看過；處理每個朋友時先檢查是不是 b。程式碼由 AI 依照這個做法寫出，並用 `collections.deque` 當隊伍，因為 list 的 `pop(0)` 要把後面的元素全部往前移，是 O(n)，`deque.popleft()` 是 O(1)。

用範例手動追蹤（`degrees(friends, "Amy", "Eve")`）：

| 拿出來 | 他的朋友 | 做什麼 | 隊伍 |
|---|---|---|---|
| 開始 | | 記 Amy | `(Amy, 0)` |
| `(Amy, 0)` | Ben、Cat | 都沒看過，記下並排隊 | `(Ben, 1)`、`(Cat, 1)` |
| `(Ben, 1)` | Amy、Dan | Amy 看過跳過；Dan 記下並排隊 | `(Cat, 1)`、`(Dan, 2)` |
| `(Cat, 1)` | Amy、Dan | 兩個都看過，跳過（Dan 不會排第二次） | `(Dan, 2)` |
| `(Dan, 2)` | Ben、Cat、Eve | Eve 就是 b | 回傳 `2 + 1 = 3` |

### 最終程式

```python
from collections import deque


def degrees(friends, a, b):
    if a == b:
        return 0
    seen = {a: True}
    queue = deque([(a, 0)])
    while queue:
        person, d = queue.popleft()
        for f in friends[person]:
            if f == b:
                return d + 1
            if f not in seen:
                seen[f] = True
                queue.append((f, d + 1))
    return -1
```

## 5. Verification

- [x] Passed the provided examples
- [x] Passed additional edge cases
- [ ] Still has unresolved problems

另外測試的邊界情況：

| 測試 | 預期輸出 | 實際輸出 |
|---|---|---|
| 只有兩個人，互為朋友 | `1` | `1` |
| 只有一個人，問自己 | `0` | `0` |
| 兩個人都沒有朋友 | `-1` | `-1` |
| 10 個人排成一直線，頭到尾 | `9` | `9` |
| 6 個人圍成一圈，0 到對面的 3 | `3` | `3` |
| 6 個人圍成一圈，0 到隔壁的 5 | `1` | `1` |
| 2000 組隨機朋友圈（1～9 人），與不使用 BFS 的距離算法（反覆更新每個人的最短距離）比對 | 全部一致 | 全部一致 |

**One edge case I tested:**

- Input：6 個人圍成一圈（每個人和左右兩人是朋友），`degrees(circle, 0, 5)`
- Expected output：`1`
- Actual output：`1`

0 往右要走 5 步才到 5，但往左只要 1 步。BFS 同時往兩邊擴散，第一層就碰到 5，確認不會因為朋友名單的順序而走遠路。

### 執行時間（與課堂排整條路線、用 `not in path` 的 BFS 比較，人排成一直線，從頭找到尾）

| 人數 | 課堂寫法 | `degrees` |
|---|---|---|
| 1,000 | 0.0043 秒 | 0.0002 秒 |
| 2,000 | 0.0178 秒 | 0.0003 秒 |
| 4,000 | 0.0781 秒 | 0.0006 秒 |
| 100,000 | （未執行） | 0.018 秒 |

人數變 2 倍，課堂寫法的時間約變 4 倍（每條路線都要複製、用 `in` 查 list），`degrees` 約變 2 倍。

### Why my solution works

BFS 用佇列一層一層往外找：先處理所有 1 度的人，再處理 2 度的人，依此類推。隊伍中的度數只會越來越大，所以第一次碰到 b 的時候，`d + 1` 一定是最少的度數。每個人在第一次被碰到時就記成看過，這時的度數已經是最少的，之後再從別的路碰到他也不會更少，所以跳過不會漏掉更好的答案。如果隊伍空了還沒碰到 b，代表從 a 出發能到的人都看過了，b 不在其中，回傳 `-1`。

### Time complexity

每個人最多被放進隊伍一次（放進去時就記成看過），所以 `while` 迴圈最多執行 n 次；每個人被拿出來時會走過他的朋友名單一次，所有朋友名單的長度加起來是 2m（每組朋友關係在兩邊各出現一次）。查詢和寫入字典、`popleft`、`append` 都是 O(1)，所以總共是 **O(n + m)**（n 為人數，m 為朋友關係的組數）。

## 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**

課堂的 BFS：用佇列一層一層往外找，第一個到達終點的就是邊數最少的。這題只需要度數，所以隊伍裡改排「人和度數」，並把課堂的 `not in path` 改成用字典記錄看過的人。

**One thing I understand better now:**

BFS 和 DFS 差在拿出路線的順序：從隊伍前面拿（先進先出）是 BFS，從後面拿（後進先出）就變成 DFS。另外，記成看過的時間點也會影響效率：放進隊伍時就記，每個人只會排隊一次。

**One thing I am still unsure about:**

如果朋友關係有「親密度」（邊有權重），想找總親密度最高或總距離最短的路線，BFS 就不一定對了。課堂提到可以改用 DFS 比較總權重，但那要試完所有路線，我還不知道有沒有更快的方法。
