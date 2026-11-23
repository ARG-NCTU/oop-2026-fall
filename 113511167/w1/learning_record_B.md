**Name:** 廖顯祐  
**Date:** 2026/11/22  
**Topic:** Tuples, Lists, Aliasing, Mutability, Cloning

## 1. Today’s Challenge

**Core concept from today’s OCW lecture:**

Understanding list mutability, aliasing, and cloning, especially how to avoid unintended side effects when working with nested lists.

**AI-generated coding challenge title:**

Shared Inventory Cleanup

## 2. My Initial Approach — Before AI Help

**My approach:**

I planned to create a new outer list to store the results. For each room, I would create a new empty list, iterate through its items, and append only those not in the banned list. Then I would append the cleaned room to the result. This approach preserves the original order and avoids modifying the input lists, even when multiple rooms share the same list object.

## 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

☑ No — I solved it independently  
☐ Yes — I received one or more hints

**The most useful hint/question from AI was:**

The AI pointed out that checking whether an item is in a list takes O(B) time in the worst case, where B is the length of the banned list.

**It helped me realize that:**

I should consider the cost of membership checks when analyzing time complexity, rather than only counting the number of loops. I also learned that empty rooms must be considered in the overall complexity.

## 4. My Revision

**Did you change your approach or code after interacting with AI?**

☑ No  
☐ Yes

**What did you change, and why?**

My original algorithm and code passed the tests without modification. However, I refined my time complexity analysis from O(NB) to O(R + N(B + 1)) to account for empty rooms and an empty banned list.

## 5. Verification

**My final program:**

☑ Passed the provided examples  
☑ Passed additional edge cases  
☐ Still has unresolved problems

**One edge case I tested:**

Input:
```python
shared = [1, 2, 2, 3]
rooms = [shared, shared, [2, 4]]
banned = [2]
```

Expected output:
```python
[[1, 3], [1, 3], [4]]
```

Actual output:
```python
[[1, 3], [1, 3], [4]]
```

The original shared list remains unchanged, and the returned inner lists are independent objects.

## 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**

I applied the concepts of aliasing, mutability, and cloning. Instead of removing elements from the original lists while iterating, I constructed new lists to avoid unintended mutations and shared-reference side effects.

**One thing I understand better now:**

Creating a new outer list does not automatically make nested objects independent. To avoid aliasing problems, I need to consider which objects are newly created and which references are shared.

**One thing I am still unsure about:**

How to safely copy more complicated nested structures containing mutable objects, and when shallow copying is sufficient versus when deep copying is necessary.