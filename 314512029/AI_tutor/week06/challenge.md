# Part B - First Event At or After Time

AI-generated Week 6 transfer challenge based on MIT 6.0001 Lecture 11. It transfers bisection search from exact membership testing to locating a boundary in a sorted sequence. The MOOS event-log setting connects the programming concept to Lab 06, but this is a standalone Python problem rather than a MOOS application.

## Problem statement

A MOOS mission log stores event timestamps in nondecreasing order. Several events may have the same timestamp.

Given the sorted list `times` and a query time `target`, return the zero-based index of the **first** event whose timestamp is greater than or equal to `target`. Return `-1` if no such event exists.

The search must use the sorted order to run in logarithmic time. Do not copy list slices and do not modify the input list.

## Input and output

Create `solution.py` with this callable:

```python
first_event_at_or_after(times, target)
```

- `times`: a Python list of integers sorted in nondecreasing order.
- `target`: an integer query timestamp.
- Return an integer index, or `-1` when every timestamp is less than `target`.
- The test runner passes arguments directly. No console input or printing is required.

## Constraints

- `0 <= len(times) <= 100000`
- `0 <= times[i] <= 1000000000`
- `times[i] <= times[i + 1]` wherever both indices exist.
- `0 <= target <= 1000000000`
- Use only concepts covered so far: functions, integers, lists and indexing, variables, comparisons, conditionals, loops, and return statements.
- The required worst-case time is `O(log n)`, where `n = len(times)`.
- The required extra space is `O(1)`.
- Invalid inputs outside these constraints need not be handled.

## Examples

### Example 1

Input: `times = [3, 8, 12, 20]`, `target = 10`

Output: `2`

Index 2 is the first position whose value, 12, is at least 10.

### Example 2

Input: `times = [2, 5, 5, 5, 11]`, `target = 5`

Output: `1`

There are three events at time 5, and index 1 is the first one.

### Example 3

Input: `times = [4, 9, 15]`, `target = 16`

Output: `-1`

No event occurs at or after time 16.

## Before coding

1. Explain how the candidate interval changes after comparing `times[mid]` with `target`.
2. Explain how this transfers the lecture's bisection-search idea while solving a different problem.

## After coding

Run `python3 verify.py`. Explain why the remaining candidate interval always contains the first qualifying position, why duplicate timestamps are handled correctly, and why the interval is reduced enough to give logarithmic time.
