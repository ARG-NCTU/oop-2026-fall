# AI Tutor Learning Reflection

**Name:** 朱昱瑋  
**Date:** 2026-10-15  
**Topic:** Recursion (Base Case, Recursive Case, Problem Reduction)

---

## 1. Today’s Challenge

**Core concept from today’s OCW lecture:**

Recursion, Base Case, Recursive Case, and reducing a problem into a smaller version of the same problem.

---

**AI-generated coding challenge title:**

Nested Digit Sum

---

## 2. My Initial Approach — Before AI Help

**Before asking AI for hints, briefly describe how you planned to solve the problem.**

**My approach:**

- Traverse the string and add all digits together.
- If the sum is greater than 9, convert it into a string and call the function recursively.
- If the sum is a single digit, return it.

---

## 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

☐ No — I solved it independently  
☑ Yes — I received one or more hints

**The most useful hint/question from AI was:**

What would happen if `if total > 9` were changed to `if total >= 9`?

**It helped me realize that:**

Having a Base Case is not enough. Every recursive call must move closer to the Base Case. Otherwise, the function may recurse forever.

---

## 4. My Revision

**Did you change your approach or code after interacting with AI?**

☐ No  
☑ Yes

**What did you change, and why?**

I re-examined the termination condition and confirmed why `total > 9` is necessary. If `>= 9` is used, input `9` repeatedly calls the function with exactly the same value and causes infinite recursion.

---

## 5. Verification

**My final program:**

☑ Passed the provided examples  
☑ Passed additional edge cases  
☐ Still has unresolved problems

**One edge case I tested:**

Input: `0000`

Expected output: `0`

Actual output: `0`

---

## 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**

Using recursion to repeatedly reduce a problem into a smaller version of itself until a Base Case is reached.

**One thing I understand better now:**

A recursive function needs both:

- A Base Case
- A guarantee that each recursive call gets closer to that Base Case

Otherwise the recursion may never terminate.

**One thing I am still unsure about:**

The impact of recursion depth and the performance differences between linear recursion and tree recursion, especially why memoization can dramatically improve efficiency.

---

## Additional Reflection from Discussion

### Why my solution works

Each recursive call replaces the original string with the sum of its digits. This new value is much smaller than the original problem and eventually becomes a single digit, triggering the Base Case.

### Time Complexity

**O(n)**

The first pass processes all n characters. Subsequent recursive calls only process a very small number of digits, so the overall complexity remains O(n).

### Which lecture example is most similar?

**Palindrome**

Because each call generates only one smaller recursive call, creating a linear recursion chain rather than a recursion tree like Fibonacci.
