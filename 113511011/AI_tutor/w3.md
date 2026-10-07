# AI Tutor for AOOP 2026

## Part A: True or False

### AI Tutor Learning Cycle (ATLC) — Suggested Student Prompt:

```

I just learned Testing, Debugging, Exceptions, and Assertions in today’s lecture.

Act as my AI Tutor.

1. Generate 5 True/False questions, one question at a time, to test my conceptual understanding of today’s topic.
2. Focus on concepts and reasoning, not memorization or Python syntax.
3. After I answer, do not immediately tell me the correct answer.
4. If my answer or reasoning is incorrect, give me a hint, counterexample, or follow-up question.
5. Let me revise my answer before explaining the concept.
6. Adjust the difficulty based on my responses.
7. After five questions, ask me to identify one question that may be ambiguous, misleading, too easy, or technically questionable.
8. Finish by asking me what misconception I corrected and what I am still unsure about.
```

### AI Tutor Learning Record

```
Topic: Testing, Debugging, Exceptions, and Assertions
Date: 9/19

========================================
Part A: True or False
========================================

① Check My Understanding

Questions completed: 5 / 5

Answers revised after AI hints: 2 / 5


Question 1:
True or False:
If a program runs without producing an exception, then the program is correct.

My answer:
False.

Reason:
A program may run successfully but still contain logic errors. For example, it may return the wrong result even though there is no SyntaxError, TypeError, or other exception.


Question 2:
True or False:
A path-complete glass-box test suite guarantees that a program is correct.

My first answer:
True.

AI hint:
Consider a function whose branches are both tested, but the condition contains an incorrect boundary such as x < -1 instead of x < 0.

My revised answer:
False.

Reason:
A path-complete test suite only guarantees that every execution path has been tested at least once. It may still miss important boundary cases. For example, abs(-1) may fail even if both branches of the function have already been tested.


Question 3:
True or False:
Black-box testing is based mainly on the program's implementation.

My answer:
False.

Reason:
Black-box testing is based on the specification, not the internal implementation. Test cases are designed from input partitions, expected behavior, and boundary conditions.


Question 4:
True or False:
When an exception is caught by an except block, the programmer must always continue execution normally.

My first answer:
True.

AI hint:
What happens in the following code?

except:
    raise ValueError("bad argument")

My revised answer:
False.

Reason:
An except block catches an exception, but the programmer can decide what to do next. The program may recover, return a special value, print a warning, or raise another exception.


Question 5:
True or False:
Assertions are mainly used to handle normal bad input from users.

My answer:
False.

Reason:
Assertions are mainly used to check assumptions and invariants that the programmer expects to always be true. User input errors are usually better handled with exceptions such as ValueError.


② My Misconception

Before: I thought…

I thought that once an exception was caught by except, the error was finished and the program should continue normally. I also thought that raise ValueError("invalid argument") was similar to returning the string "invalid argument".


Now: I understand…

Now I understand that raise and return are different.

return sends a normal result back to the caller.

raise creates an exception and interrupts the normal execution flow.

An except block catches an exception, but it can still raise another exception. For example:

except:
    raise ValueError("get_ratios called with bad arg")

This catches a lower-level error and changes it into a ValueError that better explains that the function received an invalid argument.


③ Challenge the AI

One AI-generated question I challenged:

"A path-complete glass-box test suite guarantees that a program is correct."


Why?

[x] Ambiguous
[x] Oversimplified
[ ] Technically questionable
[ ] Too easy
[ ] Other: __________


Brief explanation:

At first, "path-complete" sounds very strong because every execution path is tested. However, the lecture shows that path coverage alone is not enough. A boundary value may still reveal a bug even when every branch has already been executed.

For example:

def abs(x):
    if x < -1:
        return -x
    else:
        return x

Testing x = -2 and x = 2 covers both paths, but x = -1 still produces an incorrect result.


④ One-Minute Reflection

One thing I am still unsure about:

I am still slightly unsure about when I should catch an exception and handle it inside a function, and when I should raise the exception so that the caller handles it instead.

My current understanding is that if the function has a reasonable recovery policy, it can handle the exception. If it cannot produce a result that matches its specification, it should usually raise an exception.
```

## Part B: **LeetCode-style** Lecture Code Transfer

AI Tutor Learning Cycle (ATLC) — Suggested Student Prompt:

```
I have just studied the following lecture code from today’s OCW programming lecture.

[LECTURE CODE]

Act as my AI Tutor.

Based on the concepts and programming patterns demonstrated in the lecture code, generate ONE new LeetCode-style programming challenge.

Requirements:

1. Test the same core concept as the lecture code.
2. Do not simply ask me to reproduce or slightly modify the lecture example.
3. Create a new problem that requires me to transfer what I learned.
4. Use only programming concepts that have been covered in the course so far.
5. Provide:
    * Problem statement
    * Input/output specification
    * Constraints
    * 2–3 examples
6. Do NOT provide code, pseudocode, or the solution.

Before I write code:

7. Ask me to explain my proposed algorithm.
8. Ask me to identify which concept from the lecture code I am applying.
9. If my reasoning is incorrect, give me a hint or counterexample instead of the answer.

After I write my code:

10. Test my solution using normal and edge cases.
11. If my code fails, help me identify the problem without rewriting the solution for me.
12. Ask me to revise my solution.

Finally, ask me to explain:

* Why my solution works
* Its time complexity
* What idea from the lecture code I transferred to this new problem

```

### AI Tutor Learning Record — Coding Challenge

```
Name: 程婕茵
Date: 9/19
Topic: Exceptions, Defensive Programming, and Input Validation


1. Today’s Challenge

Core concept from today’s OCW lecture:

Using exceptions to deal with unexpected conditions, validating assumptions about input, and raising an exception when a function cannot produce a valid result according to its specification.


AI-generated coding challenge title:

Safe Matrix Column Averages


Problem Statement:

You are given a two-dimensional list called matrix.

Each inner list represents one row of numeric data.

Write a function that returns a list containing the average of each column.

All rows are expected to have the same length.

If matrix is empty, return an empty list.

If any row has a different length from the first row, the input violates the function's assumptions and the function should raise a ValueError.

You may assume that all elements inside valid rows are numbers.


Input / Output Specification:

Input:
A list of lists of numbers.

Output:
A list where result[i] is the average of column i.

If matrix is empty:
Return [].

If rows have different lengths:
Raise ValueError.


Constraints:

1. matrix may be empty.
2. Each valid row contains only numbers.
3. All valid rows should have equal length.
4. Do not use libraries that have not been covered in the course.
5. Use loops, lists, functions, conditionals, and exception-related concepts from the lecture.


Examples:

Example 1

Input:
[
    [1, 2, 3],
    [4, 5, 6]
]

Output:
[2.5, 3.5, 4.5]


Example 2

Input:
[
    [10, 20],
    [30, 40],
    [50, 60]
]

Output:
[30.0, 40.0]


Example 3

Input:
[
    [1, 2],
    [3, 4, 5]
]

Output:
ValueError


2. My Initial Approach — Before AI Help

Before asking AI for hints, briefly describe how you planned to solve the problem.

My approach:

First, I would check whether matrix is empty. If it is empty, I would return an empty list.

Then I would use the length of the first row as the expected number of columns.

Before calculating averages, I would check every row to make sure its length is equal to the first row's length.

If a row has a different length, I would raise a ValueError because the input violates the function's specification.

If the input is valid, I would create a result list.

For each column, I would loop through all rows, add the values in that column, divide by the number of rows, and append the average to the result list.

Finally, I would return the result list.


Concept from the lecture that I am applying:

I am applying defensive programming and exception handling.

The function has an assumption that all rows have equal length. Instead of allowing an IndexError to happen later during the calculation, I check the assumption early and raise a ValueError when the input is invalid.


3. AI Tutor Help

Did you ask the AI Tutor for help?

[ ] No — I solved it independently
[x] Yes — I received one or more hints


The most useful hint/question from AI was:

"Should you wait for an IndexError to happen while accessing a missing column, or can you detect the invalid structure before starting the calculation?"


It helped me realize that:

It is better to validate the structure of the matrix before doing the main computation.

This makes the error easier to understand and follows the lecture's idea of defensive programming: detect problems close to where they are introduced instead of allowing bad data to propagate.


4. My Revision

Did you change your approach or code after interacting with AI?

[ ] No
[x] Yes


What did you change, and why?

Originally, I planned to calculate each column directly and use try/except to catch IndexError if a row was too short.

After thinking about the lecture, I changed my approach.

I decided to check all row lengths before calculating the averages.

If a row length is incorrect, I raise ValueError immediately.

This is clearer because an inconsistent row length means the argument itself is invalid. It also prevents a lower-level IndexError from appearing later in the computation.


5. Verification

My final program:

[x] Passed the provided examples
[x] Passed additional edge cases
[ ] Still has unresolved problems


One edge case I tested:

Input:
[]

Expected output:
[]

Actual output:
[]


Another edge case I considered:

Input:
[
    [5]
]

Expected output:
[5.0]

Actual output:
[5.0]


Invalid-input edge case:

Input:
[
    [1, 2, 3],
    [4, 5]
]

Expected output:
ValueError

Actual output:
ValueError


6. One-Minute Reflection

What idea from the OCW lecture did you transfer to this new problem?

I transferred the idea that a function should check important assumptions about its inputs and should raise an exception when it cannot produce a result that satisfies its specification.

Instead of simply allowing an unrelated IndexError to occur later, the function can detect an invalid argument and raise ValueError with a clearer meaning.


One thing I understand better now:

I understand the difference between catching an exception and raising an exception.

except catches an exception that has already occurred.

raise creates a new exception and sends the error to the caller.

I also understand why code such as:

except:
    raise ValueError("get_ratios called with bad arg")

can be useful.

The except block catches a lower-level problem, but the function does not know how to recover from it. Therefore, it raises a clearer ValueError to tell the caller that the arguments do not satisfy the function's assumptions.


One thing I am still unsure about:

I am still unsure about how specific exception handling should be in larger programs.

For example, I want to understand better when it is appropriate to convert one exception type into another exception type, and when it is better to let the original exception continue to the caller.

```
