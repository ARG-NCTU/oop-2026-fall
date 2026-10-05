Topic: Decomposition, Abstraction, Functions, and Scope
Date: 2026/10/05

① Check My Understanding

Questions completed: 5 / 5

Answers revised after AI hints: 0 / 5

② My Misconception

Before: I thought…

I thought that printing a result inside a function was the same as returning it, so the printed value could be used directly in another calculation.
⸻
Now: I understand…

I understand that print displays information on the screen, while return sends a value back to the caller. If a function only prints its result and does not explicitly return a value, the caller receives None. I should use return when another part of the program needs the result.
⸻

③ Challenge the AI

One AI-generated question I challenged:
“A function cannot change anything outside its local scope.”
⸻
Why?
☐ Ambiguous
☑ Oversimplified
☑ Technically questionable
☐ Too easy
☐ Other: __________
Brief explanation:
The statement does not distinguish between rebinding a local name and modifying a shared object. Assigning a new value to a local parameter does not reassign the caller's variable, but a function can modify a list passed to it. A function can also explicitly use global to reassign a global variable. The question should specify the operation being performed.
⸻
④ One-Minute Reflection  

One thing I am still unsure about:
I am still unsure about how Python handles variables in nested functions, especially why reading an outer variable can work but assigning to the same name can cause UnboundLocalError.
⸻