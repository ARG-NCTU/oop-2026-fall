Name: ycchiu226\
Date: 2026/10/08\
Topic: Python Classes and Inheritance

1. Today’s Challenge

Core concept from today’s OCW lecture:

Inheritance, method overriding, parent class initialization, and class variables. The parent class provides common data and behavior, while subclasses can specialize behavior by defining their own methods.

⸻

AI-generated coding challenge title:

Smart Library System

⸻⸻

2. My Initial Approach — Before AI Help

Before asking AI for hints, briefly describe how you planned to solve the problem.

My approach:

I planned to create a parent `Member` class to handle the common information for all members, including their name, number of borrowed books, and a unique ID. I planned to use a class variable to generate the IDs.

Then I would create `StudentMember` and `FacultyMember` as subclasses. They would inherit the initialization and status-related methods from `Member`, but each subclass would have its own `borrow_book()` method with a different borrowing limit. I would also use a dictionary to store members by their IDs so that I could quickly find the correct member when processing each operation.

⸻⸻⸻

3. AI Tutor Help

Did you ask the AI Tutor for help?

☐ No — I solved it independently\
☒ Yes — I received one or more hints

The most useful hint/question from AI was:

The AI asked me to explain how the parent class and subclasses cooperate, why the solution works, and which concepts from the lecture were transferred to the new problem.

⸻

It helped me realize that:

The parent class should focus on the common parts of all members, while the subclasses should only handle the behavior that is different. I also realized that my final implementation did not need a `borrow_book()` method in the parent class because both subclasses could define their own version.

⸻

4. My Revision

Did you change your approach or code after interacting with AI?

☒ No\
☐ Yes

What did you change, and why?

I kept the core implementation unchanged because it passed the provided example and the additional edge cases. I did consider adding a check for invalid member IDs in the operation-processing part to prevent a possible `KeyError`, but the challenge guarantees valid IDs, so this was not necessary for the given problem.

⸻⸻⸻

5. Verification

My final program:

☒ Passed the provided examples\
☒ Passed additional edge cases\
☐ Still has unresolved problems

One edge case I tested:

Input: A student member attempts to borrow 4 books.

Expected output: `Alice:3` because the student borrowing limit is 3.

Actual output: `Alice:3`

6. One-Minute Reflection

What idea from the OCW lecture did you transfer to this new problem?

I transferred the idea of inheritance and method specialization from the OCW lecture. `Member` provides the common structure, while `StudentMember` and `FacultyMember` inherit from it and implement different `borrow_book()` rules. I also transferred the use of class variables for generating unique IDs and the idea of reusing the parent class's initialization.

⸻

One thing I understand better now:

I understand better how a parent class and subclasses can divide responsibilities. The parent class does not need to contain every method; subclasses can add their own methods when the behavior is specific to that type. I also understand more clearly how class variables can be shared across instances and subclasses to maintain a global ID counter.

⸻

One thing I am still unsure about:

I am still unsure about when it is better to define a method in the parent class and override it in the subclasses, compared with leaving the method out of the parent class and defining it only in the subclasses. I also want to understand more clearly when `ParentClass.method(self, ...)` should be used instead of `super().method(...)`.
