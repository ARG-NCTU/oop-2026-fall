Name: 范芷祺
Date: 2026/10/03
Topic: Recursion, Dictionaries, and Memoization

Today’s Challenge

Core concept from today’s OCW lecture:

A recursive solution should reduce a problem into smaller versions of the same problem until it reaches a base case. A dictionary can also store previously computed results so that repeated recursive subproblems do not have to be solved again.

⸻

AI-generated coding challenge title:

Recursive Package Counter

⸻⸻

My Initial Approach — Before AI Help

Before asking AI for hints, briefly describe how you planned to solve the problem.

My approach:

I planned to look up a package name in a dictionary. If the package contained smaller packages or individual items, I would recursively count the contents of each one and add the results together. At first, I did not clearly separate the base case from the recursive case, and I planned to recompute the same package every time it appeared.

⸻⸻⸻

AI Tutor Help

Did you ask the AI Tutor for help?

☐ No — I solved it independently
☑ Yes — I received one or more hints

The most useful hint/question from AI was:

“What should happen when the current item is not a key in the package dictionary? Also, if the same package appears several times, do you really need to solve that package again every time?”

⸻

It helped me realize that:

An item that is not a key in the dictionary should be the base case and count as one individual item. For repeated packages, I can store the result in another dictionary and reuse it later instead of doing the same recursive work again.

⸻

My Revision

Did you change your approach or code after interacting with AI?

☐ No
☑ Yes

What did you change, and why?

I added a clear base case: if the current name is not in the package dictionary, the function returns 1. For the recursive case, I add the counts of every component inside the package.

I also added a memo dictionary. Before recursively expanding a package, I first check whether its total count is already stored. If it is, I return the stored value. Otherwise, I calculate the value, save it in the dictionary, and then return it.

⸻⸻⸻

Verification

My final program:

☑ Passed the provided examples
☑ Passed additional edge cases
☐ Still has unresolved problems

One edge case I tested:

Input: item = "pen", packages = {"starter": ["pen", "notebook"]}

Expected output: 1

Actual output: 1

One-Minute Reflection

What idea from the OCW lecture did you transfer to this new problem?

I transferred the recursion pattern of having a base case and reducing the original problem into smaller versions of the same problem. I also transferred the idea of using a dictionary to remember results that have already been calculated.

⸻

One thing I understand better now:

I understand that recursion is not just “a function calling itself.” Each recursive call should make progress toward a base case. I also understand how a dictionary can make recursive code more efficient by avoiding repeated calculations.

⸻

One thing I am still unsure about:

I am still unsure about how to estimate the time complexity of recursive programs when memoization changes the number of repeated calls.

⸻