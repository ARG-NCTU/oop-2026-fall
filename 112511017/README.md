# 112511017

AOOP 2026 Fall coursework for [MoobyMoo](https://github.com/MoobyMoo).

Exercises and assignments will be kept in this directory.

## C++ OOP lab

The slides are labeled Lab 04; the matching starter was downloaded as `W5new.zip`.
The completed exercises are in [lab04-cpp-oop/](lab04-cpp-oop/). Only `student.cpp` was changed from the instructor's starter.

Run the lab from this directory:

```bash
cd lab04-cpp-oop
make doctor
make check
```

Validation on October 5, 2026 returned `ENV OK` and `ALL PASS (4/4)`, with AddressSanitizer and leak detection enabled.

For the TA's code explanation check:

- `double &v` is a reference, so assigning to `v` changes the caller's variable.
- `m_level(level)` initializes the battery member before the constructor body runs. `setLevel` rejects values outside 0 through 100 before changing that member.
- `MyApp` implements every pure virtual function. `override` lets the compiler check the signatures, and calls through `BaseApp*` dispatch to `MyApp`. Each `Iterate()` adds one to its own count.
- `new double[n]` allocates an array on the heap. The loop fills each element with its index, and `delete[]` releases the whole array. The caller deletes the app separately through the base class's virtual destructor.

The starter asks for a live TA check of the passing terminal output and a short explanation of a randomly selected line.

## AI tutor

[October 5 C++ OOP study draft](ai-tutor/2026-10-05-cpp-oop/) contains five True/False questions, suggested answers, and a new coding challenge. The learning-record fields that require a personal response remain marked for review.

[October 5 OCW Python study draft](ai-tutor/2026-10-05-python-oop/) covers classes and inheritance from Lectures 8 and 9. Confirm the assigned lecture and complete the personal learning-record fields before submitting it as a finished record.
