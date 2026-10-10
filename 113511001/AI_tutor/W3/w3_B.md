Name: 張永怡

Date: 2026/09/23

Topic: Testing, Debugging, Exceptions, and Assertions

1. Today’s Challenge

Core concept from today’s OCW lecture:

Exception handling using try/except and raising exceptions for invalid input.

AI-generated coding challenge title:

Process Sensor Readings


2. My Initial Approach — Before AI Help

Before asking AI for hints, briefly describe how you planned to solve the problem.

My approach:

Loop through each sensor reading, try to divide the measured value by the calibration factor, use "INVALID" when division by zero happens, raise a ValueError if the data type is wrong, and return a new list with the processed results.


3. AI Tutor Help

Did you ask the AI Tutor for help?

☐ No — I solved it independently

☑ Yes — I received one or more hints

The most useful hint/question from AI was:

“Think about which exception should specifically correspond to division by zero, and which one should correspond to bad types.”

It helped me realize that:

I should handle ZeroDivisionError and TypeError separately because they represent different problems.


4. My Revision

Did you change your approach or code after interacting with AI?

☐ No

☑ Yes

What did you change, and why?

I changed typeError to TypeError, changed tuples to lists, and fixed the control flow so the program does not append twice when division by zero happens.


5. Verification

My final program:

☑ Passed the provided examples

☑ Passed additional edge cases

☐ Still has unresolved problems

One edge case I tested:

Input: [["A", 10, 0]]

Expected output: [["A", "INVALID"]]

Actual output: [["A", "INVALID"]]


6. One-Minute Reflection

What idea from the OCW lecture did you transfer to this new problem?

I used try/except to handle different exceptions and used ValueError to report invalid input.

One thing I understand better now:

I understand better how different exceptions should be handled differently depending on the problem.

One thing I am still unsure about:

I am still unsure about when I should raise a new exception instead of handling the original exception directly.