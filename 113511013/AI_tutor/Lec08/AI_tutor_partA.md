Topic: Object-Oriented Programming
Date: 2026/10/04

① Check My Understanding

Questions completed: 5 / 5

Answers revised after AI hints: 5 / 5

② My Misconception

Before: I thought…

A class and an object were basically the same thing, and I thought I needed to pass self manually when calling a method.

⸻

Now: I understand…

A class defines a new type, while an object is an instance of that class. The __init__ method initializes the data attributes of each instance. When I call a method with dot notation, Python automatically passes the object as the first argument, which is conventionally named self.

⸻

③ Challenge the AI

One AI-generated question I challenged:

“When calling c.distance(zero), the method receives only one argument because only zero appears inside the parentheses.”

⸻

Why?

☑ Ambiguous
☐ Oversimplified
☐ Technically questionable
☐ Too easy
☐ Other: __________

Brief explanation:

The statement is confusing because only one explicit argument appears in the call, but Python also automatically passes c as the first argument, self. Therefore, the method actually receives both self and other.

⸻

④ One-Minute Reflection

One thing I am still unsure about:

I am still a little unsure about when I should define a special method such as __str__, __eq__, or __len__ instead of writing a normal method.

⸻