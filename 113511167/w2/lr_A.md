**Topic:** Recursion, Dictionaries  
**Date:** 2026/11/23

### ① Check My Understanding

**Questions completed:** 5 / 5

**Answers revised after AI hints:** 0 / 5

### ② My Misconception

**Before: I thought…**

Having a base case was enough to guarantee that recursion would terminate. I also thought tuple immutability automatically made tuples valid dictionary keys.

**Now: I understand…**

Recursion requires both a correct base case and recursive steps that make progress toward it. Dictionary keys must be hashable, and a tuple containing a list cannot be used as a key. I also understand that mutating a shared dictionary value affects all aliases, while reassigning a value to a new object does not.

### ③ Challenge the AI

**One AI-generated question I challenged:**

Q5: "If two different dictionary keys refer to the same mutable list as their value, modifying that list through one key can also change the value observed through the other key."

**Why?**

☐ Ambiguous  
☑ Oversimplified  
☐ Technically questionable  
☐ Too easy  
☐ Other: __________

**Brief explanation:**

The question could distinguish more clearly between mutation and reassignment. Modifying a shared list in place affects both dictionary entries, while assigning a new list to one key does not affect the other. The AI gave me a follow-up comparing `+=` and `+`, which helped reinforce this distinction.

### ④ One-Minute Reflection

**One thing I am still unsure about:**

How to systematically verify that every branch of a complex recursive function eventually reaches a base case, and how to design consistent return values for recursive functions with multiple branches.