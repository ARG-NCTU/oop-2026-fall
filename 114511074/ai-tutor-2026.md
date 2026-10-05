# Lab03 AI Tutor Learning Record

## Part A: True or False

### AI Tutor Learning Record

Topic: PyTest and Unit Test  
Date: 2026/09/28

① Check My Understanding

Questions completed: 5 / 5

Answers revised after AI hints: 2 / 5

② My Misconception

Before: I thought testing a program mainly meant running the whole program and checking whether the final result looked correct.

⸻

Now: I understand that unit tests can check small parts of a program separately. In pytest, I can use assert to compare the actual result with the expected result. However, I am still not very familiar with writing test cases by myself.

⸻

③ Challenge the AI

One AI-generated question I challenged:

“If a pytest test does not produce an error, it always means the program is completely correct.”

⸻

Why?

☐ Ambiguous  
☑ Oversimplified  
☐ Technically questionable  
☐ Too easy  
☐ Other: __________

Brief explanation:

Passing the existing tests only shows that the program works for those test cases. There may still be other inputs or edge cases that were not tested.

⸻

④ One-Minute Reflection

One thing I am still unsure about:

I am still not very sure how to decide which test cases are necessary, especially how many normal cases and edge cases I should write.

⸻


## Part B: LeetCode-style Lecture Code Transfer

### AI Tutor Learning Record — Coding Challenge

Name: 114511074  
Date: 2026/09/28  
Topic: PyTest, unit testing, and boundary cases

1. Today’s Challenge

Core concept from today’s OCW lecture:

Using pytest and assert to check whether a function gives the expected result, and testing both normal and invalid inputs.

⸻

AI-generated coding challenge title:

Temperature Category Tester

⸻⸻

2. My Initial Approach — Before AI Help

Before asking AI for hints, briefly describe how you planned to solve the problem.

My approach:

At first, I planned to write the function first and only test a few normal values. I did not immediately think about boundary values or invalid inputs because I am still not very familiar with designing test cases.

⸻⸻⸻

3. AI Tutor Help

Did you ask the AI Tutor for help?

☐ No — I solved it independently  
☑ Yes — I received one or more hints

The most useful hint/question from AI was:

“What values are closest to the boundaries between two categories, and what invalid input should cause an exception?”

⸻

It helped me realize that:

I should not only test ordinary values. I also need to test values directly on both sides of a boundary and check whether invalid inputs raise the expected error.

⸻

4. My Revision

Did you change your approach or code after interacting with AI?

☐ No  
☑ Yes

What did you change, and why?

I added more test cases for boundary values instead of only testing normal inputs. I also added a test for invalid input using pytest.raises. I still need more practice before I can design a complete set of tests without help.

⸻⸻⸻

5. Verification

My final program:

☑ Passed the provided examples  
☑ Passed additional edge cases  
☐ Still has unresolved problems

One edge case I tested:

Input: score = 59

Expected output: "F"

Actual output: "F"

6. One-Minute Reflection

What idea from the OCW lecture did you transfer to this new problem?

I used unit tests to check individual functions and added boundary-value tests instead of only checking normal inputs.

⸻

One thing I understand better now:

I understand better that passing a few normal examples is not enough. Boundary values and invalid inputs are also important when testing a program.

⸻

One thing I am still unsure about:

I am still not very confident about using pytest.mark.parametrize and deciding how many test cases are enough.

⸻

---






# AI Tutor for AOOP 2026

## Part A: True or False

### AI Tutor Learning Record

Topic: C++ basic concepts and object-oriented programming introduction  
Date: 2026/10/05

① Check My Understanding

Questions completed: 5 / 5

Answers revised after AI hints: 2 / 5

② My Misconception

Before: I thought a class and an object were almost the same thing, and I was not very clear about the difference between them.

⸻

Now: I understand that a class is more like a blueprint, while an object is an actual instance created from the class. However, I am still not very familiar with how to use classes in real programs.

⸻

③ Challenge the AI

One AI-generated question I challenged:

“Every object created from the same class always has exactly the same data.”

⸻

Why?

☐ Ambiguous  
☐ Oversimplified  
☐ Technically questionable  
☑ Too easy  
☐ Other: __________

Brief explanation:

This question felt relatively easy because I had already learned that different objects can store different values even if they are created from the same class.

⸻

④ One-Minute Reflection

One thing I am still unsure about:

I am still not very sure when I should use a class instead of normal variables and functions, and I need more practice with actual C++ programs.

⸻

## Part B: LeetCode-style Lecture Code Transfer

### AI Tutor Learning Record — Coding Challenge

Name: 114511074  
Date: 2026/10/05  
Topic: C++ classes, objects, and member functions

1. Today’s Challenge

Core concept from today’s OCW lecture:

Using a class to put related data and functions together, and creating objects from that class.

⸻

AI-generated coding challenge title:

Student Score Tracker

⸻⸻

2. My Initial Approach — Before AI Help

Before asking AI for hints, briefly describe how you planned to solve the problem.

My approach:

At first, I planned to use several variables and normal functions because I am more familiar with that way. I was not very sure how to organize the data using a class.

⸻⸻⸻

3. AI Tutor Help

Did you ask the AI Tutor for help?

☐ No — I solved it independently  
☑ Yes — I received one or more hints

The most useful hint/question from AI was:

“Which data belongs to each individual Student object, and which operation should be implemented as a member function?”

⸻

It helped me realize that:

The student's name and scores can be stored inside each Student object, and functions such as calculating the average can be placed inside the class. I understand the idea, but I am still not very confident about writing it by myself.

⸻

4. My Revision

Did you change your approach or code after interacting with AI?

☐ No  
☑ Yes

What did you change, and why?

I changed my original idea from using separate variables and functions to using a Student class. This made the structure clearer, but I still needed AI hints to understand how the data and functions should be organized.

⸻⸻⸻

5. Verification

My final program:

☑ Passed the provided examples  
☑ Passed additional edge cases  
☐ Still has unresolved problems

One edge case I tested:

Input: A student with only one score, 100

Expected output: Average = 100

Actual output: Average = 100

6. One-Minute Reflection

What idea from the OCW lecture did you transfer to this new problem?

I tried to use a class to keep related data and functions together instead of putting everything separately.

⸻

One thing I understand better now:

I understand the basic difference between a class and an object better than before.

⸻

One thing I am still unsure about:

I am still not very familiar with writing classes in C++, especially constructors, public/private members, and deciding what should be placed inside a class.

⸻
