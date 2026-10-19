# week4 AI Tutor Learning Record

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


