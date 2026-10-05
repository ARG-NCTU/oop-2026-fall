# AI Tutor Learning Record: Part A

Name: Yu-Liang Tan / 譚羽良

Student ID: 112511017

Week: 2

Date: 2026-10-05

Topic: MIT OCW Lecture 6, Recursion, dictionaries, and memoization

Status: New AI-assisted written responses prepared at the student's request. These are new records, not recovered historical sessions. First-person reflections are assisted wording. No one-at-a-time student hint cycle or independent student implementation is claimed.

Format: [Course AI tutor instructions](https://github.com/ARG-NCTU/oop-python-nycu/blob/d4ccf63b9252d0017e84d3bed10628f0f5ea7bc9/ai-tutor-2026.md)

Sources: [MIT lecture slides and code](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/pages/lecture-slides-code/), [course reference code](https://github.com/ARG-NCTU/oop-python-nycu/blob/d4ccf63b9252d0017e84d3bed10628f0f5ea7bc9/src/mit_ocw_exercises/lec6_recursion_dictionaries.py).

## ① Check My Understanding

Questions completed: 5 / 5 written responses supplied with AI assistance.

Answers revised after AI hints: 0 / 5 in this prepared response. The answers were supplied together without an interactive revision round. No historical revision count is claimed.

## ② My Misconception

Before: I could assume that writing a base case automatically makes a recursive function terminate.

Now: I need both a base case and progress toward it. For route counting, every move increases a coordinate and reduces the distance to the destination. A dictionary can also cache a state so repeated visits reuse its result.

## ③ Challenge the AI

One AI-generated question I challenged:

Any function that makes two recursive calls per step has exponential running time.

Why?

- [ ] Ambiguous
- [x] Oversimplified
- [ ] Technically questionable
- [ ] Too easy
- [ ] Other: None

Brief explanation: The number of recursive calls alone does not determine complexity. Their input sizes and repeated subproblems matter. Memoized Fibonacci visits only a linear number of distinct states even though a new state can request two earlier states.

## ④ One-Minute Reflection

One thing I am still unsure about: How can I tell whether a dictionary cache key includes everything needed to identify one subproblem?

## Answers and reasoning

### Question 1

A recursive function always terminates as long as it contains a base case.

Answer: False

My reasoning: The recursive calls must make progress toward the base case. A call that repeats the same input can continue indefinitely without reaching it.

### Question 2

Any function that makes two recursive calls per step has exponential running time.

Answer: False

My reasoning: Complexity depends on the sizes of those calls and whether work is repeated. Caching repeated states can reduce the number of computations substantially.

### Question 3

Assigning a new value to an existing dictionary key updates that entry rather than creating a duplicate key.

Answer: True

My reasoning: A dictionary maps each key to one current value. Reassigning the key changes that value.

### Question 4

Correct memoization can reuse a deterministic subproblem result without changing the result of the recurrence.

Answer: True

My reasoning: The cache stores a result already computed for the same state. Reusing that result avoids work while preserving the recurrence's value.

### Question 5

A cache lookup can prevent recursive evaluation of a subproblem that was already computed.

Answer: True

My reasoning: The function can return the stored value immediately instead of expanding the same recursive calls again.
