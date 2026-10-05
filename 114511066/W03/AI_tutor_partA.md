# W03 AI Tutor Learning Record — Part A

Topic: Testing, Debugging, Exceptions, and Assertions
Date: 2026/09/21

## ① Check My Understanding

Questions completed: 5 / 5

Answers revised after AI hints: 1 / 5

### Question 1

**True or False:** An `IndexError` in a list can happen when the program tries to access an index outside the valid range.

My answer: True

Result: Correct.

### Question 2

**True or False:** When reversing a list by swapping elements, the loop should go through the entire list.

My answer: True

AI hint: Think about what happens after the first half of the elements have already been swapped with the second half.

Revised answer: False

Explanation: We only need to iterate through half of the list. If we continue through the entire list, the elements will be swapped again and the list can return to its original order.

### Question 3

**True or False:** A `ZeroDivisionError` can be handled separately from a `ValueError` by using multiple `except` blocks.

My answer: True

Result: Correct.

### Question 4

**True or False:** The code inside a `finally` block only executes when an exception occurs.

My answer: False

Result: Correct.

Explanation: The `finally` block executes whether an exception occurs or not.

### Question 5

**True or False:** An `assert` statement can be used to check whether an assumption required by a function is satisfied.

My answer: True

Result: Correct.

---

## ② My Misconception

**Before: I thought…**

I thought that when reversing a list, the loop should iterate through every element because every element needs to be changed.

**Now: I understand…**

I understand that each swap changes two positions at the same time. Therefore, only half of the list needs to be visited. If I continue swapping through the entire list, I will start undoing the previous swaps.

---

## ③ Challenge the AI

**One AI-generated question I challenged:**

"Using a general `except:` is always the best way to handle errors because it catches every possible exception."

**Why?**

- [ ] Ambiguous
- [x] Oversimplified
- [ ] Technically questionable
- [ ] Too easy
- [ ] Other: __________

**Brief explanation:**

A general `except:` catches many different errors but does not tell us what actually went wrong. The lecture examples show that using specific exceptions such as `ValueError` and `ZeroDivisionError` allows different problems to be handled differently.

---

## ④ One-Minute Reflection

**One thing I am still unsure about:**

I am still a little unsure about when I should use an `assert` and when I should use `try` and `except` to handle an invalid condition.