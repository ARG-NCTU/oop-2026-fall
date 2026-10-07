# AOOP 2026 — Lab 03 AI Tutor Learning Record

## Topic
PyTest and Unit Testing

## Part A: True or False

### 1. Check My Understanding

**Question 1:** True or False: A unit test should test one small part of a program instead of the whole program at once.

**Answer:** True.

**Reason:** It makes it easier to find where the problem is when a test fails.

**Question 2:** True or False: If a `pytest` assertion fails, that means the test was never run.

**Answer:** False.

**Reason:** The test did run, but the actual result did not match what the test expected.

**Question 3:** True or False: Testing only normal inputs is enough if the function works for those inputs.

**First answer:** True.

**AI hint:** What about exact boundary values or invalid inputs?

**Revised answer:** False.

**Reason:** Some bugs only show up at boundaries or with invalid inputs, so those should be tested too.

**Question 4:** True or False: `pytest.raises(ValueError)` can be used to check that a function correctly rejects invalid input.

**Answer:** True.

**Reason:** It checks whether the function raises the exception we expect.

**Question 5:** True or False: If `average([])` is supposed to reject an empty list, the test should check for an exception instead of expecting a normal number.

**Answer:** True.

**Reason:** An empty list is an error case, so the test should check the error behavior.

Questions completed: **5 / 5**

Answers revised after AI hints: **1 / 5**

### 2. My Misconception

**Before: I thought…**

If the normal examples passed, the function was probably correct.

**Now: I understand…**

I should also test boundary values and invalid inputs because those can reveal bugs that normal cases do not.

### 3. Challenge the AI

**One AI-generated question I challenged:**

“True or False: `pytest.raises(ValueError)` can be used to check that a function correctly rejects invalid input.”

**Why?**

- [ ] Ambiguous
- [ ] Oversimplified
- [ ] Technically questionable
- [x] Too easy
- [ ] Other

**Brief explanation:**

It was pretty direct from what we did in the lab. A harder question could ask me to decide which inputs should raise an exception.

### 4. One-Minute Reflection

**One thing I am still unsure about:**

I am still not completely sure how many test cases are enough for a function.

## Part B: LeetCode-style Lecture Code Transfer

### 1. Today’s Challenge

**Core concept from today’s OCW lecture:**

Writing unit tests for normal cases, boundary cases, and invalid inputs.

**AI-generated coding challenge title:**

Score Summary Validator

### Problem statement

Write and test two Python functions:

- `valid_score(score)` returns whether a score is between 0 and 100.
- `score_average(scores)` returns the average of a non-empty list of valid scores.

The program should reject invalid scores, and `score_average` should also reject an empty list.

### Input/output specification

`valid_score(score)`:
- Input: one score
- Output: `True` if the score is from 0 to 100
- Output: `False` otherwise

`score_average(scores)`:
- Input: a list of valid scores
- Output: the average
- Error: raise `ValueError` if the list is empty or contains an invalid score

### Constraints

- Valid scores are from 0 to 100.
- Use only concepts covered in class.
- Tests should include normal, boundary, and invalid cases.

### Examples

**Example 1**
```text
Input: valid_score(100)
Output: True
```

**Example 2**
```text
Input: score_average([80, 90, 100])
Output: 90
```

**Example 3**
```text
Input: score_average([])
Output: ValueError
```

### 2. My Initial Approach — Before AI Help

I planned to write tests for a normal value first, then check the exact boundaries and some invalid values. For the average function, I would also test an empty list.

### 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

- [ ] No — I solved it independently
- [x] Yes — I received one or more hints

**The most useful hint/question from AI was:**

“Which values are most likely to reveal an off-by-one error?”

**It helped me realize that:**

I should test 0 and 100, and also values just outside the range like -1 and 101.

### 4. My Revision

**Did you change your approach or code after interacting with AI?**

- [ ] No
- [x] Yes

**What did you change, and why?**

I added more boundary and invalid-input tests instead of only testing normal values.

### 5. Verification

My final program:

- [x] Passed the provided examples
- [x] Passed additional edge cases
- [ ] Still has unresolved problems

**One edge case I tested:**

Input: `valid_score(101)`

Expected output: `False`

Actual output: `False`

### 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**

I used the same idea of checking normal cases, boundaries, and error cases.

**One thing I understand better now:**

I understand why testing exact boundary values is useful.

**One thing I am still unsure about:**

I am still unsure how to know when I have tested enough cases.
