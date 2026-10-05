# W04 AI Tutor Learning Record — Part B

Name: 114511066
Date: 2026/09/28
Topic: Object Oriented Programming

## 1. Today’s Challenge

### Core concept from today’s OCW lecture:

Classes, inheritance, instance variables, method overriding, and special methods.

The lecture showed how subclasses can inherit behavior from parent classes and override methods when they need different behavior. It also showed how special methods such as `__str__`, `__add__`, and `__eq__` can define how objects behave with Python operations.

### AI-generated coding challenge title:

**Course Member System**

### Problem Statement

Create a class `Member` that stores a person's name and age.

Then create a subclass `Student` that inherits from `Member` and also stores a student's major.

Both classes should provide their own string representation using `__str__()`.

The `Student` class should inherit the methods for getting the name and age from `Member`.

### Input/Output Specification

Example:

    m = Member("Jack", 30)
    s = Student("Alice", 20, "CS")

    print(m)
    print(s)
    print(s.get_age())

Output:

    member:Jack:30
    student:Alice:20:CS
    20

### Constraints

- `Member` stores `name` and `age`.
- `Student` must inherit from `Member`.
- Do not rewrite `get_name()` or `get_age()` in `Student`.
- Both classes must implement an appropriate `__str__()` method.

---

## 2. My Initial Approach — Before AI Help

### My approach:

My first idea was to create two separate classes and give both classes their own `name`, `age`, `get_name()`, and `get_age()` methods.

I thought this would make each class complete by itself.

---

## 3. AI Tutor Help

### Did you ask the AI Tutor for help?

- [ ] No — I solved it independently
- [x] Yes — I received one or more hints

### The most useful hint/question from AI was:

If a `Student` is also a `Member`, do you need to write the same `get_name()` and `get_age()` methods twice?

### It helped me realize that:

I could use inheritance so that `Student` automatically receives the common methods from `Member`.

The subclass only needs to add the new `major` attribute and override behavior that should be different.

---

## 4. My Revision

### Did you change your approach or code after interacting with AI?

- [ ] No
- [x] Yes

### What did you change, and why?

I changed `Student` so that it inherits from `Member`. I also called the parent constructor to initialize the common attributes instead of repeating the same initialization code.

### Final code

```python
class Member(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def __str__(self):
        return "member:" + str(self.name) + ":" + str(self.age)


class Student(Member):
    def __init__(self, name, age, major):
        Member.__init__(self, name, age)
        self.major = major

    def __str__(self):
        return "student:" + str(self.name) + ":" + \
               str(self.age) + ":" + str(self.major)