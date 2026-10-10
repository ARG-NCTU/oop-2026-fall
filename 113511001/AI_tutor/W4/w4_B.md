Name: 張永怡
Date: 2026/09/27
Topic: Object-Oriented Programming (OOP)

1. Today’s Challenge

Core concept from today’s OCW lecture:

Creating classes with instance attributes and methods, and using special methods such as __str__ and __add__ to define how objects behave.

⸻

AI-generated coding challenge title:

TimeDuration

⸻⸻

2. My Initial Approach — Before AI Help

Before asking AI for hints, briefly describe how you planned to solve the problem.

My approach:

I planned to create a class with two variables, hours and minutes, and define methods for printing and adding two TimeDuration objects. I did not initially consider how to handle the minutes when the total became 60 or more.

⸻⸻⸻

3. AI Tutor Help

Did you ask the AI Tutor for help?

☐ No — I solved it independently
☑ Yes — I received one or more hints

The most useful hint/question from AI was:

How will you convert a total such as 75 minutes into 1 extra hour and 15 minutes?

⸻

It helped me realize that:

I needed to handle the case when the total minutes were 60 or more by converting the extra minutes into hours and keeping the remaining minutes below 60.

⸻

4. My Revision

Did you change your approach or code after interacting with AI?

☐ No
☑ Yes

What did you change, and why?

I added a check for total minutes greater than or equal to 60. I used integer division to add the extra hours and modulo to find the remaining minutes. I also used __str__ to control how the object is printed and __add__ to return a new TimeDuration object.

⸻⸻⸻

5. Verification

My final program:

☑ Passed the provided examples
☑ Passed additional edge cases
☐ Still has unresolved problems

One edge case I tested:

Input: TimeDuration(0, 59) + TimeDuration(0, 59)

Expected output: 1h 58m

Actual output: 1h 58m

6. One-Minute Reflection

What idea from the OCW lecture did you transfer to this new problem?

I transferred the idea of creating my own class with instance attributes and using special methods such as __str__ and __add__ to define how objects behave.

⸻

One thing I understand better now:

I understand better how __add__ defines the + operator for objects and can return a new object instead of changing the original objects. I also understand that the time complexity of this addition is O(1) because it performs a fixed number of operations without using loops or recursion.

⸻

One thing I am still unsure about:

I am still unsure about how exceptions such as assert, try/except, and raise work inside class methods.

⸻