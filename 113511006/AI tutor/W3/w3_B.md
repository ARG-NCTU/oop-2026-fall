Name: 池旻柔
Date: 2026/09/23
Topic: Testing, Debugging, Exceptions, and Assertions

1. Today’s Challenge

Core concept from today’s OCW lecture:

Using exceptions to detect and handle invalid input, and using testing to verify that a function behaves correctly for both normal and edge cases.

⸻

AI-generated coding challenge title:

Safe Average Calculator

⸻⸻

2. My Initial Approach — Before AI Help

Before asking AI for hints, briefly describe how you planned to solve the problem.

My approach:

I planned to loop through the scores and calculate their average. Before calculating, I would check whether the list is empty and whether every score is between 0 and 100. If the input is invalid, I would raise an exception instead of returning an incorrect result.

⸻⸻⸻

3. AI Tutor Help

Did you ask the AI Tutor for help?

☐ No — I solved it independently
☑ Yes — I received one or more hints

The most useful hint/question from AI was:

“What should happen if a score is not a number, and is that the same kind of problem as a numeric score outside the valid range?”

⸻

It helped me realize that:

Different invalid inputs should be treated differently. A score with the wrong data type should cause a TypeError, while a numeric score outside the range 0 to 100 should cause a ValueError.

⸻

4. My Revision

Did you change your approach or code after interacting with AI?

☐ No
☑ Yes

What did you change, and why?

I changed my solution so that it checks the type of each score separately from its valid range. I used TypeError for non-numeric values and ValueError for an empty list or scores outside the range 0 to 100. This makes the cause of an error clearer.

⸻⸻⸻

5. Verification

My final program:

☑ Passed the provided examples
☑ Passed additional edge cases
☐ Still has unresolved problems

One edge case I tested:

Input: [80, 90, 101]

Expected output: ValueError

Actual output: ValueError

6. One-Minute Reflection

What idea from the OCW lecture did you transfer to this new problem?

I transferred the idea that a function should detect invalid input and raise an appropriate exception instead of silently returning an incorrect or special value.

⸻

One thing I understand better now:

I understand better that different types of invalid input can represent different errors, and choosing an appropriate exception makes the program easier to understand and debug.

⸻

One thing I am still unsure about:

I am still unsure about how specific exception handling should be in larger programs and when it is better to catch an exception instead of allowing it to propagate.

⸻