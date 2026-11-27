**Name:** 廖顯祐  
**Date:** 2026/11/26  
**Topic:** Python Classes and Inheritance

### 1. Today’s Challenge

**Core concept from today’s OCW lecture:**

Class inheritance, method overriding, class variables, constructor initialization, and code reusability.

**AI-generated coding challenge title:**

Smart Delivery Management System

### 2. My Initial Approach — Before AI Help

**My approach:**

I planned to create a base class that manages common delivery attributes and methods, then implement subclasses with different shipping cost calculations. I used a shared class variable to assign unique delivery IDs and implemented special methods to combine and compare delivery objects.

### 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

☐ No — I solved it independently  
☑ Yes — I received one or more hints

**The most useful hint/question from AI was:**

Can the repeated compatibility checks in the delivery combination methods be extracted into a shared method in the parent class?

**It helped me realize that:**

Inheritance is not only useful for organizing related classes but also for reducing duplicated code and improving maintainability.

### 4. My Revision

**Did you change your approach or code after interacting with AI?**

☑ No — Revision pending  
☐ Yes

**What did you change, and why?**

I identified two necessary improvements: making `ExpressDelivery` inherit from `StandardDelivery` to satisfy the required class hierarchy and extracting repeated compatibility checks into a shared parent-class method. These revisions have not yet been implemented.

### 5. Verification

**My final program:**

☑ Passed the provided examples  
☐ Passed all additional edge cases  
☑ Still has unresolved problems

**One edge case I tested through manual tracing:**

Input: Create an `ExpressDelivery` object `e` and evaluate `isinstance(e, StandardDelivery)`.

Expected output: `True`

Actual output: `False`

### 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**

I applied inheritance, method overriding, shared class variables, and `super()` to manage different delivery types while reusing common functionality.

**One thing I understand better now:**

I better understand how inheritance hierarchies affect object relationships and method resolution, as well as how shared class variables maintain consistent information across different subclasses.

**One thing I am still unsure about:**

I am still unsure how to design inheritance hierarchies that maximize code reusability without creating unnecessary dependencies between subclasses.