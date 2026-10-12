# 112511017

AOOP 2026 Fall coursework for [MoobyMoo](https://github.com/MoobyMoo).

## Coursework folders

| Material | Folder |
| --- | --- |
| Python lab and tests | [Lab 03](labs/lab03-pytest/) |
| C++ OOP lab | [Lab 04](labs/lab04-cpp-oop/) |
| Weekly tutor material, Part A and Part B | [Weekly submissions](AI_tutor/) |

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

Weekly submissions follow the October 7 announcement: `112511017/AI_tutor/wx.md`, with one Markdown file per week containing Part A and Part B.

| Week | Assigned MIT OCW lecture | Submission |
| --- | --- | --- |
| 1 | Lecture 5: Lists, aliasing, and mutation | [w1.md](AI_tutor/w1.md) |
| 2 | Lecture 6: Recursion and dictionaries | [w2.md](AI_tutor/w2.md) |
| 3 | Lecture 7: Testing and exceptions | [w3.md](AI_tutor/w3.md) |
| 4 | Lecture 8: Object oriented programming | [w4.md](AI_tutor/w4.md) |
| 5 | Lecture 9: Python classes and inheritance | [w5.md](AI_tutor/w5.md) |
| 6 | Lecture 10: Understanding program efficiency, Part 1 | [w6.md](AI_tutor/w6.md) |

The week/topic mapping is confirmed by the [official AOOP syllabus](https://timetable.nycu.edu.tw/?r=main/crsoutline&Acy=115&Sem=1&CrsNo=515106&lang=zh-tw).

Weeks 1–5 consolidate the assisted responses prepared on October 5. Week 6 was prepared on October 12. Each record states the AI assistance used and preserves the distinction between supplied answers and a student-led tutoring session. The [supporting material](ai-tutor/) includes the original records and implementations. The [C++ OOP responses](ai-tutor/2026-10-05/cpp-oop/) supplement Lab 04; the Week 5 MIT assignment is Python inheritance.
