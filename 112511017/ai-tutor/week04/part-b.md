# AI Tutor Learning Record: Part B

Name: Yu-Liang Tan / 譚羽良

Student ID: 112511017

Week: 4

Date: 2026-10-05

Topic: MIT OCW Lecture 8, Object-oriented programming, instances, methods, aliasing, and object representations

Status: New AI-assisted written responses prepared at the student's request. These are new records, not recovered historical sessions. First-person reflections are assisted wording. No one-at-a-time student hint cycle or independent student implementation is claimed.

Format: [Course AI tutor instructions](https://github.com/ARG-NCTU/oop-python-nycu/blob/d4ccf63b9252d0017e84d3bed10628f0f5ea7bc9/ai-tutor-2026.md)

Sources: [MIT lecture slides and code](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/pages/lecture-slides-code/), [course reference code](https://github.com/ARG-NCTU/oop-python-nycu/blob/d4ccf63b9252d0017e84d3bed10628f0f5ea7bc9/src/mit_ocw_exercises/lec8_classes.py).

## 1. Today's Challenge

Core concept from today's OCW lecture: Per-instance state, methods that maintain an object's rules, a snapshot copy, and `__str__`, transferring ideas from `Coordinate`, `Fraction`, and `intSet`.

AI-generated coding challenge title: Storage locker inventory

### Problem statement

Implement a `Locker` class with a positive capacity and its own ordered list of item labels. Duplicates are allowed. Processing must use the object's methods rather than write to its internal list directly.

- `add(label)` returns `True` after adding the label if there is space. A full locker returns `False` and keeps its state.
- `remove(label)` removes the first matching item. It raises `ValueError` if the label is absent, without changing state.
- `snapshot()` returns a separate list of the current labels.
- `__str__()` returns `count/capacity:` followed by the labels joined with `|`. For an empty locker of capacity 3, it returns `0/3:`.

Also implement `locker_report(capacity, operations)`. Create one locker, apply the operations in order, and return `(results, final_description)`. Log the boolean from each add. Log `True` for successful removal and `False` when removal raises `ValueError`. Separate locker instances must have independent lists.

### Input/output specification

Input: A capacity and a list of `(action, label)` tuples. Actions are `"add"` or `"remove"`.

Output: A list of operation results and the final locker representation, returned as a tuple.

### Constraints

- `1 <= capacity <= 10`
- `0 <= len(operations) <= 1000`
- Each label contains 1 through 20 ASCII letters or digits.
- Operation actions are valid.
- Use classes, methods, lists, tuples, loops, and exception handling.

### Examples

| Capacity and operations | Expected output |
| --- | --- |
| `2`, `[("add", "pen"), ("add", "pen"), ("add", "book"), ("remove", "pen"), ("add", "book")]` | `([True, True, False, True, True], "2/2:pen\|book")` |
| `1`, `[("remove", "pen"), ("add", "eraser"), ("remove", "eraser")]` | `([False, True, True], "0/1:")` |
| `3`, `[]` | `([], "0/3:")` |

## 2. My Initial Approach Before AI Help

My approach: I would initialize an empty list inside each `Locker` instance. The add method would check capacity before appending. The remove method would use first-occurrence removal, and the report function would catch only the expected `ValueError` for a missing label. A snapshot would copy the list, and `__str__` would return the requested text. This plan was supplied with AI assistance rather than recorded before help.

Which concept from the lecture code am I applying? Per-instance state, methods that maintain an object's rules, a snapshot copy, and `__str__`, transferring ideas from `Coordinate`, `Fraction`, and `intSet`.

## 3. AI Tutor Help

Did you ask the AI Tutor for help?

- [ ] No, I solved it independently
- [x] Yes, I received AI assistance

The most useful hint/question from AI was: "What happens if two lockers share the same list, or if a caller modifies the list returned by snapshot?" This identifies the need for separate instance storage and a copied snapshot.

It helped me realize that: The class groups state and behavior. Each constructor creates separate storage, and methods manage the capacity and removal rules. `__str__` exposes a description without requiring callers to build it themselves.

Assistance used: AI supplied the written approach, reflection, implementation, and tests. This assistance includes a solution, rather than only hints.

## 4. My Revision

Did you change your approach or code after interacting with AI?

- [x] No separate student revision round was recorded
- [ ] Yes

What did you change, and why? No separate student implementation or revision was recorded. The assistant's first verified implementation passed all nine tests, so no failing-code revision is claimed.

## 5. Verification

My final program is an AI-assisted implementation. The assistant ran the verification on October 5, 2026.

- [x] Passed the provided examples
- [x] Passed additional edge cases
- [ ] Still has unresolved problems

[Implementation](solution/locker.py) and [tests](solution/test_locker.py).

Run from `solution/`:

```bash
python3 -m pytest -q -p no:cacheprovider test_locker.py
```

Result: 9 tests passed. The checks cover all three examples, independent instances, snapshot isolation, missing removal without mutation, first duplicate removal, rejection when full, and 1,000 operations.

One edge case tested:

Input: Create a capacity-2 locker, add "pen", append "book" to the returned snapshot, then request another snapshot.

Expected output: `["pen"]`

Actual output: `["pen"]`

## 6. One-Minute Reflection

What idea from the OCW lecture did you transfer to this new problem? The class groups state and behavior. Each constructor creates separate storage, and methods manage the capacity and removal rules. `__str__` exposes a description without requiring callers to build it themselves.

Why my solution works: The list begins empty. add changes it only when there is room, preserving the capacity limit; a rejected add leaves it unchanged. List removal deletes the first matching label and raises before changing the list if the label is missing. The report function records those outcomes in order. A sliced snapshot does not expose the outer internal list, and each instance initializes a separate list.

Time complexity: For Q operations and capacity C, adds are amortized O(1), removals are O(C), and the final representation is O(C) for bounded label length. Total time is O(QC + C), and storage is O(Q + C), including the result log. snapshot alone takes O(C) time and space.

One thing I understand better now: Creating an object, aliasing one, and returning a copy of one of its containers are different operations with different mutation effects.

One thing I am still unsure about: How should an object protect its state if it starts storing mutable item objects instead of immutable label strings?
