# MIT 6.0001 Lecture 10 Reflection Note

**Topic:** Lecture 10: Algorithmic Complexity & Big O Notation  
**Date:** 2026-11-09  

---

## Part I: Conceptual Check & Reflection

### ① Check My Understanding

* **Questions completed:** 5 / 5
* **Answers revised after AI hints:** 1 / 5

---

### ② My Misconception

* **Before:** I thought an algorithm with $O(N^2)$ worst-case time complexity would *always* take more execution time than an algorithm with $O(N)$ for *any* input size $N$.
* **Now:** I understand that Big O describes asymptotic growth when $N$ becomes extremely large, ignoring constant factors ($c$) and lower-order terms. For small input sizes $N$, an $O(N^2)$ algorithm can actually run faster than an $O(N)$ algorithm if the $O(N)$ algorithm has a very large constant multiplier.

---

### ③ Challenge the AI

* **One AI-generated question I challenged:** Question 1 (Constant factors and asymptotic behavior)
* **Why?**
  - [x] Other: Self-correction / Clarification on asymptotic assumptions
* **Brief explanation:** The question highlights a common misconception about Big O notation. I initially overlooked how constant multipliers ($c \cdot N$) affect performance when $N$ is small before reaching the asymptotic threshold.

---

### ④ One-Minute Reflection

* **One thing I am still unsure about:**  
  How to effectively utilize space-time trade-offs (e.g., Python `set` / Hash Tables) to optimize $O(N^2)$ brute-force solutions down to $O(N)$ time complexity, and how to evaluate the extra memory costs involved.

---

## Part II: Coding Challenge Reflection

**Name:** Student  
**Date:** 2026-11-09  
**Topic:** Lecture 10 Practice — Algorithmic Complexity & Two Sum  

---

### 1. Today’s Challenge

* **Core concept from today’s OCW lecture:**  
  Analyzing nested loop time complexity using the Law of Multiplication ($O(N) \times O(N) = O(N^2)$) and worst-case performance analysis.
* **AI-generated coding challenge title:**  
  Two Sum & Complexity Analysis (`has_pair_with_sum`)

---

### 2. My Initial Approach — Before AI Help

Before asking AI for hints, briefly describe how you planned to solve the problem.

* **My approach:**  
  I used a nested loop iterating over values directly to check every pair:
  ```python
  def has_pair_with_sum(L, target):
      for i in L:
          for j in L:
              if i + j == target and i != j:
                  return True
      return False
  ```
  I correctly analyzed the worst-case time complexity as $O(N^2)$ because both loops scan the list of size $N$.

---

### 3. AI Tutor Help

* **Did you ask the AI Tutor for help?**
  - [ ] No — I solved it independently
  - [x] Yes — I received one or more hints

* **The most useful hint/question from AI was:**  
  Pointing out that comparing element values (`i != j`) fails when identical numbers exist at different positions in the list (e.g., `L = [5, 5]` and `target = 10`), and demonstrating an $O(N)$ approach using a Hash Set lookup.

* **It helped me realize that:**  
  Iterating over values instead of list indices makes it impossible to distinguish duplicate values at different memory positions.

---

### 4. My Revision

* **Did you change your approach or code after interacting with AI?**
  - [ ] No
  - [x] Yes

* **What did you change, and why?**  
  I learned to use index-based loops `range(len(L))` to avoid self-pairing while correctly handling duplicate numbers. Additionally, I learned the $O(N)$ Set-based complement lookup technique, which trades $O(N)$ memory space for $O(N)$ time efficiency.

---

### 5. Verification

* **My final program:**
  - [x] Passed the provided examples
  - [x] Passed additional edge cases
  - [ ] Still has unresolved problems

* **One edge case I tested:**
  - **Input:** `L = [5, 5]`, `target = 10`
  - **Expected output:** `True`
  - **Actual output:** `True`

---

### 6. One-Minute Reflection

* **What idea from the OCW lecture did you transfer to this new problem?**  
  The Law of Multiplication ($O(N) \times O(N) = O(N^2)$) for nested loops, worst-case input evaluation, and the concept of Space-Time Trade-offs.

* **One thing I understand better now:**  
  How nested loops produce quadratic complexity $O(N^2)$ and why indexing is critical for element tracking in Python lists.

* **One thing I am still unsure about:**  
  How Python's `set` achieves average $O(1)$ lookup time under the hood (Hash Table mechanism) and when the memory trade-off becomes non-ideal.