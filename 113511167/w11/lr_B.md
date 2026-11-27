**Name:** 廖顯祐  
**Date:** 2026/11/27  
**Topic:** Graph-theoretic Models

### 1. Today’s Challenge

**Core concept from today’s OCW lecture:**

Directed graphs, adjacency lists, breadth-first search (BFS), shortest-path search, cycle handling, and state representation.

**AI-generated coding challenge title:**

Shortest Route with Limited Access Passes

### 2. My Initial Approach — Before AI Help

**My approach:**

I planned to represent the directed graph using an adjacency list and apply BFS to find the shortest feasible route. Instead of tracking only the current node, I represented each state as a tuple containing the current node and the number of remaining access passes. I used a dictionary to record visited states and their distances, and a queue to explore states in increasing order of distance.

### 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

☑ No — I solved it independently  
☐ Yes — I received one or more hints

**The most useful hint/question from AI was:**

Can a route that reaches a node earlier but has fewer remaining access passes always replace a route that arrives later with more passes?

**It helped me realize that:**

Reaching a node earlier does not necessarily make a route better when additional resource constraints exist. Different remaining access passes can lead to different feasible future paths, so they must be considered when defining search states.

### 4. My Revision

**Did you change your approach or code after interacting with AI?**

☑ No  
☐ Yes

**What did you change, and why?**

No changes were necessary because my original implementation correctly handled resource constraints, cycles, and shortest-path search. The AI introduced dominance pruning as a potential further optimization.

### 5. Verification

**My final program:**

☑ Passed the provided examples  
☑ Passed additional edge cases  
☐ Still has unresolved problems

**One edge case I tested through manual tracing:**

Input: `n = 3, roads = [[0, 1, 1], [1, 2, 0]], start = 0, target = 2, k = 0`

Expected output: `-1`

Actual output (manual tracing): `-1`

### 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**

I transferred the adjacency-list representation and BFS shortest-path search from Lecture 3 to a resource-constrained graph problem. I combined these concepts with the state representation techniques from Lecture 2, achieving an expected time complexity of O((V+E)(k+1)) and an auxiliary space complexity of O(V(k+1)+E).

**One thing I understand better now:**

I better understand how state-space expansion transforms a constrained optimization problem into a standard shortest-path search problem while preserving the optimality guarantee of BFS.

**One thing I am still unsure about:**

I am still unsure how to systematically identify dominated states and apply dominance pruning to reduce time and memory consumption without eliminating potentially optimal routes.