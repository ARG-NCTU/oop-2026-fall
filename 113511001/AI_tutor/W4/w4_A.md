Topic: Object-Oriented Programming (OOP) — Classes and Objects
Date: 2026/09/27

① Check My Understanding

Questions completed: 5 / 5

Answers revised after AI hints: 1 / 5

② My Misconception

Before: I thought that if two objects contained the same attribute values, they would automatically be considered equal.

⸻

Now: I understand that two separately created objects are different instances, even if their data attributes have the same values. In the lecture’s Coordinate class, __eq__ is not defined, so the class does not define == to compare x and y. If I want two objects with the same attribute values to be treated as equal, I need to define __eq__ for the class.

⸻

③ Challenge the AI

One AI-generated question I challenged:

“The internal list self.vals is part of the object’s internal representation, while methods such as insert, member, and remove provide the interface for interacting with that representation.”

⸻

Why?

☐ Ambiguous
☐ Oversimplified
☐ Technically questionable
☑ Too easy
☐ Other: __________

Brief explanation:

The question was too easy because the lecture directly explains that objects contain an internal representation and methods provide an interface for interacting with that data. The intSet example also clearly shows self.vals as the internal data and insert, member, and remove as methods.

⸻

④ One-Minute Reflection

One thing I am still unsure about:

I am still unsure about how exceptions work inside class methods, especially the difference between try/except, raise, and assert.

⸻