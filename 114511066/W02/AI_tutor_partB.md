# W02 AI Tutor Learning Record — Part B

Name: 114511066
Date: 2026/09/14
Topic: Recursion and Dictionaries

## 1. Today’s Challenge

### Core concept from today’s OCW lecture:

Recursion, dictionaries, frequency counting, and memoization.

The lecture showed how recursion solves a problem by reducing it into smaller versions of the same problem. It also showed how dictionaries can store frequencies and previously calculated results.

### AI-generated coding challenge title:

**Most Frequent Number**

### Problem Statement

Given a list of integers, use a dictionary to count how many times each number appears.

Return a tuple containing a list of the most frequent numbers and their frequency.

If more than one number has the highest frequency, return all of them.

### Input/Output

Input:

    nums = [1, 2, 2, 3, 3, 4]

Output:

    ([2, 3], 2)

### Constraints

- The input contains at least one integer.
- A number may appear more than once.
- More than one number may have the highest frequency.
- Use a dictionary to store the frequencies.

### Examples

Example 1:

    Input: [1, 2, 2, 3]
    Output: ([2], 2)

Example 2:

    Input: [1, 1, 2, 2, 3]
    Output: ([1, 2], 2)

Example 3:

    Input: [5]
    Output: ([5], 1)

---

## 2. My Initial Approach — Before AI Help

### My approach:

My first idea was to create an empty dictionary and iterate through the input list.

If a number was already a key in the dictionary, I would increase its value by one. Otherwise, I would add the number to the dictionary with a value of one.

Then I would find the largest frequency and collect all keys with that frequency.

---

## 3. AI Tutor Help

### Did you ask the AI Tutor for help?

- [ ] No — I solved it independently
- [x] Yes — I received one or more hints

### The most useful hint/question from AI was:

What should happen if two or more numbers have the same maximum frequency?

### It helped me realize that:

I should not only keep one number as the answer. I need a list to store every key whose frequency is equal to the maximum frequency.

This is similar to the `most_common_words()` example from the lecture.

---

## 4. My Revision

### Did you change your approach or code after interacting with AI?

- [ ] No
- [x] Yes

### What did you change, and why?

I changed my solution so that it first creates the frequency dictionary and then finds every number with the maximum frequency.

### Final code

```python
def most_frequent(nums):
    freqs = {}

    for n in nums:
        if n in freqs:
            freqs[n] += 1
        else:
            freqs[n] = 1

    highest = max(freqs.values())
    result = []

    for n in freqs:
        if freqs[n] == highest:
            result.append(n)

    return (result, highest)