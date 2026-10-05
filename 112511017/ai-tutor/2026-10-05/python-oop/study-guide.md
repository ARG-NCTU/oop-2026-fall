# AI tutor learning record: Python classes and inheritance, Part A

Name: Yu-Liang Tan / 譚羽良

Student ID: 112511017

Date: 2026-10-05

Topic: MIT OCW 6.0001, Lecture 8 object-oriented programming and Lecture 9 Python classes and inheritance

Status: AI-generated study and response draft. The exact lecture assignment for this week has not yet been confirmed. Suggested answers are not a record of the student's answers, hints, or revisions.

## Sources

- [MIT OCW Lecture 8](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/lecture-8-object-oriented-programming/)
- [MIT OCW Lecture 9](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/lecture-9-python-classes-and-inheritance/)
- The course reference repository's `lec8_classes.py` and `lec9_inheritance.py`, including `Coordinate`, `Fraction`, `intSet`, `Animal`, `Person`, `Student`, and `Rabbit`.

## Five True/False questions

### 1. Calling an instance method

Statement: For the lecture's `Coordinate` class, `c.distance(origin)` and `Coordinate.distance(c, origin)` pass the same objects to the method.

Suggested answer: True. The bound call supplies `c` as `self`; the explicit class call passes it as the first argument. Both use `c` and `origin` to calculate the distance.

Tutor hint if needed: Compare the definition's two parameters with the arguments in each call.

### 2. Object identity and aliasing

Statement: After `b = a`, where `a` is a `Coordinate`, changing `b.x` cannot change the value seen through `a.x` because the variable names differ.

Suggested answer: False. The assignment gives the two names references to the same object. A separate `Coordinate(a.x, a.y)` would create a new object instead.

Tutor hint if needed: Count constructor calls rather than variable names.

### 3. Inherited initialization

Statement: The lecture's `Cat` must define its own `__init__` before `Cat(5)` can work.

Suggested answer: False. `Cat` does not define an initializer, so it inherits the base initializer. If a subclass defines its own `__init__`, it must explicitly invoke the needed parent initialization; Python does not automatically run every initializer in the hierarchy.

Tutor hint if needed: Look for `Cat.__init__`, then trace which implementation Python finds.

### 4. Overridden behavior

Statement: `s.speak()` on a lecture `Student` object always executes `Person.speak()` because `Student` inherits from `Person`.

Suggested answer: False. `Student` defines its own `speak`, which overrides the inherited method. Inherited methods remain available when they are not replaced, but an ordinary call uses the subclass's override when present.

Tutor hint if needed: Inheritance can reuse behavior and also replace a specific behavior. Which definition is found first?

### 5. Shared counters and per-object values

Statement: After a `Rabbit` saves `self.rid = Rabbit.tag`, incrementing `Rabbit.tag` changes every previously created rabbit's `rid`.

Suggested answer: False. The shared class counter advances for the next object. Each existing `rid` keeps the integer value assigned to that instance. This differs from multiple attributes referring to one shared mutable list.

Tutor hint if needed: Compare the class attribute `Rabbit.tag` with the instance attribute `r1.rid` after creating a second rabbit.

## 1. Check my understanding

Questions generated: 5 / 5

Questions personally completed: [fill after answering] / 5

Answers revised after AI hints: [fill from the actual interaction] / 5

## 2. My misconception

Suggested reflection, keep only if accurate for you:

Before: I thought that a subclass needed to copy its parent's methods and initializer to use them.

Now: I understand that methods are inherited through attribute lookup. A subclass can reuse them, override selected methods, and call the parent initializer when its own initializer needs the parent's setup. Reusing the interface does not mean every method call executes the parent implementation.

## 3. Challenge the AI

Candidate question: "A class attribute is shared by all objects, so changing it changes each object's attributes."

Reason: Ambiguous and oversimplified.

Suggested explanation: The statement must distinguish a class attribute from an instance attribute. Assigning `self.rid = Rabbit.tag` stores a value in the instance. Later incrementing the class counter does not update that instance's `rid`. Mutating a shared list is a different case.

My actual challenged question and explanation: [review or replace]

## 4. One-minute reflection

Suggested remaining question: When should a subclass override a method, and when is composition a better way to reuse behavior?

One thing I am still unsure about: [write your own remaining question]
