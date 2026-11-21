# AI Tutor — Part B | Optimization Lecture 1

**Name:** 范芷祺
**Date:** 2026/11/21
**Topic:** Optimization Problems and Greedy Algorithms
**Record type:** AI-prepared example and reference implementation.

## 1. Today's Challenge

### Core concept from today's OCW lecture:

An optimization problem consists of an objective function and a set of constraints.

A greedy algorithm attempts to optimize the objective by repeatedly selecting the best available option according to a particular criterion.

### Coding challenge title:

[LeetCode #1710 — Maximum Units on a Truck](https://leetcode.com/problems/maximum-units-on-a-truck/)

### Problem Description

Each element in boxTypes contains two integers:

* boxTypes[i][0]: Number of available boxes of this type.
* boxTypes[i][1]: Number of units in each box of this type.

The truck can carry at most truckSize boxes.

Return the maximum total number of units that can be loaded onto the truck.

### Examples

| boxTypes | truckSize | Output |
|---|---:|---:|
| [[1,3],[2,2],[3,1]] | 4 | 8 |
| [[5,10],[2,5],[4,7],[3,9]] | 10 | 91 |
| [[2,4]] | 5 | 8 |

---

## 2. My Initial Approach — Before AI Help

### My approach (sample):

I considered loading boxes in their original input order until the truck reached its maximum capacity.

However, this approach might load boxes containing fewer units before boxes containing more units.

A better approach would prioritize the number of units contained in each box.

### My initial complexity prediction:

If I repeatedly search for the box type containing the largest number of units per box, each search requires O(n) time.

Since there are at most n box types to process, the total worst-case time complexity is O(n²).

---

## 3. AI Tutor Help

### Did you ask the AI Tutor for help?

* [ ] No — I solved it independently
* [x] Yes — AI-generated self-review hint

### The most useful hint/question from AI:

Suppose two available boxes occupy the same amount of truck capacity, but one contains more units than the other.

Is there any reason to choose the box containing fewer units first?

### It helped me realize that:

Every box consumes exactly one unit of truck capacity.

Therefore, choosing the box with the highest number of units per box cannot be worse than choosing a box with fewer units.

Unlike the general 0/1 knapsack problem, all boxes have the same cost in terms of capacity.

---

## 4. My Revision

### Did you change your approach or code after interacting with AI?

* [ ] No
* [x] Yes — illustrative revision

### What did you change, and why?

Instead of loading boxes in their original order, I repeatedly search for the available box type with the highest number of units per box.

I load as many boxes of that type as possible without exceeding the remaining truck capacity.

After processing a box type, I mark it as unavailable by setting its remaining box count to zero.

This implements the greedy selection strategy without using built-in sorting functions.

---

## 5. Verification

### My final program (C++ reference implementation):

```cpp
class Solution {
public:
    int maximumUnits(vector<vector<int>>& boxTypes,
                     int truckSize) {
        int n = boxTypes.size();
        int total = 0;

        while (truckSize > 0) {
            int best = -1;

            for (int i = 0; i < n; i++) {
                if (boxTypes[i][0] > 0) {
                    if (best == -1 ||
                        boxTypes[i][1] > boxTypes[best][1]) {
                        best = i;
                    }
                }
            }

            if (best == -1) {
                break;
            }

            int take = boxTypes[best][0];

            if (take > truckSize) {
                take = truckSize;
            }

            total += take * boxTypes[best][1];
            truckSize -= take;

            boxTypes[best][0] = 0;
        }

        return total;
    }
};
```

### Verification Cases

| boxTypes | truckSize | Expected Output |
|---|---:|---:|
| [[1,3],[2,2],[3,1]] | 4 | 8 |
| [[5,10],[2,5],[4,7],[3,9]] | 10 | 91 |
| [[2,4]] | 5 | 8 |
| [[3,5]] | 1 | 5 |
| [[2,3],[3,3]] | 4 | 12 |
| [[1,1],[1,100]] | 1 | 100 |

### Verification Status

* [x] Normal and edge-case expected outputs identified
* [x] Representative examples manually traced
* [ ] LeetCode submission verified

### One edge case:

**Input:** boxTypes = [[1,1],[1,100]], truckSize = 1

**Expected output:** 100

This case demonstrates why processing the boxes in their original input order is not sufficient.

---

## 6. One-Minute Reflection

### Why does my solution work?

Every box occupies exactly one position in the truck.

If a solution includes a box with fewer units while leaving a box with more units unused, replacing the smaller-value box with the larger-value box increases the total number of units without violating the capacity constraint.

Therefore, selecting boxes in descending order of units per box produces an optimal solution.

### Time Complexity

**Time complexity:** O(n²)

Each iteration searches through all n box types to find the best available type.

There are at most n box types to process.

The algorithm can be improved to O(n log n) by implementing Merge Sort to sort the box types first, followed by a linear scan.

**Auxiliary space complexity:** O(1)

The algorithm only uses a fixed number of integer variables and modifies the input directly.

### What idea from the OCW lecture did I transfer to this new problem?

I transferred the greedy selection strategy from the knapsack problem to another resource-allocation problem.

The truck capacity acts as the constraint, and the total number of units acts as the objective function.

### One thing I understand better now:

Greedy algorithms are not always optimal, but they can produce an optimal solution when the structure of the problem guarantees that each local decision is safe.

### One thing I am still unsure about:

How to construct a formal exchange argument to prove the correctness of more complicated greedy algorithms.