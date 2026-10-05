# AI tutor learning record: C++ OOP, Part B

Name: Yu-Liang Tan / 譚羽良

Student ID: 112511017

Date: 2026-10-05

Topic: Transferring encapsulation and virtual dispatch to a new problem

Status: AI-assisted written response prepared at the student's request. The approach, reflection, implementation, and tests were supplied or verified by the assistant. No independent student work or historical hint cycle is claimed.

Format: [Course AI tutor instructions](https://github.com/ARG-NCTU/oop-python-nycu/blob/d4ccf63b9252d0017e84d3bed10628f0f5ea7bc9/ai-tutor-2026.md)

## 1. Today's Challenge

Core concept from today's OCW lecture: This record transfers the C++ lab concepts listed below. It is not assigned to a verified OCW Python lecture.

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

My approach: The proposed approach is to give each device private energy, expose use and remaining through a common abstract interface, and create the appropriate concrete type once. The dispatcher then calls use through `Device*`. Each use method checks the required energy before subtracting it. This is an AI-assisted plan, not a reconstructed before-help student response.

Which concept from the lecture code am I applying? Encapsulation protects state, and virtual dispatch selects the concrete energy rule through the same base interface.

## 3. AI Tutor Help

Did you ask the AI Tutor for help?

- [ ] No, I solved it independently
- [x] Yes, I received AI assistance

The most useful hint/question from AI was: "Where should the energy check happen so a rejected request leaves the device unchanged?" It directs attention to validation before assignment.

It helped me realize that: I can transfer the `BaseApp`/`MyApp` pattern to `Device` and its two implementations. The dispatcher uses one interface, while each subclass supplies its own energy calculation. A virtual destructor permits deletion through the base pointer.

Assistance used: AI supplied the written approach, response text, implementation, and verification. This is more than hints, and it is not independent student work.

## 4. My Revision

Did you change your approach or code after interacting with AI?

- [x] No separate student revision round was recorded
- [ ] Yes

What did you change, and why? No separate student code revision occurred. AI supplied the implementation, then compiled it and ran the examples and edge cases. The first verified version passed all six checks.

## 5. Verification

My final program is an AI-assisted implementation. The checks below were run by the assistant on October 5, 2026.

- [x] Passed the provided examples
- [x] Passed additional edge cases
- [ ] Still has unresolved problems

[Implementation](solution/device_dispatcher.cpp) and [test runner](solution/test_device_dispatcher.py).

Run from `solution/`:

```bash
make check
```

Result: 6 tests passed with AddressSanitizer, UndefinedBehaviorSanitizer, and leak detection. The checks cover all three examples, rejection preserving state, zero requests, 100 devices, and 1,000 requests.

One edge case tested: An efficient device rejects a cost of 3 with energy 1, then accepts a cost of 1.

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

Actual output:

```text
REJECT 1
ACCEPT 0
```

## 6. One-Minute Reflection

What idea from the OCW lecture did you transfer to this new problem? I can transfer the `BaseApp`/`MyApp` pattern to `Device` and its two implementations. The dispatcher uses one interface, while each subclass supplies its own energy calculation. A virtual destructor permits deletion through the base pointer.

Why my solution works: Each successful use subtracts exactly the required energy. Each rejected use returns before changing energy. `EfficientDevice` computes half the cost rounded up with `cost / 2 + cost % 2`. Each device owns separate state, and virtual dispatch chooses the correct rule. Finally, deleting every device through a virtual base destructor releases the allocations.

Time complexity: For d devices and q requests, creation and deletion take O(d), and each request takes O(1). Total time is O(d + q), with O(d) storage for the device pointers and objects.

One thing I understand better now: A shared interface lets a processing loop use different behaviors without testing the device type for each request.

One thing I am still unsure about: When would an owning smart pointer be preferable to the manual new and delete pattern used in this exercise?
