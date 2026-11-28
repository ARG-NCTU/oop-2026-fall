# AI Tutor Learning Record — W11 / MIT 6.0002 Lecture 3

**Name**　劉育麟  
**Date**　2026/11/16（課表日期）  
**OCW Topic**　Graph-theoretic Models  
**課程教材**　[Lecture 3 投影片，第 15–21、25–27、32–36 頁](../material2/MIT6_0002F16_lec3.pdf)

> 初答、提示後的修正與反思採示範作答。Part B 的互動式 Python 範例列出實際執行結果。

---

# Part A: True or False

## ① Check My Understanding

**Questions completed**　5 / 5　｜　**Answers revised after AI hints**　1 / 5（示範第 4 題）

| 題號 | 判斷題 | 初答 → 定稿 | 理由 |
| --- | --- | --- | --- |
| 1 | 課堂的無向 `Graph` 沿用 `Digraph` 的鄰接串列，可用兩條方向相反的邊表示兩個不同節點之間的一條無向邊。 | T → T | `Graph.addEdge` 會插入給定方向，再插入反方向，因此兩端都能在鄰居中找到對方。 |
| 2 | 在每條邊都花一個單位時間的圖中，BFS 第一次到達終點時，已找到邊數最少的路徑。 | T → T | BFS 先處理距離起點較近的層，同一層代表相同的邊數。 |
| 3 | 只要圖中沒有環，DFS 第一條找到的路徑就一定最短。 | F → F | 即使無環，仍可能同時有 `S → A → B → T` 和 `S → T`。先展開 `A` 就可能先找到長路。 |
| 4 | 投影片 BFS 的 `nextNode not in tmpPath` 可以保證每個節點在整次搜尋中最多入列一次。 | T → F | 它只排除當前路徑中已經出現的節點。兩條路可以分別走到同一個節點。 |
| 5 | 如果每條邊的延遲不同，使用相同的 FIFO 佇列順序，第一次到達終點仍一定具有最小總延遲。 | F → F | 假設直達邊花 8 週期，繞經一個節點的兩條邊各花 1 週期，則兩條邊的路徑更快。 |

## ② My Misconception

**Before — I thought…**　我以為 BFS 看過某個節點之後，其他路徑就不會再把它加入佇列。

**Now — I understand…**　設 `S` 分別連到 `A`、`B`，兩者又都連到 `T`。課堂的佇列存整條路徑。`T` 沒在 `[S, A]` 裡，也沒在 `[S, B]` 裡，所以 `[S, A, T]` 和 `[S, B, T]` 都有機會入列。若目的只是求每個節點的最少邊數，則可在節點第一次入列時就標記距離。

## ③ Challenge the AI

**選題**　第 2 題　｜　**原因**　☒ Oversimplified

「最短路徑」要先說明量測單位。如果每經過一條線路就需要一個週期，邊數最少確實也代表時間最短。若每條線路的延遲不同，則需要比較沿路延遲的總和。把同一張圖的邊標上第 5 題的延遲，就能看出 BFS 的保證依賴哪項條件。

## ④ One-Minute Reflection

我還想釐清如果題目要列出所有同長的最短路徑，第一次找到節點之後還要保留哪些資訊。只存一個距離就足夠回答「最快幾步」，卻不足以直接還原所有走法。

---

# Part B: LeetCode-style Lecture Code Transfer

## 1. Today’s Challenge

**Earliest Signal Arrival（每個模組最早收到訊號的週期）**

有 `n` 個模組，以 `0` 到 `n−1` 編號。`links` 中每個 `(u, v)` 表示訊號可由 `u` 傳至 `v`，每條線路恰花一個週期。`sources` 中的模組都在第 0 週期同時收到訊號。回傳長度為 `n` 的串列，第 `i` 格是模組 `i` 最早收到訊號的週期，無法到達時填 `-1`。

`1 ≤ n ≤ 10,000`，端點與起點皆為有效編號。起點可以為空或重複，線路可以重複，也可能形成自環。各線路可同時傳遞。

```pycon
>>> earliest_arrivals(6, [(0, 1), (1, 2), (3, 2), (2, 4)], [0, 3])
[0, 1, 1, 0, 2, -1]
>>> earliest_arrivals(3, [(0, 1), (1, 2)], [2])
[-1, -1, 0]
```

第一例中，模組 2 從模組 0 出發要走兩步，從模組 3 出發只要一步，所以填 1。第二例中線路有方向，訊號無法從模組 2 逆向傳回去。

## 2. My Initial Approach — Before AI Help

我會從每個起點分別跑一次 BFS，再對同一個模組取最小距離。這樣可以求出答案，但若許多起點都能到達同一大片區域，就會重複掃描那些線路。

## 3. AI Tutor Help

**示範提示**　既然所有起點都在第 0 週期收到訊號，能不能先把它們放在同一層？第一個被發現的鄰居此時應記成第幾週期？

所有起點的距離都已知為 0。先讓它們全部入列，之後發現的第一層自然是距離任一起點最近的一步。

## 4. My Revision

我改成一次多起點 BFS。建好有向鄰接串列後，把所有不同起點標成 `0` 並入列。第一次發現鄰居時就寫下距離並入列，讓匯流、環與重複線路都不會造成重複展開。用串列尾端加入元素，另用 `head` 指向下一個要讀的位置。

## 5. Verification

**My final program**

```python
def earliest_arrivals(n, links, sources):
    outgoing = [[] for _ in range(n)]
    for source, target in links:
        outgoing[source].append(target)

    distance = [-1] * n
    queue = []
    for source in sources:
        if distance[source] == -1:
            distance[source] = 0
            queue.append(source)

    head = 0
    while head < len(queue):
        current = queue[head]
        head += 1
        for neighbor in outgoing[current]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)
    return distance
```

- [x] Passed the provided examples
- [x] Passed additional edge cases

**邊界測試**　空起點、單一模組、自環與重複線路、兩路匯流，以及一個起點也可由另一個起點到達。

```pycon
>>> earliest_arrivals(3, [(0, 1)], [])
[-1, -1, -1]
>>> earliest_arrivals(1, [], [0])
[0]
>>> earliest_arrivals(3, [(0, 0), (0, 1), (0, 1), (1, 0)], [0, 0])
[0, 1, -1]
>>> earliest_arrivals(4, [(0, 1), (0, 2), (1, 3), (2, 3)], [0])
[0, 1, 1, 2]
>>> earliest_arrivals(3, [(0, 1), (1, 2)], [0, 1])
[0, 0, 1]
```

## 6. One-Minute Reflection

**正確性**　初始佇列中的模組距離都為 0。距離 `d` 的模組展開時，新發現的鄰居可在 `d+1` 週期到達。如果它有一條更短的路徑，該路徑的前一個模組會位在更早的層，理應早已發現它。因此第一次寫下的距離就是最短距離。佇列清空後仍為 `-1` 的模組，沒有任何起點可沿線路到達。

**複雜度與課程轉用**　令 `V` 是模組數、`E` 是輸入線路筆數、`S` 是輸入起點筆數（含重複）。建圖與初始化需 `O(V + E + S)`，每個已達模組最多入列一次，每條出邊最多掃描一次，整體時間為 `O(V + E + S)`，空間為 `O(V + E)`。講義 `Digraph.childrenOf` 的鄰居在本題可直接用模組編號索引，佇列只需保存節點。

**仍想釐清**　若再要求回傳「最早是哪個起點送達」，同一層可能出現兩個來源都能同時送達。我會先定義平手規則，再決定發現鄰居時要保存哪些來源資訊。
