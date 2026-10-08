Topic: Python Classes and Inheritance    Date: 2026/10/08

① Check My Understanding

Questions completed: 5 / 5

Answers revised after AI hints: 0 / 5

② My Misconception

Before: I thought…

I did not have a major misconception about inheritance before the quiz, but I wanted to make sure I understood how Python chooses methods when a subclass overrides a method from its parent class, and how inherited methods such as `__init__()` are handled.

⸻

Now: I understand…

I understand that when a subclass overrides a method, Python normally uses the subclass's version when calling that method through a subclass instance. If the subclass does not define the method, Python searches upward through the inheritance hierarchy and uses the first matching method it finds.

I also understand that if a subclass does not define its own `__init__()`, it can inherit the parent's `__init__()`. However, if the subclass defines its own `__init__()`, the parent's `__init__()` is not automatically called; the subclass can explicitly call the parent's method when needed.

I also learned that class variables are shared between instances of a class, unlike instance attributes.

⸻

③ Challenge the AI

One AI-generated question I challenged:

Question 5, which used the inheritance hierarchy `Student → Cat → Animal`.

⸻

Why?

☐ Ambiguous\
☐ Oversimplified\
☐ Technically questionable\
☐ Too easy\
☒ Other: Unnatural inheritance hierarchy

Brief explanation:

The question was technically valid for testing multi-level inheritance, but the hierarchy was semantically strange because a `Student` is not a type of `Cat`. I thought the example could be misleading even though the method-lookup concept being tested was correct.

⸻

④ One-Minute Reflection

One thing I am still unsure about:

I am still interested in how Python inheritance compares with C++ inheritance, especially how Python can explicitly call a parent's overridden method without using C++-style pointers. I want to understand more about when to use something like `Animal.speak(self)` versus `super().speak()` and how this relates to Python's method lookup.
