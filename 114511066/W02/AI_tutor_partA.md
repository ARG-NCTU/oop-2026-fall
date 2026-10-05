# W02 AI Tutor Learning Record — Part A

Topic: Recursion and Dictionaries
Date: 2026/09/14

## ① Check My Understanding

Questions completed: 5 / 5

Answers revised after AI hints: 1 / 5

### Question 1

**True or False:** A recursive function needs a base case so that the recursive calls can eventually stop.

My answer: True

Result: Correct.

### Question 2

**True or False:** In the Towers of Hanoi example, solving the problem for `n` disks involves solving smaller versions of the same problem for `n-1` disks.

My answer: True

Result: Correct.

### Question 3

**True or False:** In a Python dictionary, every key must have a unique value.

My answer: True

AI hint: Think about whether two different words in a frequency dictionary could have the same frequency.

Revised answer: False

Explanation: Dictionary keys must be unique, but different keys can have the same value. For example, two different words can both appear three times.

### Question 4

**True or False:** In `lyrics_to_frequencies`, checking `if word in myDict` determines whether the word has already been used as a dictionary key.

My answer: True

Result: Correct.

### Question 5

**True or False:** `fib_efficient` can avoid calculating the same Fibonacci values repeatedly by storing previously calculated results in a dictionary.

My answer: True

Result: Correct.

---

## ② My Misconception

**Before: I thought…**

I thought that both keys and values in a dictionary had to be unique.

**Now: I understand…**

I understand that dictionary keys must be unique, but multiple keys can have the same value. A dictionary can therefore be useful for mapping different items to their frequencies or previously calculated results.

---

## ③ Challenge the AI

**One AI-generated question I challenged:**

"Recursive Fibonacci and memoized Fibonacci always require approximately the same amount of computation."

**Why?**

- [ ] Ambiguous
- [x] Oversimplified
- [ ] Technically questionable
- [ ] Too easy
- [ ] Other: __________

**Brief explanation:**

The normal recursive Fibonacci function repeatedly calculates the same values. The memoized version stores previously calculated results in a dictionary, so it can reuse them instead of repeating the same recursive calculations.

---

## ④ One-Minute Reflection

**One thing I am still unsure about:**

I am still a little unsure about how to decide when recursion is better than using a loop, especially when both approaches can solve the same problem.