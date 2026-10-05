# AI tutor learning record: C++ OOP, Part B

Name: Yu-Liang Tan / 譚羽良

Student ID: 112511017

Date: 2026-10-05

Topic: Transferring encapsulation and virtual dispatch to a new problem

Status: AI-generated challenge and response draft. This is a transfer exercise based on the C++ lab. It is not a verified assignment for a particular OCW lecture. The student approach, hint history, revisions, and personal reflection remain to be recorded during the actual learning cycle.

## 1. Today's challenge

Core concepts from the C++ lab: Private state, constructor initialization, input validation before assignment, inheritance, `virtual`, `override`, and deleting an object through a base pointer with a virtual destructor.

AI-generated challenge title: Energy-limited delivery devices

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

## 2. My initial approach, before AI help

Before writing code, answer these tutor questions:

1. How will the common interface let the dispatcher handle both device types?
2. Where will you check the required energy so a failed request preserves state?
3. Which concept from `BaseApp` and `MyApp` are you transferring?

My initial approach: [write before asking for hints]

## 3. AI tutor help

Did I ask for help? [record the actual interaction]

The most useful hint or question was: [fill if a hint was used]

It helped me realize that: [fill from your experience]

## 4. My revision

Did I change my approach or code? [record after implementation]

What I changed and why: [fill from the actual revision]

## 5. Verification

The expected outputs above were calculated from the problem rules. No student solution to this new challenge has been supplied or tested yet.

- Passed the provided examples: [record after running your solution]
- Passed additional edge cases: [record after testing]
- Unresolved problems: [record after testing]

One edge case to test:

Input:

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

Actual output: [paste your program's output]

## 6. One-minute reflection

Suggested transfer explanation: The dispatcher uses a common base interface, as the lab's framework uses `BaseApp*`. Virtual dispatch chooses the concrete energy rule. Private state and validation before assignment prevent a failed request from changing the device's energy.

Why my solution works: [explain after implementation]

Time complexity: [justify how many operations each request performs]

One thing I understand better now: [write your own reflection]

One thing I am still unsure about: [write your own remaining question]
