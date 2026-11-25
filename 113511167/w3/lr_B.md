**Name:** 廖顯祐  
**Date:** 2026/11/25  
**Topic:** Testing, Debugging, Exceptions, and Assertions

### 1. Today’s Challenge

**Core concept from today’s OCW lecture:**

Exception handling, assertions, and defensive programming.

**AI-generated coding challenge title:**

Fault-Tolerant Inventory System

### 2. My Initial Approach — Before AI Help

**My approach:**

I planned to process each order sequentially, use `try-except` to handle invalid quantity conversions, and use conditional statements to validate orders before updating the inventory. I also planned to use an assertion to ensure that all stock quantities remained non-negative.

### 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

☑ No — I solved it independently  
☐ Yes — I received one or more hints

**The most useful hint/question from AI was:**

How does checking every product's stock after each order affect the overall time complexity?

**It helped me realize that:**

Although assertions help detect internal errors, repeatedly checking the entire inventory introduces additional computational costs.

### 4. My Revision

**Did you change your approach or code after interacting with AI?**

☑ No  
☐ Yes

**What did you change, and why?**

No code changes were necessary because my original implementation satisfied the problem requirements. However, I refined my complexity analysis and recognized a possible optimization that checks only the modified product.

### 5. Verification

**My final program:**

☑ Passed the provided examples  
☑ Passed additional edge cases  
☐ Still has unresolved problems

**One edge case I tested through manual tracing:**

Input: `inventory = {"apple": 2}, orders = [["apple", "2"], ["apple", "1"]]`

Expected output: `({"apple": 0}, ["SUCCESS", "INSUFFICIENT_STOCK"])`

Actual output (manual tracing): `({"apple": 0}, ["SUCCESS", "INSUFFICIENT_STOCK"])`

### 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**

I applied exception handling to recover from invalid inputs without interrupting subsequent operations and used assertions to verify internal program invariants.

**One thing I understand better now:**

I understand the difference between recoverable input errors and violations of internal program assumptions. I also learned that assertions can affect time complexity.

**One thing I am still unsure about:**

I am still unsure how to balance the thoroughness of assertion checks with computational efficiency in large-scale applications.