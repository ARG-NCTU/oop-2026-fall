# MIT 6.0001 Lecture 6 Study Reflection Log

**Name:** [Your Name]  
**Date:** 2026 / 10 / 17  
**Topic:** Recursion and Dictionaries (MIT 6.0001 Lecture 6)

---

## PART A: Conceptual Check (Check My Understanding)

### ① Check My Understanding
* **Questions completed:** 5 / 5
* **Answers revised after AI hints:** 2 / 5 (Question 2: Hashability of Tuples containing Lists; Question 5: Mutating Dictionaries during iteration)

### ② My Misconception
* **Before (I thought):**  
  I thought Tuples could always serve as dictionary keys simply because Tuples are immutable data types[cite: 29, 74]. I also thought that modifying a data structure during iteration only caused errors in ordered sequences like Lists[cite: 23].
* **Now (I understand):**  
  A Tuple containing mutable elements (like Lists) is unhashable because its content—and therefore its Hash Value—can change, causing dictionary lookup failures[cite: 74]. Furthermore, mutating *any* data structure (Lists or Dictionaries) directly during iteration breaks the iterator and triggers a runtime error[cite: 23, 79].

### ③ Challenge the AI
* **Question challenged:** Questions 1–5 overall structure.
* **Reason:**  
  * ☑ Ambiguous / Pattern-Predictable
  * ☑ Other: All answers being "False" and containing absolute phrasing (e.g., "guaranteed", "never") made the pattern too easy to guess.
* **Brief explanation:**  
  When all True/False questions evaluate to "False", it becomes too easy to guess the answers based on test-taking patterns rather than deep conceptual reasoning.

### ④ One-Minute Reflection
* **One thing I am still unsure about:**  
  How to intuitively trace deep recursion stacks without getting overwhelmed, and how Python manages call stack memory allocation when executing deep recursive functions[cite: 37, 38].

---

## PART B: Coding Challenge (Team Sales Calculator)

### 1. Today’s Challenge
* **Core concepts from OCW lecture:** Recursion, Dictionary Lookup, and Memoization[cite: 32, 70, 82].
* **AI-generated coding challenge title:** Team Sales Calculator

### 2. My Initial Approach — Before AI Help
* **My approach:**  
  I attempted to use an `elif hierarchy[employee] == []` check as the Base Case, initialize `memo[employee] = sales[employee]`, and iterate through subordinates[cite: 32, 70]. However, I tried to accumulate `memo[employee] += memo[subordinate]` before `memo[employee]` was initialized in some branches, causing `KeyError` bugs[cite: 71], and included redundant checks before recursive calls[cite: 82].

### 3. AI Tutor Help
* **Did you ask the AI Tutor for help?**  
  ☑ Yes — I received one or more hints.
* **Most useful hint/question:**  
  The AI pointed out that if `if employee in memo:` is placed at the top as a guard clause[cite: 82], the separate `elif` check for empty subordinates and the inner `if subordinate not in memo:` check become redundant because the base cases and cached values are handled naturally[cite: 32, 51, 82].
* **It helped me realize that:**  
  Recursive code can be made much cleaner by letting the base case return naturally through the loop (an empty subordinate list simply skips the `for` loop[cite: 51]) and relying on top-level guard clauses for memoization[cite: 82].

### 4. My Revision
* **What I changed:**  
  1. Moved `if employee in memo: return memo[employee]` to the very beginning of the function[cite: 82].
  2. Simplified the main body by initializing `memo[employee] = sales[employee]`[cite: 70], accumulating recursive calls directly: `memo[employee] += get_total_sales(...)`[cite: 35, 82], and removing redundant checks.

### 5. Verification
* **Passed provided examples:** ☑ Yes
* **Passed additional edge cases:** ☑ Yes
* **One edge case tested:**
  * **Input:** `employee = "Charlie"` (employee with no subordinates)[cite: 70]
  * **Expected output:** `70`[cite: 70]
  * **Actual output:** `70`[cite: 70]

### 6. One-Minute Reflection
* **Time Complexity:**
  * **Without Memoization (Worst-Case):** $O(N!)$ due to redundant re-computations of overlapping organizational subtrees[cite: 81, 83].
  * **With Memoization (Optimized):** $O(N)$ where $N$ is the total number of employees, because each employee node is visited and computed exactly once, with subsequent lookups running in $O(1)$ time[cite: 82, 83].
* **Concept Transfer:**  
  Transferred **Base Case**, **Recursive Reduction**, and **Memoization** directly from Lecture 6 into solving real-world hierarchical aggregation problems[cite: 32, 35, 82].
* **One thing I understand better now:**  
  How Memoization transforms exponential-time recursive algorithms into linear-time $O(N)$ solutions by using dictionaries as lookup caches[cite: 82, 83].