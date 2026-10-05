# AI Tutor Learning Record: Part A

Name: Yu-Liang Tan / 譚羽良

Student ID: 112511017

Date: 2026-10-05

Topic: MIT OCW 6.0001, Lecture 8 object-oriented programming and Lecture 9 Python classes and inheritance

Status: Written responses and first-person reflection text prepared with AI assistance at the student's request. This records the current assisted response, not a restored historical tutoring session. No one-at-a-time hint and revision cycle was performed.

Format: [Course AI tutor instructions](https://github.com/ARG-NCTU/oop-python-nycu/blob/d4ccf63b9252d0017e84d3bed10628f0f5ea7bc9/ai-tutor-2026.md)

## ① Check My Understanding

Questions completed: 5 / 5 written responses supplied with AI assistance.

Answers revised after AI hints: 0 / 5 in this prepared response. The answers were supplied together, without an interactive hint and revision round. Historical revision counts were not recovered.

## ② My Misconception

Before: I could confuse a shared class counter with the identifier already stored in each object.

Now: I can separate class state from instance state. `Rabbit.tag` is the counter for the next object, while `self.rid` stores the integer assigned to one rabbit. Increasing the counter does not rewrite existing identifiers. Inheritance also reuses methods without copying their definitions into each subclass.

## ③ Challenge the AI

One AI-generated question I challenged:

After a `Rabbit` saves `self.rid = Rabbit.tag`, incrementing `Rabbit.tag` changes every previously created rabbit's `rid`.

Why?

- [ ] Ambiguous
- [x] Oversimplified
- [ ] Technically questionable
- [ ] Too easy
- [ ] Other: None

Brief explanation: The statement needs to distinguish changing a class attribute from changing an instance attribute. Assigning `self.rid = Rabbit.tag` stores the current integer value in the instance. Later rebinding `Rabbit.tag` leaves that value unchanged. Sharing a mutable list would behave differently.

## ④ One-Minute Reflection

One thing I am still unsure about: When should I override a parent method, and when would composition be a clearer design than inheritance?

## Answers and reasoning

### Question 1

For the lecture's `Coordinate` class, `c.distance(origin)` and `Coordinate.distance(c, origin)` pass the same objects to the method.

Answer: True

My reasoning: The bound call supplies c as self. The class call supplies c explicitly as the first argument, so the method receives the same two objects.

### Question 2

After `b = a`, where `a` is a `Coordinate`, changing `b.x` cannot change the value seen through `a.x` because the variable names differ.

Answer: False

My reasoning: b = a binds both names to the same object. Updating b.x changes the object also reached through a. Constructing another `Coordinate` would create a separate object.

### Question 3

The lecture's `Cat` must define its own `__init__` before `Cat(5)` can work.

Answer: False

My reasoning: `Cat` inherits `Animal.__init__` because it does not define its own initializer. A subclass that defines its own initializer must explicitly call the needed parent initialization.

### Question 4

`s.speak()` on a lecture `Student` object always executes `Person.speak()` because `Student` inherits from `Person`.

Answer: False

My reasoning: `Student` defines its own speak method. An ordinary call on a `Student` instance uses that override rather than `Person.speak`.

### Question 5

After a `Rabbit` saves `self.rid = Rabbit.tag`, incrementing `Rabbit.tag` changes every previously created rabbit's `rid`.

Answer: False

My reasoning: Each rabbit stores the integer value that `Rabbit.tag` held at creation. Incrementing the class counter changes the value used for later rabbits, not the earlier `rid` values.

## Reference material

The [earlier suggested answers and hints](study-guide.md) remain available for study. No earlier personal answer sequence or hint history is claimed here.

The draft covers Lectures 8 and 9. The exact assigned lecture still needs confirmation.
