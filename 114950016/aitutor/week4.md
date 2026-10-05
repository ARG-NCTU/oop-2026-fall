# AI Tutor Learning Record — Week 4

Topic: Object Oriented Programming
Date: 2026/09/28

## Part A: True or False

### ① Check My Understanding

Questions completed: 5 / 5

Answers revised after AI hints: 2 / 5


### ② My Misconception

Before: I thought a class was mainly just a place to group several related functions together.

Now: I understand that a class defines a new type of object. An object can contain both data attributes and methods, so the data and the operations that work on that data can be organized together.


### ③ Challenge the AI

One AI-generated question I challenged:

> All objects created from the same class must have exactly the same attribute values.

Why?

☐ Ambiguous  
☐ Oversimplified  
☑ Technically questionable  
☐ Too easy  
☐ Other: __________

Brief explanation:

Objects created from the same class have the same type and can use the same methods, but each instance can store different values.

For example, `Coordinate(3, 4)` and `Coordinate(0, 0)` are both Coordinate objects, but their `x` and `y` values are different.


### ④ One-Minute Reflection

One thing I am still unsure about:

I am still a little confused about `self`. I understand that it refers to the current object, but sometimes I still need to think about why I write `self.x` instead of only `x`.


---

## Part B: Coding Challenge

Name: 高芮妮
Date: 2026/09/28
Topic: Classes, Objects, Attributes and Methods


## 1. Today’s Challenge

Core concept from today’s OCW lecture:

Creating a new type with a class, storing information in instance variables, and defining methods that operate on each object.

AI-generated coding challenge title:

**Student Profile Class**

The challenge asks me to create a `Student` class.

Each Student object should store a name, student ID, and score.

The class should also provide methods to update the score and check whether the student passes.

When the object is printed, it should display useful student information instead of the default Python object representation.


## 2. My Initial Approach — Before AI Help

Before asking AI for hints, briefly describe how you planned to solve the problem.

My approach:

I planned to define a `Student` class and use `__init__` to store the student's name, ID, and score.

Then I would add a method called `is_pass()` that returns whether the score is at least 60.


## 3. AI Tutor Help

Did you ask the AI Tutor for help?

☐ No — I solved it independently  
☑ Yes — I received one or more hints

The most useful hint/question from AI was:

> If you print a Student object directly, what will Python display if you do not define a `__str__` method?

It helped me realize that:

Without `__str__`, printing an object usually gives a default representation that is not very useful to the user.

I can define `__str__` so that the object displays information such as the student's name, ID, and score.


## 4. My Revision

Did you change your approach or code after interacting with AI?

☐ No  
☑ Yes

What did you change, and why?

I added a `__str__` method to the Student class.

I also made sure that methods use `self` so that each Student object works with its own data.

For example, changing the score of one Student should not change the score of another Student.


## 5. Verification

My final program:

☑ Passed the provided examples  
☑ Passed additional edge cases  
☐ Still has unresolved problems

One test I tried:

Input:

`Student("Amy", "114950016", 85)`

Expected result:

The object should store the name `"Amy"`, ID `"114950016"`, and score `85`.

Actual result:

The object stored all three values correctly.


Another test:

Input score:

`59`

Expected result:

`is_pass()` should return `False`.

Actual result:

`False`


## 6. One-Minute Reflection

What idea from the OCW lecture did you transfer to this new problem?

I transferred the idea that a class combines an internal data representation with an interface of methods.

The Student object stores its own data, while methods provide a clear way to interact with that data.

One thing I understand better now:

I understand the difference between a class and an instance better. A class defines the type, while an instance is a specific object created from that class.

I also understand that `self` refers to the specific instance using the method.

One thing I am still unsure about:

I am still not completely sure when I should define a special method such as `__str__`, `__add__`, or `__eq__` instead of writing a normal method.