Topic: Tuples, Lists, Aliasing, Mutability, and Cloning
Date: 2026/10/03

① Check My Understanding

Questions completed: 5 / 5

Answers revised after AI hints: 3 / 5

② My Misconception

Before: I thought…

Assigning one list variable to another, such as B = A, would create an independent copy. I also thought it was safe to remove elements from a list while iterating over that same list.

⸻

Now: I understand…

B = A creates an alias, so both variables point to the same mutable list object. If I need a separate outer list, I can clone it with slicing such as B = A[:]. I also understand that mutating a list while iterating over it can cause elements to be skipped, so it is safer to iterate over a clone when removing elements from the original list.

⸻

③ Challenge the AI

One AI-generated question I challenged:

“Using copy = original[:] always makes the copy completely independent from the original list.”

⸻

Why?

☐ Ambiguous
☐ Oversimplified
☑ Technically questionable
☐ Too easy
☐ Other: __________

Brief explanation:

For a simple list, slicing creates a new outer list. However, if the list contains inner lists, the inner lists may still be shared between the original and the clone. Therefore, saying the copy is “completely independent” is too strong.

⸻

④ One-Minute Reflection

One thing I am still unsure about:

I am still unsure about how aliasing works with nested lists, especially when the outer list is cloned but the inner lists are still shared.

⸻