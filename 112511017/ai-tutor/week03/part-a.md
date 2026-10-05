# AI Tutor Learning Record: Part A

Name: Yu-Liang Tan / 譚羽良

Student ID: 112511017

Week: 3

Date: 2026-10-05

Topic: MIT OCW Lecture 7, Testing, debugging, exceptions, assertions, and boundary cases

Status: New AI-assisted written responses prepared at the student's request. These are new records, not recovered historical sessions. First-person reflections are assisted wording. No one-at-a-time student hint cycle or independent student implementation is claimed.

Format: [Course AI tutor instructions](https://github.com/ARG-NCTU/oop-python-nycu/blob/d4ccf63b9252d0017e84d3bed10628f0f5ea7bc9/ai-tutor-2026.md)

Sources: [MIT lecture slides and code](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/pages/lecture-slides-code/), [course reference code](https://github.com/ARG-NCTU/oop-python-nycu/blob/d4ccf63b9252d0017e84d3bed10628f0f5ea7bc9/src/mit_ocw_exercises/lec7_debug_except.py).

## ① Check My Understanding

Questions completed: 5 / 5 written responses supplied with AI assistance.

Answers revised after AI hints: 0 / 5 in this prepared response. The answers were supplied together without an interactive revision round. No historical revision count is claimed.

## ② My Misconception

Before: I could treat one passing example as enough evidence that a program is correct.

Now: I need normal cases, boundary cases, and cases from each failure category. A conversion error should be handled explicitly, and an invalid reading should not partially change the totals.

## ③ Challenge the AI

One AI-generated question I challenged:

Passing several test examples proves that a program is correct for every possible input.

Why?

- [ ] Ambiguous
- [x] Oversimplified
- [ ] Technically questionable
- [ ] Too easy
- [ ] Other: None

Brief explanation: A finite set of passing tests does not cover every possible input. Tests can expose failures and support confidence, while a correctness argument explains why the algorithm handles the stated input categories.

## ④ One-Minute Reflection

One thing I am still unsure about: How should I divide a complicated input space into useful test categories without testing every possible value?

## Answers and reasoning

### Question 1

Passing several test examples proves that a program is correct for every possible input.

Answer: False

My reasoning: Those tests check only their chosen cases. Untested branches, boundaries, and interactions can still contain bugs.

### Question 2

For a valid range from 0 through 100, tests at 0 and 100 and just outside the range are useful.

Answer: True

My reasoning: They distinguish inclusive boundaries from values that must be rejected and help expose off-by-one errors.

### Question 3

Converting the string "not-a-number" with int raises `ZeroDivisionError`.

Answer: False

My reasoning: Invalid integer text raises `ValueError`. `ZeroDivisionError` concerns division by zero, so a handler must target the actual failure.

### Question 4

Catching every exception with one broad handler always makes the program more correct.

Answer: False

My reasoning: It can hide unrelated programming errors. Handling the expected exception makes the recovery rule clearer and lets unexpected failures remain visible.

### Question 5

An assertion can express a condition that the programmer expects to hold at a particular point.

Answer: True

My reasoning: Assertions document and check an internal expectation. They do not by themselves prove the rest of the program correct.
