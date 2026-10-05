# AI Tutor Learning Record — Week 2

Topic: Recursion and Dictionaries
Date: 2026/09/14

## Part A: True or False

### ① Check My Understanding

Questions completed: 5 / 5

Answers revised after AI hints: 2 / 5


### ② My Misconception

Before: I thought recursion was just a function calling itself repeatedly, and as long as the input became smaller, the function would eventually stop.

Now: I understand that recursion needs both a recursive step and at least one base case. The recursive step must reduce the problem into a smaller version of the same problem, and the base case is what actually stops the recursion.


### ③ Challenge the AI

One AI-generated question I challenged:

> A recursive function does not need a base case if every recursive call uses a smaller input.

Why?

☐ Ambiguous  
☐ Oversimplified  
☑ Technically questionable  
☐ Too easy  
☐ Other: __________

Brief explanation:

Even if the input becomes smaller, the function still needs a condition that stops the recursion.

For example, in the factorial example, the function stops when `n == 1`. Without that base case, the function would continue calling itself.


### ④ One-Minute Reflection

One thing I am still unsure about:

I am still a little confused about the order in which recursive calls return their values, especially when one function creates many different recursive calls.


---

## Part B: Coding Challenge

Name: 高芮妮
Date: 2026/09/14
Topic: Recursion, Dictionaries and Memoization


## 1. Today’s Challenge

Core concept from today’s OCW lecture:

Using recursion to reduce a problem into smaller versions of the same problem, and using a dictionary to remember results that have already been calculated.

AI-generated coding challenge title:

**Fast Staircase Counter**

The challenge asks me to calculate how many different ways a person can reach the top of a staircase if each move can climb either 1 step or 2 steps.

The solution should first use recursion and then use a dictionary to avoid repeating the same calculations.


## 2. My Initial Approach — Before AI Help

Before asking AI for hints, briefly describe how you planned to solve the problem.

My approach:

I noticed that to reach step `n`, the final move must come from either step `n-1` or step `n-2`.

So I planned to use:

`ways(n) = ways(n-1) + ways(n-2)`

I also needed base cases for the smallest values of `n`.


## 3. AI Tutor Help

Did you ask the AI Tutor for help?

☐ No — I solved it independently  
☑ Yes — I received one or more hints

The most useful hint/question from AI was:

> When your recursive function calculates `ways(n-1)` and `ways(n-2)`, are some smaller values being calculated again and again?

It helped me realize that:

The recursive solution repeats many calculations.

For example, different branches of the recursion may both need the result of `ways(3)`.

This is similar to the Fibonacci example in the lecture.


## 4. My Revision

Did you change your approach or code after interacting with AI?

☐ No  
☑ Yes

What did you change, and why?

I added a dictionary to store answers that had already been calculated.

Before making another recursive call, I first checked whether the result already existed in the dictionary.

If it did, I returned the saved result directly.

I changed this because it avoids recalculating the same values many times.


## 5. Verification

My final program:

☑ Passed the provided examples  
☑ Passed additional edge cases  
☐ Still has unresolved problems

One test I tried:

Input:

`n = 1`

Expected output:

`1`

Actual output:

`1`


Another test:

Input:

`n = 5`

Expected output:

`8`

Actual output:

`8`


## 6. One-Minute Reflection

What idea from the OCW lecture did you transfer to this new problem?

I transferred the idea of decreasing a problem into smaller versions of itself and using base cases to stop the recursion.

I also used the dictionary idea from the Fibonacci example to save intermediate results and avoid repeated calculations.

One thing I understand better now:

I understand that recursion is not just “calling the same function again.” Each recursive call solves a smaller version of the problem and has its own scope.

I also understand why dictionaries are useful for memoization.

One thing I am still unsure about:

I am still not completely sure how to compare the efficiency of a normal recursive solution and a memoized recursive solution for very large inputs.