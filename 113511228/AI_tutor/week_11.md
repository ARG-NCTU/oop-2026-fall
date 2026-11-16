# AI Tutor Learning Record — Week 11

**Course:** Advanced Object-Oriented Programming (AOOP, NYCU, 115-1)  
**Topic:** Graph-theoretic Models  
**Scheduled date:** 2026-11-16  
**OCW reference:** [MIT 6.0002 Lecture 3](https://ocw.mit.edu/courses/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/resources/lecturegraphspy/)  
**Course lab / note:** Lab 09: Midterm Question Bank Introduction; Project Proposal Due  
**Python solution:** [`week_11.py`](./week_11.py)

> **Disclosure:** This is an **AI-generated demonstration of a complete tutor session**. The "Student" replies, revisions, challenges, and reflections were generated as examples; they are **not** a transcript of the student’s actual answers or AI interactions. The `.py` file is real, importable Python code and its test results were executed.

## Learning focus

- **Lecture idea:** Graph representations, vertices/edges and breadth-first search for unweighted shortest paths.
- **Transfer task:** Minimum Transfers Between Campus Buildings.
- **Tutor strategy:** One True/False question at a time; provide a hint before correction if the demonstration learner answers incorrectly; then raise the reasoning difficulty.

---

## Part A — True or False
### AI Tutor Learning Cycle (ATLC): one question at a time

**AI Tutor:** I will ask five conceptual True/False questions. I will check your reasoning and give a hint before disclosing an answer if needed.

#### Question 1/5 — Foundational

**AI Tutor:** A graph can represent relationships between objects using vertices and edges. **True or False? Explain briefly.**

**Student:** True.

**AI Tutor (feedback):** Correct. **Answer: True.** Vertices represent entities; edges encode connections.

**AI Tutor (adaptive follow-up):** You handled the foundation, so I will add a less obvious condition in the next question.

#### Question 2/5 — Foundational

**AI Tutor:** An unweighted graph’s shortest path by edge count can be found with BFS. **True or False? Explain briefly.**

**Student:** True.

**AI Tutor (feedback):** Correct. **Answer: True.** BFS visits reachable vertices in nondecreasing distance from the start.

#### Question 3/5 — Application

**AI Tutor:** BFS always finds the least total-weight path in a graph with arbitrary positive edge weights. **True or False? Explain briefly.**

**Student (initial):** True — BFS always finds a shortest path, so positive edge weights should not matter.

**AI Tutor (hint — no answer yet):** If one edge costs 100 but two other edges cost 1 each, which route has fewer edges and which has less cost?

**Student (revised answer):** False. BFS minimizes the number of edges when edge costs are equal; arbitrary weights need a weighted-path method.

**AI Tutor (feedback):** Correct after revision. **Answer: False.** BFS minimizes edge count, not general weighted cost; weighted methods are needed. This is the main misconception to watch for.

**AI Tutor (adaptive follow-up):** Good correction. The next question will test whether you can apply the distinction rather than repeat the rule.

#### Question 4/5 — Application

**AI Tutor:** A visited set can prevent a graph traversal from looping forever around cycles. **True or False? Explain briefly.**

**Student:** True.

**AI Tutor (feedback):** Correct. **Answer: True.** Repeated vertices need not be enqueued again.

#### Question 5/5 — Challenge

**AI Tutor:** In a disconnected graph, every vertex must be reachable from any starting vertex. **True or False? Explain briefly.**

**Student:** False.

**AI Tutor (feedback):** Correct. **Answer: False.** Disconnected components contain vertices with no path between them.

### ① Check My Understanding — completed record

| Field | Completed result |
|---|---|
| Questions completed | **5 / 5** |
| Answers revised after AI hints | **1 / 5** (illustrative simulation) |
| Final answers after discussion | **5 / 5 correct** (illustrative simulation) |

### ② My Misconception

**AI Tutor:** What misconception did you correct?

**Student — Before: I thought…** I assumed any shortest-path problem could be solved using BFS.

**Student — Now: I understand…** I can distinguish unweighted shortest paths from weighted shortest paths. A path objective must be defined before choosing a graph algorithm.

### ③ Challenge the AI

**AI Tutor:** Choose one question that was ambiguous, misleading, oversimplified, technically questionable, or too easy. Explain why.

**Student:** I challenge **Q3**: “BFS always finds the least total-weight path in a graph with arbitrary positive edge weights.”

- **Reason category:** Technically questionable
- **My explanation:** “Shortest” needs an objective: BFS optimizes number of edges when all edge costs are equal, not arbitrary weighted distance.

**AI Tutor (responds to challenge):** That is a fair critique. A more precise version would be:

> Does BFS minimize edge count on an unweighted graph, while weighted minimum-cost paths require different assumptions?

**Student:** The revised wording makes the scope and assumption clearer.

### ④ One-Minute Reflection

**AI Tutor:** What do you understand better, and what remains uncertain?

**Student — One thing I understand better:** I can distinguish unweighted shortest paths from weighted shortest paths.

**Student — One thing I am still unsure about:** When to prefer Dijkstra over Bellman–Ford for weighted graphs.

---

## Part B — LeetCode-style Lecture Code Transfer

### 1. Today’s Challenge (shown before the solution)

**Name:** Student — model-answer demonstration  
**Date:** 2026-11-16  
**Topic:** Graph-theoretic Models

**Core concept from today’s OCW lecture:** Graph representations, vertices/edges and breadth-first search for unweighted shortest paths.

**AI Tutor — Challenge title:** **Minimum Transfers Between Campus Buildings**

**Problem statement:** There are n buildings numbered 0 to n-1. Each undirected walkway joins two buildings and counts as one transfer. Return the minimum number of walkways required to travel from start to goal, or -1 if unreachable.

**Input/output specification:** Input: n: int; edges: list[tuple[int, int]]; start: int; goal: int. Output: int minimum number of edges or -1.

**Constraints:** 1 <= n <= 100000; 0 <= number of edges <= 200000; 0 <= building labels < n; graph may have cycles or disconnected components.

- **Example 1:** Input `(5, [(0, 1), (1, 2), (0, 3), (3, 2)], 0, 2)` → Output `2`
- **Example 2:** Input `(4, [(0, 1), (2, 3)], 0, 3)` → Output `-1`
- **Example 3:** Input `(3, [], 2, 2)` → Output `0`

**AI Tutor:** Before writing code, explain your proposed algorithm and name the lecture concept you are transferring.

### 2. My Initial Approach — Before AI Help

**Student (initial approach):** I will use depth-first search and return as soon as I encounter the destination.

**Student (lecture concept I intended to apply):** Graph representations, vertices/edges and breadth-first search for unweighted shortest paths.

### 3. AI Tutor Help

**Did I ask AI Tutor for help?** ☑ Yes — one example hint; ☐ No.

**AI Tutor (does not provide the code):** Which traversal visits nodes in increasing number of steps from the start?

**Student:** DFS reaches a destination, but the first found route may not have the fewest edges.

**AI Tutor (follow-up question):** If you use a stack rather than a queue, will you necessarily visit vertices by increasing number of edges?

**Student — What the hint helped me realize:** I can distinguish unweighted shortest paths from weighted shortest paths.

### 4. My Revision

**Did I change my approach or code?** ☑ Yes (demonstration); ☐ No.

**Student (revised algorithm):** Build adjacency lists and run BFS using a queue. Assign each newly discovered building distance +1 from the current building.

**Student (what changed and why):** Use collections.deque and mark neighbors visited when enqueued to preserve BFS layers and avoid repeats.

**AI Tutor:** Your reasoning now addresses the key issue. Write and run the code yourself, then verify it using examples and edge cases. The completed worked-example solution is saved separately as [`week_11.py`](./week_11.py).

### 5. Verification — actual executable Python

**My final program:** [`week_11.py`](./week_11.py) (function `min_transfers`)

**Run it from this folder:**

```bash
python week_11.py
```

**Actual automated check:** `Week 11: PASS (5 test cases)`

- ☑ Passed the provided examples
- ☑ Passed additional edge cases
- ☐ Still has unresolved problems in the tested cases

**One edge case considered:** When start and goal are identical, the answer must be zero; unreachable nodes return -1.

- **Input arguments:** `(4, [(0, 1), (1, 2), (2, 3), (0, 3)], 0, 3)`
- **Expected output:** `1`
- **Actual output:** `1`

**Verification detail:** Also tested unreachable targets, cycles, and start equal to goal.

**AI Tutor:** Why is the revised solution correct? What are its time and auxiliary-space complexities?

**Student — Correctness argument:** BFS processes vertices by nondecreasing edge count, so the first recorded distance to a vertex is minimal.

**Student — Complexity:** Time O(V+E) to build and traverse the graph; space O(V+E) for adjacency lists, distances and the queue.

### 6. One-Minute Reflection

**Student — Idea transferred from the OCW lecture:** I used the graph model and breadth-first traversal to solve a minimum-transfer navigation problem.

**Student — One thing I understand better now:** I can distinguish unweighted shortest paths from weighted shortest paths.

**Student — One thing I am still unsure about:** When to prefer Dijkstra over Bellman–Ford for weighted graphs.

**AI Tutor — Closing feedback:** You completed the conceptual check, revised one mistaken explanation with a hint, challenged an imprecise question, and applied the same lecture idea to a new problem. Review the remaining uncertainty before the next topic.

---

## Sources and academic-integrity note

- Class topic, date and lab: user-provided NYCU 115-1 AOOP syllabus (`1151_515106syllabus.docx`).
- MIT OCW lecture reference: [MIT 6.0002 Lecture 3](https://ocw.mit.edu/courses/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/resources/lecturegraphspy/).
- Assignment record template: [AI Tutor for AOOP 2026](https://github.com/ARG-NCTU/oop-python-nycu/blob/main/ai-tutor-2026.md).
- The questions, learner responses, challenges, program, and explanations are AI-generated model content, not quotations of MIT source code or verified firsthand student work. Do not present the simulated dialogue as an actual independent student session.
