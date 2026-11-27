**Topic:** Python Classes and Inheritance  
**Date:** 2026/11/26

### ① Check My Understanding

Questions completed: **5 / 5**

Answers revised after AI hints: **0 / 5**

### ② My Misconception

**Before: I thought…**

A parent class's constructor would automatically execute when a subclass defines its own constructor. I also thought that a method defined in a parent class would always call the parent class's version of another method.

**Now: I understand…**

A subclass must explicitly call the parent class's constructor if it overrides `__init__`. Additionally, when a method calls another method through `self`, Python determines which implementation to execute based on the actual object's class and method resolution order (MRO).

### ③ Challenge the AI

**One AI-generated question I challenged:**

Q1: If `Student` inherits from `Person`, and `Person` inherits from `Animal`, a `Student` object can use methods defined in `Animal` even if those methods are not explicitly defined in either `Student` or `Person`.

**Why?**

☐ Ambiguous  
☐ Oversimplified  
☐ Technically questionable  
☑ Too easy  
☐ Other

**Brief explanation:**

The question only tests basic method lookup in a single inheritance chain. A more challenging question could combine inheritance with method overriding, class variables, and attribute shadowing to test a deeper understanding of Python's attribute resolution mechanism.

### ④ One-Minute Reflection

**One thing I am still unsure about:**

I am still unsure how to design constructor initialization using `super()` in multiple inheritance when parent classes require different parameters. I also want to better understand when to extend inherited behavior using `super().method()` instead of completely overriding a method.