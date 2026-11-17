<!-- AI prompt
I just learned Graph-theoretic Models (Node / Edge / Digraph / Graph classes, depth-first search and breadth-first search for shortest paths) in today's lecture.

Act as my AI Tutor.

1. Generate 5 True/False questions, one question at a time, to test my conceptual understanding of today's topic.
2. Focus on concepts and reasoning, not memorization or Python syntax.
3. After I answer, do not immediately tell me the correct answer.
4. If my answer or reasoning is incorrect, give me a hint, counterexample, or follow-up question.
5. Let me revise my answer before explaining the concept.
6. Adjust the difficulty based on my responses.
7. After five questions, ask me to identify one question that may be ambiguous, misleading, too easy, or technically questionable.
8. Finish by asking me what misconception I corrected and what I am still unsure about.
-->

# 📝 Learning Reflection & Concept Check — Part A

**Topic:** Graph-theoretic Models, DFS, BFS (MIT 6.0002 Lecture 3)  
**Date:** 2026-11-16  

---

### ① Check My Understanding

* **Questions completed:** 5 / 5
* **Hints requested before answering:** 1 / 5  

| 題號 | 主題 | 我的答案 | 結果 |
| :--- | :--- | :--- | :--- |
| Q1 | 刪掉 `DFS` 中的 `if node not in path` 是否只是變慢、結果仍正確 | False | ✅ 看提示後答對 |
| Q2 | 邊加上權重後，`BFS` 找到的第一條路徑是否一定是總距離最短 | False | ✅ 一次答對 |
| Q3 | 連續兩次 `addNode(Node('Boston'))` 是否一定拋出 `ValueError` | False | ✅ 一次答對 |
| Q4 | 有等長路徑時，DFS 版與 BFS 版 `shortestPath` 是否回傳同一條路徑 | False | ✅ 看提示後答對 |
| Q5 | `buildCityGraph(Graph)` 中 `childrenOf(Boston)` 的 `Providence` 是否只出現一次 | False | ✅ 一次答對 |

---

### ② My Misconception

**Before: I thought…**  
Q4 看提示前沒有直接作答。原本以為 DFS 和 BFS 都保證找到最短路徑，回傳的應該就是同一條；也沒注意到剪枝條件 `len(path) < len(shortest)` 比的是「目前已走的節點數」。

⸻

**Now: I understand…**  
DFS 走到倒數第二個節點時，`len(path)` 仍小於 `len(shortest)`，所以會繼續找到另一條等長路徑並覆蓋 `shortest`。遇到等長路徑時，DFS 回傳最後找到的那條，BFS 回傳最先找到的那條，兩者可能不同。所以 docstring 寫的是「Returns **a** shortest path」，只保證回傳其中一條最短路徑。

---

### ③ Challenge the AI

**One AI-generated question I challenged:**  
Q5：「用 `buildCityGraph(Graph)`（無向版）建圖。`Graph.addEdge` 會自動補上反向邊，而 `buildCityGraph` 同時加了 `Boston → Providence` 和 `Providence → Boston`。因此在這張圖中，`g.childrenOf(g.getNode('Boston'))` 裡的 `Providence` 只會出現一次。」

⸻

**Why?**

* [ ] Ambiguous
* [ ] Oversimplified
* [ ] Technically questionable
* [ ] Too easy
* [x] Other

**Brief explanation:**  
程式相關的題目要附上原始程式碼，不然根本不知道函式的功能和定義。這題需要知道 `Digraph.addEdge` 只檢查節點、不檢查重複邊，也需要知道 `buildCityGraph` 完整的加邊順序，但題目都沒有附上。（題號是採用 AI 建議的 Q5。）

**改寫建議：**  

> 已知以下程式碼：
> ```python
> class Digraph(object):
>     def addEdge(self, edge):
>         src = edge.getSource()
>         dest = edge.getDestination()
>         if not (src in self.edges and dest in self.edges):
>             raise ValueError('Node not in graph')
>         self.edges[src].append(dest)
>
> class Graph(Digraph):
>     def addEdge(self, edge):
>         Digraph.addEdge(self, edge)
>         rev = Edge(edge.getDestination(), edge.getSource())
>         Digraph.addEdge(self, rev)
>
> g = Graph()
> # add nodes Boston, Providence ...
> g.addEdge(Edge(boston, providence))
> g.addEdge(Edge(providence, boston))
> ```
> 執行後，`g.childrenOf(boston)` 中的 `providence` 只出現一次。（答案：False）

---

### ④ One-Minute Reflection

**One thing I am still unsure about:**  
沒有。

⸻
