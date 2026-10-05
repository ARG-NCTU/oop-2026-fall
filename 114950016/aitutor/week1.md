# AI Tutor Learning Record — Week 1

Topic: Tuples, Lists, Aliasing, Mutability and Cloning
Date: 2026/09/07

## Part A: True or False

### ① Check My Understanding

Questions completed: 5 / 5

Answers revised after AI hints: 2 / 5


### ② My Misconception

Before: I thought tuples and lists were basically the same, and the main difference was only that tuples use parentheses while lists use square brackets.

Now: I understand that the more important difference is mutability. A tuple is immutable, so its elements cannot be changed after it is created, while a list is mutable and its elements can be modified.


### ③ Challenge the AI

One AI-generated question I challenged:

> If two variables have the same list values, they must refer to the same list object.

Why?

☐ Ambiguous  
☑ Oversimplified  
☐ Technically questionable  
☐ Too easy  
☐ Other: __________

Brief explanation:

Two lists can contain exactly the same values but still be different objects.

For example, if I use cloning such as `chill = cool[:]`, the two lists initially contain the same elements, but changing `chill` does not change `cool`.

However, if I write `hot = warm`, both variables point to the same list object, so changing one can affect the other.


### ④ One-Minute Reflection

One thing I am still unsure about:

I am still confused about nested lists. If one list contains another list, I sometimes cannot immediately tell which variables point to the same object and which changes will cause side effects.


---

## Part B: Coding Challenge

Name: 高芮妮
Date: 2026/09/07
Topic: Mutability, Aliasing and Cloning


## 1. Today’s Challenge

Core concept from today’s OCW lecture:

Understanding how mutable lists behave in memory, especially aliasing, cloning, and side effects.

AI-generated coding challenge title:

**Safe Duplicate Removal**

The challenge asks me to remove from `L1` every element that also appears in `L2`.

The important rule is that the program should correctly remove all matching values without skipping elements.


## 2. My Initial Approach — Before AI Help

Before asking AI for hints, briefly describe how you planned to solve the problem.

My approach:

I planned to loop directly through `L1`.

For every element in `L1`, if that element was also in `L2`, I would use `L1.remove()` to remove it.


## 3. AI Tutor Help

Did you ask the AI Tutor for help?

☐ No — I solved it independently  
☑ Yes — I received one or more hints

The most useful hint/question from AI was:

> What happens to the positions of the remaining elements if you change the length of a list while a loop is still iterating over that same list?

It helped me realize that:

Mutating a list while iterating over it can make the loop skip elements.

Python keeps track of its current position in the loop, but removing an item changes the list length and shifts the remaining elements.


## 4. My Revision

Did you change your approach or code after interacting with AI?

☐ No  
☑ Yes

What did you change, and why?

I first cloned `L1` using:

`L1_copy = L1[:]`

Then I iterated over `L1_copy`.

If an element also appeared in `L2`, I removed that element from the original `L1`.

I changed my approach because the copied list does not change while I am iterating over it, so the loop will not accidentally skip an element.


## 5. Verification

My final program:

☑ Passed the provided examples  
☑ Passed additional edge cases  
☐ Still has unresolved problems

One example I tested:

Input:

`L1 = [1, 2, 3, 4]`

`L2 = [1, 2, 5, 6]`

Expected output:

`L1 = [3, 4]`

Actual output:

`L1 = [3, 4]`


One additional edge case I tested:

Input:

`L1 = [1, 1, 2, 3]`

`L2 = [1]`

Expected output:

`L1 = [2, 3]`

Actual output:

`L1 = [2, 3]`


## 6. One-Minute Reflection

What idea from the OCW lecture did you transfer to this new problem?

I transferred the idea that lists are mutable objects and modifying them can create side effects, especially when more than one variable refers to the same list or when the list is being changed during iteration.

One thing I understand better now:

I understand the difference between aliasing and cloning better. Aliasing means two variable names point to the same list object, while cloning creates a separate list object with copied elements.

One thing I am still unsure about:

I am still not completely sure how cloning behaves when the list contains other lists, because the outer list may be copied but the inner lists may still be shared.