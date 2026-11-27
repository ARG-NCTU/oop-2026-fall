**Name:** 廖顯祐  
**Date:** 2026/11/27  
**Topic:** Optimization Problems and Dynamic Programming

### 1. Today’s Challenge

**Core concept from today’s OCW lecture:**

Recursive optimization, dynamic programming, memoization, optimal substructure, overlapping subproblems, and pruning.

**AI-generated coding challenge title:**

Minimum-Cost Robot Navigation

### 2. My Initial Approach — Before AI Help

**My approach:**

I planned to use recursive dynamic programming with a dictionary to store previously computed results. Each state consists of the current row, column, and number of remaining coupons. At each cell, I considered whether to pay the energy cost or use a coupon, then explored both possible movement directions. I also introduced a pruning condition to terminate the search when the remaining coupons could cover all remaining cells.

### 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

☑ No — I solved it independently  
☐ Yes — I received one or more hints

**The most useful hint/question from AI was:**

Would the pruning strategy still guarantee global optimality if negative energy costs were allowed?

**It helped me realize that:**

The pruning strategy is valid because all energy costs are non-negative, making zero the theoretical lower bound. An optimization technique must be justified by the problem's constraints rather than simply reducing computational work.

### 4. My Revision

**Did you change your approach or code after interacting with AI?**

☑ No  
☐ Yes

**What did you change, and why?**

No changes were necessary because my original implementation satisfied the correctness and efficiency requirements. The AI identified a redundant condition in my base case, but it did not affect correctness.

### 5. Verification

**My final program:**

☑ Passed the provided examples  
☑ Passed additional edge cases  
☐ Still has unresolved problems

**One edge case I tested through manual tracing:**

Input: `grid = [[7]], k = 1`

Expected output: `0`

Actual output (manual tracing): `0`

### 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**

I transferred the memoized recursive optimization pattern from the 0/1 knapsack problem to a resource-constrained navigation problem. By defining a complete state and reusing previously computed results, I reduced exponential recursive exploration to an expected time complexity of O(mn(k+1)).

**One thing I understand better now:**

I better understand how state representation determines the correctness and efficiency of dynamic programming. I also learned how memoization and pruning can work together to eliminate unnecessary computations while preserving global optimality.

**One thing I am still unsure about:**

I am still unsure how to systematically design the smallest sufficient state representation for more complex optimization problems and identify effective pruning conditions without accidentally eliminating globally optimal solutions.