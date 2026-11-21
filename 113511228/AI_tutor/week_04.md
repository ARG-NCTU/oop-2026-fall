# AI Tutor Learning Record — Week 04

**Course:** Advanced Object-Oriented Programming (AOOP, NYCU, 115-1)  
**Topic:** Object-Oriented Programming  
**Scheduled date:** 2026-09-28  
**OCW reference:** [MIT 6.0001 Lecture 8](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/lec8_classes/)  
**Course lab / note:** Teacher’s Day holiday; OCW self-study assigned  
**Python solution:** [`week_04.py`](./week_04.py)

> **Disclosure:** This is an **AI-generated demonstration of a complete tutor session**. The "Student" replies, revisions, challenges, and reflections were generated as examples; they are **not** a transcript of the student’s actual answers or AI interactions. The `.py` file is real, importable Python code and its test results were executed.

## Learning focus

- **Lecture idea:** Classes, state, methods, encapsulation and invariants.
- **Transfer task:** Study-Room Seat Booking.
- **Tutor strategy:** One True/False question at a time; provide a hint before correction if the demonstration learner answers incorrectly; then raise the reasoning difficulty.

---

## Part A — True or False
### AI Tutor Learning Cycle (ATLC): one question at a time

**AI Tutor:** I will ask five conceptual True/False questions. I will check your reasoning and give a hint before disclosing an answer if needed.

#### Question 1/5 — Foundational

**AI Tutor:** A class can define both data attributes and methods operating on those attributes. **True or False? Explain briefly.**

**Student:** True.

**AI Tutor (feedback):** Correct. **Answer: True.** This groups an object’s state with the behaviors that manage that state.

**AI Tutor (adaptive follow-up):** You handled the foundation, so I will add a less obvious condition in the next question.

#### Question 2/5 — Foundational

**AI Tutor:** Two objects created from the same class must always share one state instance. **True or False? Explain briefly.**

**Student (initial):** True — all objects created from a class share the class definition, so they should share the data.

**AI Tutor (hint — no answer yet):** If two students each create a StudyRoom object, should booking a seat in one room fill a seat in the other?

**Student (revised answer):** False. Instance attributes can be different for different objects; class attributes are a separate concept.

**AI Tutor (feedback):** Correct after revision. **Answer: False.** Instance attributes normally belong to each object independently. This is the main misconception to watch for.

**AI Tutor (adaptive follow-up):** Good correction. The next question will test whether you can apply the distinction rather than repeat the rule.

#### Question 3/5 — Application

**AI Tutor:** A class method should maintain the object’s stated invariants after a successful operation. **True or False? Explain briefly.**

**Student:** True.

**AI Tutor (feedback):** Correct. **Answer: True.** For example, a booking system should never exceed capacity.

#### Question 4/5 — Challenge

**AI Tutor:** Object-oriented design means that every problem must use inheritance. **True or False? Explain briefly.**

**Student:** False.

**AI Tutor (feedback):** Correct. **Answer: False.** Many designs need only objects, composition or ordinary functions.

#### Question 5/5 — Challenge

**AI Tutor:** Calling a method can change an object’s state without returning that object. **True or False? Explain briefly.**

**Student:** True.

**AI Tutor (feedback):** Correct. **Answer: True.** Methods can modify instance attributes as a side effect.

### ① Check My Understanding — completed record

| Field | Completed result |
|---|---|
| Questions completed | **5 / 5** |
| Answers revised after AI hints | **1 / 5** (illustrative simulation) |
| Final answers after discussion | **5 / 5 correct** (illustrative simulation) |

### ② My Misconception

**AI Tutor:** What misconception did you correct?

**Student — Before: I thought…** I thought writing OOP required complex inheritance trees.

**Student — Now: I understand…** I can use a small class to bundle state and operations without inheritance. A class defines a blueprint, while each instance can have its own state.

### ③ Challenge the AI

**AI Tutor:** Choose one question that was ambiguous, misleading, oversimplified, technically questionable, or too easy. Explain why.

**Student:** I challenge **Q4**: “Object-oriented design means that every problem must use inheritance.”

- **Reason category:** Too easy
- **My explanation:** Inheritance is optional in object-oriented programming; treating it as compulsory ignores simpler designs.

**AI Tutor (responds to challenge):** That is a fair critique. A more precise version would be:

> When modeling a room reservation system, is inheritance optional if one class already encapsulates the needed state and methods?

**Student:** The revised wording makes the scope and assumption clearer.

### ④ One-Minute Reflection

**AI Tutor:** What do you understand better, and what remains uncertain?

**Student — One thing I understand better:** I can use a small class to bundle state and operations without inheritance.

**Student — One thing I am still unsure about:** How to decide when a simple function is better than a class.

---

## Part B — LeetCode-style Lecture Code Transfer

### 1. Today’s Challenge (shown before the solution)

**Name:** Student — model-answer demonstration  
**Date:** 2026-09-28  
**Topic:** Object-Oriented Programming

**Core concept from today’s OCW lecture:** Classes, state, methods, encapsulation and invariants.

**AI Tutor — Challenge title:** **Study-Room Seat Booking**

**Problem statement:** Implement a class that tracks reservations for a room with limited capacity. reserve(name) returns True only if the person is not already booked and space remains. cancel(name) returns True only if the person was booked. remaining() returns the number of available seats. Implement process_bookings(capacity, operations) to return a result for every command.

**Input/output specification:** Input: capacity: nonnegative int; operations: list of (action, name) where action is reserve/cancel/remaining. Output: list of bool/int results in command order; name is ignored for remaining.

**Constraints:** 0 <= capacity <= 100; 0 <= number of operations <= 1000; names are strings.

- **Example 1:** Input `(2, [("reserve", "Amy"), ("reserve", "Amy"), ("remaining", ""), ("cancel", "Amy")])` → Output `[True, False, 1, True]`
- **Example 2:** Input `(1, [("reserve", "A"), ("reserve", "B"), ("remaining", "")])` → Output `[True, False, 0]`
- **Example 3:** Input `(0, [("remaining", ""), ("reserve", "A")])` → Output `[0, False]`

**AI Tutor:** Before writing code, explain your proposed algorithm and name the lecture concept you are transferring.

### 2. My Initial Approach — Before AI Help

**Student (initial approach):** I will append every reserve request to a list until its length reaches capacity.

**Student (lecture concept I intended to apply):** Classes, state, methods, encapsulation and invariants.

### 3. AI Tutor Help

**Did I ask AI Tutor for help?** ☑ Yes — one example hint; ☐ No.

**AI Tutor (does not provide the code):** Can one person appear twice without reducing available seats twice?

**Student:** Two reservations from the same person would consume two seats and break the uniqueness requirement.

**AI Tutor (follow-up question):** What invariant must remain true even when the same person tries to reserve twice?

**Student — What the hint helped me realize:** I can use a small class to bundle state and operations without inheritance.

### 4. My Revision

**Did I change my approach or code?** ☑ Yes (demonstration); ☐ No.

**Student (revised algorithm):** Keep capacity and a collection of reserved names as instance state; expose methods for each valid operation.

**Student (what changed and why):** Check duplicate names before adding; check capacity before accepting a new reservation.

**AI Tutor:** Your reasoning now addresses the key issue. Write and run the code yourself, then verify it using examples and edge cases. The completed worked-example solution is saved separately as [`week_04.py`](./week_04.py).

### 5. Verification — actual executable Python

**My final program:** [`week_04.py`](./week_04.py) (function `process_bookings`)

**Run it from this folder:**

```bash
python week_04.py
```

**Actual automated check:** `Week 04: PASS (4 test cases)`

- ☑ Passed the provided examples
- ☑ Passed additional edge cases
- ☐ Still has unresolved problems in the tested cases

**One edge case considered:** A zero-capacity room cannot accept reservations; repeated reservations should not consume extra space.

- **Input arguments:** `(1, [('reserve', 'A'), ('reserve', 'A'), ('cancel', 'B'), ('remaining', '')])`
- **Expected output:** `[True, False, False, 0]`
- **Actual output:** `[True, False, False, 0]`

**Verification detail:** Also tested zero capacity, duplicate booking and cancellation.

**AI Tutor:** Why is the revised solution correct? What are its time and auxiliary-space complexities?

**Student — Correctness argument:** The reserve method guards both uniqueness and capacity; cancel updates the same state; remaining derives a valid count.

**Student — Complexity:** Expected O(1) per operation with a set; total expected O(m) time and O(min(m, capacity)) space.

### 6. One-Minute Reflection

**Student — Idea transferred from the OCW lecture:** I transferred the class/state/method abstraction into a real reservation-system model.

**Student — One thing I understand better now:** I can use a small class to bundle state and operations without inheritance.

**Student — One thing I am still unsure about:** How to decide when a simple function is better than a class.

**AI Tutor — Closing feedback:** You completed the conceptual check, revised one mistaken explanation with a hint, challenged an imprecise question, and applied the same lecture idea to a new problem. Review the remaining uncertainty before the next topic.

---

## Sources and academic-integrity note

- Class topic, date and lab: user-provided NYCU 115-1 AOOP syllabus (`1151_515106syllabus.docx`).
- MIT OCW lecture reference: [MIT 6.0001 Lecture 8](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/lec8_classes/).
- Assignment record template: [AI Tutor for AOOP 2026](https://github.com/ARG-NCTU/oop-python-nycu/blob/main/ai-tutor-2026.md).
- The questions, learner responses, challenges, program, and explanations are AI-generated model content, not quotations of MIT source code or verified firsthand student work. Do not present the simulated dialogue as an actual independent student session.
