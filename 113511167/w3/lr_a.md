**Topic:** Testing, Debugging, Exceptions, and Assertions  
**Date:** 2026/11/25

### ① Check My Understanding

Questions completed: **5 / 5**

Answers revised after AI hints: **0 / 5**

### ② My Misconception

**Before: I thought…**

Handling an exception and preventing a program from crashing might be enough to ensure that the program continues correctly.

**Now: I understand…**

Exception handling does not guarantee program correctness. The program must properly recover from the error or propagate the exception if it cannot safely continue.

### ③ Challenge the AI

**One AI-generated question I challenged:**

Q4: If an exception is successfully caught and handled, and the program continues running without crashing, this guarantees that the program's subsequent results are correct.

**Why?**

☑ Ambiguous  
☐ Oversimplified  
☐ Technically questionable  
☐ Too easy  
☐ Other

**Brief explanation:**

The phrase “successfully caught and handled” is ambiguous because successful handling could imply that the error has already been properly resolved. The question should distinguish between preventing a crash and ensuring logical correctness.

### ④ One-Minute Reflection

**One thing I am still unsure about:**

I am still unsure about when to use assertions instead of explicit exceptions in real-world applications, especially when checking critical internal invariants, and when to re-raise an exception rather than handle it locally.