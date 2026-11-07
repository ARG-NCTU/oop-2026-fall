**Topic:** Understanding Program Efficiency — Big O Notation and Time Complexity  
**Date:** November 7, 2026

### ① Check My Understanding

**Questions completed:** 5 / 5

**Answers revised after AI hints:** 1 / 5

### ② My Misconception

**Before: I thought…**

I thought that \(\log n\) grows faster than \(n^{0.5}\). I was confused about how logarithmic and polynomial functions behave when the input size becomes very large.

---

**Now: I understand…**

I understand that any positive polynomial power of \(n\) eventually grows faster than a logarithmic function. For example, \(n\log n\) grows more slowly than \(n^{1.5}\) as \(n\) approaches infinity. Big O notation focuses on long-term growth rates rather than actual execution time for small inputs.

---

### ③ Challenge the AI

**One AI-generated question I challenged:**

Question 1: Since Algorithm A is \(O(n)\) and Algorithm B is \(O(n^2)\), Algorithm A will always run faster than Algorithm B, regardless of input size.

**Why?**

☐ Ambiguous  
☑ Oversimplified  
☐ Technically questionable  
☑ Too easy  
☐ Other: __________

**Brief explanation:**

The word "always" makes the statement too easy to reject. Although \(O(n)\) has a better growth rate than \(O(n^2)\), constant factors can make the quadratic algorithm faster for small inputs. A more challenging question could ask us to find the input size at which one algorithm becomes more efficient than the other.

---

### ④ One-Minute Reflection

**One thing I am still unsure about:**

I am still unsure how to analyze the time complexity of more complicated nested loops, especially when the inner loop depends on the outer loop variable or when the algorithm contains multiple conditions and early termination. I want to practice determining the worst-case complexity without simply multiplying the number of loops.

---