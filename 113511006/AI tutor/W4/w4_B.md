Name: 池旻柔
Date: 2026/10/05
Topic: Decomposition, Abstraction, Functions, and Scope
1. Today’s Challenge
Core concept from today’s OCW lecture:
Dividing a program into reusable functions, specifying their inputs and outputs, returning results to the caller, and passing a function as an argument.
⸻
AI-generated coding challenge title:
Score Adjustment and Passing Counter
⸻⸻
2. My Initial Approach — Before AI Help
Before asking AI for hints, briefly describe how you planned to solve the problem.
My approach:
I planned to use one loop to add five points to each score, limit the adjusted score to 100, and count how many adjusted scores were at least 60. I initially planned to print the count inside the function without returning it.
⸻⸻⸻
3. AI Tutor Help
Did you ask the AI Tutor for help?
☐ No — I solved it independently
☐ Yes — I received one or more hints
The most useful hint/question from AI was:
“If your function only prints the count, what value will another function receive when it calls it? Which parts of the calculation could be separate functions?”
⸻
It helped me realize that:
Returning the count makes it available for later calculations. Separating adjustment, passing-score checking, and counting also makes the code easier to reuse and test.
⸻
4. My Revision
Did you change your approach or code after interacting with AI?
☐ No
☐ Yes
What did you change, and why?
I separated the program into apply_adjustment, add_bonus, is_passing, and count_passing. I used return to send results to the caller and kept print in the demonstration code. I also passed the adjustment function as an argument so that a different adjustment rule could be used without rewriting the counter.
⸻⸻⸻
5. Verification
My final program:
☑ Passed the provided examples
☑ Passed additional edge cases
☐ Still has unresolved problems
One edge case I tested:
Input: count_passing([], add_bonus)
Expected output: 0
Actual output: 0
6. One-Minute Reflection
What idea from the OCW lecture did you transfer to this new problem?
I transferred decomposition by giving each function a specific task. I also used abstraction by documenting what each function accepts and returns, so the caller can use it without needing every implementation detail.
⸻
One thing I understand better now:
I understand better that return and print have different purposes. I also understand that passing add_bonus supplies the function itself, while calling add_bonus(score) supplies its returned value. The temporary variables inside count_passing are local to that function call.
⸻
One thing I am still unsure about:
I am still unsure about tracing nested function calls and keeping track of which variables belong to each scope.
⸻