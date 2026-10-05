# AI Tutor Learning Record — Week 3

Topic: Testing, Debugging, Exceptions and Assertions
Date: 2026/09/21

## Part A: True or False

### ① Check My Understanding

Questions completed: 5 / 5

Answers revised after AI hints: 2 / 5


### ② My Misconception

Before: I thought testing and debugging were almost the same thing because both are used when a program does not work correctly.

Now: I understand that testing is used to check whether the program behaves according to its specification, while debugging is the process of finding out why an incorrect result happened and fixing the source of the problem.


### ③ Challenge the AI

One AI-generated question I challenged:

> If a program passes all current test cases, it must be completely correct.

Why?

☐ Ambiguous  
☑ Oversimplified  
☐ Technically questionable  
☐ Too easy  
☐ Other: __________

Brief explanation:

Passing the current tests only shows that the program works for the tested cases.

There may still be bugs in inputs or code paths that were not tested, especially boundary conditions or unusual inputs.


### ④ One-Minute Reflection

One thing I am still unsure about:

I am still a little confused about how to decide which test cases are enough, especially when there are many possible inputs and code paths.


---

## Part B: Coding Challenge

Name: 高芮妮
Date: 2026/09/21
Topic: Testing, Exceptions and Defensive Programming


## 1. Today’s Challenge

Core concept from today’s OCW lecture:

Designing useful test cases, handling unexpected conditions with exceptions, and checking assumptions using assertions.

AI-generated coding challenge title:

**Safe Grade Average**

The challenge asks me to write a function that calculates the average of a list of grades.

The function should work for normal grade lists, but it should also handle invalid situations such as an empty list.


## 2. My Initial Approach — Before AI Help

Before asking AI for hints, briefly describe how you planned to solve the problem.

My approach:

I planned to calculate the result using:

`sum(grades) / len(grades)`

Then I would test the function using a normal list such as:

`[80, 90, 100]`


## 3. AI Tutor Help

Did you ask the AI Tutor for help?

☐ No — I solved it independently  
☑ Yes — I received one or more hints

The most useful hint/question from AI was:

> What happens if the grade list is empty, and have you tested the boundary or error cases instead of only normal inputs?

It helped me realize that:

If the list is empty, `len(grades)` is 0, so the function causes a `ZeroDivisionError`.

Testing only normal inputs is not enough. I also need to think about boundary and unexpected inputs.


## 4. My Revision

Did you change your approach or code after interacting with AI?

☐ No  
☑ Yes

What did you change, and why?

I added a check for the empty-list case.

I considered using an assertion such as:

`assert len(grades) != 0, "no grades data"`

This makes the program stop immediately if an assumption about the input is not satisfied.

I also added more test cases instead of testing only one normal example.


## 5. Verification

My final program:

☑ Passed the provided examples  
☑ Passed additional edge cases  
☐ Still has unresolved problems

One normal test:

Input:

`[80, 90, 100]`

Expected output:

`90`

Actual output:

`90`


One edge case:

Input:

`[]`

Expected result:

The program should report that there is no grade data instead of trying to divide by zero.

Actual result:

The assertion detected the invalid input.


## 6. One-Minute Reflection

What idea from the OCW lecture did you transfer to this new problem?

I transferred the idea that testing should include more than normal examples. I should also think about boundary conditions and invalid inputs.

I also used the idea of assertions as defensive programming to check whether the assumptions of a function are satisfied.

One thing I understand better now:

I understand the difference between testing and debugging better. Testing helps reveal that something is wrong, while debugging focuses on finding how the unexpected result happened.

One thing I am still unsure about:

I am still not completely sure when I should use an assertion and when I should raise and handle a normal exception with `try/except`.