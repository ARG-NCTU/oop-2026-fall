# AI Tutor for AOOP 2026 - Week 3 Learning Record

## Part A: True or False

**Topic:** Testing, Debugging, Exceptions & Assertions[cite: 83]  
**Date:** 2026-10-23

### ① Check My Understanding
* **Questions completed:** 5 / 5
* **Answers revised after AI hints:** 0 / 5 (Answered all 5 correctly on the first attempt!)

### ② My Misconception
* **Before:** I was already familiar with standard testing, but I used to think path-complete glass-box testing guaranteed a bug-free program[cite: 92].
* **Now:** I understand that path-complete glass-box testing might still miss boundary cases or missing paths in specification[cite: 92, 93]. Furthermore, `assert` should be used for internal program invariants[cite: 113, 116], while `try...except` and raising exceptions should handle bad external inputs[cite: 103, 106, 116].

### ③ Challenge the AI
* **One AI-generated question I challenged:** Question 1[cite: 92, 93]
* **Why?**
  - [ ] Ambiguous
  - [x] Oversimplified
  - [ ] Technically questionable
  - [ ] Too easy
  - [ ] Other: __________________
* **Brief explanation:** The concept of "path-complete" can easily trick developers into thinking 100% path coverage equals 100% correctness[cite: 92]. In reality, missing code paths or missing boundary conditions won't be caught by coverage alone[cite: 92, 93].

### ④ One-Minute Reflection
* **One thing I am still unsure about:** How to write efficient regression tests for large-scale production code without drastically slowing down build pipelines[cite: 88].

---

## Part B: LeetCode-style Lecture Code Transfer

**Name:** 112610039  
**Date:** 2026-10-23  
**Topic:** Exception Handling & Defensive Programming[cite: 83, 85, 100]

### 1. Today’s Challenge
* **Core concept from today’s OCW lecture:** Using `raise` for bad input validation[cite: 106], `try...except` to catch runtime errors like `ZeroDivisionError`[cite: 103, 110], and `assert` statements to check data invariants[cite: 113, 114].
* **AI-generated coding challenge title:** Robust Batch Grade Processor

### 2. My Initial Approach — Before AI Help
* **My approach:** Check input type using `isinstance(class_data, list)` and raise a `TypeError` if invalid[cite: 101, 106]. Iterate through students, compute the sum of grades, and wrap the average division in a `try...except ZeroDivisionError` block[cite: 103, 110]. Add an `assert` statement to guarantee $0.0 \le \text{avg} \le 100.0$ before filtering[cite: 113, 114, 116].

### 3. AI Tutor Help
* **Did you ask the AI Tutor for help?**
  - [x] No — I solved it independently
  - [ ] Yes — I received one or more hints
* **The most useful hint/question from AI was:** N/A (Solved directly)
* **It helped me realize that:** N/A

### 4. My Revision
* **Did you change your approach or code after interacting with AI?**
  - [x] No
  - [ ] Yes
* **What did you change, and why?** No changes required; initial code passed all defensive checks and requirements.

### 5. Verification
* **My final program:**
  - [x] Passed the provided examples
  - [x] Passed additional edge cases
  - [ ] Still has unresolved problems
* **One edge case I tested:**
  - **Input:** `class_data = [["Bob", []]], min_passing_avg = 60`
  - **Expected output:** Print warning `"student Bob has no grades"` and return `[]`
  - **Actual output:** Printed warning `"student Bob has no grades"` and returned `[]`

### 6. One-Minute Reflection
* **What idea from the OCW lecture did you transfer to this new problem?** Combining defensive preconditions (`raise Exception`)[cite: 106], graceful runtime recovery (`try...except`)[cite: 103], and internal state checking (`assert`)[cite: 113] to make code resilient to edge cases[cite: 85, 116].
* **One thing I understand better now:** The distinct responsibilities of Python exceptions versus assertions[cite: 100, 113, 116].
* **One thing I am still unsure about:** How logging frameworks are typically integrated with exception handling in production instead of plain `print` warnings[cite: 111].