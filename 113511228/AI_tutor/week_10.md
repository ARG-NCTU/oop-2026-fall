# AI Tutor Learning Record — Week 10

**Course:** Advanced Object-Oriented Programming (AOOP, NYCU, 115-1)  
**Topic:** Optimization Problems  
**Scheduled date:** 2026-11-09  
**OCW reference:** [MIT 6.0002 Lecture 2](https://ocw.mit.edu/courses/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/pages/lecture-slides-and-files/)  
**Course lab / note:** Lab 08: LeetCode  
**Python solution:** [`week_10.py`](./week_10.py)

> **Disclosure:** This is an **AI-generated demonstration of a complete tutor session**. The "Student" replies, revisions, challenges, and reflections were generated as examples; they are **not** a transcript of the student’s actual answers or AI interactions. The `.py` file is real, importable Python code and its test results were executed.

## Learning focus

- **Lecture idea:** Optimal substructure and dynamic programming for 0/1 selection.
- **Transfer task:** Maximum Workshop Satisfaction.
- **Tutor strategy:** One True/False question at a time; provide a hint before correction if the demonstration learner answers incorrectly; then raise the reasoning difficulty.

---

## Part A — True or False
### AI Tutor Learning Cycle (ATLC): one question at a time

**AI Tutor:** I will ask five conceptual True/False questions. I will check your reasoning and give a hint before disclosing an answer if needed.

#### Question 1/5 — Foundational

**AI Tutor:** Dynamic programming is useful when a problem contains repeated overlapping subproblems. **True or False? Explain briefly.**

**Student:** True.

**AI Tutor (feedback):** Correct. **Answer: True.** Results can be reused instead of recomputed many times.

**AI Tutor (adaptive follow-up):** You handled the foundation, so I will add a less obvious condition in the next question.

#### Question 2/5 — Foundational

**AI Tutor:** A 0/1 knapsack item may be selected any number of times. **True or False? Explain briefly.**

**Student:** False.

**AI Tutor (feedback):** Correct. **Answer: False.** Each item is either taken once or not taken.

#### Question 3/5 — Application

**AI Tutor:** A one-dimensional 0/1 knapsack update usually iterates capacities downward. **True or False? Explain briefly.**

**Student (initial):** False — whether capacity is updated from low to high or high to low should not matter.

**AI Tutor (hint — no answer yet):** If there is one item of duration 1 and value 5, could an ascending update incorrectly use it twice at budget 2?

**Student (revised answer):** True. Descending capacities prevent a just-updated value from allowing reuse of the same 0/1 item.

**AI Tutor (feedback):** Correct after revision. **Answer: True.** Descending updates stop the current item from being reused in the same iteration. This is the main misconception to watch for.

**AI Tutor (adaptive follow-up):** Good correction. The next question will test whether you can apply the distinction rather than repeat the rule.

#### Question 4/5 — Application

**AI Tutor:** Memoization can reduce repeated recursion work by caching states. **True or False? Explain briefly.**

**Student:** True.

**AI Tutor (feedback):** Correct. **Answer: True.** A repeated state can return its stored answer.

#### Question 5/5 — Challenge

**AI Tutor:** An optimization algorithm is correct whenever its first solution is feasible. **True or False? Explain briefly.**

**Student:** False.

**AI Tutor (feedback):** Correct. **Answer: False.** Optimality requires comparison or a proof that no better feasible solution exists.

### ① Check My Understanding — completed record

| Field | Completed result |
|---|---|
| Questions completed | **5 / 5** |
| Answers revised after AI hints | **1 / 5** (illustrative simulation) |
| Final answers after discussion | **5 / 5 correct** (illustrative simulation) |

### ② My Misconception

**AI Tutor:** What misconception did you correct?

**Student — Before: I thought…** I thought DP updates could run in either direction with no difference.

**Student — Now: I understand…** I understand update order controls whether an item can be reused. The iteration order is part of the algorithmic invariant in one-dimensional 0/1 knapsack DP.

### ③ Challenge the AI

**AI Tutor:** Choose one question that was ambiguous, misleading, oversimplified, technically questionable, or too easy. Explain why.

**Student:** I challenge **Q3**: “A one-dimensional 0/1 knapsack update usually iterates capacities downward.”

- **Reason category:** Technically questionable
- **My explanation:** Descending capacity order is crucial in the shown one-array 0/1 DP; an ascending update could accidentally permit reuse.

**AI Tutor (responds to challenge):** That is a fair critique. A more precise version would be:

> In a one-array implementation of 0/1 knapsack, why do we normally process capacity from high to low?

**Student:** The revised wording makes the scope and assumption clearer.

### ④ One-Minute Reflection

**AI Tutor:** What do you understand better, and what remains uncertain?

**Student — One thing I understand better:** I understand update order controls whether an item can be reused.

**Student — One thing I am still unsure about:** How to reconstruct the chosen items as well as the optimum value.

---

## Part B — LeetCode-style Lecture Code Transfer

### 1. Today’s Challenge (shown before the solution)

**Name:** Student — model-answer demonstration  
**Date:** 2026-11-09  
**Topic:** Optimization Problems

**Core concept from today’s OCW lecture:** Optimal substructure and dynamic programming for 0/1 selection.

**AI Tutor — Challenge title:** **Maximum Workshop Satisfaction**

**Problem statement:** Choose workshops to maximize total satisfaction within a limited time budget. Each workshop has a positive duration and a satisfaction value; it can be attended at most once. Return the maximum possible total satisfaction.

**Input/output specification:** Input: durations: list[int], values: list[int], budget: int. Output: int maximum satisfaction.

**Constraints:** 0 <= n <= 100; 1 <= duration <= 100; 0 <= value <= 1000; 0 <= budget <= 1000; durations and values have equal length.

- **Example 1:** Input `([2, 3, 4], [4, 5, 10], 5)` → Output `10`
- **Example 2:** Input `([1, 2, 3], [5, 6, 8], 3)` → Output `11`
- **Example 3:** Input `([], [], 7)` → Output `0`

**AI Tutor:** Before writing code, explain your proposed algorithm and name the lecture concept you are transferring.

### 2. My Initial Approach — Before AI Help

**Student (initial approach):** I will update dp capacities from small to large for each workshop.

**Student (lecture concept I intended to apply):** Optimal substructure and dynamic programming for 0/1 selection.

### 3. AI Tutor Help

**Did I ask AI Tutor for help?** ☑ Yes — one example hint; ☐ No.

**AI Tutor (does not provide the code):** Can the current workshop be counted more than once if dp is updated forward?

**Student:** For a 0/1 item, ascending order can reuse a state updated by that same item, accidentally treating it as unbounded.

**AI Tutor (follow-up question):** If the capacity loop increases, could the newly updated state immediately reuse the current workshop?

**Student — What the hint helped me realize:** I understand update order controls whether an item can be reused.

### 4. My Revision

**Did I change my approach or code?** ☑ Yes (demonstration); ☐ No.

**Student (revised algorithm):** Maintain dp[b] as the best value achievable within capacity b; process each workshop once using capacities in descending order.

**Student (what changed and why):** Iterate from budget down to duration to guarantee each workshop is chosen at most once.

**AI Tutor:** Your reasoning now addresses the key issue. Write and run the code yourself, then verify it using examples and edge cases. The completed worked-example solution is saved separately as [`week_10.py`](./week_10.py).

### 5. Verification — actual executable Python

**My final program:** [`week_10.py`](./week_10.py) (function `maximize_satisfaction`)

**Run it from this folder:**

```bash
python week_10.py
```

**Actual automated check:** `Week 10: PASS (6 test cases)`

- ☑ Passed the provided examples
- ☑ Passed additional edge cases
- ☐ Still has unresolved problems in the tested cases

**One edge case considered:** A workshop longer than the entire budget cannot be chosen.

- **Input arguments:** `([1], [5], 0)`
- **Expected output:** `0`
- **Actual output:** `0`

**Verification detail:** Also tested an item that exceeds the budget and the empty-workshop case.

**AI Tutor:** Why is the revised solution correct? What are its time and auxiliary-space complexities?

**Student — Correctness argument:** For each item and capacity, the optimal answer is the better of excluding it or including it once with remaining capacity.

**Student — Complexity:** Time O(nB), extra space O(B), for n workshops and integer budget B.

### 6. One-Minute Reflection

**Student — Idea transferred from the OCW lecture:** I converted exponential subset search into DP over reusable (item, remaining capacity) states.

**Student — One thing I understand better now:** I understand update order controls whether an item can be reused.

**Student — One thing I am still unsure about:** How to reconstruct the chosen items as well as the optimum value.

**AI Tutor — Closing feedback:** You completed the conceptual check, revised one mistaken explanation with a hint, challenged an imprecise question, and applied the same lecture idea to a new problem. Review the remaining uncertainty before the next topic.

---

## Sources and academic-integrity note

- Class topic, date and lab: user-provided NYCU 115-1 AOOP syllabus (`1151_515106syllabus.docx`).
- MIT OCW lecture reference: [MIT 6.0002 Lecture 2](https://ocw.mit.edu/courses/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/pages/lecture-slides-and-files/).
- Assignment record template: [AI Tutor for AOOP 2026](https://github.com/ARG-NCTU/oop-python-nycu/blob/main/ai-tutor-2026.md).
- The questions, learner responses, challenges, program, and explanations are AI-generated model content, not quotations of MIT source code or verified firsthand student work. Do not present the simulated dialogue as an actual independent student session.
