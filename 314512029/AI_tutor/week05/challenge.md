# Part B — First Unsafe Monitoring Window

AI-generated Week 5 transfer challenge based on the supplied program-efficiency material, especially accumulation, early return, and loop analysis. This is a simulated monitoring problem inspired by the MOOS lecture context, not a MOOS control component.

## Problem statement

A simulated vessel records one nonnegative integer risk reading per second. An alert occurs when the sum of exactly `k` consecutive readings is **strictly greater than** `limit`.

Return the zero-based start index of the earliest complete window that causes an alert. Return `-1` if none does. A partial window at the end does not count. Do not change the input list.

## Input / output

Create `solution.py` with a callable named `first_unsafe_window(readings, k, limit)`.

- `readings`: a Python list of integers, in chronological order.
- `k`: the number of consecutive readings in one complete window.
- `limit`: the permitted sum for one window.
- Return one integer: the earliest matching start index, or `-1`.
- The test runner passes arguments directly; no console input or printing is required.

## Constraints

- `0 <= len(readings) <= 1000`
- `0 <= readings[i] <= 100`
- `1 <= k <= 1000`; `k` may exceed the list length.
- `0 <= limit <= 100000`
- Use concepts already present in the provided lecture examples: functions, integers, lists/indexing, variables, comparisons, conditionals, loops, and return statements. No third-party libraries are needed.
- There is no requirement to discover a more advanced algorithm. Explain the complexity of the algorithm you actually implement, using `n = len(readings)` and `k` separately.
- Invalid inputs outside these constraints need not be handled.

## Examples

### Example 1

Input: `readings = [2, 4, 3, 8, 1], k = 2, limit = 8`

Output: `2`

The complete window totals, in order, are 6, 7, 11, and 9. The earliest total strictly above 8 starts at index 2.

### Example 2

Input: `readings = [3, 3, 3], k = 2, limit = 6`

Output: `-1`

Both complete windows total exactly 6. Equality does not cause an alert.

### Example 3

Input: `readings = [9, 1], k = 3, limit = 5`

Output: `-1`

There is no complete window of three readings.

## Before coding — answer these first

1. Explain your proposed algorithm in your own words, including when it stops and what happens when no complete window exists.
2. Which concept or pattern from the lecture are you applying, and how is this task different from reproducing a lecture example?

Record the answers in `../w5.md`, then ask the tutor to review them. If the reasoning is incorrect, the tutor should give a hint or counterexample and let you revise before explaining. No solution or pseudocode is supplied here.

## After coding

Run `python3 verify.py`. Discuss a failure with the tutor before revising your own code. Passing finite cases is evidence, not a proof. Finally explain why your method always returns the earliest valid index (or correctly returns `-1`), its time complexity, and the lecture idea you transferred.
