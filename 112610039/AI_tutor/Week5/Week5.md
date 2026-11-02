# AI Tutor for AOOP 2026 - Week 5 Learning Record

## Part A: True or False

**Topic:** Python Classes & Inheritance (Lecture 9)[cite: 136]  
**Date:** 2026-10-24

### ① Check My Understanding
* **Questions completed:** 5 / 5
* **Answers revised after AI hints:** 0 / 5 (Answered all 5 correctly on the first attempt!)

### ② My Misconception
* **Before:** I understood basic inheritance, but I used to think Python automatically invoked a superclass's `__init__` even when a subclass defined its own constructor[cite: 152, 154].
* **Now:** I understand that defining `__init__` in a subclass overrides the superclass constructor, so parent initialization must be explicitly called (e.g., `BankAccount.__init__(self, ...)` )[cite: 154, 155]. I also learned how method lookup resolves from bottom-to-top in class hierarchies[cite: 153], and how class variables are shared across all class instances[cite: 156].

### ③ Challenge the AI
* **One AI-generated question I challenged:** Question 5[cite: 159]
* **Why?**
  - [ ] Ambiguous
  - [ ] Oversimplified
  - [x] Technically questionable
  - [ ] Too easy
  - [ ] Other: __________________
* **Brief explanation:** Comparing nested attributes like `self.parent1 == other.parent1` directly in `__eq__` causes infinite recursive calls and raises an `AttributeError` when encountering `None`[cite: 159]. It is essential to compare unique IDs or explicitly filter out `None` values[cite: 156, 159].

### ④ One-Minute Reflection
* **One thing I am still unsure about:** How multiple inheritance and Python's Method Resolution Order (MRO / `super()`) work when classes form complex diamond inheritance structures.

---

## Part B: LeetCode-style Lecture Code Transfer

**Name:** 112610039
**Date:** 2026-10-24  
**Topic:** Class Inheritance, Method Overriding & Class Variables[cite: 136, 150, 152, 156]

### 1. Today’s Challenge
* **Core concept from today’s OCW lecture:** Building subclass hierarchies with `class Subclass(Superclass)`[cite: 150], utilizing class variables for global instance counting[cite: 156], and extending or overriding methods while encapsulating state[cite: 144, 152].
* **AI-generated coding challenge title:** Bank Account Hierarchy (`BankAccount` & `SavingsAccount`)

### 2. My Initial Approach — Before AI Help
* **My approach:** Created `BankAccount` with class variable `account_counter = 1000` to auto-assign IDs[cite: 156]. Subclassed `SavingsAccount(BankAccount)`, called `BankAccount.__init__(self, owner, balance)`[cite: 154, 155], and overrode `__str__`[cite: 152]. In `apply_interest`, I called `self.deposit(self, interest)`.

### 3. AI Tutor Help
* **Did you ask the AI Tutor for help?**
  - [ ] No — I solved it independently
  - [x] Yes — I received one or more hints
* **The most useful hint/question from AI was:** Pointing out that calling `self.deposit(self, interest)` passes `self` twice because dot notation automatically binds the instance as the first parameter[cite: 104, 107, 128, 152].
* **It helped me realize that:** Instance method calls on `self` should be `self.deposit(interest)` without explicitly passing `self` again[cite: 107, 128, 152].

### 4. My Revision
* **Did you change your approach or code after interacting with AI?**
  - [ ] No
  - [x] Yes
* **What did you change, and why?** Fixed `self.deposit(interest)` in `apply_interest`[cite: 128, 152], and added missing curly braces around `{self.owner}` in `BankAccount.__str__`.

### 5. Verification
* **My final program:**
  - [x] Passed the provided examples
  - [x] Passed additional edge cases
  - [ ] Still has unresolved problems
* **One edge case I tested:**
  - **Input:** `acc = SavingsAccount("Bob", 500.0, 0.05); acc.apply_interest()`
  - **Expected output:** Balance updated to `525.0`
  - **Actual output:** Balance updated to `525.0`

### 6. One-Minute Reflection
* **What idea from the OCW lecture did you transfer to this new problem?** Reusing parent methods (`deposit`) within child class logic (`apply_interest`) to avoid code duplication and maintain data invariants[cite: 144, 152].
* **One thing I understand better now:** How subclassing enables code reuse and structural specialization without breaking existing class interfaces[cite: 150, 152].
* **One thing I am still unsure about:** When it is preferred to use `super().__init__()` over explicit parent class calls like `BankAccount.__init__(self, ...)`.