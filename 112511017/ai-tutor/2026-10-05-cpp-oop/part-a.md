# AI tutor learning record: C++ OOP, Part A

Name: Yu-Liang Tan / 譚羽良

Student ID: 112511017

Date: 2026-10-05

Topic: References, encapsulation, constructors, virtual functions, and dynamic arrays

Status: AI-generated draft for student review. The suggested answers below are study responses, not a transcript of completed tutoring. Replace the review fields with your actual answers and reflections before submitting this as a completed learning record.

Sources: [Lab 04 code](../../labs/lab04-cpp-oop/student.cpp), [instructor's concept guide](../../labs/lab04-cpp-oop/GUIDE.md), and the AOOP 2026 AI tutor learning-record format.

## Five True/False questions

### 1. References

Statement: If `clamp_value` takes `double v` instead of `double &v`, assigning to `v` inside the function still changes the caller's variable.

Suggested answer: False. Passing by value creates a separate copy. A reference parameter is an alias for the caller's variable, so changing it changes that variable.

Tutor hint if needed: Start with `double x = 15`. After the function returns, which variable received the assignment, a copy or `x`?

### 2. Encapsulation

Statement: A private member alone guarantees that the member always contains a valid value.

Suggested answer: False. `private` restricts direct access from outside the class. The constructor and member functions still need to enforce the rules. In this lab, `setLevel` checks the range, but the constructor stores the supplied value directly as required by the exercise.

Tutor hint if needed: What happens with `Battery b(120)` in the current implementation?

### 3. Initialization

Statement: `Battery::Battery(double level) : m_level(level) {}` initializes `m_level` before the constructor body runs.

Suggested answer: True. The member initialization list initializes the member. Assigning to it inside the constructor body would be a later assignment instead.

Tutor hint if needed: Compare initializing a member with changing an already initialized member. Which happens first?

### 4. Virtual dispatch

Statement: Calling `Iterate()` through a `BaseApp*` that points to a `MyApp` object executes `MyApp::Iterate()`.

Suggested answer: True. `Iterate` is virtual in the base class, so the call selects the override for the actual object. The base pointer determines which operations can be called, while the object's type determines the virtual implementation.

Tutor hint if needed: Compare this call with calling a nonvirtual function through a base pointer.

### 5. Heap lifetime

Statement: When `make_buffer` returns, the dynamically allocated array is automatically destroyed because its local pointer variable goes out of scope.

Suggested answer: False. The local pointer variable goes out of scope, but the allocated array remains alive. The caller receives its address and must eventually release it with `delete[]`, here through `free_buffer`.

Tutor hint if needed: Distinguish the pointer variable from the allocation it points to.

## 1. Check my understanding

Questions generated: 5 / 5

Questions personally completed: [fill after answering] / 5

Answers revised after AI hints: [fill from the actual interaction] / 5

## 2. My misconception

Suggested reflection, keep only if it describes your experience:

Before: I thought that making a field private was enough to keep its value valid.

Now: I understand that private access prevents outside code from writing directly to the field, but the constructor and member functions must also validate values. The lab's setter rejects invalid levels before assignment, so a rejected update preserves the old level.

## 3. Challenge the AI

Candidate question to challenge: "A private member alone guarantees that the member always contains a valid value."

Reason: Oversimplified if it is presented without distinguishing access control from validation.

Suggested explanation: Encapsulation can provide a place to enforce a rule, but it does not enforce that rule automatically. `Battery(120)` is a counterexample in the supplied exercise because the required constructor directly initializes `m_level`.

My actual chosen question and explanation: [review the candidate or replace it]

## 4. One-minute reflection

Suggested point to investigate: How should a constructor handle an invalid initial value when it cannot return `false` like a setter? Should it reject construction, clamp the value, or use a default?

One thing I am still unsure about: [write your own remaining question]
