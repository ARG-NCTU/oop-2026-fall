# Week 1 AI tutor material recovered from September 7

Name: Yu-Liang Tan / 譚羽良

Student ID: 112511017

Original source date: 2026-09-07

Topic: Lecture 5, tuples, lists, aliasing, mutability, and cloning

Status: Recovered AI-generated answer key from an earlier conversation. This is the previously generated study material, not evidence of a completed student tutoring session. The reflection and revision counts below were labeled as samples in the original response.

## Part A: True/False answer key

### Question 1

If two variables refer to the same Python list, modifying it through one variable affects what the other variable observes.

**Answer: True.**

Both variables are aliases pointing to the same mutable list object.

### Question 2

If a tuple contains a list, nothing inside that tuple can be changed.

**Answer: False.**

The tuple’s elements cannot be reassigned, but a mutable list stored inside the tuple can still be modified.

### Question 3

Using `copied = original[:]` always creates a completely independent copy.

**Answer: False.**

Slicing creates a shallow copy. The outer list is independent, but nested mutable objects may still be shared.

### Question 4

It is always safe to remove elements from a list while iterating directly over that list.

**Answer: False.**

Removing elements changes indices and may cause the loop to skip items. Iterate over a copy when removal is required.

### Question 5

`sorted(items)` and `items.sort()` have the same effect.

**Answer: False.**

`sorted(items)` returns a new sorted list and preserves `items`. `items.sort()` mutates `items` and returns `None`.

## Sample learning record from the original answer key

These entries illustrate the required format. The counts and first-person reflection are sample responses supplied by AI, not verified student responses.

**Topic:** Tuples, Lists, Aliasing, Mutability, and Cloning

**Questions completed:** Sample: 5/5

**Answers revised after hints:** Sample: 2/5

**Before:** I thought cloning a list using slicing copied every nested object.

**Now:** I understand that slicing creates only a shallow copy. Nested mutable objects can remain shared.

**Question challenged:** “If a tuple is immutable, everything contained inside it is immutable.”

**Reason:** Technically questionable and potentially misleading. Tuple immutability prevents replacing its elements, but it does not make contained mutable objects immutable.

**Still unsure about:** When to use a shallow copy versus a deep copy for nested data.
