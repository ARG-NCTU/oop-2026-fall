**Name:** 廖顯祐  
**Date:** 2026/11/23  
**Topic:** Recursion, Dictionaries, Memoization

## 1. Today’s Challenge

**Core concept from today’s OCW lecture:**

Using recursion to divide a problem into smaller subproblems, defining correct base cases, and using dictionaries for memoization to avoid repeated calculations.

**AI-generated coding challenge title:**

Robot Paths with Obstacles

## 2. My Initial Approach — Before AI Help

**My approach:**

I planned to define a recursive function that counts the number of valid paths from the current position to the destination. Since the robot can only move right or down, the total number of paths is the sum of the results from these two directions. I would return 0 for obstacles or out-of-bounds positions and 1 when reaching the destination. I also planned to use a dictionary with coordinate tuples as keys to store previously calculated results.

## 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

☑ No — I solved it independently  
☐ Yes — I received one or more hints

**The most useful hint/question from AI was:**

The AI asked me to consider how many unique states exist in the grid and how deep the recursion call stack could become.

**It helped me realize that:**

Memoization reduces repeated calculations by ensuring each valid state is fully computed at most once. I also learned to analyze the dictionary storage and recursion stack separately when calculating space complexity.

## 4. My Revision

**Did you change your approach or code after interacting with AI?**

☑ No  
☐ Yes

**What did you change, and why?**

My original algorithm and implementation were correct and passed all tests without modification. The AI's feedback helped me strengthen my explanation of why the algorithm works and why memoization reduces the time complexity to O(mn).

## 5. Verification

**My final program:**

☑ Passed the provided examples  
☑ Passed additional edge cases  
☐ Still has unresolved problems

**One edge case I tested:**

Input:
```python
grid = [[1, 0], [0, 0]]
```

**Expected output:** `0`

**Actual output:** `0`

The starting position is blocked, so no valid path exists.

## 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**

I applied recursion and dictionary-based memoization to a two-dimensional path-counting problem. I used recursive calls to solve smaller subproblems and stored their results in a dictionary using coordinate tuples as keys.

**One thing I understand better now:**

I understand how to define meaningful recursive return values and base cases. I also learned that memoization can reduce exponential repeated computation to O(mn) time by avoiding recalculation of the same states.

**One thing I am still unsure about:**

How to design recursive algorithms when the problem contains cycles or allows movement in multiple directions, and how to guarantee termination and correctness in those situations.