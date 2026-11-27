**Name:** 廖顯祐  
**Date:** 2026/11/27  
**Topic:** Introduction and Optimization Problems

### 1. Today’s Challenge

**Core concept from today’s OCW lecture:**

Optimization problems, objective functions, constraints, greedy algorithms, and global optimality.

**AI-generated coding challenge title:**

Maximum Non-Overlapping Study Sessions

### 2. My Initial Approach — Before AI Help

**My approach:**

I planned to sort all study sessions by their ending times and sequentially select the earliest finishing session that does not overlap with previously selected sessions. I used a variable to track the ending time of the last selected session and a counter to record the total number of selected sessions.

### 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

☑ No — I solved it independently  
☐ Yes — I received one or more hints

**The most useful hint/question from AI was:**

If the first session in an optimal schedule is replaced with the earliest finishing session, will the remaining sessions still be feasible?

**It helped me realize that:**

An exchange argument can be used to prove that a greedy selection does not reduce the quality of an optimal solution, establishing global optimality rather than simply relying on experimental results.

### 4. My Revision

**Did you change your approach or code after interacting with AI?**

☑ No  
☐ Yes

**What did you change, and why?**

No code changes were necessary because my original implementation satisfied the correctness and efficiency requirements. The AI's feedback helped me better understand the mathematical reasoning behind the greedy selection criterion.

### 5. Verification

**My final program:**

☑ Passed the provided examples  
☑ Passed additional edge cases  
☐ Still has unresolved problems

**One edge case I tested through manual tracing:**

Input: `sessions = [[1, 3], [3, 5], [5, 7], [2, 6]]`

Expected output: `3`

Actual output (manual tracing): `3`

### 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**

I applied the greedy algorithm pattern of sorting candidates according to a selection criterion and selecting feasible candidates to maximize an objective function. By choosing sessions with the earliest ending times, I achieved global optimality with O(n log n) time complexity and O(n) auxiliary space.

**One thing I understand better now:**

I better understand that the effectiveness of a greedy algorithm depends on the problem structure and the selection criterion. Unlike the general 0/1 knapsack problem, interval scheduling has a greedy-choice property that guarantees global optimality.

**One thing I am still unsure about:**

I am still unsure how to systematically identify the greedy-choice property in unfamiliar optimization problems and construct rigorous exchange arguments to prove global optimality.