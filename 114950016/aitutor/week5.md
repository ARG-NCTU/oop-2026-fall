# AI Tutor Learning Record — Week 5

Topic: Python Classes and Inheritance
Date: 2026/10/05

## Part A: True or False

### ① Check My Understanding

Questions completed: 5 / 5

Answers revised after AI hints: 2 / 5


### ② My Misconception

Before: I thought inheritance meant that a child class simply copies everything from the parent class and then becomes a completely separate class.

Now: I understand that a child class inherits the data and behavior of the parent class, and it can also add new attributes, add new methods, or override existing methods.


### ③ Challenge the AI

One AI-generated question I challenged:

> If a subclass defines a method with the same name as its superclass, Python will always use the superclass version first.

Why?

☐ Ambiguous  
☐ Oversimplified  
☑ Technically questionable  
☐ Too easy  
☐ Other: __________

Brief explanation:

Python first looks for the method in the current class.

If it cannot find the method there, it continues looking up the class hierarchy.

So if the subclass defines its own version of the method, that version will be used first.


### ④ One-Minute Reflection

One thing I am still unsure about:

I am still a little confused about when I should use getters and setters instead of directly accessing an attribute with dot notation.


---

## Part B: Coding Challenge

Name: 高芮妮
Date: 2026/10/05
Topic: Inheritance, Information Hiding and Method Overriding


## 1. Today’s Challenge

Core concept from today’s OCW lecture:

Using inheritance to reuse common data and behavior, while allowing subclasses to add or override functionality.

AI-generated coding challenge title:

**School Member Hierarchy**

The challenge asks me to create a parent class called `Person`, and two subclasses called `Student` and `Teacher`.

All people should have a name and age.

A Student should also have a major, and a Teacher should also have a subject.

Both subclasses should have their own version of a `speak()` method.


## 2. My Initial Approach — Before AI Help

Before asking AI for hints, briefly describe how you planned to solve the problem.

My approach:

At first, I planned to create separate Student and Teacher classes.

I would define `name`, `age`, and `speak()` independently in both classes.


## 3. AI Tutor Help

Did you ask the AI Tutor for help?

☐ No — I solved it independently  
☑ Yes — I received one or more hints

The most useful hint/question from AI was:

> If Student and Teacher both have name and age, is it necessary to write the same code twice?

It helped me realize that:

The shared attributes should be placed in a parent class.

Then Student and Teacher can inherit the common data and methods instead of repeating the same code.


## 4. My Revision

Did you change your approach or code after interacting with AI?

☐ No  
☑ Yes

What did you change, and why?

I created a parent class called `Person` that stores the shared attributes `name` and `age`.

Then I made `Student` and `Teacher` inherit from `Person`.

Each subclass adds its own extra attribute.

I also gave each subclass its own `speak()` method so that the behavior can be different even though they share the same parent class.

I changed my approach because inheritance reduces repeated code and makes the relationship between the classes clearer.


## 5. Verification

My final program:

☑ Passed the provided examples  
☑ Passed additional edge cases  
☐ Still has unresolved problems

One test I tried:

Input:

`Student("Amy", 20, "CS")`

Expected result:

The object should store the name `"Amy"`, age `20`, and major `"CS"`.

Actual result:

The object stored all three values correctly.


Another test:

Calling `speak()` on both a Student and a Teacher object.

Expected result:

Each subclass should use its own version of `speak()`.

Actual result:

The Student and Teacher objects produced different outputs as expected.


## 6. One-Minute Reflection

What idea from the OCW lecture did you transfer to this new problem?

I transferred the idea that subclasses can inherit common data and behavior from a parent class, while still adding or changing their own behavior.

One thing I understand better now:

I understand method overriding better. Python looks for a method in the current class first, and only looks up the hierarchy if it cannot find it there.

I also understand why inheritance is useful for avoiding repeated code.

One thing I am still unsure about:

I am still not completely sure when data should be stored as an instance variable and when it should be a class variable shared by all instances.