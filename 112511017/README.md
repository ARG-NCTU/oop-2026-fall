# 112511017

AOOP 2026 Fall coursework for [MoobyMoo](https://github.com/MoobyMoo).

## Coursework folders

| Material | Folder |
| --- | --- |
| Python lab and tests | [Lab 03](labs/lab03-pytest/) |
| C++ OOP lab | [Lab 04](labs/lab04-cpp-oop/) |
| Weekly tutor material, Part A and Part B | [AI tutor](ai-tutor/) |

Run the Python lab tests from this directory:

```bash
python3 -m pytest labs/lab03-pytest
```

## C++ OOP lab

The slides are labeled Lab 04; the matching starter was downloaded as `W5new.zip`.
The completed exercises are in [labs/lab04-cpp-oop/](labs/lab04-cpp-oop/). Only `student.cpp` was changed from the instructor's starter.

Run the lab from this directory:

```bash
cd labs/lab04-cpp-oop
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

[Recovered material and status for Weeks 1–4](ai-tutor/). Week 1 contains completed AI-assisted written responses plus the recovered references. Completed personal records for Weeks 2–4 have not been located.

[October 5 C++ OOP responses](ai-tutor/2026-10-05/cpp-oop/) contains five explained answers and a completed AI-assisted challenge response. Its delivery-device implementation passed six tests with sanitizers.

[October 5 OCW Python responses](ai-tutor/2026-10-05/python-oop/) covers classes and inheritance from Lectures 8 and 9, with AI-assisted answers and reflections. Its shipping-quote implementation passed eight tests. The exact assigned lecture still needs confirmation.
