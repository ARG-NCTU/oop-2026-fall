# AI Tutor for AOOP 2026

## Part A: True or False

### AI Tutor Learning Record

Topic: LeetCode platform and Python problem-solving  
Date: 2026/11/09

### ① Check My Understanding

Questions completed: 5 / 5

Correct answers: 4 / 5

Answers revised after AI hints: 0 / 5

### ② My Misconception

**Before:**

I thought LeetCode only provided fixed test cases, and I didn't know that users could add their own test cases.

---

**Now:**

I understand that LeetCode allows users to add or modify test cases to check different inputs. This can help find problems that may not appear in the provided examples.

### ③ Challenge the AI

**One AI-generated question I challenged:**

"In LeetCode, passing all the selected Run test cases guarantees that the solution will also pass Submit."

---

**Why?**

☐ Ambiguous  
☐ Oversimplified  
☑ Technically questionable  
☐ Too easy  
☐ Other: __________

**Brief explanation:**

I think this statement is not always correct because Run only checks selected test cases, while Submit uses more test cases. Even if the code passes Run, it may still fail when submitted.

### ④ One-Minute Reflection

**One thing I am still unsure about:**

I am still not very familiar with solving programming problems independently. I can understand the solutions with explanations, but I need more practice to figure out the logic by myself.

---

## Part B: LeetCode-style Lecture Code Transfer

### AI Tutor Learning Record — Coding Challenge

Name: 114511074  
Date: 2026/11/09  
Topic: LeetCode problem-solving and Python programming

### 1. Today’s Challenge

**Core concept from today's lecture:**

Learning how to understand programming problems, write Python code, test different inputs, and submit solutions on LeetCode.

---

**AI-generated coding challenge title:**

Two Sum and Best Time to Buy and Sell Stock

---

### 2. My Initial Approach — Before AI Help

**My approach:**

At first, I thought about checking different pairs of numbers for Two Sum. For the stock problem, I knew I needed to compare buying and selling prices, but I was not sure how to find the maximum profit efficiently.

---

### 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

☐ No — I solved it independently  
☑ Yes — I received one or more hints

**The most useful hint/question from AI was:**

"Instead of checking every pair of numbers, can you store the numbers you have already seen?"

---

**It helped me realize that:**

I could use a dictionary to store numbers and their indices in Two Sum. For the stock problem, I learned to keep track of the minimum price and update the maximum profit while checking each day's price.

---

### 4. My Revision

**Did you change your approach or code after interacting with AI?**

☐ No  
☑ Yes

**What did you change, and why?**

With AI's help, I used a dictionary for Two Sum instead of comparing every pair. For the stock problem, I used `min_price` and `max_profit` to calculate the maximum profit. These methods made the solutions more efficient, but I still needed explanations to understand the code.

---

### 5. Verification

**My final program:**

☑ Passed the provided examples  
☑ Passed additional test cases through Submit  
☐ Still has unresolved problems

**Verification results:**

Two Sum: Accepted — 66/66 test cases passed.

Best Time to Buy and Sell Stock: Accepted — 213/213 test cases passed.

**One test case checked:**

Input: `prices = [7, 1, 5, 3, 6, 4]`

Expected output: `5`

Actual output: `5`

---

### 6. One-Minute Reflection

**What idea from the lecture did you transfer to this new problem?**

I learned how to read the problem requirements, understand the input and output, and use Run and Submit to check my Python solutions.

---

**One thing I understand better now:**

I understand how to use LeetCode better than before. I also learned that using a dictionary or keeping track of the minimum value can make solving problems more efficient. However, I still need more practice to write these solutions on my own.
