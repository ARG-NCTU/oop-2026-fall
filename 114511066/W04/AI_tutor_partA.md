# W04 AI Tutor Learning Record — Part A

Topic: Object Oriented Programming
Date: 2026/10/05

## ① Check My Understanding

Questions completed: 5 / 5

Answers revised after AI hints: 1 / 5

### Question 1

**True or False:** Each object created from the `Animal` class can have its own `age` and `name`.

My answer: True

Result: Correct.

### Question 2

**True or False:** Because `Cat` inherits from `Animal`, a `Cat` object can use `get_age()` even though `get_age()` is not written again inside the `Cat` class.

My answer: True

Result: Correct.

### Question 3

**True or False:** The `Student` class must rewrite every method from `Person` before it can use them.

My answer: True

AI hint: Look at `Student` in the lecture code. Does it define `get_name()` itself before `s1.get_name()` is called?

Revised answer: False

Explanation: `Student` inherits methods from `Person`, and `Person` also inherits methods from `Animal`. A subclass only needs to redefine a method when different behavior is needed.

### Question 4

**True or False:** `Rabbit.tag` is shared by all `Rabbit` objects rather than giving every rabbit an independent copy of `tag`.

My answer: True

Result: Correct.

### Question 5

**True or False:** The expression `r4 = r1 + r2` can call the `__add__()` method defined in the `Rabbit` class.

My answer: True

Result: Correct.

---

## ② My Misconception

**Before: I thought…**

I thought that when a new subclass was created, it had to define all of the methods it wanted to use again.

**Now: I understand…**

I understand that a subclass inherits methods and attributes from its parent class. It only needs to redefine a method when it wants different behavior. For example, `Student` can use `get_name()` from its parent classes but defines its own `speak()` method.

---

## ③ Challenge the AI

**One AI-generated question I challenged:**

"`Student.speak()` replaces `Person.speak()` for every `Person` object."

**Why?**

- [ ] Ambiguous
- [x] Oversimplified
- [ ] Technically questionable
- [ ] Too easy
- [ ] Other: __________

**Brief explanation:**

`Student.speak()` overrides the inherited method only for `Student` objects. A normal `Person` object still uses the `speak()` method defined in `Person`.

---

## ④ One-Minute Reflection

**One thing I am still unsure about:**

I am still a little unsure about when a variable should be a class variable like `Rabbit.tag` and when it should be an instance variable like `self.age`.