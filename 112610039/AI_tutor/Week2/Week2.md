# AI Tutor for AOOP 2026 - Week 2 Learning Record

## Part A: True or False

**Topic:** Recursion and Dictionaries[cite: 25, 28]  
**Date:** 2026-10-20

### ① Check My Understanding
* **Questions completed:** 5 / 5
* **Answers revised after AI hints:** 2 / 5 (Question 4 & Question 5)

### ② My Misconception
* **Before:** I thought modifying a dictionary during iteration would just skip elements like lists do[cite: 23], and that Memoization could be applied to any function regardless of side effects[cite: 80, 81].
* **Now:** I understand that mutating a dictionary's size during iteration raises a `RuntimeError` in Python. Furthermore, Memoization is only valid for pure functions without side effects[cite: 81], as skipping execution via cached returns will bypass those side effects[cite: 81].

### ③ Challenge the AI
* **One AI-generated question I challenged:** Question 3[cite: 72]
* **Why?**
  - [ ] Ambiguous
  - [ ] Oversimplified
  - [x] Technically questionable
  - [ ] Too easy
  - [ ] Other: __________________
* **Brief explanation:** The question tests whether a tuple containing a mutable list can be used as a dictionary key[cite: 4, 7, 72]. It highlights a subtle rule: while tuples are immutable[cite: 4], any structure containing unhashable elements like lists becomes unhashable itself[cite: 72].

### ④ One-Minute Reflection
* **One thing I am still unsure about:** How Python manages stack call frames during deep recursion and how to handle recursion depth limits when target values are extremely large[cite: 30, 35].

---

## Part B: LeetCode-style Lecture Code Transfer

**Name:** 112610039 
**Date:** 2026-10-20  
**Topic:** Recursion, Base Cases & Memoization with Dictionaries[cite: 25, 28, 30, 80]

### 1. Today’s Challenge
* **Core concept from today’s OCW lecture:** Breaking problems down recursively using base cases[cite: 30, 33] and storing intermediate results in a dictionary (Memoization) to optimize performance[cite: 80, 81].
* **AI-generated coding challenge title:** Clustered Target Sum (Memoized Recursion)

### 2. My Initial Approach — Before AI Help
* **My approach:** I attempted to write a recursive function with `mem = {}` declared inside the function body[cite: 80]. I used a loop over candidates and tried to store boolean flags in the local dictionary.

### 3. AI Tutor Help
* **Did you ask the AI Tutor for help?**
  - [ ] No — I solved it independently
  - [x] Yes — I received one or more hints
* **The most useful hint/question from AI was:** Explaining that `mem = {}` inside the function resets the dictionary on every recursive call frame because each call creates an independent scope[cite: 36, 80]. To persist memory, the dictionary must be passed as a parameter across recursive call frames[cite: 80].
* **It helped me realize that:** Mutable arguments like dictionaries are passed by reference[cite: 7, 19], allowing all recursive steps to update and share a single cache[cite: 80].

### 4. My Revision
* **Did you change your approach or code after interacting with AI?**
  - [ ] No
  - [x] Yes
* **What did you change, and why?** I added `memo=None` to the function parameters[cite: 80], initialized `memo = {}` on top-level call, added base cases (`target == 0` and `target < 0`)[cite: 30, 33], and updated `memo[target]` before returning[cite: 80].

### 5. Verification
* **My final program:**
  - [x] Passed the provided examples
  - [x] Passed additional edge cases
  - [ ] Still has unresolved problems
* **One edge case I tested:**
  - **Input:** `target = 7, candidates = [2, 4]`
  - **Expected output:** `False`
  - **Actual output:** `False`

### 6. One-Minute Reflection
* **What idea from the OCW lecture did you transfer to this new problem?** Combining recursive divide-and-conquer logic with dictionary lookups for memoization[cite: 30, 69, 80].
* **One thing I understand better now:** How passing mutable structures through recursive scope frames preserves state across function calls without global variables[cite: 7, 36, 80].
* **One thing I am still unsure about:** How to modify the algorithm to return the exact list of candidate numbers that sum up to `target` instead of just returning a boolean `True`/`False`.