Name: 張永怡
Date: 2026/10/03
Topic: Python Classes and Inheritance

1. Today’s Challenge

Core concept from today’s OCW lecture:

Using inheritance, method overriding, class variables, and special methods such as __add__ to create related object types and define how objects interact.

AI-generated coding challenge title:

Game Characters and Team Power

2. My Initial Approach — Before AI Help

Before asking AI for hints, briefly describe how you planned to solve the problem.

My approach:

I planned to make Warrior and Mage subclasses of Character because they share common attributes such as name and level. I planned to make Team a separate object that stores character objects and calculates their total power.

3. AI Tutor Help

Did you ask the AI Tutor for help?

☐ No — I solved it independently
☑ Yes — I received one or more hints

The most useful hint/question from AI was:

I was asked to think about which object Python uses to call __add__ when evaluating w + m.

It helped me realize that:

__add__ needed to be defined in Character, because Warrior and Mage inherit from Character. This allows expressions such as w + m to create a Team object.

4. My Revision

Did you change your approach or code after interacting with AI?

☐ No
☑ Yes

What did you change, and why?

I moved __add__ into the Character class so that Warrior and Mage could inherit it. I also corrected the use of the shared class variable for unique IDs and passed self correctly when calling the parent class constructor.

5. Verification

My final program:

☑ Passed the provided examples
☑ Passed additional edge cases
☐ Still has unresolved problems

One edge case I tested:

Input: Warrior("A", 1) and Warrior("B", 100)

Expected output: Team total power = 202

Actual output: Team total power = 202

6. One-Minute Reflection

What idea from the OCW lecture did you transfer to this new problem?

I transferred the ideas of inheritance and special methods from the lecture. Like the Rabbit example using __add__, my Character class uses __add__ to create a new Team object from two character objects.

One thing I understand better now:

I understand better how subclasses inherit methods from a parent class and how method overriding allows different subclasses to have different behavior while sharing the same general structure.

One thing I am still unsure about:

I am still unsure about why object is the base class at the top of the Python class hierarchy and what exactly the object class provides.