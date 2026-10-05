# AI Tutor Learning Record: Part B

Name: Yu-Liang Tan / 譚羽良

Student ID: 112511017

Week: 2

Date: 2026-10-05

Topic: MIT OCW Lecture 6, Recursion, dictionaries, and memoization

Status: New AI-assisted written responses prepared at the student's request. These are new records, not recovered historical sessions. First-person reflections are assisted wording. No one-at-a-time student hint cycle or independent student implementation is claimed.

Format: [Course AI tutor instructions](https://github.com/ARG-NCTU/oop-python-nycu/blob/d4ccf63b9252d0017e84d3bed10628f0f5ea7bc9/ai-tutor-2026.md)

Sources: [MIT lecture slides and code](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/pages/lecture-slides-code/), [course reference code](https://github.com/ARG-NCTU/oop-python-nycu/blob/d4ccf63b9252d0017e84d3bed10628f0f5ea7bc9/src/mit_ocw_exercises/lec6_recursion_dictionaries.py).

## 1. Today's Challenge

Core concept from today's OCW lecture: A decreasing recursive subproblem and dictionary memoization, as demonstrated by the lecture's recursive examples and `fib_efficient`.

AI-generated coding challenge title: Delivery routes around blocked cells

### Problem statement

A delivery robot starts at `(0, 0)` in a rectangular grid and must reach `(rows - 1, cols - 1)`. It may move only one cell right or one cell down. Some cells are blocked. Count the distinct valid routes.

A blocked starting cell or destination permits no route. In an unblocked one-cell grid, staying at that cell counts as one route. Use recursion with a dictionary cache to avoid recomputing the same state.

### Input/output specification

Callable: `count_delivery_routes(rows, cols, blocked)`.

Input: Grid dimensions and a list of blocked `(row, col)` tuples.

Output: A nonnegative integer route count. Do not modify `blocked`.

### Constraints

- `1 <= rows, cols <= 20`
- Blocked coordinates are distinct and within the grid.
- `0 <= len(blocked) <= rows * cols`
- Use functions, recursion, tuples, lists, and dictionaries.

### Examples

| Input | Expected output |
| --- | --- |
| `count_delivery_routes(3, 3, [(1, 1)])` | `2` |
| `count_delivery_routes(2, 3, [])` | `3` |
| `count_delivery_routes(1, 1, [(0, 0)])` | `0` |

## 2. My Initial Approach Before AI Help

My approach: I would represent a recursive state by its row and column. A blocked or out-of-grid cell contributes zero routes, and an unblocked destination contributes one. Every other cell contributes the sum of the routes through its right and down neighbors. I would store that count in a dictionary keyed by the coordinate tuple. This plan was prepared with AI assistance rather than recorded before help.

Which concept from the lecture code am I applying? A decreasing recursive subproblem and dictionary memoization, as demonstrated by the lecture's recursive examples and `fib_efficient`.

## 3. AI Tutor Help

Did you ask the AI Tutor for help?

- [ ] No, I solved it independently
- [x] Yes, I received AI assistance

The most useful hint/question from AI was: "Can two different earlier routes reach the same remaining subproblem?" This question identifies why a coordinate-based cache is useful.

It helped me realize that: The same cell can be reached by different prefixes, but the number of routes from that cell onward is the same. Caching that suffix count avoids repeating its recursion.

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

[Implementation](solution/delivery_routes.py) and [tests](solution/test_delivery_routes.py).

Run from `solution/`:

```bash
python3 -m pytest -q -p no:cacheprovider test_delivery_routes.py
```

Result: 9 tests passed. The checks cover all three examples, the unblocked one-cell grid, blocked endpoints, an impassable barrier, single-row and single-column grids, input preservation, and a 20-by-20 grid checked against a combinatorial count.

One edge case tested:

Input: `count_delivery_routes(1, 1, [])`

Expected output: `1`

Actual output: `1`

## 6. One-Minute Reflection

What idea from the OCW lecture did you transfer to this new problem? The same cell can be reached by different prefixes, but the number of routes from that cell onward is the same. Caching that suffix count avoids repeating its recursion.

Why my solution works: At an invalid or blocked cell, there are no valid routes. At the destination, there is exactly one completed route. Every remaining route starts with either a right move or a down move, so the two counts can be added without overlap. Every valid move reduces the remaining distance, establishing termination. Memoization preserves these counts while computing each nonterminal state once.

Time complexity: For R rows, C columns, and B blocked cells, expected time is O(RC + B) with constant-time dictionary operations and bounded integer arithmetic. Extra space is O(RC + B), including the blocked lookup and memo, with recursion depth O(R + C).

One thing I understand better now: A cache key describes a subproblem, not the entire path that reached it.

One thing I am still unsure about: How would the termination argument change if the robot could also move left or up?
