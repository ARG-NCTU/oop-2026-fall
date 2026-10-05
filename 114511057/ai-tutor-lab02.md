# AI Tutor Learning Record — Lab 02

**Name:** 陳芊蓉  
**Student ID:** 114511057  
**Topic:** Git and GitHub

---

# Part A: True or False

## ① Check My Understanding

**Questions completed:** 5 / 5

**Answers revised after AI hints:** 1 / 5

### Question 1

**Q:** `git add` uploads my files directly to GitHub.

**Answer:** False.

`git add` puts selected changes into the staging area. It does not upload them to GitHub.

### Question 2

**Q:** `git commit` creates a version record in the local repository.

**Answer:** True.

A commit records the staged changes in the local Git history.

### Question 3

**Q:** After making a commit, I still need `git push` if I want the commit to appear on GitHub.

**Answer:** True.

A commit is stored locally first. `git push` sends the local commit to the remote repository.

### Question 4

**Q:** A private SSH key can be copied and uploaded to GitHub.

**Answer:** False.

Only the public key should be added to GitHub. The private key should not be shared.

### Question 5

**Q:** `git status` can help me check which files have been modified or are ready to be committed.

**Answer:** True.

It is useful for checking the current state before using commands such as `git add` or `git commit`.

---

## ② My Misconception

**Before: I thought…**

I thought `git add`, `git commit`, and `git push` were almost the same and all of them were used to upload files to GitHub.

**Now: I understand…**

They represent different steps. `git add` selects changes for the staging area, `git commit` creates a local version record, and `git push` sends the local commits to the remote repository on GitHub.

---

## ③ Challenge the AI

**One AI-generated question I challenged:**

“After making a commit, I still need `git push` if I want the commit to appear on GitHub.”

**Why?**

☐ Ambiguous  
☒ Oversimplified  
☐ Technically questionable  
☐ Too easy  
☐ Other: __________

**Brief explanation:**

The question is useful for beginners, but it is quite simple. A more challenging question could ask about the difference between the staging area, local repository, and remote repository.

---

## ④ One-Minute Reflection

**One thing I am still unsure about:**

I am still unsure about how to handle conflicts when the remote repository has changes that are different from my local repository.

---

# Part B: LeetCode-style Lecture Code Transfer

## 1. Today’s Challenge

**Core concept from today’s OCW lecture:**

Understanding the Git workflow from the working directory to the staging area, local repository, and remote repository.

**AI-generated coding challenge title:**

**Git Command Sequence Checker**

### Problem Statement

You are given the current state of a file in a Git project.

Determine which Git command should be used next to move the file toward being uploaded to GitHub.

The possible states are:

- `"modified"` — the file has been changed but is not staged.
- `"staged"` — the file has been added to the staging area.
- `"committed"` — the change has been committed locally.

Return the appropriate next command:

- `"modified"` → `"git add"`
- `"staged"` → `"git commit"`
- `"committed"` → `"git push"`

### Input

A string representing the current Git state.

### Output

A string representing the next Git command.

### Constraints

The input will be one of:

`"modified"`, `"staged"`, or `"committed"`.

### Examples

**Example 1**

Input: `"modified"`

Output: `"git add"`

**Example 2**

Input: `"staged"`

Output: `"git commit"`

**Example 3**

Input: `"committed"`

Output: `"git push"`

---

## 2. My Initial Approach — Before AI Help

**My approach:**

I planned to check the current state and use conditions to return the corresponding Git command.

---

## 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

☐ No — I solved it independently  
☒ Yes — I received one or more hints

**The most useful hint/question from AI was:**

“Where does a change go after `git add`, and where does it go after `git commit`?”

**It helped me realize that:**

Git has different stages. A modified file is first added to the staging area, then committed to the local repository, and finally pushed to the remote repository.

---

## 4. My Revision

**Did you change your approach or code after interacting with AI?**

☐ No  
☒ Yes

**What did you change, and why?**

I changed my explanation so that I did not treat `add`, `commit`, and `push` as the same operation. I connected each command to a different location in the Git workflow.

---

## 5. Verification

**My final program:**

☒ Passed the provided examples  
☒ Passed additional edge cases  
☐ Still has unresolved problems

**One edge case I tested:**

Input: `"committed"`

Expected output: `"git push"`

Actual output: `"git push"`

---

## 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**

I transferred the idea that Git changes move through different locations before they finally appear on GitHub.

**One thing I understand better now:**

I understand the difference between `git add`, `git commit`, and `git push` better.

**One thing I am still unsure about:**

I am still unsure about `git pull`, merge conflicts, and what I should do when my local repository and the remote repository have different changes.
