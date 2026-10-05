# AI Tutor Learning Record: Part B

Name: Yu-Liang Tan / 譚羽良

Student ID: 112511017

Week: 3

Date: 2026-10-05

Topic: MIT OCW Lecture 7, Testing, debugging, exceptions, assertions, and boundary cases

Status: New AI-assisted written responses prepared at the student's request. These are new records, not recovered historical sessions. First-person reflections are assisted wording. No one-at-a-time student hint cycle or independent student implementation is claimed.

Format: [Course AI tutor instructions](https://github.com/ARG-NCTU/oop-python-nycu/blob/d4ccf63b9252d0017e84d3bed10628f0f5ea7bc9/ai-tutor-2026.md)

Sources: [MIT lecture slides and code](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/pages/lecture-slides-code/), [course reference code](https://github.com/ARG-NCTU/oop-python-nycu/blob/d4ccf63b9252d0017e84d3bed10628f0f5ea7bc9/src/mit_ocw_exercises/lec7_debug_except.py).

## 1. Today's Challenge

Core concept from today's OCW lecture: Classifying inputs, catching a specific conversion exception, validating a range, and checking normal and edge cases.

AI-generated coding challenge title: Checked laboratory measurements

### Problem statement

A laboratory receives measurement lines in the form `name,value`. Sum valid readings for each name, and report each invalid line with its zero-based index and reason. Continue processing after a bad line.

Classify errors in this order:

1. `format`: The line does not contain exactly two comma-separated fields, or the stripped name is empty.
2. `number`: The stripped value cannot be converted with Python's `int` function.
3. `range`: The converted value is outside 0 through 100.

Strip surrounding whitespace from both fields. Accepted integer syntax follows `int`, so a leading plus sign and leading zeroes are valid. Do not modify the input list. An invalid line must not change any total. A valid zero reading still creates an entry for its name.

### Input/output specification

Callable: `parse_measurements(lines)`.

Input: A list of ASCII strings.

Output: `(totals, errors)`, where `totals` is a name-to-sum dictionary and `errors` is a list of `(index, reason)` tuples in input order.

### Constraints

- `0 <= len(lines) <= 1000`
- Each line has at most 100 characters.
- Values outside 0 through 100 are rejected.
- Use loops, strings, dictionaries, tuples, and exception handling.

### Examples

| Input | Expected output |
| --- | --- |
| `["A,20", "bad", "B,x", "A,35"]` | `({"A": 55}, [(1, "format"), (2, "number")])` |
| `["A,0", "B,100", "B,101", "A,-1"]` | `({"A": 0, "B": 100}, [(2, "range"), (3, "range")])` |
| `[]` | `({}, [])` |

## 2. My Initial Approach Before AI Help

My approach: I would examine each line in input order. I would check the field count and name first, try converting the value with a `ValueError` handler, then check its range. Only after all checks pass would I update the name's total. Each failed check would append one error and continue to the next line. This is an AI-assisted plan rather than a recovered before-help answer.

Which concept from the lecture code am I applying? Classifying inputs, catching a specific conversion exception, validating a range, and checking normal and edge cases.

## 3. AI Tutor Help

Did you ask the AI Tutor for help?

- [ ] No, I solved it independently
- [x] Yes, I received AI assistance

The most useful hint/question from AI was: "At which point is it safe to change the totals?" This focuses the design on completing validation before mutation.

It helped me realize that: Validation order makes the error category predictable, and a specific exception handler catches conversion failure without hiding every possible programming error.

Assistance used: AI supplied the written approach, reflection, implementation, and tests. This assistance includes a solution, rather than only hints.

## 4. My Revision

Did you change your approach or code after interacting with AI?

- [x] No separate student revision round was recorded
- [ ] Yes

What did you change, and why? No separate student implementation or revision was recorded. The assistant's first verified implementation passed all nine tests, so no failing-code revision is claimed.

## 5. Verification

My final program is an AI-assisted implementation. The assistant ran the verification on October 5, 2026.

- [x] Passed the provided examples
- [x] Passed additional edge cases
- [ ] Still has unresolved problems

[Implementation](solution/measurements.py) and [tests](solution/test_measurements.py).

Run from `solution/`:

```bash
python3 -m pytest -q -p no:cacheprovider test_measurements.py
```

Result: 9 tests passed. The checks cover all three examples, empty names, extra separators, invalid numeric text, whitespace and signed integers, invalid readings preserving totals, input preservation, and 1,000 lines.

One edge case tested:

Input: `parse_measurements(["A,40", "A,101", "A,60"])`

Expected output: `({"A": 100}, [(1, "range")])`

Actual output: `({"A": 100}, [(1, "range")])`

## 6. One-Minute Reflection

What idea from the OCW lecture did you transfer to this new problem? Validation order makes the error category predictable, and a specific exception handler catches conversion failure without hiding every possible programming error.

Why my solution works: Each line reaches exactly one outcome. A format failure stops its processing first; otherwise conversion either raises `ValueError` or returns an integer. The range check then either rejects that integer or allows a single total update. Invalid lines never reach the update. Iterating in order also keeps the error list in the required order.

Time complexity: For N lines of maximum length L, processing takes O(NL) under the bounded input sizes and ordinary dictionary lookup assumptions. Output and temporary string storage use O(NL) space in the worst case. With the fixed 100-character limit, this is O(N) time and space in the number of lines.

One thing I understand better now: Error handling should define a recovery rule for a known failure, and state should be updated only after validation succeeds.

One thing I am still unsure about: When should an invalid line be recorded and skipped, and when should the caller receive an exception instead?
