# Topic: Lec_7 Testing, Debugging, Exceptions, Assertions
Date: 2026-10-16

## ① Check My Understanding

Questions completed: 5 / 5

Answers revised after AI hints: 2 / 5

---

## ② My Misconception

### Before: I thought…

I thought Black Box Testing was sufficient to complete testing.

---

### Now: I understand…

Black Box Testing and Glass Box Testing serve different purposes.

- Black Box Testing focuses on specifications, inputs, outputs, and boundary cases.
- Glass Box Testing focuses on internal branches and execution paths.
- Passing all branches does not guarantee that all boundary conditions have been tested.
- The two approaches complement each other rather than replace one another.

---

## ③ Challenge the AI

### One AI-generated question I challenged:

Question 1 (`except: pass`)

---

### Why?

☐ Ambiguous

☐ Oversimplified

☑ Technically questionable

☐ Too easy

☐ Other: __________

### Brief explanation:

The scenario felt somewhat unrealistic because developers generally should not intentionally swallow all exceptions with `except: pass`.

However, I later learned that such code does appear in practice and can make debugging significantly harder because it hides important error information.

---

## ④ One-Minute Reflection

### One thing I am still unsure about:

The exact distinction between `assert` and `raise`.

Current understanding:

- Both can stop execution early by triggering an exception.
- `assert` is used to verify assumptions that the programmer believes must always be true.
- `raise` is used to actively report invalid states, violated specifications, or illegal inputs.

My remaining question:

When designing a function, how do I decide whether a particular condition should be handled with `assert` versus `raise`?
