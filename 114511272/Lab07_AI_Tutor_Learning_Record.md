# AOOP 2026 — Lab 07 AI Tutor Learning Record

## Topic
pybind11: Calling C++ functions and classes from Python

## Part A: True or False

### 1. Check My Understanding

**Question 1:** True or False: `PYBIND11_MODULE(gradecpp, m)` defines the Python module name used by `import gradecpp`.

**Answer:** True.

**Reason:** The module name in the binding code must match the compiled extension module that Python imports.

**Question 2:** True or False: `m.def("add_bonus", &add_bonus)` is optional if the C++ function is already defined in `grade.cpp`.

**Answer:** False.

**Reason:** A C++ function is not automatically exposed to Python. `m.def` makes it available through the module.

**Question 3:** True or False: With `#include <pybind11/stl.h>`, pybind11 can convert a Python list to `std::vector<double>` when calling `average_scores`.

**Answer:** True.

**Reason:** The STL conversion header enables automatic conversions for supported containers.

**Question 4:** True or False: If `average_scores` throws `std::invalid_argument`, Python receives a `ValueError`.

**Answer:** True.

**Reason:** pybind11 translates this standard C++ exception type into the corresponding Python exception.

**Question 5:** True or False: Changing `grade.cpp` changes the already compiled Python extension immediately, without recompiling.

**Answer:** False.

**Reason:** Python imports the compiled extension, so the C++ code needs to be rebuilt after edits.

**Questions completed:** 5 / 5 (sample exercise answers; review before submitting)

**Answers revised after AI hints:** Not recorded; fill in your actual answer history.

### 2. My Misconception

**Before: I thought…**

[Write what initially confused you about compiling C++ or importing the module.]

**Now: I understand…**

The `.cpp` file is compiled into a Python extension module, and pybind11 bindings decide which C++ functions and methods Python can call.

### 3. Challenge the AI

**One AI-generated question I challenged:**

“True or False: Changing `grade.cpp` changes the imported Python module without recompiling.”

**Why?**

- [ ] Ambiguous
- [ ] Oversimplified
- [ ] Technically questionable
- [ ] Too easy
- [ ] Other

**Brief explanation:**

[Choose the reason that reflects your opinion and explain it in one sentence.]

### 4. One-Minute Reflection

**One thing I am still unsure about:**

[Add a genuine question you still have about pybind11 or C++/Python interoperability.]

## Part B: LeetCode-style Lecture Code Transfer

### 1. Today's Challenge

**Core concept from today's lab:**

Binding C++ functions and an object-oriented class into a Python module with pybind11.

**AI-generated coding challenge title:**

Student Score Analyzer

### Problem statement

Create a C++ extension called `gradecpp` that Python can import. Bind two functions and one class:

- `add_bonus(score, bonus)`: return the sum, capped at 100.
- `average_scores(scores)`: compute the mean of a nonempty vector; reject an empty vector.
- `GradeBook`: maintain scores with methods `add(score)`, `count()`, and `average()`.

### Input/output specification

- `add_bonus`: two numeric arguments; one numeric return value.
- `average_scores`: a list of numbers; one numeric return value, or `ValueError` for an empty list.
- `GradeBook`: stores numbers and returns its item count or average.

### Constraints

- Use `pybind11/stl.h` for list/vector conversion.
- Export functions with `m.def()` and class methods with `py::class_` and `.def()`.
- Keep the module name `gradecpp`.

### Examples

```text
add_bonus(78, 10) -> 88
add_bonus(95, 10) -> 100
average_scores([60, 80, 100]) -> 80
average_scores([]) -> ValueError
GradeBook with scores 60, 80, 100 -> count 3, average 80
```

### 2. My Initial Approach — Before AI Help

[Describe your own first attempt. For example, did you start from the C++ TODOs or try to run Python first?]

### 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

- [x] Yes — I asked for step-by-step setup and help locating the project directory in WSL.

**The most useful hint/question from AI was:**

“The compiler says `grade.cpp: No such file or directory`. Check the current directory and navigate to the folder containing the source files.”

**It helped me realize that:**

The compile command must run from the folder that contains `grade.cpp`, or provide the correct file path.

### 4. My Revision

**Did you change your approach or code after interacting with AI?**

- [x] Yes — I changed my setup procedure to locate the correct folder before compiling.

**What did you change, and why?**

I checked the Windows user directory through WSL and worked on finding the extracted project files. This resolves the file-location problem once the correct folder is selected.

### 5. Verification

**My final program:**

- [ ] Passed the provided examples — confirm after running `python lab.py`
- [ ] Passed additional edge cases — confirm only if tested
- [ ] Still has unresolved problems — update based on actual results

**One edge case to test:**

Input: `add_bonus(95, 10)`

Expected output: `100`

Actual output: [Fill in after running the program]

### 6. One-Minute Reflection

**What idea from the lab did you transfer to this new problem?**

I used pybind11 to make C++ functions and a class callable from Python and checked how data types and exceptions move between the two languages.

**One thing I understand better now:**

The difference between C++ source code, a compiled Python extension, and the Python script that imports it.

**One thing I am still unsure about:**

[Complete based on your own experience.]
