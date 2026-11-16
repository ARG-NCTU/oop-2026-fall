# AI Tutor Learning Record — Week 03

**Course:** Advanced Object-Oriented Programming (AOOP, NYCU, 115-1)  
**Topic:** Testing, Debugging, Exceptions, and Assertions  
**Scheduled date:** 2026-09-21  
**OCW reference:** [MIT 6.0001 Lecture 7](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/lec7_debug_except/)  
**Course lab / note:** Lab 03: PyTest and Unit Test  
**Python solution:** [`week_03.py`](./week_03.py)

> **Disclosure:** This is an **AI-generated demonstration of a complete tutor session**. The "Student" replies, revisions, challenges, and reflections were generated as examples; they are **not** a transcript of the student’s actual answers or AI interactions. The `.py` file is real, importable Python code and its test results were executed.

## Learning focus

- **Lecture idea:** Robust input parsing, exception handling, boundary tests and assertions.
- **Transfer task:** Sum Valid Integer Scores.
- **Tutor strategy:** One True/False question at a time; provide a hint before correction if the demonstration learner answers incorrectly; then raise the reasoning difficulty.

---

## Part A — True or False
### AI Tutor Learning Cycle (ATLC): one question at a time

**AI Tutor:** I will ask five conceptual True/False questions. I will check your reasoning and give a hint before disclosing an answer if needed.

#### Question 1/5 — Foundational

**AI Tutor:** An exception handler can allow a program to continue after an expected input error. **True or False? Explain briefly.**

**Student:** True.

**AI Tutor (feedback):** Correct. **Answer: True.** Catching a specific exception permits a controlled alternative path.

**AI Tutor (adaptive follow-up):** You handled the foundation, so I will add a less obvious condition in the next question.

#### Question 2/5 — Foundational

**AI Tutor:** A passing test suite proves that no bugs exist in a program. **True or False? Explain briefly.**

**Student (initial):** True — once all of my sample tests pass, there cannot be another bug.

**AI Tutor (hint — no answer yet):** What if an untested empty input, negative number, or malformed string reaches the function?

**Student (revised answer):** False. The tests provide evidence only for cases they cover, not a proof for all inputs.

**AI Tutor (feedback):** Correct after revision. **Answer: False.** Tests only check behaviors represented by their cases and assumptions. This is the main misconception to watch for.

**AI Tutor (adaptive follow-up):** Good correction. The next question will test whether you can apply the distinction rather than repeat the rule.

#### Question 3/5 — Application

**AI Tutor:** Assertions are suitable as the only way to validate all untrusted user input in production code. **True or False? Explain briefly.**

**Student:** False.

**AI Tutor (feedback):** Correct. **Answer: False.** Assertions can be disabled; explicit checks and exceptions are safer for required validation.

#### Question 4/5 — Challenge

**AI Tutor:** A unit test should include invalid inputs or boundary cases when relevant. **True or False? Explain briefly.**

**Student:** True.

**AI Tutor (feedback):** Correct. **Answer: True.** Many bugs are exposed by empty, invalid or extreme inputs.

#### Question 5/5 — Challenge

**AI Tutor:** Catching every exception without inspecting it always makes debugging easier. **True or False? Explain briefly.**

**Student:** False.

**AI Tutor (feedback):** Correct. **Answer: False.** A broad catch can conceal unexpected programming errors.

### ① Check My Understanding — completed record

| Field | Completed result |
|---|---|
| Questions completed | **5 / 5** |
| Answers revised after AI hints | **1 / 5** (illustrative simulation) |
| Final answers after discussion | **5 / 5 correct** (illustrative simulation) |

### ② My Misconception

**AI Tutor:** What misconception did you correct?

**Student — Before: I thought…** I assumed that passing two simple sample tests meant the program was completely correct.

**Student — Now: I understand…** I understand tests raise confidence but do not establish universal correctness; edge and invalid cases matter. A thorough test plan needs normal, boundary, invalid, and regression cases.

### ③ Challenge the AI

**AI Tutor:** Choose one question that was ambiguous, misleading, oversimplified, technically questionable, or too easy. Explain why.

**Student:** I challenge **Q2**: “A passing test suite proves that no bugs exist in a program.”

- **Reason category:** Oversimplified
- **My explanation:** “All tests passed” does not establish correctness for unseen inputs or unspecified requirements.

**AI Tutor (responds to challenge):** That is a fair critique. A more precise version would be:

> Does passing a specified set of tests establish correctness for those checks without proving correctness for every possible input?

**Student:** The revised wording makes the scope and assumption clearer.

### ④ One-Minute Reflection

**AI Tutor:** What do you understand better, and what remains uncertain?

**Student — One thing I understand better:** I understand tests raise confidence but do not establish universal correctness; edge and invalid cases matter.

**Student — One thing I am still unsure about:** How much test coverage is enough for a small assignment.

---

## Part B — LeetCode-style Lecture Code Transfer

### 1. Today’s Challenge (shown before the solution)

**Name:** Student — model-answer demonstration  
**Date:** 2026-09-21  
**Topic:** Testing, Debugging, Exceptions, and Assertions

**Core concept from today’s OCW lecture:** Robust input parsing, exception handling, boundary tests and assertions.

**AI Tutor — Challenge title:** **Sum Valid Integer Scores**

**Problem statement:** Given a list of strings, attempt to parse each entry using int(). Return a pair (sum_of_valid_values, invalid_indices). A value is invalid when int() raises ValueError. Preserve the order of invalid indices.

**Input/output specification:** Input: tokens: list[str]. Output: tuple[int, list[int]].

**Constraints:** 0 <= len(tokens) <= 1000; tokens are strings; whitespace and signed decimal integers follow the behavior of Python int().

- **Example 1:** Input `["10", "bad", "-3"]` → Output `(7, [1])`
- **Example 2:** Input `[" 5 ", "2.5", "+7"]` → Output `(12, [1])`
- **Example 3:** Input `[]` → Output `(0, [])`

**AI Tutor:** Before writing code, explain your proposed algorithm and name the lecture concept you are transferring.

### 2. My Initial Approach — Before AI Help

**Student (initial approach):** I will accept strings only when token.isdigit() is true.

**Student (lecture concept I intended to apply):** Robust input parsing, exception handling, boundary tests and assertions.

### 3. AI Tutor Help

**Did I ask AI Tutor for help?** ☑ Yes — one example hint; ☐ No.

**AI Tutor (does not provide the code):** Which operation defines validity in the problem: isdigit() or an actual int() conversion?

**Student:** A valid negative number or a string with surrounding spaces may fail isdigit() even though int(token) can parse it.

**AI Tutor (follow-up question):** Would testing only strings containing digits handle negative numbers and spaces correctly?

**Student — What the hint helped me realize:** I understand tests raise confidence but do not establish universal correctness; edge and invalid cases matter.

### 4. My Revision

**Did I change my approach or code?** ☑ Yes (demonstration); ☐ No.

**Student (revised algorithm):** Enumerate the tokens and try converting each with int. On ValueError, record its position instead of terminating the function.

**Student (what changed and why):** Use int(token) inside try/except ValueError, rather than a digits-only filter, and add invalid-input tests.

**AI Tutor:** Your reasoning now addresses the key issue. Write and run the code yourself, then verify it using examples and edge cases. The completed worked-example solution is saved separately as [`week_03.py`](./week_03.py).

### 5. Verification — actual executable Python

**My final program:** [`week_03.py`](./week_03.py) (function `sum_valid_scores`)

**Run it from this folder:**

```bash
python week_03.py
```

**Actual automated check:** `Week 03: PASS (4 test cases)`

- ☑ Passed the provided examples
- ☑ Passed additional edge cases
- ☐ Still has unresolved problems in the tested cases

**One edge case considered:** Whitespace around a valid integer should be accepted; decimal strings such as "2.5" should be rejected.

- **Input arguments:** `([' -2 ', '+5', 'two', ''],)`
- **Expected output:** `(3, [2, 3])`
- **Actual output:** `(3, [2, 3])`

**Verification detail:** Also tested whitespace, signed integers, malformed decimals and an empty list.

**AI Tutor:** Why is the revised solution correct? What are its time and auxiliary-space complexities?

**Student — Correctness argument:** The loop classifies each token exactly once using the same conversion rule specified in the prompt.

**Student — Complexity:** Time O(L) over the total number of input characters; output space O(k) for k invalid items.

### 6. One-Minute Reflection

**Student — Idea transferred from the OCW lecture:** I transferred exception handling and test design from lecture into a robust data-cleaning function.

**Student — One thing I understand better now:** I understand tests raise confidence but do not establish universal correctness; edge and invalid cases matter.

**Student — One thing I am still unsure about:** How much test coverage is enough for a small assignment.

**AI Tutor — Closing feedback:** You completed the conceptual check, revised one mistaken explanation with a hint, challenged an imprecise question, and applied the same lecture idea to a new problem. Review the remaining uncertainty before the next topic.

---

## Sources and academic-integrity note

- Class topic, date and lab: user-provided NYCU 115-1 AOOP syllabus (`1151_515106syllabus.docx`).
- MIT OCW lecture reference: [MIT 6.0001 Lecture 7](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/lec7_debug_except/).
- Assignment record template: [AI Tutor for AOOP 2026](https://github.com/ARG-NCTU/oop-python-nycu/blob/main/ai-tutor-2026.md).
- The questions, learner responses, challenges, program, and explanations are AI-generated model content, not quotations of MIT source code or verified firsthand student work. Do not present the simulated dialogue as an actual independent student session.
