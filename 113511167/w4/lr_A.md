**Topic:** Object-Oriented Programming\
**Date:** 2026/11/25

### ① Check My Understanding

Questions completed: **5 / 5**

Answers revised after AI hints: **0 / 5**

### ② My Misconception

**Before: I thought…**

Two objects with identical string representations might automatically be considered equal when compared using the `==` operator.

**Now: I understand…**

The `__str__` method only controls an object's string representation. Value-based equality must be defined separately through `__eq__`. Identical string representations do not guarantee object equality.

### ③ Challenge the AI

**One AI-generated question I challenged:**

Q1: When two objects are independently created from the same class, modifying an integer instance attribute of one object automatically changes the corresponding attribute of the other object because they belong to the same class.

**Why?**

☐ Ambiguous\
☐ Oversimplified\
☐ Technically questionable\
☑ Too easy\
☐ Other

**Brief explanation:**

The question only tests the basic concept of independent instance attributes. A more challenging question could involve mutable class attributes or multiple instances sharing a reference to the same mutable object, testing a deeper understanding of object state and shared references.

### ④ One-Minute Reflection

**One thing I am still unsure about:**

I am still unsure when `__eq__` should return `False` rather than `NotImplemented` when comparing objects of different types. I also want to better understand how overriding `__eq__` affects object hashability and the use of objects as dictionary keys or set elements.