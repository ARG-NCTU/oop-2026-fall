# AI Tutor Learning Record: Part A

Name: Yu-Liang Tan / 譚羽良

Student ID: 112511017

Date: 2026-10-05

Topic: References, encapsulation, constructors, virtual functions, and dynamic arrays

Status: Written responses and first-person reflection text prepared with AI assistance at the student's request. This records the current assisted response, not a restored historical tutoring session. No one-at-a-time hint and revision cycle was performed.

Format: [Course AI tutor instructions](https://github.com/ARG-NCTU/oop-python-nycu/blob/d4ccf63b9252d0017e84d3bed10628f0f5ea7bc9/ai-tutor-2026.md)

## ① Check My Understanding

Questions completed: 5 / 5 written responses supplied with AI assistance.

Answers revised after AI hints: 0 / 5 in this prepared response. The answers were supplied together, without an interactive hint and revision round. Historical revision counts were not recovered.

## ② My Misconception

Before: I might treat a private member as a guarantee that its value is valid.

Now: I can separate access control from validation. Private prevents direct outside access, but constructors and member functions must enforce the valid range. The supplied Battery constructor accepts its argument directly, while `setLevel` checks before changing the member.

## ③ Challenge the AI

One AI-generated question I challenged:

A private member alone guarantees that the member always contains a valid value.

Why?

- [ ] Ambiguous
- [x] Oversimplified
- [ ] Technically questionable
- [ ] Too easy
- [ ] Other: None

Brief explanation: Private controls who can access a member, not which values the class stores. `Battery(120)` is a counterexample in this lab because the constructor directly initializes `m_level`. Encapsulation makes validation possible but does not perform it automatically.

## ④ One-Minute Reflection

One thing I am still unsure about: How should a constructor report an invalid initial value when it cannot return a boolean like a setter?

## Answers and reasoning

### Question 1

If `clamp_value` takes `double v` instead of `double &v`, assigning to `v` inside the function still changes the caller's variable.

Answer: False

My reasoning: A value parameter is a copy, so changing it does not change the caller's variable. A `double &` parameter refers to the original variable and can change it.

### Question 2

A private member alone guarantees that the member always contains a valid value.

Answer: False

My reasoning: Private prevents direct access from outside the class. The constructor and member functions can still store invalid values unless they validate them.

### Question 3

`Battery::Battery(double level) : m_level(level) {}` initializes `m_level` before the constructor body runs.

Answer: True

My reasoning: The member initialization list initializes `m_level` before the constructor body executes. Assignment inside the body happens later.

### Question 4

Calling `Iterate()` through a `BaseApp*` that points to a `MyApp` object executes `MyApp::Iterate()`.

Answer: True

My reasoning: `Iterate` is virtual in `BaseApp`, and `MyApp` overrides it. A call through a `BaseApp` pointer dispatches to the implementation for the actual `MyApp` object.

### Question 5

When `make_buffer` returns, the dynamically allocated array is automatically destroyed because its local pointer variable goes out of scope.

Answer: False

My reasoning: Only the local pointer variable ends its lifetime. The array allocated by `new[]` remains alive until the caller releases it with `delete[]`.

## Reference material

The [earlier suggested answers and hints](study-guide.md) remain available for study. No earlier personal answer sequence or hint history is claimed here.
