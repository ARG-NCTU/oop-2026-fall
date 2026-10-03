Topic: Python Classes and Inheritance    Date: 2026/10/03

① Check My Understanding

Questions completed: 5 / 5

Answers revised after AI hints: 0 / 5

② My Misconception

Before: I thought inheritance mainly meant that a child class could use methods from its parent class, but I was not completely sure how a child class could replace inherited behavior.

Now: I understand method overriding better through real examples. A subclass can define a method with the same name as a parent method, and the subclass version will be used for instances of that subclass.

③ Challenge the AI

One AI-generated question I challenged:

“In the lecture’s Rabbit class, when you write r4 = r1 + r2, Python uses the Rabbit.__add__() method, and r4 becomes a new Rabbit whose parents are r1 and r2.”

Why?

☐ Ambiguous
☐ Oversimplified
☐ Technically questionable
☑ Too easy
☐ Other: __________

Brief explanation:

The question was too easy because it directly followed the lecture example. The code clearly shows that __add__ returns a new Rabbit with self and other as its parents, so it did not require much reasoning.

④ One-Minute Reflection

One thing I am still unsure about:

I am still unsure about why object is the base class at the top of the Python class hierarchy and what exactly the object class provides.