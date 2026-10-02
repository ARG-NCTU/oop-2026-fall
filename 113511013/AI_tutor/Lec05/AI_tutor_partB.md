Name: 范芷祺
Date: 2026/10/03
Topic: List Mutation, Aliasing, Cloning, and Safe Iteration

Today’s Challenge

Core concept from today’s OCW lecture:

Lists are mutable, two variables can alias the same list, cloning creates a separate outer list, and mutating a list while iterating over it can cause elements to be skipped.

⸻

AI-generated coding challenge title:

Safe Playlist Cleanup

⸻⸻

My Initial Approach — Before AI Help

Before asking AI for hints, briefly describe how you planned to solve the problem.

My approach:

I planned to loop directly through the playlist. If a song appeared in the blocked list, I would remove it from the playlist immediately. After the loop, I planned to return the playlist.

⸻⸻⸻

AI Tutor Help

Did you ask the AI Tutor for help?

☐ No — I solved it independently
☑ Yes — I received one or more hints

The most useful hint/question from AI was:

“If you remove an element from the same list that the for loop is currently iterating over, could the next element shift position and be skipped?”

⸻

It helped me realize that:

I should not mutate the same list that I am using for iteration. I should first clone the playlist, iterate over the clone, and remove blocked songs from the original list. I also realized that returning the original list directly would create another alias, so I should return a clone.

⸻

My Revision

Did you change your approach or code after interacting with AI?

☐ No
☑ Yes

What did you change, and why?

I created playlist_copy = playlist[:] and iterated over that copy. When a song in the copy was also in the blocked list, I removed one matching occurrence from the original playlist. After cleaning the original playlist, I returned playlist[:] so that the returned result was a separate outer list instead of an alias.

⸻⸻⸻

Verification

My final program:

☑ Passed the provided examples
☑ Passed additional edge cases
☐ Still has unresolved problems

One edge case I tested:

Input: playlist = ["A", "A", "B"], blocked = ["A", "B"]

Expected output: playlist == [], returned list == []

Actual output: playlist == [], returned list == []

One-Minute Reflection

What idea from the OCW lecture did you transfer to this new problem?

I transferred the idea of cloning a list before iterating when I need to mutate the original list. I also applied the difference between aliasing and cloning.

⸻

One thing I understand better now:

I understand why changing a list during iteration can skip elements, and I understand that B = A creates an alias while B = A[:] creates a new outer list.

⸻

One thing I am still unsure about:

I am still unsure about shallow cloning with nested lists, because the outer list can be different while the inner lists are still shared.

⸻