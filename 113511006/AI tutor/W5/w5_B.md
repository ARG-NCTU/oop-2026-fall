Name: 池旻柔
Date: 2026/10/05
Topic: Tuples, Lists, Aliasing, Mutability, and Cloning
1. Today’s Challenge
Core concept from today’s OCW lecture:
Processing lists through iteration and membership checks, returning multiple values in a tuple, and using cloning to avoid unwanted side effects. The challenge also applies the lecture's warning about modifying a list during iteration.
⸻
AI-generated coding challenge title:
Score Cleaner and Safe Backup
The main task is to accept a list of integer scores, retain unique valid scores from 0 through 100, sort them, and return the cleaned list together with the number of invalid occurrences. Repeated valid scores are removed but are not counted as invalid. The input must remain unchanged.
Two additional tasks are to remove all blocked values while preserving the order and duplicates of retained items, and to copy a two-dimensional list of integers so that changes to a backup's rows do not affect the original.
⸻⸻
2. My Initial Approach — Before AI Help
Before asking AI for hints, briefly describe how you planned to solve the problem.
My approach:
I planned to assign cleaned = scores, loop over cleaned, and remove invalid values directly. I would then remove repeated values and sort the remaining scores. For the backup, I initially planned to use rows[:] without copying each inner row.
⸻⸻⸻
3. AI Tutor Help
Did you ask the AI Tutor for help?
☐ No — I solved it independently
☐ Yes — I received one or more hints
The most useful hint/question from AI was:
“Does cleaned = scores create a new list? After removing an element, which value moves into its old index? If you copy only the outer list, are the inner rows copied too?”
⸻
It helped me realize that:
Assignment creates another reference to the same object. Removing an element while iterating can shift later elements and cause the loop to skip them. A shallow copy also keeps references to the same inner rows. These are different problems, so I need to choose a suitable copying or construction strategy for each task.
⸻
4. My Revision
Did you change your approach or code after interacting with AI?
☐ No
☐ Yes
What did you change, and why?
I created a new valid-score list instead of modifying the input. I checked each score's range, counted invalid occurrences separately, and appended valid scores only when they were not already present. I used sorted to return an ordered list and returned it together with the invalid count in a tuple.
For blocked values, I built a new result list, so consecutive blocked values could be removed without skipping any elements. For the two-dimensional backup, I copied every row using row[:]. This works for the specified integer rows, but it is not a general deep copy for arbitrarily nested objects.
⸻⸻⸻
5. Verification
My final program:
☑ Passed the provided examples
☑ Passed additional edge cases
☐ Still has unresolved problems
One edge case I tested:
Input: clean_scores([0, 100, -1, 101, 100])
Expected output: ([0, 100], 2)
Actual output: ([0, 100], 2)
Additional edge cases verified in the supplied program:
- An empty score list returns ([], 0).
- All-invalid input [-1, 101, -1] returns ([], 3).
- Repeated valid scores [60, 60, 60] return ([60], 0).
- Consecutive blocked values in [1, 2, 2, 3, 4] with blocked [1, 2] produce [3, 4].
- Retained duplicates keep their original order.
- Both inputs to remove_blocked remain unchanged.
- Editing a copied row does not change the original integer rows.
- Empty outer lists and empty rows can also be copied.
6. One-Minute Reflection
What idea from the OCW lecture did you transfer to this new problem?
I transferred list iteration, membership checks, tuple returns, and cloning to a score-processing problem. I also used the idea that a function should make its mutation behavior clear to callers.
⸻
One thing I understand better now:
I understand better that aliasing and cloning are different. I can avoid accidental changes by building a new result list, and I need to copy inner rows when independence is required for this two-dimensional example. I also understand that sort changes an existing list and returns None, while sorted returns a new sorted list. Returning a tuple does not make the list inside it immutable.
⸻
One thing I am still unsure about:
I am still unsure about when to use a general deep copy and when shared references are intentional. I also want to learn more efficient ways to remove duplicates from very large lists without repeatedly scanning the values already collected.
⸻