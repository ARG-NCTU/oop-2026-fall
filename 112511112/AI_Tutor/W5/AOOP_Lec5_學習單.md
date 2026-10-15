# AOOP Lec5 學習單

Topic: Tuple, List, Mutability, Aliasing, Cloning  
Date: 2026-10-15

## ① Check My Understanding

Questions completed: 5 / 5  
Answers revised after AI hints: 2 / 5

---

## ② My Misconception

### Before: I thought…
I thought immutable simply meant an object could not be changed at all.

---

### Now: I understand…
Immutable only guarantees that the container's bindings cannot be directly changed.
If the container stores references to mutable objects, those underlying objects may still be modified.
Therefore, aliasing and side effects can still occur when mutable objects are nested inside immutable containers.

---

## ③ Challenge the AI

### One AI-generated question I challenged:
Question 1:

> If two variables point to the same list, then as long as one variable is renamed, the other variable will also be affected.

---

### Why?

☑ Ambiguous  
☐ Oversimplified  
☐ Technically questionable  
☐ Too easy  
☐ Other: __________

### Brief explanation:

The term "rename" is ambiguous.

It could mean:

- Rebinding a variable to a new object (`M = [4,5,6]`)
- Mutating the shared object (`M.append(4)`)

These lead to completely different outcomes.
A better question should explicitly distinguish between rebinding and mutating.

---

## ④ One-Minute Reflection

### One thing I am still unsure about:

The difference between shallow copy and deep copy.

Current understanding:

- Shallow copy duplicates only the first layer.
- Nested mutable objects may still be shared.
- Deep copy recursively duplicates nested objects.

I would like more practice tracing object references and predicting when changes propagate between copies.

---

## Personal Summary

### Key Lec5 Takeaway

Variables are not the main thing to track.
Objects are.

When analyzing code, ask:

1. How many objects exist?
2. Which names point to the same object?
3. Is the operation a rebind or a mutate?
4. Is the object mutable or immutable?

### Distinction Learned

```text
Aliasing + Mutable Object
    -> Possible side effects

Aliasing + Immutable Object
    -> Usually safe

Immutable Container + Mutable Contents
    -> Side effects may still occur
```
