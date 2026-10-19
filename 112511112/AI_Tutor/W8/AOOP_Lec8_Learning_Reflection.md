# AOOP Lec 8 Learning Reflection

Topic: AOOP Lec 8 - Object-Oriented Programming (Class, Instance, self, Methods)
Date: 2026-10-17

## ① Check My Understanding

Questions completed: 5 / 5

Answers revised after AI hints: 1 / 5

---

## ② My Misconception

### Before: I thought…
I thought that a class method cannot function without `self`, and removing `self` would disconnect the method from the object instance entirely.

---

### Now: I understand…
I now understand that methods are fundamentally functions. The current object can still be passed manually as an argument, so the functionality can still work without the special `self` convention. Using `self` is mainly part of the object-oriented design style that automatically associates a method call with the current instance.

I also learned that objects with identical attribute values are not necessarily the same object. Two instances can have the same state while still having different identities.

---

## ③ Challenge the AI

### One AI-generated question I challenged:
The question about whether defining `__str__()` usually implies a better class design.

---

### Why?
☑ Ambiguous
☐ Oversimplified
☑ Technically questionable
☐ Too easy
☐ Other:

### Brief explanation:
The word “usually” is vague and subjective. A class can have an excellent `__str__()` implementation while still having poor abstraction or encapsulation. Conversely, a well-designed class may not define `__str__()` at all. Therefore, `__str__()` is not a reliable indicator of design quality.

---

## ④ One-Minute Reflection

### One thing I am still unsure about:
I am still not fully certain what properties and characteristics an object contains. In particular, I want to become more comfortable identifying:

- An object's identity
- Instance attributes (state)
- Methods (behavior)
- Which data belongs to each instance individually
- How attributes and methods work together within a class
