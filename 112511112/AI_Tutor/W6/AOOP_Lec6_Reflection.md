# AOOP Lec6 Learning Reflection Worksheet

Topic: AOOP Lec6 - Recursion & Dictionary  
Date: 2026-10-15

## ① Check My Understanding

Questions completed: 5 / 5  
Answers revised after AI hints: 2 / 5

---

## ② My Misconception

### Before: I thought…

A tuple containing a list could still be used as a dictionary key because the outer object is a tuple.

---

### Now: I understand…

Dictionary keys must be hashable. While tuples are usually hashable, a tuple that contains mutable objects (such as lists) is not hashable and therefore cannot be used as a dictionary key.

I also reinforced the idea that recursion requires both:

- A Base Case (to stop recursion)
- A Recursive Case (to reduce the problem)

Reducing the problem alone is not sufficient.

---

## ③ Challenge the AI

### One AI-generated question I challenged:

Question 5:

> Using a dictionary to store previously computed Fibonacci results (memoization) changes the efficiency of the algorithm but not its correctness.

---

### Why?

☐ Ambiguous  
☐ Oversimplified  
☐ Technically questionable  
☑ Too easy  
☐ Other: __________

### Brief explanation:

The answer was almost immediate because memoization clearly reduces repeated computation without changing the mathematical definition of Fibonacci.

---

## ④ One-Minute Reflection

### One thing I am still unsure about:

Why does Python essentially treat mutable objects as unhashable?

Current understanding:

- Dictionary lookup relies on a stable hash value.
- Mutable objects can change after insertion.
- If the hash changed, the dictionary could lose track of where the key belongs.

I understand the intuition, but I would like a deeper understanding of the relationship between mutability, hashability, and dictionary implementation.
