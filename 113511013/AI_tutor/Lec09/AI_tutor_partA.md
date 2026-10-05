Topic: Python Classes and Inheritance
Date: 2026/10/04

① Check My Understanding

Questions completed: 5 / 5

Answers revised after AI hints: 5 / 5

② My Misconception

Before: I thought…

A subclass had to rewrite all of the methods and data attributes from its parent class. I also thought that if a subclass did not define its own __init__, creating an instance of that subclass would fail.

⸻

Now: I understand…

A subclass automatically inherits the data and methods of its parent class unless it overrides them. If a subclass does not define its own __init__, it can use the parent class's __init__. If the subclass does define its own __init__, it can explicitly call the parent constructor to initialize inherited data.

⸻

③ Challenge the AI

One AI-generated question I challenged:

“If a subclass defines a method with the same name as a method in its parent class, Python always uses the parent-class version first.”

⸻

Why?

☐ Ambiguous
☐ Oversimplified
☑ Technically questionable
☐ Too easy
☐ Other: __________

Brief explanation:

For an instance of a subclass, Python first looks for the method in the subclass itself. If the method is not found there, Python searches upward through the inheritance hierarchy. Therefore, a subclass method with the same name overrides the parent-class method.

⸻

④ One-Minute Reflection

One thing I am still unsure about:

I am still a little unsure about when a subclass should inherit the parent's __init__ directly and when it should define a new __init__ and call the parent constructor.

⸻