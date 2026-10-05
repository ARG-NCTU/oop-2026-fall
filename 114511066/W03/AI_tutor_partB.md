# W03 AI Tutor Learning Record — Part B

Name: 114511066
Date: 2026/09/21
Topic: Testing, Debugging, Exceptions, and Assertions

## 1. Today’s Challenge

### Core concept from today’s OCW lecture:

Debugging, exception handling, and checking invalid inputs.

The lecture showed how bugs can come from incorrect indices, incorrect loop ranges, or modifying data incorrectly. It also introduced `try`, `except`, `else`, `finally`, `raise`, and `assert` for detecting and handling problems.

### AI-generated coding challenge title:

**Safe Average Calculator**

### Problem Statement

Write a function `safe_average(values)` that receives a list.

The function should calculate and return the average of the numbers in the list.

If the list is empty, return `0.0`.

If an element cannot be converted to a number, raise a `ValueError`.

### Input/Output Specification

Input:

    [80, 90, 100]

Output:

    90.0

### Constraints

- The input is a list.
- The list may be empty.
- Elements are expected to represent numbers.
- Invalid elements should cause a `ValueError`.

### Examples

Example 1:

    Input: [80, 90, 100]
    Output: 90.0

Example 2:

    Input: []
    Output: 0.0

Example 3:

    Input: [10, "abc", 20]
    Output: ValueError

---

## 2. My Initial Approach — Before AI Help

### My approach:

My first idea was to calculate the average directly using:

    sum(values) / len(values)

I thought this would be enough because the formula for an average is straightforward.

---

## 3. AI Tutor Help

### Did you ask the AI Tutor for help?

- [ ] No — I solved it independently
- [x] Yes — I received one or more hints

### The most useful hint/question from AI was:

What happens when `values` is an empty list and `len(values)` is zero?

### It helped me realize that:

The program would try to divide by zero and cause a `ZeroDivisionError`.

I also realized that invalid data could cause another type of error, so different exceptions may need different handling.

---

## 4. My Revision

### Did you change your approach or code after interacting with AI?

- [ ] No
- [x] Yes

### What did you change, and why?

I added exception handling for an empty list and raised a `ValueError` when the input contains invalid data.

### Final code

```python
def safe_average(values):
    try:
        nums = []
        for value in values:
            nums.append(float(value))
        return sum(nums) / len(nums)
    except ZeroDivisionError:
        return 0.0
    except (ValueError, TypeError):
        raise ValueError("invalid value")