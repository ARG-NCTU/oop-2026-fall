# AI tutor learning record: C++ OOP, Part B

Name: Yu-Liang Tan / 譚羽良

Student ID: 112511017

Date: 2026-10-05

Topic: Transferring encapsulation and virtual dispatch to a new problem

Status: AI-generated challenge and response draft. This is a transfer exercise based on the C++ lab. It is not a verified assignment for a particular OCW lecture. The student approach, hint history, revisions, and personal reflection remain to be recorded during the actual learning cycle.

Format: [Course AI tutor instructions](https://github.com/ARG-NCTU/oop-python-nycu/blob/d4ccf63b9252d0017e84d3bed10628f0f5ea7bc9/ai-tutor-2026.md)

## 1. Today's Challenge

Core concept from today's OCW lecture: [OCW lecture not confirmed for this C++ lab draft]

C++ lab concepts transferred: Private state, constructor initialization, input validation before assignment, inheritance, `virtual`, `override`, and deleting an object through a base pointer with a virtual destructor.

AI-generated coding challenge title: Energy-limited delivery devices

### Problem statement

A dispatcher controls several devices. Every device starts with an energy value between 0 and 100. A delivery request has a nonnegative integer cost.

There are two device types:

- `StandardDevice` spends the requested cost.
- `EfficientDevice` spends half the requested cost, rounded up.

A device accepts a request only when it has enough energy. A rejected request must leave its energy unchanged. A request with zero cost is valid.

Implement a common abstract `Device` interface with `use(int cost)` and `remaining() const`. The concrete classes must implement the interface with `override`. Keep each device's energy private. Process requests through `Device*` so that the dispatcher does not need a conditional on the device type for each request. Release every allocated device after processing, using a virtual base destructor.

### Input and output

The first line contains `d q`, the number of devices and requests.

Each of the next `d` lines contains a type, `S` or `E`, and an initial energy value.

Each of the next `q` lines contains a zero-based device index and a requested cost.

For every request, print `ACCEPT` or `REJECT`, followed by that device's remaining energy. Devices keep independent state across requests.

### Constraints

- `1 <= d <= 100`
- `0 <= q <= 1000`
- Initial energy is an integer from 0 through 100.
- Requested cost is an integer from 0 through 1000.
- Device indices are valid.

### Example 1: Different virtual implementations

Input:

```text
2 4
S 10
E 10
0 7
1 7
0 4
1 12
```

Expected output:

```text
ACCEPT 3
ACCEPT 6
REJECT 3
ACCEPT 0
```

### Example 2: Zero energy and zero-cost requests

Input:

```text
1 2
S 0
0 0
0 1
```

Expected output:

```text
ACCEPT 0
REJECT 0
```

### Example 3: Rounding and rejection preserve state

Input:

```text
1 3
E 2
0 3
0 1
0 0
```

Expected output:

```text
ACCEPT 0
REJECT 0
ACCEPT 0
```

## 2. My Initial Approach Before AI Help

Before writing code, answer these tutor questions:

1. How will the common interface let the dispatcher handle both device types?
2. Where will you check the required energy so a failed request preserves state?
3. Which concept from `BaseApp` and `MyApp` are you transferring?

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

No student solution to this challenge has been recorded or tested. Expected outputs follow the stated problem rules. This C++ exercise transfers lab concepts; confirm whether the assigned OCW record must instead cover Python.

One edge case I tested: [record the case actually run]

Suggested edge case input:

```text
1 2
E 1
0 3
0 1
```

Expected output:

```text
REJECT 1
ACCEPT 0
```

Actual output: [not recorded]

## 6. One-Minute Reflection

What idea from the OCW lecture did you transfer to this new problem? [personal response not recorded]

Why my solution works: [explain after writing and testing your solution]

Time complexity: [state and justify after implementation]

One thing I understand better now: [personal response not recorded]

One thing I am still unsure about: [personal response not recorded]
