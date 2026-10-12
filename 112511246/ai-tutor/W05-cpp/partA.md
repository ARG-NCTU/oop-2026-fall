Topic: C++ OOP — References, Encapsulation, Virtual Functions, and new/delete
Date: 2026/10/07

① Check My Understanding

Questions completed: 5 / 5

Answers revised after AI hints: 1 / 5

② My Misconception

Before: I thought…

I thought `override` was the keyword that made a function polymorphic. When the AI
asked what happens if a child class marks a function `override` while the parent
function is not `virtual`, I answered that it would still compile and simply lose
the polymorphic behavior.

⸻

Now: I understand…

I understand that `virtual` and `override` do completely different jobs. `virtual`
is what enables dynamic dispatch, so the version that runs is decided at run time by
the actual type of the object. `override` is only a compile-time check that asks the
compiler to confirm I really am overriding a virtual function from the base class.
Because it is a check, it does not silently pass when there is nothing to override —
the compilation fails.

⸻

③ Challenge the AI

One AI-generated question I challenged:

Q1, which asked whether removing the `&` from a reference parameter would still
compile and only change the runtime result.

⸻

Why?

☐ Ambiguous
☐ Oversimplified
☐ Technically questionable
☑ Too easy
☐ Other: __________

Brief explanation:

The question already stated that the code "still compiles successfully, only the
result differs," which gave away the answer inside the question itself. I could
choose True just by reading the wording, without actually understanding that a
value parameter modifies a copy. A better version would ask what the result of
`make check` is after removing the `&`, with compile error, FAIL and PASS as the
options, so that the reasoning is not revealed.

⸻

④ One-Minute Reflection

One thing I am still unsure about:

I am still unsure how to decide which functions should be `virtual` when I design a
class myself. In this lab the framework only knows the base class, so `virtual` was
clearly required, but I do not yet have a standard for making that decision in my
own code.

⸻
