**Topic:** Graph-theoretic Models  
**Date:** 2026/11/27

### ① Check My Understanding

Questions completed: **5 / 5**

Answers revised after AI hints: **0 / 5**

### ② My Misconception

**Before: I thought…**

The first path found by DFS might be the shortest path. I also thought that the current node alone could be sufficient as a memoization key in graph search problems.

**Now: I understand…**

DFS does not guarantee that the first path found is the shortest, while BFS guarantees the minimum number of edges in an unweighted graph. When searching for simple paths using recursive DFS and memoization, the state must also account for previously visited nodes because different search histories may impose different constraints on future decisions.

### ③ Challenge the AI

**One AI-generated question I challenged:**

Q1: If there is a directed path from A to E, then there must also be a directed path from E to A because all nodes belong to the same connected structure.

**Why?**

☐ Ambiguous  
☐ Oversimplified  
☐ Technically questionable  
☑ Too easy  
☐ Other

**Brief explanation:**

The question only tests the basic concept that reachability in directed graphs is not necessarily symmetric. A more challenging question could examine reflexivity, symmetry, transitivity, and strongly connected components.

### ④ One-Minute Reflection

**One thing I am still unsure about:**

I am still unsure how shortest-path algorithms handle negative edge weights and negative cycles. I also want to understand when state-space expansion is appropriate for graph optimization problems involving additional resource constraints or path-dependent restrictions, and how it affects computational complexity.