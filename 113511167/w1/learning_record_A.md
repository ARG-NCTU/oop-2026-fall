**Topic:** Tuples, Lists, Aliasing, Mutability, Cloning  
**Date:** 2026/11/22

### ① Check My Understanding

**Questions completed:** 5 / 5

**Answers revised after AI hints:** 0 / 5

### ② My Misconception

**Before: I thought…**

An immutable tuple meant that everything inside it could not be changed. I was also unsure about the difference between reassignment, mutation, and copying.

**Now: I understand…**

Tuple immutability only prevents replacing its elements, not modifying mutable objects inside it. Reassignment changes which object a variable refers to, while mutation changes the object itself. A shallow copy creates a new outer list but still shares references to nested objects.

### ③ Challenge the AI

**One AI-generated question I challenged:**

Question 4: "Creating a shallow copy of a nested list guarantees that modifying any element inside the copied list cannot affect the original list."

**Why?**

☑ Ambiguous  
☐ Oversimplified  
☐ Technically questionable  
☐ Too easy  
☐ Other: __________

**Brief explanation:**

The phrase "modifying any element" is ambiguous. Replacing an outer list element does not affect the original list, but mutating a shared nested list can. The answer is still False, but the question should distinguish between replacing an element and mutating a shared object.

### ④ One-Minute Reflection

**One thing I am still unsure about:**

How to distinguish shallow copying from deep copying in more complicated nested structures, especially when some inner objects are mutable and others are immutable.