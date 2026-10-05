# AI Tutor Learning Record - Week 5 / Lab 4

Name: 陳芊蓉
Student ID: 114511057
Date: 2026/10/05
Topic: C++ Reference, Encapsulation, Inheritance, and Dynamic Memory

## Part A: True or False

### 1. Check My Understanding

Questions completed: 5 / 5

1. If a function parameter is passed by reference, changing it inside
   the function can change the original variable.
   Answer: True

2. If m_level is private, code outside the Battery class can directly
   modify m_level.
   Answer: False

3. A constructor can use an initializer list to initialize a data member
   when an object is created.
   Answer: True

4. A BaseApp pointer can point to an object of a derived class such as
   MyApp.
   Answer: True

5. Memory allocated using new double[n] should be released using
   delete[].
   Answer: True

Answers revised after AI hints: 1 / 5

### 2. My Misconception

Before:
I thought a reference created another copy of a variable, so changing
the reference would not affect the original variable.

Now:
I understand that a reference is another name for the original variable.
If a function receives a variable by reference, changing the reference
can directly change the original variable.

### 3. Challenge the AI

One AI-generated question I challenged:

"A BaseApp pointer can point to an object of a derived class such as
MyApp."

Why?

[X] Oversimplified

Brief explanation:
I think this question is a little simplified because I am still learning
how inheritance, virtual functions, and override work together.

### 4. One-Minute Reflection

One thing I am still unsure about:

I am still unsure about how virtual functions and override work when a
derived object is accessed through a base-class pointer.


## Part B: LeetCode-style Lecture Code Transfer

### 1. Today's Challenge

Core concept from today's OCW lecture:

Using references to modify original variables and using class methods
to control access to private data.

AI-generated coding challenge title:

Safe Temperature Controller

### 2. My Initial Approach - Before AI Help

My approach:

First, I planned to check whether a temperature was smaller than 0 or
greater than 100. If it was outside the range, I would change it to the
nearest valid value. Then I would store the valid value in the object.

### 3. AI Tutor Help

Did you ask the AI Tutor for help?

[X] Yes - I received hints

The most useful hint/question from AI was:

"What is the difference between passing a normal variable and passing
it with &?"

It helped me realize that:

A reference does not create another copy. It allows the function to
modify the original variable directly.

### 4. My Revision

Did you change your approach or code after interacting with AI?

[X] Yes

What did you change, and why?

I understood why the function parameter uses a reference. I also learned
to check whether a value is valid before changing private data.

### 5. Verification

[X] Passed the provided examples
[X] Passed additional edge cases
[ ] Still has unresolved problems

One edge case I tested:

Input: 120
Expected output: 100
Actual output: 100

### 6. One-Minute Reflection

What idea from the OCW lecture did you transfer to this new problem?

I used a reference to modify the original value and used encapsulation
to control how private data is changed.

One thing I understand better now:

I understand better why a reference parameter uses & and how it can
change the original variable.

One thing I am still unsure about:

I am still unsure about inheritance and virtual functions, especially
how a base-class pointer calls a function from a derived class.
