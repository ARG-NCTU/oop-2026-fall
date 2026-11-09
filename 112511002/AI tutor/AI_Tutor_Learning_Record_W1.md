# AI Tutor Learning Record — Lecture 5

**Name:** 劉育麟  
**Date:** 2026/11/09  
**Topic:** Tuples, Lists, Aliasing, Mutability, Cloning

---

# Part A: True or False

## ① Check My Understanding

**Questions completed:** 5 / 5

**Answers revised after AI hints:** 2 / 5

## ② My Misconception

### Before: I thought…

I thought `b = a[:]` would copy not only the outer list, but also the inner lists. Therefore, I expected `a` and `b` to be completely independent.

### Now: I understand…

I understand that `a[:]` only creates a shallow copy. The outer list is new, but the elements inside still refer to the same original objects. Therefore, if `a[0]` and `b[0]` refer to the same inner list, executing `b[0].append(5)` will also affect what is seen through `a[0]`.

## ③ Challenge the AI

**One AI-generated question I challenged:**

The question that iterated through `L` while using `L.remove(x)` to delete even numbers.

**Why?**

- [x] Ambiguous
- [ ] Oversimplified
- [ ] Technically questionable
- [ ] Too easy
- [ ] Other

### Brief explanation

For the given list `L = [1, 2, 3, 4, 5, 6]`, the final result is indeed `[1, 3, 5]`. However, the explanation in the statement is incorrect because the loop does not examine every original element. After elements are removed, the remaining elements shift positions while the loop continues advancing, so `3` and `5` are skipped.

Therefore, if the question only asks about the final result, the statement is true. If the explanation is also considered part of the statement, then it is false. This makes the question ambiguous.

## ④ One-Minute Reflection

### One thing I am still unsure about

I am still becoming familiar with how immutability works when a Tuple contains a mutable object such as a List.

For example, with:

```python
t = ([1, 2], 3)
```

I now understand that `t[0].append(4)` is allowed because it modifies the List object that `t[0]` refers to, while `t[0] = [1, 2, 4]` is not allowed because it attempts to replace an element of the Tuple itself.

I would like to become more confident about distinguishing mutation of a referenced object from reassignment of an element inside an immutable container.

---

# Part B: LeetCode-style Lecture Code Transfer

## 1. Today’s Challenge

### Core concept from today’s OCW lecture

List iteration, mutation, and cloning. In particular, I learned that modifying the same list while iterating over it may cause elements to be skipped. A safer approach is to create a copy for iteration and modify the original list separately.

### AI-generated coding challenge title

**Remove Blocked Items**

---

## 2. My Initial Approach — Before AI Help

### My approach

My initial idea was to convert `blocked` into a set for faster lookup, scan through `items`, store the allowed elements in a temporary list, and finally use slice assignment to write the result back into the original `items`.

This approach would preserve the order and number of occurrences of all allowed elements while modifying the original list.

---

## 3. AI Tutor Help

### Did you ask the AI Tutor for help?

- [ ] No — I solved it independently
- [x] Yes — I received one or more hints

### The most useful hint/question from AI was

The AI pointed out that `set()` and slice assignment were not concepts demonstrated in the current Lecture 5 material. It suggested using the lecture pattern of cloning a list with `[:]`, iterating through the copy, and modifying the original list.

### It helped me realize that

I could solve the problem using only concepts from Lecture 5. By iterating over a cloned list, I can safely call `remove()` on the original list without changing the sequence being traversed.

---

## 4. My Revision

### Did you change your approach or code after interacting with AI?

- [ ] No
- [x] Yes

### What did you change, and why?

Instead of using a set and a temporary result list, I created a shallow copy of `items` using `items[:]`.

I then iterated through the copy. If an element appeared in `blocked`, I called `items.remove(item)` on the original list.

This separates iteration from mutation, so deleting elements from `items` does not cause the loop to skip elements in the copied list.

---

## 5. Verification

### My final program

```python
def remove_blocked(items, blocked):
    items_copy = items[:]
    for item in items_copy:
        if item in blocked:
            items.remove(item)
```

- [x] Passed the provided examples
- [x] Passed additional edge cases
- [ ] Still has unresolved problems

### One edge case I tested

**Input:**

```python
items = [1, 1, 1]
blocked = [1]
```

**Expected output:** `[]`

**Actual output:** `[]`

The copied list contains all three occurrences of `1`, so the loop calls `remove()` three times and removes every occurrence from the original list.

---

## 6. One-Minute Reflection

### What idea from the OCW lecture did you transfer to this new problem?

I transferred the idea of separating **iteration** from **mutation** by using **cloning**. Instead of iterating over a list while modifying it, I iterate over a copy and modify the original list.

### One thing I understand better now

I understand why modifying a list during iteration can cause elements to be skipped. I also understand how `L[:]` can be used to create a separate outer list for safe iteration while intentionally modifying the original list.

I can also explain why the solution works: if a blocked value occurs `k` times, the copied list contains those same `k` occurrences, so `remove()` is called exactly `k` times on the original list.

For complexity, if `n = len(items)` and `m = len(blocked)`, the worst-case time complexity is **O(nm + n²)**.

### One thing I am still unsure about

I would like to become more confident about choosing between cloning a list and constructing a new result list, especially when considering both mutation requirements and time complexity.
