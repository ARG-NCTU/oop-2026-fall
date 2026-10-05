Topic: Tuples, Lists, Aliasing, Mutability, and Cloning
Date: 2026/10/05
① Check My Understanding
Questions completed: 5 / 5
Answers revised after AI hints:0 / 5
② My Misconception
Before: I thought…
I thought that assigning one list to another variable created an independent copy. I also thought that using slicing to copy a nested list would make all its inner lists independent.
⸻
Now: I understand…
I understand that backup = original creates an alias, so both names refer to the same list. Mutating that list through either name is visible through the other. Using original[:] creates a new outer list, but it is a shallow copy: inner lists may still be shared. For a two-dimensional list of integers, copying each row allows the backup's scores to be changed without changing the original.
I also understand that tuples are immutable at their positions, while lists are mutable. However, a tuple can contain a mutable list, and the contents of that list can still change.
⸻
③ Challenge the AI
One AI-generated question I challenged:
“After backup = original[:], changing backup will never affect original.”
⸻
Why?
☐ Ambiguous
☑ Oversimplified
☑ Technically questionable
☐ Too easy
☐ Other: __________
Brief explanation:
The statement does not specify what kind of change is made. Appending to the new outer list does not change the original outer list. However, when original = [[1, 2]], modifying backup[0][0] changes the shared inner list and is also visible through original. The question should distinguish between changing the outer container and mutating a shared nested object.
⸻
④ One-Minute Reflection
One thing I am still unsure about:
I am still unsure about copying structures with more than two levels of nested lists and deciding when sharing objects is useful. I understand better why removing elements while iterating over the same list can skip values, and why creating a new result list is often easier to reason about.
⸻