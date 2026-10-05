# AI tutor learning record: Python classes and inheritance, Part B

Name: Yu-Liang Tan / 譚羽良

Student ID: 112511017

Date: 2026-10-05

Topic: MIT OCW 6.0001 classes, inherited initialization, overridden methods, and shared counters

Status: AI-generated transfer challenge and response draft. Confirm the week's lecture assignment and complete the student-response fields during your actual tutoring session.

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

Before coding, answer:

1. Which state belongs to each instance, and which state belongs to the shared class?
2. How will each subclass initialize the common state?
3. How will the final loop obtain different prices without testing the type of each object?

My approach: [not recorded]

Which concept from the lecture code am I applying? [personal response not recorded]

## 3. AI Tutor Help

Did you ask the AI Tutor for help?

- [ ] No, I solved it independently
- [ ] Yes, I received one or more hints

The most useful hint/question from AI was: [not recorded]

It helped me realize that: [personal response not recorded]

## 4. My Revision

Did you change your approach or code after interacting with AI?

- [ ] No
- [ ] Yes

What did you change, and why? [not recorded]

## 5. Verification

My final program:

- [ ] Passed the provided examples
- [ ] Passed additional edge cases
- [ ] Still has unresolved problems

No student solution to this challenge has been recorded or tested. Expected outputs follow the stated problem rules. Independent test scenarios start with the tracking counter at 1.

One edge case I tested: [record the case actually run]

Suggested edge case input:

```text
[("S", 1), ("S", 1)]
```

Expected output:

```text
(["001:7", "002:7"], 14)
```

Actual output: [not recorded]

## 6. One-Minute Reflection

What idea from the OCW lecture did you transfer to this new problem? [personal response not recorded]

Why my solution works: [explain after writing and testing your solution]

Time complexity: [state and justify after implementation]

One thing I understand better now: [personal response not recorded]

One thing I am still unsure about: [personal response not recorded]
