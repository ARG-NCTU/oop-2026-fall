# AI Tutor for AOOP 2026

## Part A: True or False

### AI Tutor Learning Cycle (ATLC) — Suggested Student Prompt:

```

I just learned Recursion and Dictionaries in today’s lecture.

Act as my AI Tutor.

1. Generate 5 True/False questions, one question at a time, to test my conceptual understanding of today’s topic.
2. Focus on concepts and reasoning, not memorization or Python syntax.
3. After I answer, do not immediately tell me the correct answer.
4. If my answer or reasoning is incorrect, give me a hint, counterexample, or follow-up question.
5. Let me revise my answer before explaining the concept.
6. Adjust the difficulty based on my responses.
7. After five questions, ask me to identify one question that may be ambiguous, misleading, too easy, or technically questionable.
8. Finish by asking me what misconception I corrected and what I am still unsure about.
```

### AI Tutor Learning Record

```
Topic: Recursion and Dictionaries
Date: 9/16


========================================
Part A: True or False
========================================

1. Check My Understanding

Questions completed: 5 / 5

Answers revised after AI hints: 1 / 5


Question 1:

True or False:

A function is a correct recursive solution simply because it calls
itself.


My answer:

False.


Reason:

Calling itself only makes the function recursive syntactically.

A correct recursive solution also needs a valid base case and a
recursive step that moves toward that base case.

The recursive calls must correctly solve smaller versions of the same
problem.


Question 2:

True or False:

If a recursive function has a base case somewhere in its code, it is
guaranteed to terminate.


My first answer:

True.


AI hint:

Consider a function with a base case for n == 0, but whose recursive
step calls itself using n + 1.

If the function starts with n = 5, will it ever reach the base case?


My revised answer:

False.


Reason:

Having a base case is not enough.

The recursive step must move the problem toward the base case.

If each call moves farther away, or does not make progress, the base
case may never be reached.


Question 3:

True or False:

Each recursive call to a function has its own local environment.


My answer:

True.


Reason:

Each recursive call creates a new function scope.

Local variables in one call are separate from the local variables in
another call.

When the deeper recursive call returns, execution continues in the
previous call's environment.


Question 4:

True or False:

A dictionary can associate a key with a value and can be modified after
it is created.


My answer:

True.


Reason:

Dictionaries store key-value pairs and are mutable.

A program can add new keys, update existing values, and use keys to
retrieve information.


Question 5:

True or False:

A recursive solution must always physically create a smaller list before
making the next recursive call.


My answer:

False.


Reason:

The problem must become smaller conceptually, but the program does not
have to create a new list.

For example, a recursive function can keep the original list and use an
index that moves forward.

The remaining work becomes smaller even though the list object itself
does not change.


2. My Misconception

Before: I thought...

I thought that recursion mainly meant that a function keeps calling
itself until the answer appears.

I did not fully understand why the base case and the direction of the
recursive step were both important.


Now: I understand...

A recursive solution has two essential parts.

First, it needs a base case that can be solved directly.

Second, the recursive step needs to transform the problem into a
simpler version of the same problem.

Each recursive call must make progress toward the base case.

A base case that can never be reached does not prevent infinite
recursion.


3. Challenge the AI

One AI-generated question I challenged:

"If a function calls itself, then it is a correct recursive solution."


Why?

[ ] Ambiguous
[x] Oversimplified
[x] Technically questionable
[ ] Too easy
[ ] Other: __________


Brief explanation:

Calling itself only tells us that a function is recursive.

It does not prove that the algorithm is correct.

A valid recursive solution also needs a correct base case, a recursive
step that solves a smaller version of the same problem, and progress
toward the base case.

A recursive function can call itself and still produce an incorrect
answer or fail to terminate.


4. One-Minute Reflection

One thing I am still unsure about:

I am still practicing how to choose the correct base case and how to
identify the smaller version of a problem.

I also want to become more comfortable tracing recursive calls and
understanding how several function environments can exist at the same
time.

```

## Part B: **LeetCode-style** Lecture Code Transfer

AI Tutor Learning Cycle (ATLC) — Suggested Student Prompt:

```
I have just studied the following lecture code from today’s OCW programming lecture.

[LECTURE CODE]

Act as my AI Tutor.

Based on the concepts and programming patterns demonstrated in the lecture code, generate ONE new LeetCode-style programming challenge.

Requirements:

1. Test the same core concept as the lecture code.
2. Do not simply ask me to reproduce or slightly modify the lecture example.
3. Create a new problem that requires me to transfer what I learned.
4. Use only programming concepts that have been covered in the course so far.
5. Provide:
    * Problem statement
    * Input/output specification
    * Constraints
    * 2–3 examples
6. Do NOT provide code, pseudocode, or the solution.

Before I write code:

7. Ask me to explain my proposed algorithm.
8. Ask me to identify which concept from the lecture code I am applying.
9. If my reasoning is incorrect, give me a hint or counterexample instead of the answer.

After I write my code:

10. Test my solution using normal and edge cases.
11. If my code fails, help me identify the problem without rewriting the solution for me.
12. Ask me to revise my solution.

Finally, ask me to explain:

* Why my solution works
* Its time complexity
* What idea from the lecture code I transferred to this new problem
```

### AI Tutor Learning Record — Coding Challenge

```
========================================
Part B: LeetCode-style Lecture Code Transfer
========================================

Name: 程婕茵
Date: 9/16
Topic: Recursion and Dictionaries


1. Today's Challenge

Core concept from today's OCW lecture:

The main concepts are recursion and dictionaries.

A recursive solution reduces a problem into a smaller version of the
same problem.

A correct recursive function needs at least one base case and a
recursive step that moves the problem toward the base case.

The lecture also introduced dictionaries as mutable objects that store
information using key-value pairs.


AI-generated coding challenge title:

Recursive Word Frequency Counter


Problem Statement:

You are given a list of words.

Your task is to count how many times each word appears in the list and
return the result as a dictionary.

Each unique word should be used as a dictionary key.

The value associated with each key should be the number of times that
word appears in the input list.

You must process the list recursively.

You may not use a for loop or while loop to process the words.


Input / Output Specification:

Input:

words

A list of strings.


Output:

A dictionary.

For every unique word in the input list:

result[word]

should equal the number of times that word appears.


If the input list is empty:

Return:

{}


Constraints:

1. words may be empty.
2. Every element in words is a string.
3. Use recursion to process the input list.
4. Do not use a for loop or while loop to process the words.
5. Use a dictionary to store word frequencies.
6. Each recursive call must move closer to a base case.
7. Use only programming concepts covered through Lecture 6.


Examples:

Example 1

Input:

words = [
    "cat",
    "dog",
    "cat",
    "bird",
    "dog",
    "cat"
]

Output:

{
    "cat": 3,
    "dog": 2,
    "bird": 1
}


Example 2

Input:

words = []

Output:

{}


Example 3

Input:

words = [
    "apple",
    "apple",
    "apple",
    "apple"
]

Output:

{
    "apple": 4
}


2. My Initial Approach - Before AI Help

Before asking AI for hints, briefly describe how you planned to solve
the problem.

My approach:

I planned to go through the list of words and store the count of each
word in a dictionary.

If a word already existed as a key in the dictionary, I would increase
its value by 1.

If the word did not exist, I would add it to the dictionary with a
value of 1.

At first, I was thinking about using a normal for loop because that was
the most familiar way for me to process a list.


Concept from the lecture that I am applying:

I am applying recursion and dictionaries.

The dictionary stores each word as a key and its frequency as a value.

For the recursive part, the larger problem is reduced into:

1. process the current word
2. recursively process the remaining unprocessed words


3. AI Tutor Help

Did you ask the AI Tutor for help?

[ ] No - I solved it independently
[x] Yes - I received one or more hints


The most useful hint/question from AI was:

"What is the smallest version of the problem that you can solve
directly?"


It helped me realize that:

When the current index reaches the length of the list, there are no more
words to process.

That can be used as the base case.

It also helped me understand that after processing one word, the
remaining problem is the same problem with one fewer unprocessed word.


4. My Revision

Did you change your approach or code after interacting with AI?

[ ] No
[x] Yes


What did you change, and why?

Originally, I planned to solve the problem using a for loop.

I changed the approach so that a recursive helper function keeps track
of the current position in the list.

The base case happens when the index reaches the length of the list.

At that point, there are no more words to process.

For every recursive step, the index increases by 1.

This means that each recursive call has a smaller amount of remaining
work and moves closer to the base case.

The dictionary is updated as the recursive calls process each word.


5. My Final Program

def count_words(words):
    counts = {}

    def helper(index):
        if index == len(words):
            return

        word = words[index]

        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

        helper(index + 1)

    helper(0)

    return counts


6. Why My Solution Works

The base case is:

if index == len(words):
    return

This stops the recursion when all words have been processed.

For every recursive call, the index increases by 1.

Therefore, the amount of remaining work decreases on every call.

Eventually, the index reaches the length of the list and the base case
is reached.

For each word:

If the word already exists in the dictionary, its count is increased by
1.

If the word does not exist, it is added to the dictionary with a count
of 1.

Because every word is processed exactly once, the dictionary contains
the correct frequency of each word when the recursion finishes.


7. Verification

My final program:

[x] Passed the provided examples
[x] Passed additional edge cases
[ ] Still has unresolved problems


Normal Case:

Input:

words = [
    "cat",
    "dog",
    "cat",
    "bird",
    "dog",
    "cat"
]

Expected output:

{
    "cat": 3,
    "dog": 2,
    "bird": 1
}

Actual output:

{
    "cat": 3,
    "dog": 2,
    "bird": 1
}


Edge Case 1: Empty List

Input:

words = []

Expected output:

{}

Actual output:

{}


Why this edge case matters:

The recursive helper starts with index = 0.

Since len(words) is also 0, the base case is reached immediately.


Edge Case 2: One Repeated Word

Input:

words = [
    "apple",
    "apple",
    "apple",
    "apple"
]

Expected output:

{
    "apple": 4
}

Actual output:

{
    "apple": 4
}


Why this edge case matters:

This checks whether the program correctly updates an existing dictionary
key multiple times.


Edge Case 3: All Words Are Different

Input:

words = [
    "red",
    "blue",
    "green"
]

Expected output:

{
    "red": 1,
    "blue": 1,
    "green": 1
}

Actual output:

{
    "red": 1,
    "blue": 1,
    "green": 1
}


8. Time and Space Complexity

Let:

n = number of words in the input list


Time Complexity:

Each word is processed exactly once.

Dictionary lookup and update are treated as O(1) on average.

Therefore, the total time complexity is:

O(n)


Space Complexity:

The dictionary may contain up to n different words.

Therefore, the dictionary can require:

O(n)

space.

The recursive call stack may also contain up to n active recursive
calls.

Therefore, the recursive stack can require:

O(n)

space.

The total additional space complexity is:

O(n)


9. What Idea I Transferred from the Lecture

The main idea I transferred from Lecture 6 is decrease-and-conquer.

Instead of trying to solve the entire problem at once, each recursive
call processes one word and leaves a smaller amount of work for the next
recursive call.

I also transferred the idea of using a dictionary to associate keys with
values.

In this problem:

word = key

frequency = value

The dictionary is mutable, so the recursive calls can update the same
dictionary while processing the list.


10. One-Minute Reflection

What idea from the OCW lecture did you transfer to this new problem?

I transferred the idea that recursion solves a larger problem by reducing
it to smaller versions of the same problem.

Each recursive call must move closer to a base case.

I also used a dictionary to store information as key-value pairs.


One thing I understand better now:

I understand that recursion is not just a function calling itself.

A recursive solution also needs a base case and a recursive step that
makes progress toward that base case.

I also understand how a dictionary can be updated while recursive calls
are processing data.


One thing I am still unsure about:

I am still practicing how to trace recursive calls when several calls
are active at the same time.

I also want to understand recursion memory usage better, especially what
happens to each function's local variables while deeper recursive calls
are running.
```
