Name: 范芷祺
Date: 2026/10/03
Topic: Testing, Debugging, and In-place List Modification

Today’s Challenge

Core concept from today’s OCW lecture:

Modifying a list in place while carefully managing indices and avoiding overwriting values. The challenge also applied testing with normal and boundary cases.

AI-generated coding challenge title:

Move Zeros In Place

My Initial Approach — Before AI Help

Before asking AI for hints, briefly describe how you planned to solve the problem.

My approach:

I planned to scan the list from index 0. When I found a zero, I would count it and move the next non-zero value forward to replace it. After scanning the whole list, I would use the number of zeros to fill the remaining positions at the end of the list with zeros.

AI Tutor Help

Did you ask the AI Tutor for help?

☐ No — I solved it independently
☑ Yes — I received one or more hints

The most useful hint/question from AI was:

The AI suggested using two different positions: one position to scan through the list and another position to record where the next non-zero value should be written.

It helped me realize that:

I should separate the scanning position from the writing position. This avoids losing track of values or accidentally duplicating elements while modifying the list in place.

My Revision

Did you change your approach or code after interacting with AI?

☐ No
☑ Yes

What did you change, and why?

I changed my solution to use two indices. One index scans every element in the list, while the other marks the next position where a non-zero element should be placed. After all non-zero elements are moved forward, I fill the remaining positions with zeros.

I also learned that Python does not use ++, so I changed pos1++ to pos1 += 1.

This made the algorithm clearer and avoided problems caused by modifying values while scanning the list.

Verification

My final program:

☐ Passed the provided examples
☐ Passed additional edge cases
☑ Still has unresolved problems

One edge case I tested:

Input: [0, 0, 0]

Expected output: [0, 0, 0]

Actual output: Not yet executed locally

One-Minute Reflection

What idea from the OCW lecture did you transfer to this new problem?

I transferred the idea of modifying a list in place and carefully managing indices. Like the reverse-list example from the lecture, I had to avoid overwriting important values and think carefully about how each index moves.

One thing I understand better now:

I understand better how two indices can have different roles: one can scan the input while the other records where the next useful value should be written. I also understand why edge cases such as an empty list, a list with all zeros, or a list with no zeros should be tested.

One thing I am still unsure about:

I am still a little unsure about how to set up and run Python correctly in my current VS Code and PowerShell environment.