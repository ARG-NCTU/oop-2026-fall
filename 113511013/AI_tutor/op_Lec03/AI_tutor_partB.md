# AI Tutor — Part B | Optimization Lecture 3

**Name:** 范芷祺
**Date:** 2026/11/21
**Topic:** Graph Representation, Breadth-First Search, and Shortest Paths
**Record type:** AI-prepared example and reference implementation.

## 1. Today's Challenge

### Core concept from today's OCW lecture:

A graph consists of vertices and edges that represent relationships between different objects.

Breadth-First Search explores vertices in increasing order of distance from the starting vertex.

Therefore, it can be used to find the shortest path in an unweighted graph.

### Coding challenge title:

[LeetCode #1091 — Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/)

### Problem Description

Given an n x n binary matrix grid, return the length of the shortest clear path from the top-left cell to the bottom-right cell.

A clear path must satisfy the following conditions:

* Every cell in the path must contain 0.
* Adjacent cells can be connected horizontally, vertically, or diagonally.
* The path length is the number of cells visited, including the starting and ending cells.

If no valid path exists, return -1.

### Examples

| grid | Output |
|---|---:|
| [[0,1],[1,0]] | 2 |
| [[0,0,0],[1,1,0],[1,1,0]] | 4 |
| [[1,0,0],[1,1,0],[1,1,0]] | -1 |

---

## 2. My Initial Approach — Before AI Help

### My approach (sample):

I initially considered using Depth-First Search to explore all possible paths from the top-left cell to the bottom-right cell.

Each recursive call would examine the eight neighboring cells.

Whenever a valid path reached the destination, I would compare its length with the shortest path discovered so far.

I would also need to prevent the algorithm from revisiting a cell within the current path.

### My initial complexity prediction:

Although DFS can find the shortest path by examining every possible simple path, the number of possible paths may become exponentially large.

Therefore, this approach is inefficient for a large matrix.

Returning immediately when DFS first reaches the destination would be faster, but it would not guarantee the shortest path.

---

## 3. AI Tutor Help

### Did you ask the AI Tutor for help?

* [ ] No — I solved it independently
* [x] Yes — AI-generated self-review hint

### The most useful hint/question from AI:

Every movement between two neighboring cells has the same cost.

Which graph traversal algorithm explores all positions at distance k before exploring positions at distance k + 1?

### It helped me realize that:

The matrix can be represented as an unweighted graph.

Each cell containing 0 represents a vertex, and each valid movement between neighboring cells represents an edge.

Since all movements have the same cost, Breadth-First Search can guarantee that the first time the destination is reached corresponds to the shortest path.

---

## 4. My Revision

### Did you change your approach or code after interacting with AI?

* [ ] No
* [x] Yes — illustrative revision

### What did you change, and why?

I replaced Depth-First Search with Breadth-First Search.

I use a queue to store cells that have been discovered but have not yet been processed.

The algorithm starts from the top-left cell and explores all eight possible neighboring directions.

Whenever a valid cell is added to the queue, I mark it as visited by changing its value to 1.

I process the queue level by level and increase the path length after completing each level.

When the destination is reached, I return the current path length.

If the queue becomes empty before reaching the destination, I return -1.

---

## 5. Verification

### My final program (C++ reference implementation):

```cpp
class Solution {
public:
    int shortestPathBinaryMatrix(
        vector<vector<int>>& grid) {

        int n = grid.size();

        if (grid[0][0] == 1 ||
            grid[n - 1][n - 1] == 1) {
            return -1;
        }

        int dx[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
        int dy[8] = {-1, 0, 1, -1, 1, -1, 0, 1};

        queue<pair<int, int>> q;

        q.push({0, 0});

        grid[0][0] = 1;

        int distance = 1;

        while (!q.empty()) {
            int levelSize = q.size();

            for (int i = 0; i < levelSize; i++) {
                int x = q.front().first;
                int y = q.front().second;

                q.pop();

                if (x == n - 1 && y == n - 1) {
                    return distance;
                }

                for (int d = 0; d < 8; d++) {
                    int nx = x + dx[d];
                    int ny = y + dy[d];

                    if (nx >= 0 && nx < n &&
                        ny >= 0 && ny < n &&
                        grid[nx][ny] == 0) {

                        q.push({nx, ny});

                        grid[nx][ny] = 1;
                    }
                }
            }

            distance++;
        }

        return -1;
    }
};
```

### Verification Cases

| Input | Expected Output |
|---|---:|
| [[0,1],[1,0]] | 2 |
| [[0,0,0],[1,1,0],[1,1,0]] | 4 |
| [[1,0,0],[1,1,0],[1,1,0]] | -1 |
| [[0]] | 1 |
| [[1]] | -1 |
| [[0,0],[0,1]] | -1 |
| [[0,1,0],[1,1,1],[0,1,0]] | -1 |
| [[0,0,0],[0,0,0],[0,0,0]] | 3 |

### Verification Status

* [x] Normal and edge-case expected outputs identified
* [x] Representative examples manually traced
* [ ] LeetCode submission verified

### One edge case:

**Input:** grid = [[0]]

**Expected output:** 1

The matrix contains only one cell, so the starting position is also the destination.

The algorithm must return 1 instead of 0 because the problem defines path length as the number of visited cells rather than the number of edges.

Another important case is:

**Input:** grid = [[0,1],[1,0]]

**Expected output:** 2

This verifies that diagonal movement is correctly supported.

---

## 6. One-Minute Reflection

### Why does my solution work?

Breadth-First Search explores vertices in increasing order of their distance from the starting vertex.

At each iteration, the queue contains cells belonging to the current distance level and cells discovered for the following level.

When the destination is removed from the queue, all cells that could be reached at smaller distances have already been processed.

Therefore, the current distance must represent the shortest possible path.

Marking a cell as visited when it is inserted into the queue also prevents repeated exploration of the same cell.

### Time Complexity

**Time complexity:** O(n²)

The matrix contains at most n² cells.

Each cell is inserted into the queue at most once.

For each cell, the algorithm examines eight possible neighboring cells, which requires constant time.

Therefore:

T(n) = O(8n²) = O(n²)

**Auxiliary space complexity:** O(n²)

In the worst case, the queue may store up to O(n²) cells.

Because I use the original matrix to record visited cells, I do not require an additional visited matrix.

### What idea from the OCW lecture did I transfer to this new problem?

I transferred the lecture's Breadth-First Search algorithm from a city-based graph to a two-dimensional matrix.

Instead of explicitly constructing an adjacency list, I generate neighboring vertices directly using the eight possible movement directions.

I also applied the shortest-path property of BFS and the concept of preventing repeated visits.

### One thing I understand better now:

A graph does not necessarily need to be represented explicitly using vertices and adjacency lists.

A matrix can also represent a graph implicitly, where each cell is a vertex and valid movements represent edges.

I also understand why BFS is more suitable than DFS for finding the shortest path in an unweighted graph.

### One thing I am still unsure about:

How to modify a graph search algorithm when different movements have different costs.

I would like to learn how weighted shortest-path algorithms work and how they differ from ordinary Breadth-First Search.