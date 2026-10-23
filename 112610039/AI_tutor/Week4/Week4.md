# AI Tutor for AOOP 2026 - Week 4 Learning Record

## Part A: True or False

**Topic:** Object Oriented Programming (Lecture 8)[cite: 118]  
**Date:** 2026-10-24

### ① Check My Understanding
* **Questions completed:** 5 / 5
* **Answers revised after AI hints:** 0 / 5 (Answered all 5 correctly on the first attempt!)

### ② My Misconception
* **Before:** I was familiar with classes, but I used to view `self` as a special keyword rather than just an explicit parameter passed implicitly during method calls[cite: 149, 150, 152].
* **Now:** I understand that `c.method(arg)` is syntactic sugar for `Class.method(c, arg)`[cite: 152], where `c` is passed as `self`. I also learned that in Python, classes themselves are instances of `type`[cite: 141, 155], and `__str__` must always return a string[cite: 154].

### ③ Challenge the AI
* **One AI-generated question I challenged:** Question 2[cite: 153, 154]
* **Why?**
  - [ ] Ambiguous
  - [ ] Oversimplified
  - [x] Technically questionable
  - [ ] Too easy
  - [ ] Other: __________________
* **Brief explanation:** The claim that `__str__` can return integers/floats because Python automatically converts them is technically incorrect[cite: 154]. Python strictly requires `__str__` to return a `str` object[cite: 154], raising a `TypeError` otherwise[cite: 101, 153].

### ④ One-Minute Reflection
* **One thing I am still unsure about:** How Python internally manages attribute lookups via standard dictionaries (`__dict__`) versus optimized representations like `__slots__`.

---

## Part B: LeetCode-style Lecture Code Transfer

**Name:* 112610039
**Date:** 2026-10-24  
**Topic:** OOP Class Design, Dunder Methods & Operator Overloading[cite: 118, 127, 135, 156]

### 1. Today’s Challenge
* **Core concept from today’s OCW lecture:** Creating custom object types with `class`[cite: 125], encapsulating state with `self`[cite: 121, 127], and overriding special methods (`__str__`, `__add__`, `__eq__`) for custom behaviors[cite: 133, 135, 156].
* **AI-generated coding challenge title:** 2D Vector Operations (`Vector2D` Class)

### 2. My Initial Approach — Before AI Help
* **My approach:** Defined `__init__` to assign `self.x` and `self.y`[cite: 127]. Overrode `__str__` to return `(x, y)`[cite: 133, 154] and `magnitude()` using exponentiation[cite: 130]. Implemented `__eq__` and `__add__` by operating on `other.x` and `other.y`[cite: 135, 156].

### 3. AI Tutor Help
* **Did you ask the AI Tutor for help?**
  - [ ] No — I solved it independently
  - [x] Yes — I received one or more hints
* **The most useful hint/question from AI was:** Reminding me to add defensive `isinstance(other, Vector2D)` checks inside `__add__` and `__eq__`[cite: 106, 134].
* **It helped me realize that:** Operating on `other.x` directly without checking type will crash with `AttributeError` if `other` is an integer or string[cite: 97, 134].

### 4. My Revision
* **Did you change your approach or code after interacting with AI?**
  - [ ] No
  - [x] Yes
* **What did you change, and why?** Added `if not isinstance(other, Vector2D): raise TypeError(...)` in `__add__`[cite: 106, 134], and returned `False` in `__eq__` when `other` is not a `Vector2D`[cite: 134, 135].

### 5. Verification
* **My final program:**
  - [x] Passed the provided examples
  - [x] Passed additional edge cases
  - [ ] Still has unresolved problems
* **One edge case I tested:**
  - **Input:** `v1 = Vector2D(3, 4); v1 == "hello"`
  - **Expected output:** `False`
  - **Actual output:** `False`

### 6. One-Minute Reflection
* **What idea from the OCW lecture did you transfer to this new problem?** Bundling data attributes (`x`, `y`)[cite: 121, 126] with custom procedural methods/operators (`__add__`, `__eq__`)[cite: 126, 135, 156] to build clean, modular abstractions[cite: 121, 123, 137].
* **One thing I understand better now:** How operator overloading allows custom objects to integrate seamlessly with standard Python operators like `+` and `==`[cite: 135, 156].
* **One thing I am still unsure about:** How inheritance and method resolution order (MRO) work when extending custom classes in Python[cite: 123, 125, 137].