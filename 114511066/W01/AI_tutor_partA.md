# W01 AI Tutor Learning Record — Part A

Topic: Tuples, Lists, Aliasing, Mutability, and Cloning
Date: 2026/10/05

## ① Check My Understanding

Questions completed: 5 / 5

Answers revised after AI hints: 1 / 5

### Question 1
**True or False:** A tuple can contain different data types, but its elements cannot be changed after the tuple is created.

My answer: True

Result: Correct.

### Question 2
**True or False:** `L1 + L2` modifies `L1` by adding all elements of `L2` to it.

My answer: True

AI hint: Think about the difference between `+` and `extend()`.

Revised answer: False

Explanation: `L1 + L2` creates a new list and does not change the original lists. `L1.extend(L2)` modifies `L1`.

### Question 3
**True or False:** If two variables are aliases of the same list, modifying the list through one variable can also affect what is seen through the other variable.

My answer: True

Result: Correct.

### Question 4
**True or False:** `sorted(L)` and `L.sort()` have the same effect on the original list.

My answer: False

Result: Correct.

Explanation: `sorted(L)` returns a new sorted list without modifying `L`, while `L.sort()` directly modifies the original list.

### Question 5
**True or False:** It is always safe to remove elements from a list while iterating over that same list.

My answer: False

Result: Correct.

Explanation: Removing elements changes the list length and positions during iteration, so some elements may be skipped.

---

## ② My Misconception

**Before: I thought…**

I thought using `+` on two lists would directly add the elements into the original list, similar to `append()` or `extend()`.

**Now: I understand…**

I understand that `+` creates a new list, while methods such as `append()` and `extend()` mutate the original list. I should pay attention to whether an operation creates a new object or causes a side effect.

---

## ③ Challenge the AI

**One AI-generated question I challenged:**

"Using `sorted(L)` is basically the same as using `L.sort()`."

**Why?**

- [x] Ambiguous
- [ ] Oversimplified
- [ ] Technically questionable
- [ ] Too easy
- [ ] Other: __________

**Brief explanation:**

They may produce the same ordering, but their behavior is different. `sorted(L)` returns a new sorted list and keeps `L` unchanged, while `L.sort()` mutates `L`.

---

## ④ One-Minute Reflection

**One thing I am still unsure about:**

I am still a little unsure about aliasing when there are nested lists. I understand that two variables can point to the same list, but nested mutable objects seem more complicated when cloning is involved.