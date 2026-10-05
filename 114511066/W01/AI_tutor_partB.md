# W01 AI Tutor Learning Record — Part B

Name: 114511066
Date: 2026/09/07
Topic: Tuples, Lists, Aliasing, Mutability, and Cloning

## 1. Today’s Challenge

### Core concept from today’s OCW lecture:

List iteration, mutation, aliasing, and cloning.

I learned that lists are mutable objects. If two variables refer to the same list, changing the list through one variable can also affect the other variable. I also learned that modifying a list while iterating over it may cause unexpected results, so making a copy of the list can be useful.

### AI-generated coding challenge title:

**Remove Blocked Values**

### Problem Statement

You are given two lists of integers, `values` and `blocked`.

Remove every element from `values` that also appears in `blocked`.

The original `blocked` list must not be modified.

For example:

Input:

    values = [1, 2, 3, 2, 4]
    blocked = [2, 4]

Output:

    values = [1, 3]

### Constraints

- Both inputs are lists of integers.
- A value may appear more than once.
- All occurrences of a blocked value must be removed.
- Do not create the final result as a completely separate output list.
- Modify `values` using the list concepts from the lecture.

---

## 2. My Initial Approach — Before AI Help

### My approach:

At first, I planned to iterate directly through `values`. If an element was also in `blocked`, I would remove it from `values`.

For example:

    for e in values:
        if e in blocked:
            values.remove(e)

I thought this would remove every blocked value.

---

## 3. AI Tutor Help

### Did you ask the AI Tutor for help?

- [ ] No — I solved it independently
- [x] Yes — I received one or more hints

### The most useful hint/question from AI was:

What happens to the positions of the remaining elements when an element is removed from a list that is currently being iterated over?

### It helped me realize that:

Removing elements from the same list that I am iterating over can cause some elements to be skipped.

For example, if there are two blocked values next to each other, removing the first one changes the index of the second one.

This is similar to the `remove_dups()` example from the lecture.

---

## 4. My Revision

### Did you change your approach or code after interacting with AI?

- [ ] No
- [x] Yes

### What did you change, and why?

Instead of iterating directly over `values`, I first made a clone using slicing.

Then I iterated over the copy while removing elements from the original list.

Final program:

```python
def remove_blocked(values, blocked):
    values_copy = values[:]

    for e in values_copy:
        if e in blocked:
            values.remove(e)

    return values