# AI tutor learning record: Python classes and inheritance, Part B

Name: Yu-Liang Tan / 譚羽良

Student ID: 112511017

Date: 2026-10-05

Topic: MIT OCW 6.0001 classes, inherited initialization, overridden methods, and shared counters

Status: AI-assisted written response prepared at the student's request. The approach, reflection, implementation, and tests were supplied or verified by the assistant. No independent student work or historical hint cycle is claimed.

Format: [Course AI tutor instructions](https://github.com/ARG-NCTU/oop-python-nycu/blob/d4ccf63b9252d0017e84d3bed10628f0f5ea7bc9/ai-tutor-2026.md)

## 1. Today's Challenge

Core concept from today's OCW lecture: The `Animal` hierarchy reuses common initialization and replaces selected behavior. `Rabbit.tag` assigns an identifier at object creation. Methods such as `__str__` provide an object representation.

AI-generated coding challenge title: Shipping quotes with shared tracking numbers

### Problem statement

A shipping desk receives parcel descriptions. Each parcel has a positive integer weight and is either standard or express.

Create a common `Parcel` class that initializes the weight and assigns a tracking number from a class counter, starting at 1. Both parcel types share the same sequence. Use subclasses `StandardParcel` and `ExpressParcel` that implement `quote()`:

- A standard quote is `5 + 2 * weight`.
- An express quote is `10 + 3 * weight`.

Each subclass must reuse the base initializer. Store a tracking number in each instance when that instance is created, so later creations do not change earlier tracking numbers.

Implement `__str__` so it produces the parcel's three-digit tracking number, followed by a colon and its quote. A loop processing a mixed list of parcels must call `quote()` through the common interface without checking the parcel type in that loop.

Return a list of those parcel strings in input order and the total quote. Create a new object for every description, including identical descriptions.

### Input and output specification

The callable interface is `shipping_quotes(descriptions)`.

Input: A list of `(kind, weight)` tuples, where `kind` is `"S"` or `"E"`.

Output: A tuple containing the list of parcel strings and the total integer quote.

For the examples, each scenario starts with the tracking counter at 1. Within one execution, consecutive calls continue the same sequence. Tests must reset the counter before independent scenarios, not before every parcel.

### Constraints

- `0 <= len(descriptions) <= 100`
- `1 <= weight <= 1000`
- All descriptions contain valid kinds and weights.
- Use course concepts such as classes, methods, inheritance, lists, tuples, loops, and integer arithmetic.

### Examples

| Input | Expected result |
| --- | --- |
| `[("S", 2), ("E", 2), ("S", 1)]` | `(["001:9", "002:16", "003:7"], 32)` |
| `[]` | `([], 0)` |
| `[("E", 1), ("E", 1)]` | `(["001:13", "002:13"], 26)` |

## 2. My Initial Approach Before AI Help

My approach: The proposed approach is to put weight and tracking initialization in `Parcel`, inherit that initializer in both subclasses, and override `quote` with the appropriate formula. I create one object per description, then process the mixed list through `quote` and str. The shared counter advances on creation and is not reset inside `shipping_quotes`. This plan was prepared with AI assistance, not recorded before AI help.

Which concept from the lecture code am I applying? Inherited initialization, overridden instance methods, `__str__`, and a shared class counter with per-instance stored identifiers.

## 3. AI Tutor Help

Did you ask the AI Tutor for help?

- [ ] No, I solved it independently
- [x] Yes, I received AI assistance

The most useful hint/question from AI was: "Which value is shared by the class, and which value belongs to one parcel?" It separates the next tracking number from the identifier already assigned to an object.

It helped me realize that: I can reuse the base initializer, override one method for each price rule, and use a class counter to assign identifiers. The assigned identifier stays on the instance even after the counter increases.

Assistance used: AI supplied the written approach, response text, implementation, and verification. This is more than hints, and it is not independent student work.

## 4. My Revision

Did you change your approach or code after interacting with AI?

- [x] No separate student revision round was recorded
- [ ] Yes

What did you change, and why? No separate student code revision occurred. AI supplied the implementation and eight tests. The verified version passed the examples, state checks, and bounds checks.

## 5. Verification

My final program is an AI-assisted implementation. The checks below were run by the assistant on October 5, 2026.

- [x] Passed the provided examples
- [x] Passed additional edge cases
- [ ] Still has unresolved problems

[Implementation](solution/shipping_quotes.py) and [tests](solution/test_shipping_quotes.py).

Run from `solution/`:

```bash
python3 -m pytest -q -p no:cacheprovider test_shipping_quotes.py
```

Result: 8 tests passed. They cover the three examples, duplicate standard parcels, counter continuity across calls, stable stored identifiers, maximum weight, and 100 parcels. Each independent test resets the counter; consecutive calls inside one test share it.

One edge case tested: Identical descriptions create distinct tracking numbers.

Input: `[("S", 1), ("S", 1)]`, with the initial counter set to 1.

Expected output: `(["001:7", "002:7"], 14)`

Actual output: `(["001:7", "002:7"], 14)`

## 6. One-Minute Reflection

What idea from the OCW lecture did you transfer to this new problem? I can reuse the base initializer, override one method for each price rule, and use a class counter to assign identifiers. The assigned identifier stays on the instance even after the counter increases.

Why my solution works: Every description constructs a new parcel and receives the next shared tracking number. Both subclasses inherit the same initializer, so their identifiers use one sequence. `quote` selects the subclass formula, and `__str__` reads that object's stored identifier and `quote`. The final loop keeps input order and adds every price once to the total.

Time complexity: For n descriptions, time and extra space are O(n) under unit-cost integer arithmetic and bounded label lengths. If tracking numbers grow across many calls, formatting and storing labels also depend on their digit length.

One thing I understand better now: Sharing a counter does not mean sharing the identifier assigned to each object. Method overriding also lets one loop process both parcel types.

One thing I am still unsure about: How should the counter be scoped if separate shipping desks need separate sequences, or if multiple calls run concurrently?

The exact assigned OCW lecture still needs confirmation. This response covers the existing classes and inheritance study draft.
