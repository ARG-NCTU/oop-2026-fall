**Name:** 廖顯祐  
**Date:** 2026/11/25  
**Topic:** Object-Oriented Programming

### 1. Today’s Challenge

**Core concept from today’s OCW lecture:**

Object-oriented programming, data abstraction, instance attributes, and operator overloading.

**AI-generated coding challenge title:**

Smart Shopping Cart

### 2. My Initial Approach — Before AI Help

**My approach:**

I planned to use a dictionary to store product names, prices, and quantities within each shopping cart. I designed methods to manage the cart's contents and implemented special methods for addition, equality comparison, length calculation, and string representation. To maintain object independence, I planned to create a new object when combining two shopping carts.

### 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

☑ No — I solved it independently  
☐ Yes — I received one or more hints

**The most useful hint/question from AI was:**

What would happen if a negative quantity were passed to the `remove_item` method?

**It helped me realize that:**

Even when a program satisfies the specified input constraints, additional input validation may be necessary to prevent unexpected behavior in real-world applications.

### 4. My Revision

**Did you change your approach or code after interacting with AI?**

☑ No  
☐ Yes

**What did you change, and why?**

No code changes were necessary because my original implementation satisfied the problem requirements. However, I recognized the importance of defensive programming and validating inputs beyond the given constraints.

### 5. Verification

**My final program:**

☑ Passed the provided examples  
☑ Passed additional edge cases  
☐ Still has unresolved problems

**One edge case I tested through manual tracing:**

Input: Cart A contains 2 apples at $20 each. Create Cart B by combining Cart A with itself.

Expected output: Cart B contains 4 apples with a total cost of $80, while Cart A remains unchanged.

Actual output (manual tracing): Cart B contains 4 apples with a total cost of $80, and Cart A still contains 2 apples.

### 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**

I applied data abstraction, independent instance attributes, and special methods to create a shopping cart class that encapsulates its data and supports interactions between objects.

**One thing I understand better now:**

I better understand how operator overloading allows custom objects to support standard Python operators and how creating new objects prevents unintended modifications to existing instances.

**One thing I am still unsure about:**

I am still unsure how to balance data encapsulation, input validation, and computational efficiency when designing more complex classes for real-world applications.