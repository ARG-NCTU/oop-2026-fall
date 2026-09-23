Name: 張永怡
Date: 2026/09/23
Topic: Recursion and Dictionaries

1. Today’s Challenge

Core concept from today’s OCW lecture:

Recursion, divide-and-conquer, and using smaller subproblems to solve a larger problem.

AI-generated coding challenge title:

Robot Grid Paths

2. My Initial Approach — Before AI Help

Before asking AI for hints, briefly describe how you planned to solve the problem.

My approach:

I planned to use recursion. From each position, there are two possible directions, so I would recursively count the paths from both smaller cases and add them together. When there is only one row or one column left, there is only one possible path.

3. AI Tutor Help

Did you ask the AI Tutor for help?

☐ No — I solved it independently
☑ Yes — I received one or more hints

The most useful hint/question from AI was:

The AI asked me to think about what happens when rows == 1 or cols == 1.

It helped me realize that:

This condition can be used as the base case because there is only one possible path when only one row or one column remains.

4. My Revision

Did you change your approach or code after interacting with AI?

☐ No
☑ Yes

What did you change, and why?

I made the base case more specific by returning 1 when rows == 1 or cols == 1. I then used two recursive calls for the two possible directions and added their results together.

5. Verification

My final program:

☑ Passed the provided examples
☑ Passed additional edge cases
☐ Still has unresolved problems

One edge case I tested:

Input: rows = 1, cols = 5

Expected output: 1

Actual output: 1

6. One-Minute Reflection

What idea from the OCW lecture did you transfer to this new problem?

I transferred the idea of recursion and divide-and-conquer by breaking the path-counting problem into smaller versions of the same problem.

One thing I understand better now:

I understand better how to identify a base case and how multiple recursive calls can combine their results to solve a larger problem.

One thing I am still unsure about:

I am still not fully confident about analyzing the time complexity of recursive functions with multiple recursive calls.