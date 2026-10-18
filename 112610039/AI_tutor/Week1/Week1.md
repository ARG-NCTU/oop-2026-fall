# AI Tutor for AOOP 2026 - Week 1 Learning Record

## Part A: True or False

**Topic:** Tuples, Lists, Aliasing, Mutability, Cloning[cite: 1, 3]  
**Date:** 2026-10-18

### ① Check My Understanding
* **Questions completed:** 5 / 5[cite: 4]
* **Answers revised after AI hints:** 2 / 5 (Question 2 & Question 4)

### ② My Misconception
* **Before:** I thought tuple elements could never be modified under any condition[cite: 4], and that `list.sort()` returns the newly sorted list[cite: 21].
* **Now:** I understand that if a tuple contains a mutable object (like a list), the internal elements of that list can still be modified in-place[cite: 7, 22]. Additionally, in-place list operations like `.sort()` return `None`, not the mutated list[cite: 21].

### ③ Challenge the AI
* **One AI-generated question I challenged:** Question 4[cite: 21]
* **Why?**
  - [ ] Ambiguous
  - [x] Oversimplified
  - [ ] Technically questionable
  - [ ] Too easy
  - [ ] Other: __________________
* **Brief explanation:** The question tested two concepts at once (whether the list is mutated in-place and what the return value of `.sort()` is)[cite: 21], making it easy to overlook that `.sort()` evaluates to `None`[cite: 21].

### ④ One-Minute Reflection
* **One thing I am still unsure about:** How Python manages memory references and garbage collection when deeply nested mutable objects inside immutable structures are modified[cite: 22].

---

## Part B: LeetCode-style Lecture Code Transfer

**Name:** [ 請填寫你的姓名 / 學號 ]  
**Date:** 2026-10-18  
**Topic:** List Mutability, Aliasing & In-Place Mutation[cite: 3, 9, 19, 21]

### 1. Today’s Challenge
* **Core concept from today’s OCW lecture:** In-place list mutation, avoiding iteration side effects, and distinguishing aliasing from cloning[cite: 9, 19, 20, 23].
* **AI-generated coding challenge title:** Duplicate Even Numbers In-Place

### 2. My Initial Approach — Before AI Help
* **My approach:** I assigned `copied_nums = nums` and used a `for num in copied_nums:` loop to iterate[cite: 10, 19]. When encountering an even number, I shifted all subsequent elements to the right by one position to duplicate the even number in-place while keeping the array length constant[cite: 9, 21].

### 3. AI Tutor Help
* **Did you ask the AI Tutor for help?**
  - [ ] No — I solved it independently
  - [x] Yes — I received one or more hints
* **The most useful hint/question from AI was:** Pointing out that `copied_nums = nums` is aliasing (pointing to the same object) rather than cloning[cite: 19, 20], which caused the `for` loop to read the newly inserted duplicate element again[cite: 23].
* **It helped me realize that:** Modifying a list in-place while iterating over it via an alias causes unwanted side effects because Python's iterator advances on the mutated list[cite: 17, 19, 23].

### 4. My Revision
* **Did you change your approach or code after interacting with AI?**
  - [ ] No
  - [x] Yes
* **What did you change, and why?** I updated my code to `copied_nums = nums[:]` to clone the list[cite: 20]. This kept the iterator on an unmodified snapshot while I updated the original `nums` list in-place[cite: 9, 17, 20].

### 5. Verification
* **My final program:**
  - [x] Passed the provided examples
  - [x] Passed additional edge cases
  - [ ] Still has unresolved problems
* **One edge case I tested:**
  - **Input:** `nums = [2, 1, 4, 3]`
  - **Expected output:** `[2, 2, 1, 4]`
  - **Actual output:** `[2, 2, 1, 4]`

### 6. One-Minute Reflection
* **What idea from the OCW lecture did you transfer to this new problem?** The concept that lists are mutable objects updated in memory[cite: 7, 9, 17], and that aliasing vs. cloning dictates whether iteration state remains isolated from in-place mutations[cite: 19, 20, 23].
* **One thing I understand better now:** Why iterating over a list while mutating it causes index desynchronization and unexpected loops[cite: 23].
* **One thing I am still unsure about:** The performance/time-complexity difference between in-place element shifting $O(N^2)$ versus creating a new list $O(N)$ at the expense of memory space.