# AI Tutor Learning Record: Part A

Name: Yu-Liang Tan / 譚羽良

Student ID: 112511017

Week: 4

Date: 2026-10-05

Topic: MIT OCW Lecture 8, Object-oriented programming, instances, methods, aliasing, and object representations

Status: New AI-assisted written responses prepared at the student's request. These are new records, not recovered historical sessions. First-person reflections are assisted wording. No one-at-a-time student hint cycle or independent student implementation is claimed.

Format: [Course AI tutor instructions](https://github.com/ARG-NCTU/oop-python-nycu/blob/d4ccf63b9252d0017e84d3bed10628f0f5ea7bc9/ai-tutor-2026.md)

Sources: [MIT lecture slides and code](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/pages/lecture-slides-code/), [course reference code](https://github.com/ARG-NCTU/oop-python-nycu/blob/d4ccf63b9252d0017e84d3bed10628f0f5ea7bc9/src/mit_ocw_exercises/lec8_classes.py).

## ① Check My Understanding

Questions completed: 5 / 5 written responses supplied with AI assistance.

Answers revised after AI hints: 0 / 5 in this prepared response. The answers were supplied together without an interactive revision round. No historical revision count is claimed.

## ② My Misconception

Before: I could confuse giving an object another name with constructing another object.

Now: Assignment can create an alias, while a constructor creates a new instance. Initializing a list inside `__init__` gives each new locker its own list. Methods then manage that instance's state, and `__str__` supplies a readable representation.

## ③ Challenge the AI

One AI-generated question I challenged:

After `second = first`, where first is an object, second refers to a newly constructed object.

Why?

- [ ] Ambiguous
- [ ] Oversimplified
- [ ] Technically questionable
- [x] Too easy
- [ ] Other: None

Brief explanation: This mostly repeats the aliasing idea from the earlier lists topic. A stronger question would compare assigning an existing object with constructing a second object and then mutating one of them.

## ④ One-Minute Reflection

One thing I am still unsure about: How should I decide whether a method changes the current object or returns a separate result object?

## Answers and reasoning

### Question 1

For an instance method, the bound call supplies the instance as the self argument.

Answer: True

My reasoning: That is why `object.method(other)` can use the same object as the first argument of `Class.method(object, other)`.

### Question 2

After `second = first`, where first is an object, second refers to a newly constructed object.

Answer: False

My reasoning: The assignment binds another name to the existing object. No constructor call occurs.

### Question 3

Creating `self.items = []` inside `__init__` on each construction creates a new list for each instance.

Answer: True

My reasoning: The list expression is evaluated separately during each initialization. The two instances therefore begin with different list objects.

### Question 4

A class can implement addition by returning a new object without changing either operand.

Answer: True

My reasoning: The lecture's `Fraction.__add__` calculates a numerator and denominator and constructs a result `Fraction` rather than changing the operands.

### Question 5

A `__str__` method should print the representation and return None.

Answer: False

My reasoning: It must return a string. The caller, such as print, decides whether to display that returned representation.
