# AI Tutor Learning Record — Week 05

**Course:** Advanced Object-Oriented Programming (AOOP, NYCU, 115-1)  
**Topic:** Python Classes and Inheritance  
**Scheduled date:** 2026-10-05  
**OCW reference:** [MIT 6.0001 Lecture 9](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/lec9_inheritance/)  
**Course lab / note:** Lab 04: C++ OOP and Build Tool; Project Idea Discussions (1)  
**Python solution:** [`week_05.py`](./week_05.py)

> **Disclosure:** This is an **AI-generated demonstration of a complete tutor session**. The "Student" replies, revisions, challenges, and reflections were generated as examples; they are **not** a transcript of the student’s actual answers or AI interactions. The `.py` file is real, importable Python code and its test results were executed.

## Learning focus

- **Lecture idea:** Subclassing, overriding methods and runtime polymorphism.
- **Transfer task:** Polymorphic Shipping Calculator.
- **Tutor strategy:** One True/False question at a time; provide a hint before correction if the demonstration learner answers incorrectly; then raise the reasoning difficulty.

---

## Part A — True or False
### AI Tutor Learning Cycle (ATLC): one question at a time

**AI Tutor:** I will ask five conceptual True/False questions. I will check your reasoning and give a hint before disclosing an answer if needed.

#### Question 1/5 — Foundational

**AI Tutor:** A subclass can override an inherited method to provide different behavior. **True or False? Explain briefly.**

**Student:** True.

**AI Tutor (feedback):** Correct. **Answer: True.** Method lookup can select the subclass implementation.

**AI Tutor (adaptive follow-up):** You handled the foundation, so I will add a less obvious condition in the next question.

#### Question 2/5 — Foundational

**AI Tutor:** Inheritance automatically guarantees that every subclass obeys its parent’s intended contract. **True or False? Explain briefly.**

**Student (initial):** True — if a class inherits from another class, Python ensures its behavior remains correct.

**AI Tutor (hint — no answer yet):** Could a child class override cost() to return a negative charge without causing a syntax error?

**Student (revised answer):** False. Inheritance gives access to behavior, but cannot guarantee the subclass preserves the contract.

**AI Tutor (feedback):** Correct after revision. **Answer: False.** The programmer must preserve compatible behavior and invariants. This is the main misconception to watch for.

**AI Tutor (adaptive follow-up):** Good correction. The next question will test whether you can apply the distinction rather than repeat the rule.

#### Question 3/5 — Application

**AI Tutor:** Polymorphism allows different object types to be used through a common method interface. **True or False? Explain briefly.**

**Student:** True.

**AI Tutor (feedback):** Correct. **Answer: True.** Client code can call the same method without branching on concrete types.

#### Question 4/5 — Challenge

**AI Tutor:** Using super() can invoke a parent-class implementation. **True or False? Explain briefly.**

**Student:** True.

**AI Tutor (feedback):** Correct. **Answer: True.** It provides access to methods in the applicable method resolution order.

#### Question 5/5 — Challenge

**AI Tutor:** Creating a subclass necessarily copies all parent implementation code into the new source file. **True or False? Explain briefly.**

**Student:** False.

**AI Tutor (feedback):** Correct. **Answer: False.** The subclass normally inherits behavior via attribute/method lookup.

### ① Check My Understanding — completed record

| Field | Completed result |
|---|---|
| Questions completed | **5 / 5** |
| Answers revised after AI hints | **1 / 5** (illustrative simulation) |
| Final answers after discussion | **5 / 5 correct** (illustrative simulation) |

### ② My Misconception

**AI Tutor:** What misconception did you correct?

**Student — Before: I thought…** I thought extending a class always preserved every behavior automatically.

**Student — Now: I understand…** I understand child classes can override methods incorrectly and still run without a syntax error. Substitutability is a design responsibility, not a language guarantee.

### ③ Challenge the AI

**AI Tutor:** Choose one question that was ambiguous, misleading, oversimplified, technically questionable, or too easy. Explain why.

**Student:** I challenge **Q2**: “Inheritance automatically guarantees that every subclass obeys its parent’s intended contract.”

- **Reason category:** Technically questionable
- **My explanation:** Syntactically valid inheritance does not guarantee substitutability or semantic correctness.

**AI Tutor (responds to challenge):** That is a fair critique. A more precise version would be:

> Does Python permit a subclass override even when the override violates a documented behavior contract?

**Student:** The revised wording makes the scope and assumption clearer.

### ④ One-Minute Reflection

**AI Tutor:** What do you understand better, and what remains uncertain?

**Student — One thing I understand better:** I understand child classes can override methods incorrectly and still run without a syntax error.

**Student — One thing I am still unsure about:** How to detect violations of the Liskov Substitution Principle in larger programs.

---

## Part B — LeetCode-style Lecture Code Transfer

### 1. Today’s Challenge (shown before the solution)

**Name:** Student — model-answer demonstration  
**Date:** 2026-10-05  
**Topic:** Python Classes and Inheritance

**Core concept from today’s OCW lecture:** Subclassing, overriding methods and runtime polymorphism.

**AI Tutor — Challenge title:** **Polymorphic Shipping Calculator**

**Problem statement:** Design a base ShippingMethod class with a cost(weight) interface. Standard shipping costs 5 + 2*weight; Express costs 12 + 4*weight; Pickup costs 0. Implement calculate_shipping(requests) to process (mode, weight) pairs by creating the appropriate subclass and calling its cost method.

**Input/output specification:** Input: requests: list[tuple[str, int]] with mode Standard/Express/Pickup. Output: list[int] shipping charges.

**Constraints:** 0 <= number of requests <= 1000; 0 <= weight <= 1000; each mode is one of the three named options.

- **Example 1:** Input `[("Standard", 3), ("Express", 2), ("Pickup", 9)]` → Output `[11, 20, 0]`
- **Example 2:** Input `[ ("Standard", 0) ]` → Output `[5]`
- **Example 3:** Input `[]` → Output `[]`

**AI Tutor:** Before writing code, explain your proposed algorithm and name the lecture concept you are transferring.

### 2. My Initial Approach — Before AI Help

**Student (initial approach):** I will put all three shipping formulas in one giant if/elif statement inside the main loop.

**Student (lecture concept I intended to apply):** Subclassing, overriding methods and runtime polymorphism.

### 3. AI Tutor Help

**Did I ask AI Tutor for help?** ☑ Yes — one example hint; ☐ No.

**AI Tutor (does not provide the code):** Can the client call one method without knowing which concrete shipping mode it has?

**Student:** That could compute outputs but would not practice the requested inheritance and polymorphic common interface.

**AI Tutor (follow-up question):** Can the client use the same method call for all three modes without embedding every formula inside the loop?

**Student — What the hint helped me realize:** I understand child classes can override methods incorrectly and still run without a syntax error.

### 4. My Revision

**Did I change my approach or code?** ☑ Yes (demonstration); ☐ No.

**Student (revised algorithm):** Define one abstract-like parent interface and separate subclasses for each shipping rule; dispatch to an object then use the same cost method.

**Student (what changed and why):** Move price formulas into overridden methods, leaving the processing loop independent of the concrete rule.

**AI Tutor:** Your reasoning now addresses the key issue. Write and run the code yourself, then verify it using examples and edge cases. The completed worked-example solution is saved separately as [`week_05.py`](./week_05.py).

### 5. Verification — actual executable Python

**My final program:** [`week_05.py`](./week_05.py) (function `calculate_shipping`)

**Run it from this folder:**

```bash
python week_05.py
```

**Actual automated check:** `Week 05: PASS (3 test cases)`

- ☑ Passed the provided examples
- ☑ Passed additional edge cases
- ☐ Still has unresolved problems in the tested cases

**One edge case considered:** Pickup always costs zero, even when the weight is large.

- **Input arguments:** `([],)`
- **Expected output:** `[]`
- **Actual output:** `[]`

**Verification detail:** Also tested that different subclasses are invoked through the same `cost` interface.

**AI Tutor:** Why is the revised solution correct? What are its time and auxiliary-space complexities?

**Student — Correctness argument:** Every request selects its specified subclass, and the corresponding overridden cost method implements exactly the stated formula.

**Student — Complexity:** Time O(n) for n requests; extra space O(n) for the returned charges.

### 6. One-Minute Reflection

**Student — Idea transferred from the OCW lecture:** I transferred inheritance and polymorphic method dispatch into shipping-price rules.

**Student — One thing I understand better now:** I understand child classes can override methods incorrectly and still run without a syntax error.

**Student — One thing I am still unsure about:** How to detect violations of the Liskov Substitution Principle in larger programs.

**AI Tutor — Closing feedback:** You completed the conceptual check, revised one mistaken explanation with a hint, challenged an imprecise question, and applied the same lecture idea to a new problem. Review the remaining uncertainty before the next topic.

---

## Sources and academic-integrity note

- Class topic, date and lab: user-provided NYCU 115-1 AOOP syllabus (`1151_515106syllabus.docx`).
- MIT OCW lecture reference: [MIT 6.0001 Lecture 9](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/lec9_inheritance/).
- Assignment record template: [AI Tutor for AOOP 2026](https://github.com/ARG-NCTU/oop-python-nycu/blob/main/ai-tutor-2026.md).
- The questions, learner responses, challenges, program, and explanations are AI-generated model content, not quotations of MIT source code or verified firsthand student work. Do not present the simulated dialogue as an actual independent student session.
