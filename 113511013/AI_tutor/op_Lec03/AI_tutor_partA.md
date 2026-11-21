# AI Tutor — Part A | Optimization Lecture 3

**Topic:** Graph-theoretic Models — Graph Representation, DFS, BFS, and Shortest Paths
**Date:** 2026/11/21
**Record type:** AI-prepared sample answers and reflections.

## ① Check My Understanding

**Questions completed:** 5 / 5 (AI-prepared responses)
**Answers revised after AI hints:** 0 / 5

### Q1 — Directed and Undirected Graphs

**Statement:** If there is an edge from node A to node B in a directed graph, there must also be an edge from node B to node A.

**Sample answer:** **False.**

Edges in a directed graph have a specific direction.

An edge from A to B does not necessarily imply the existence of an edge from B to A.

In an undirected graph, however, the connection can be traversed in either direction.

**AI self-check question:** If a road is one-way from A to B, can a vehicle legally travel from B to A along the same road?

**Concept learned:** Edge direction determines which transitions are allowed in a graph.

### Q2 — Adjacency List and Adjacency Matrix

**Statement:** An adjacency list is generally more space-efficient than an adjacency matrix when a graph contains relatively few edges.

**Sample answer:** **True.**

An adjacency matrix requires O(V²) space, where V is the number of vertices.

An adjacency list stores the vertices and their neighboring vertices, requiring O(V + E) space, where E is the number of edges.

For a sparse graph, E is much smaller than V².

Therefore, an adjacency list generally requires less memory.

**AI self-check question:** How much memory would an adjacency matrix require for a graph with 1000 vertices but only 100 edges?

**Concept learned:** The appropriate graph representation depends on the structure and density of the graph.

### Q3 — Depth-First Search

**Statement:** The first path found by Depth-First Search must be the shortest path between the starting node and the destination.

**Sample answer:** **False.**

Depth-First Search explores one branch as deeply as possible before backtracking.

It might discover a long path before exploring a shorter alternative.

For example, consider the following directed edges:

* A -> B
* B -> C
* C -> D
* A -> D

Depending on the exploration order, DFS might first discover A -> B -> C -> D.

However, A -> D is a shorter path.

**AI self-check question:** Does DFS explore paths according to their length?

**Concept learned:** DFS can discover a valid path, but the first path it discovers is not necessarily the shortest.

### Q4 — Breadth-First Search

**Statement:** Breadth-First Search guarantees that the first path reaching the destination has the minimum number of edges in an unweighted graph.

**Sample answer:** **True.**

BFS explores nodes in increasing order of their distance from the starting node.

It first explores all nodes one edge away, then all nodes two edges away, and continues level by level.

Therefore, when the destination is first reached, no path containing fewer edges can remain undiscovered.

**AI self-check question:** Can BFS explore a path of length four before processing all paths of length three?

**Concept learned:** BFS uses level-by-level exploration to find shortest paths in unweighted graphs.

### Q5 — Weighted Shortest Paths

**Statement:** Breadth-First Search always finds the minimum-cost path in a graph with different edge weights.

**Sample answer:** **False.**

BFS minimizes the number of edges rather than the sum of their weights.

Consider the following graph:

* A -> B, weight = 1
* B -> C, weight = 1
* A -> C, weight = 10

BFS may select A -> C because it contains only one edge.

However, A -> B -> C has a total cost of 2, which is smaller than 10.

**AI self-check question:** Is a path with fewer edges necessarily cheaper than a path containing more edges?

**Concept learned:** Ordinary BFS guarantees minimum-hop paths, but it does not generally guarantee minimum-weight paths.

---

## ② My Misconception

### Before: I thought…

Both Depth-First Search and Breadth-First Search could find the shortest path simply by terminating when the destination was first reached.

I also thought that BFS would work for weighted graphs in the same way as unweighted graphs.

### Now: I understand…

DFS explores one branch as deeply as possible before backtracking, so the first path it discovers may not be the shortest.

BFS explores nodes level by level, which guarantees the minimum number of edges in an unweighted graph.

However, when edges have different weights, the path with the fewest edges may not have the smallest total cost.

Therefore, the choice of graph search algorithm depends on the objective of the problem.

---

## ③ Challenge the AI

### One AI-generated question I challenged:

Q4 — Breadth-First Search guarantees that the first path reaching the destination has the minimum number of edges.

### Why?

* [x] Ambiguous
* [ ] Oversimplified
* [x] Technically questionable
* [ ] Too easy
* [ ] Other

### Brief explanation:

The statement is correct for minimum-hop shortest paths.

However, the term "shortest path" can refer either to the minimum number of edges or the minimum total edge weight.

These are different optimization objectives when edge weights are unequal.

The question should explicitly distinguish unweighted shortest paths from weighted shortest paths.

---

## ④ One-Minute Reflection

### One thing I am still unsure about:

How to efficiently find the shortest path when the edges have different weights.

I would also like to understand the difference between using a visited array for ordinary graph traversal and tracking only nodes in the current path when searching for multiple possible paths.