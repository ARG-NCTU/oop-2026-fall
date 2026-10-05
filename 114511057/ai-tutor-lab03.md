# AI Tutor Learning Record — Lab 03

**Name:** 陳芊蓉  
**Student ID:** 114511057  
**Topic:** PyTest and Unit Test

---

# Part A: True or False

## ① Check My Understanding

**Questions completed:** 5 / 5

**Answers revised after AI hints:** 1 / 5

### Question 1

**Q:** In pytest, a test function should usually start with `test_` so that pytest can automatically find it.

**Answer:** True.

Pytest uses naming rules to find test files and test functions automatically.

### Question 2

**Q:** If an `assert` statement is true, the test will fail.

**Answer:** False.

An `assert` describes the expected condition. If the condition is true, the test passes. If it is false, the test fails.

### Question 3

**Q:** `pytest.raises(ValueError)` can be used when we expect a function to produce a `ValueError`.

**Answer:** True.

It allows us to test whether invalid input produces the expected exception.

### Question 4

**Q:** Testing only one normal score, such as 75, is enough to verify that a letter grade function works correctly.

**Answer:** False.

Boundary values such as 90/89, 80/79, 70/69, and 60/59 should also be tested because errors often happen at the boundaries.

### Question 5

**Q:** If `average([])` is supposed to raise a `ValueError`, a test should check that the exception actually occurs.

**Answer:** True.

An empty list is an invalid case for this function, so the test should verify that the expected error is raised.

---

## ② My Misconception

**Before: I thought…**

I thought unit testing was mainly checking whether the program could run without errors.

**Now: I understand…**

Unit testing checks whether a small part of the program produces the expected result for specific inputs. It is also important to test boundary values and invalid inputs, not only normal cases.

---

## ③ Challenge the AI

**One AI-generated question I challenged:**

“Testing only one normal score, such as 75, is enough to verify that a letter grade function works correctly.”

**Why?**

☐ Ambiguous  
☒ Oversimplified  
☐ Technically questionable  
☐ Too easy  
☐ Other: __________

**Brief explanation:**

The question is simple because it is clear that one normal value is not enough. A better question could ask which boundary values are necessary to detect errors in the grade ranges.

---

## ④ One-Minute Reflection

**One thing I am still unsure about:**

I am still a little unsure about when I should use separate test functions and when I should use `pytest.mark.parametrize` for multiple test cases.

---

# Part B: LeetCode-style Lecture Code Transfer

## 1. Today’s Challenge

**Core concept from today’s OCW lecture:**

Using unit tests to check normal inputs, boundary values, and invalid inputs.

**AI-generated coding challenge title:**

**Ticket Price Checker**

### Problem Statement

Write a function that determines a ticket category based on a person's age.

The categories are:

- Age 0–5: `"Free"`
- Age 6–17: `"Child"`
- Age 18–64: `"Adult"`
- Age 65 or above: `"Senior"`

If the age is negative, the function should raise a `ValueError`.

Create tests to verify that the function works correctly for normal values, boundary values, and invalid input.

### Input

An integer representing a person's age.

### Output

A string representing the ticket category.

### Constraints

- Age must not be negative.
- Negative ages should raise `ValueError`.

### Examples

**Example 1**

Input: `10`

Output: `"Child"`

**Example 2**

Input: `18`

Output: `"Adult"`

**Example 3**

Input: `65`

Output: `"Senior"`

---

## 2. My Initial Approach — Before AI Help

**My approach:**

I planned to divide the ages into different ranges using conditions. Then I would write tests for each category and check whether the returned string is correct.

---

## 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

☐ No — I solved it independently  
☒ Yes — I received one or more hints

**The most useful hint/question from AI was:**

“What values are most likely to reveal an error between two age ranges?”

**It helped me realize that:**

I should test values on both sides of each boundary instead of testing only normal values.

For example, I should test `5` and `6`, `17` and `18`, and `64` and `65`.

---

## 4. My Revision

**Did you change your approach or code after interacting with AI?**

☐ No  
☒ Yes

**What did you change, and why?**

I added boundary test cases because I realized that conditions such as `<`, `<=`, `>` and `>=` can easily cause mistakes at the boundary.

I also added a test for a negative age using `pytest.raises(ValueError)`.

---

## 5. Verification

**My final program:**

☒ Passed the provided examples  
☒ Passed additional edge cases  
☐ Still has unresolved problems

**One edge case I tested:**

Input: `-1`

Expected output: `ValueError`

Actual output: `ValueError`

---

## 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**

I transferred the idea of testing normal values, boundary values, and invalid inputs instead of checking only one example.

**One thing I understand better now:**

I understand why boundary testing is important and how `pytest.raises` can test whether an invalid input produces the correct exception.

**One thing I am still unsure about:**

I am still unsure about how to organize a large number of test cases efficiently when a program becomes more complicated.
