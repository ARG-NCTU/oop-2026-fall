# AI Tutor for AOOP 2026 - Week 11 Learning Record

## Part A: True or False

**Topic:** Graph-theoretic Models, DFS & BFS (6.0002 Lecture 3)  
**Date:** 2026-11-22

### ① Check My Understanding
* **Questions completed:** 5 / 5
* **Answers revised after AI hints:** 1 / 5 (Revised Question 4 after clarifying why standard BFS only guarantees minimum hop count rather than minimum weighted sum)

### ② My Misconception
* **Before:** I used to think that Breadth-First Search (BFS) also finds the shortest weighted path because it expands outward layer by layer from the source node.
* **Now:** I understand that standard BFS explores paths in increasing order of edge count (hops), which guarantees the shortest unweighted path, but a path with more hops can have a smaller total edge weight. In contrast, DFS can be modified to track cumulative edge weights and find the true shortest weighted path.

### ③ Challenge the AI
* **One AI-generated question I challenged:** Question 4
* **Why?**
  - [x] Ambiguous
  - [ ] Oversimplified
  - [ ] Technically questionable
  - [ ] Too easy
  - [ ] Other: __________________
* **Brief explanation:** Standard BFS is naturally associated with "shortest path" in introductory problems, so without explicitly contrasting hop count against edge weights, it is easy to assume BFS optimizes total path weight as well.

### ④ One-Minute Reflection
* **One thing I am still unsure about:** How Dijkstra's algorithm improves upon weighted DFS by using a priority queue (min-heap) to find shortest weighted paths in graphs with non-negative edge weights without exploring redundant paths.

---

## Part B: LeetCode-style Lecture Code Transfer

**Name:** [ 請填寫你的姓名 / 學號 ]  
**Date:** 2026-11-22  
**Topic:** Graph OOP Hierarchy (`Digraph` / `Graph`), Substitution Rule & BFS Shortest Path

### 1. Today’s Challenge
* **Core concept from today’s OCW lecture:** Modeling networks using `Node`, `Edge`, `Digraph`, and `Graph` (where `Graph` subclasses `Digraph` following the Substitution Rule), and implementing Breadth-First Search (`BFS`) with cycle avoidance to find the shortest unweighted path.
* **AI-generated coding challenge title:** City Route Network & BFS Shortest Path (`Digraph`, `Graph`, `shortest_path_bfs`)

### 2. My Initial Approach — Before AI Help
* **My approach:** Implemented `Node`, `Edge`, `Digraph` (using an adjacency list dictionary `self.edges`), and `Graph(Digraph)` with type and membership validation (`isinstance` and `has_node`). Implemented `shortest_path_bfs` using a FIFO path queue (`path_queue.pop(0)`) and checked `if neighbor not in tmp_path:` to prevent infinite loops on cyclic graphs.

### 3. AI Tutor Help
* **Did you ask the AI Tutor for help?**
  - [x] No — I solved it independently
  - [ ] Yes — I received one or more hints
* **The most useful hint/question from AI was:** N/A (Solved independently; received structural refactoring tips on calling `super().add_edge()` in `Graph` and accessing neighbors via `children_of()`)
* **It helped me realize that:** Delegating edge insertion to `super().add_edge()` in `Graph` avoids duplicating validation logic, and encapsulating neighbor lookups inside `children_of()` keeps `shortest_path_bfs` decoupled from internal dictionary representations.

### 4. My Revision
* **Did you change your approach or code after interacting with AI?**
  - [ ] No
  - [x] Yes
* **What did you change, and why?** Refactored `Graph.add_edge` to invoke `super().add_edge()` for both directions, added `children_of(node)` to `Digraph` for proper encapsulation, and enforced non-empty string validation in `Node.__init__`.

### 5. Verification
* **My final program:**
  - [x] Passed the provided examples
  - [x] Passed additional edge cases
  - [ ] Still has unresolved problems
* **One edge case I tested:**
  - **Input:** `shortest_path_bfs(g, g.get_node('Chicago'), g.get_node('Boston'))` on the directed city graph
  - **Expected output:** `None` (no directed path exists from Chicago back to Boston despite cycles in the graph)
  - **Actual output:** `None`

### 6. One-Minute Reflection
* **What idea from the OCW lecture did you transfer to this new problem?** Applying the Liskov Substitution Principle by making `Graph` a subclass of `Digraph` so a single `shortest_path_bfs` function works on both directed and undirected graphs, while using path-membership checks to handle cycles safely.
* **One thing I understand better now:** Why `Graph` should inherit from `Digraph` (every undirected graph is a symmetric directed graph) and how FIFO path queues guarantee minimum-hop paths in unweighted graphs.
* **One thing I am still unsure about:** The time and space complexity overhead of copying path lists (`tmp_path.copy()`) in `path_queue` compared to maintaining a `visited` set and a `parent` backpointer dictionary on very large graphs.