# Weekly AI tutor submissions

One Markdown record per week at `112511017/AI_tutor/wx.md`, combining Part A and Part B.

- [Week 1](w1.md): Lecture 5, tuples, lists, aliasing, mutability, and cloning.
- [Week 2](w2.md): Lecture 6, recursion and dictionaries.
- [Week 3](w3.md): Lecture 7, testing, debugging, exceptions, and assertions.
- [Week 4](w4.md): Lecture 8, object-oriented programming.
- [Week 5](w5.md): Lecture 9, Python classes and inheritance.
- [Week 6](w6.md): Lecture 10, understanding program efficiency, Part 1.
- [Week 7](w7.md): Lecture 11, understanding program efficiency, Part 2.
- [Week 8](w8.md): Lecture 12, searching and sorting. Challenge: count out-of-order event pairs.
- [Week 9](w9.md): 6.0002 Lecture 1, introduction and optimization. Challenge: greedy inspection planning.
- [Week 10](w10.md): 6.0002 Lecture 2, optimization. Challenge: minimum upgrade cost.
- [Week 11](w11.md): 6.0002 Lecture 3, graph models. Challenge: shortest route around closed stations.

The lecture mapping follows the [official course syllabus](https://timetable.nycu.edu.tw/?r=main/crsoutline&Acy=115&Sem=1&CrsNo=515106&lang=zh-tw).

## Supporting code and references

- [Implementations and tests](solutions/), grouped by week.
- [Study references](references/), including the Week 1 answer key and Week 5 class/inheritance notes.

Each weekly record identifies the AI assistance used. Reference answer keys and sample reflections are study material.

Weeks 10 and 11 were prepared ahead of their November 9 and November 16 course dates. Preparation does not establish lecture attendance, video completion, or a live student hint/revision sequence.

All 109 tests passed on November 2, 2026. [Verification details](verification.json) include per-week counts, commands, interpreter version, and the report-to-lecture mapping.

From the repository root, the prepared environment runs without activation:

```bash
112511017/AI_tutor/.venv/bin/python -m pytest -q -p no:cacheprovider 112511017/AI_tutor/solutions
```

On another machine, create the environment with Python 3.11 or newer:

```bash
python3 -m venv 112511017/AI_tutor/.venv
112511017/AI_tutor/.venv/bin/python -m ensurepip
112511017/AI_tutor/.venv/bin/python -m pip install -r 112511017/AI_tutor/requirements-dev.txt
```

From the repository root, run one week's tests:

```bash
cd 112511017/AI_tutor
.venv/bin/python -m pytest -q -p no:cacheprovider solutions/w7
```
