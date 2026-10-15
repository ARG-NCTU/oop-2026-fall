# AOOP Lec5 Coding Challenge Reflection Sheet

**Name:** 朱昱瑋  
**Date:** 20261015 
**Topic:** Tuple, Immutability, Aliasing, Copying

<br>

## 1. Today's Challenge

### Core concept from today's OCW lecture:
- Tuple vs List
- Immutable vs Mutable objects
- Rebind vs Mutate
- Aliasing
- Shallow Copy vs Deep Copy

### AI-generated coding challenge title:
**Exploring Immutable Containers and Hidden Mutability**

⸻⸻

## 2. My Initial Approach — Before AI Help

Before asking AI for hints, briefly describe how you planned to solve the problem.

### My approach:
I initially understood immutability as simply “cannot be changed.” I assumed tuples were completely protected from modification and that aliasing mainly applied to lists. I also tended to think that assignment created a copy rather than another reference.

⸻⸻⸻

## 3. AI Tutor Help

### Did you ask the AI Tutor for help?
☐ No — I solved it independently  
☑ Yes — I received one or more hints

### The most useful hint/question from AI was:
"If a tuple contains a list, is the tuple protecting the list itself, or only the reference to the list?"

### It helped me realize that:
Tuple immutability only protects one layer.
If a tuple stores a mutable object such as a list, the list itself can still be changed.
The reference is protected, but the referenced object's contents may not be.

⸻

## 4. My Revision

### Did you change your approach or code after interacting with AI?
☐ No  
☑ Yes

### What did you change, and why?
I revised my mental model of immutable objects.

Before:
- Immutable means nothing inside can change.

Now:
- Immutable means the object itself cannot be mutated.
- However, contained mutable objects may still change.
- Assignment (`a = b`) creates aliasing instead of copying.
- Rebinding and mutation are different operations.

⸻⸻⸻

## 5. Verification

### My final program:
☑ Passed the provided examples  
☑ Passed additional edge cases  
☐ Still has unresolved problems

### One edge case I tested:

Input:
```python
A = ([1, 2],)
A[0].append(3)
print(A)
```

Expected output:
```python
([1, 2, 3],)
```

Actual output:
```python
([1, 2, 3],)
```

Observation:
The tuple itself was unchanged, but the list inside it was successfully mutated.

## 6. One-Minute Reflection

### What idea from the OCW lecture did you transfer to this new problem?
The distinction between mutating an object and rebinding a variable is crucial for understanding Python behavior.

⸻

### One thing I understand better now:
I originally thought immutability simply meant an object could not change. Now I understand it protects only that object's structure, and mutable objects referenced inside may still be modified.

⸻

### One thing I am still unsure about:
The difference between shallow copy and deep copy, especially when nested lists and other containers are involved.

⸻

## 7. Personal Summary

### My Lec5 Takeaway

- Tuple and str share many behaviors because both are immutable sequences.
- Aliasing can occur with any object type.
- Mutable objects reveal aliasing effects more clearly.
- Rebind changes a reference.
- Mutate changes an object.
- Shallow copy copies only the first level.
- Deep copy recursively duplicates all contained objects.

### One-Sentence Summary

"Immutability protects an object's structure, not necessarily the mutable objects it may reference."
