Topic: Tuples, Lists, Aliasing, Mutability, and Cloning
Date: 2026/09/23

① Check My Understanding

Questions completed: 5 / 5

Answers revised after AI hints: 0 / 5

② My Misconception

Before: I thought…
Copying a list would always make a completely independent copy.

Now: I understand…
Using [:] creates a new outer list, but nested lists may still be shared. Also, assigning one list variable to another creates an alias, so both variables can refer to the same object.

③ Challenge the AI

One AI-generated question I challenged:
Question 3 about sorted() and sort().

Why?

☐ Ambiguous
☐ Oversimplified
☐ Technically questionable
☑ Too easy
☐ Other: __________

Brief explanation:
The question was too easy because the lecture directly explained that sorted() returns a new sorted list without changing the original list, while sort() mutates the original list.

④ One-Minute Reflection

One thing I am still unsure about:
I am still a little unsure about when I should use a tuple instead of a list.