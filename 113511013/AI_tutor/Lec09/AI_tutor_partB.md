Name: 范芷祺
Date: 2026/10/04
Topic: Object-Oriented Programming

Today’s Challenge

Core concept from today’s OCW lecture:

Objects combine an internal data representation with methods that define how users interact with the object. A class defines a new type, __init__ initializes each instance, self refers to the current object, and special methods such as __str__ can customize built-in behavior.

⸻

AI-generated coding challenge title:

Reading Progress Tracker

⸻⸻

My Initial Approach — Before AI Help

Before asking AI for hints, briefly describe how you planned to solve the problem.

My approach:

I planned to create a BookProgress class with the book title, total number of pages, and number of pages already read. I would write separate functions outside the class to update the number of pages and calculate how many pages are left.

⸻⸻⸻

AI Tutor Help

Did you ask the AI Tutor for help?

☐ No — I solved it independently
☑ Yes — I received one or more hints

The most useful hint/question from AI was:

“If the operations only make sense for a BookProgress object, would it be clearer to make them methods of the class instead of separate functions? Which object should self refer to when the method is called?”

⸻

It helped me realize that:

The data and the operations that work on that data should be bundled together inside the class. I should use instance attributes such as self.title, self.total_pages, and self.pages_read, and methods can use self to access or modify the current object.

⸻

My Revision

Did you change your approach or code after interacting with AI?

☐ No
☑ Yes

What did you change, and why?

I moved the behavior into the class. I used __init__ to initialize the title, total pages, and pages already read. I added a read() method to increase the reading progress without allowing it to go past the total number of pages, and a remaining() method to return how many pages are left. I also added __str__ so that printing the object gives a useful description instead of the default memory-style representation.

⸻⸻⸻

Verification

My final program:

☑ Passed the provided examples
☑ Passed additional edge cases
☐ Still has unresolved problems

One edge case I tested:

Input: Create BookProgress("Python", 100), then call read(150)

Expected output: The progress should stop at 100 pages, so remaining() should return 0

Actual output: 0

One-Minute Reflection

What idea from the OCW lecture did you transfer to this new problem?

I transferred the idea of using a class to bundle data attributes together with methods that operate on those attributes. I also used __init__, self, dot notation, and __str__.

⸻

One thing I understand better now:

I understand the difference between defining a class and creating an instance of that class. I also understand that self refers to the particular object that called the method and is passed automatically by Python.

⸻

One thing I am still unsure about:

I am still unsure about how to decide which operations should become normal methods and which should be implemented as special methods such as __eq__ or __len__.

⸻