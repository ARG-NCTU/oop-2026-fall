# AOOP 2026 — Lab 04 AI Tutor Learning Record

## Topic
C++ References, Classes, Inheritance, Virtual Functions, and Dynamic Memory

## Part A: True or False

### 1. Check My Understanding

**Question 1:** True or False: If a function parameter is written as `double &v`, changing `v` inside the function can change the original variable.

**Answer:** True.

**Reason:** `v` is a reference to the original variable, not a copy.

**Question 2:** True or False: A `private` data member can be changed directly from outside the class.

**Answer:** False.

**Reason:** Outside code has to use public functions to access or change private data.

**Question 3:** True or False: If a derived class uses `override`, the function can have different parameters from the virtual function in the base class.

**First answer:** True.

**AI hint:** If the parameters are different, is it still the same function being overridden?

**Revised answer:** False.

**Reason:** The function has to match the virtual function in the base class.

**Question 4:** True or False: Memory created with `new double[n]` should be released with `delete p`.

**First answer:** True.

**AI hint:** Does `new[]` use the same kind of `delete` as normal `new`?

**Revised answer:** False.

**Reason:** `new[]` has to be matched with `delete[]`.

**Question 5:** True or False: If a `BaseApp*` points to a `MyApp` object and `Iterate()` is virtual, calling `app->Iterate()` can run `MyApp::Iterate()`.

**Answer:** True.

**Reason:** Because the function is virtual, C++ can call the version from the actual object type.

Questions completed: **5 / 5**

Answers revised after AI hints: **2 / 5**

### 2. My Misconception

**Before: I thought…**

I thought `override` could still work even if the function was a little different, and I also thought `delete` and `delete[]` were basically the same.

**Now: I understand…**

The function has to correctly match the base-class virtual function, and `new[]` has to be paired with `delete[]`.

### 3. Challenge the AI

**One AI-generated question I challenged:**

“True or False: A `private` data member can be changed directly from outside the class.”

**Why?**

- [ ] Ambiguous
- [ ] Oversimplified
- [ ] Technically questionable
- [x] Too easy
- [ ] Other

**Brief explanation:**

It was pretty easy because `private` was directly explained in the lecture. A harder question could ask how to safely change private data from outside the class.

### 4. One-Minute Reflection

**One thing I am still unsure about:**

I am still not fully sure how `vptr` and `vtable` work internally.

## Part B: LeetCode-style Lecture Code Transfer

### 1. Today’s Challenge

**Core concept from today’s OCW lecture:**

Using references, classes, inheritance, and virtual functions.

**AI-generated coding challenge title:**

Smart Device Status Tracker

### Problem statement

Create a base class called `Device` with these pure virtual functions:

```cpp
virtual std::string Name() const = 0;
virtual bool Update() = 0;
virtual int Count() const = 0;
```

Create a derived class called `Sensor` that:

- has a private integer counter,
- starts the counter at `0`,
- returns `"Sensor"` from `Name()`,
- adds 1 to the counter every time `Update()` is called,
- returns `true` from `Update()`,
- returns the current counter from `Count()`.

Also create:

```cpp
void limit_value(int &value, int min, int max);
```

This function should change the original value so it stays between `min` and `max`.

### Input/output specification

There is no keyboard input.

The program should create a `Sensor`, call `Update()` several times, and check the count.

`limit_value()` should directly change the integer passed into it.

### Constraints

- The counter starts at 0.
- `limit_value()` must use a reference.
- `Sensor` must inherit from `Device`.
- The three virtual functions must use `override`.
- Only use concepts covered in class.

### Examples

**Example 1**
```text
Starting count: 0
Update called 3 times
Final count: 3
```

**Example 2**
```text
value = 150
min = 0
max = 100

After limit_value:
value = 100
```

**Example 3**
```text
value = 50
min = 0
max = 100

After limit_value:
value = 50
```

### 2. My Initial Approach — Before AI Help

I planned to make the base class first, then make `Sensor` inherit from it. I would keep the counter private, increase it in `Update()`, and return it in `Count()`. For `limit_value()`, I would use a reference so the original variable changes.

### 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

- [ ] No — I solved it independently
- [x] Yes — I received one or more hints

**The most useful hint/question from AI was:**

“What has to match between the base-class virtual function and the function marked `override`?”

**It helped me realize that:**

The function signature has to match, including things like `const`.

### 4. My Revision

**Did you change your approach or code after interacting with AI?**

- [ ] No
- [x] Yes

**What did you change, and why?**

I checked the function signatures and made sure `Name()` and `Count()` had `const`. I also used `override` for all three functions.

### 5. Verification

My final program:

- [x] Passed the provided examples
- [x] Passed additional edge cases
- [ ] Still has unresolved problems

**One edge case I tested:**

Input:
```text
value = -10
min = 0
max = 100
```

Expected output:
```text
0
```

Actual output:
```text
0
```

### 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**

I used references to change the original variable and inheritance with virtual functions to give the child class its own behavior.

**One thing I understand better now:**

I understand why `override` is useful because the compiler checks whether the function really matches the base-class function.

**One thing I am still unsure about:**

I am still unsure how `vtable` and `vptr` work internally.
