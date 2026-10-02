Topic: Recursion and Dictionaries
Date: 2026/10/03

① Check My Understanding

Questions completed: 5 / 5

Answers revised after AI hints: 4 / 5

② My Misconception

Before: I thought…

A recursive function only needed to call itself, and Python would somehow know when to stop. I also thought recursion was always more efficient than using a loop.

⸻

Now: I understand…

A recursive function needs at least one base case and each recursive call must move toward a smaller or simpler version of the same problem. Otherwise, the recursion may never terminate. I also understand that recursion can be simpler and more intuitive for the programmer, but it is not always more efficient for the computer.

⸻

③ Challenge the AI

One AI-generated question I challenged:

“A Python dictionary can use any Python object as a key.”

⸻

Why?

☐ Ambiguous
☐ Oversimplified
☑ Technically questionable
☐ Too easy
☐ Other: __________

Brief explanation:

The statement is too broad. Dictionary values can be mutable or immutable, but dictionary keys must be unique and hashable. In this lecture, I can think of valid keys as immutable types such as integers, strings, tuples, floats, and booleans. A list cannot be used as a dictionary key.

⸻

④ One-Minute Reflection

One thing I am still unsure about:

I am still a little unsure about how to decide whether recursion or iteration is the better choice for a new problem, especially when both approaches are possible.

⸻