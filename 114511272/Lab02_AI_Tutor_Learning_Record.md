# AOOP 2026 — Lab 02 AI Tutor Learning Record

## Topic
Git and GitHub: SSH, repositories, commits, push, pull, and basic collaboration

## Part A: True or False

### 1. Check My Understanding

**Question 1:** True or False: `git add` sends a file directly to GitHub.

**First answer:** True.

**AI hint:** Before a change reaches GitHub, does it go through the staging area and a local commit first?

**Revised answer:** False.

**Reason:** `git add` only puts the change into the staging area. It still needs `git commit`, and then `git push` sends the commit to GitHub.

**Question 2:** True or False: `git commit` creates a saved version in the local repository.

**Answer:** True.

**Reason:** A commit records the staged changes in the local repository history.

**Question 3:** True or False: After using `git push -u origin main` once, I usually only need `git push` for later pushes on the same branch.

**Answer:** True.

**Reason:** The `-u` option sets the upstream branch, so later pushes can use the shorter command.

**Question 4:** True or False: The private SSH key should be copied into GitHub Settings.

**First answer:** True.

**AI hint:** Which SSH key is safe to share: the file ending in `.pub`, or the private key without `.pub`?

**Revised answer:** False.

**Reason:** Only the public key should be added to GitHub. The private key should never be shared.

**Question 5:** True or False: `git pull` is used to bring newer changes from the remote repository into the current local branch.

**Answer:** True.

**Reason:** `git pull` updates the local branch with changes from the remote repository.

Questions completed: **5 / 5**

Answers revised after AI hints: **2 / 5**

### 2. My Misconception

**Before: I thought…**

I thought `git add` basically uploaded the file, and I was also confused about which SSH key gets added to GitHub.

**Now: I understand…**

The normal order is working directory → staging area → local commit → remote repository. I also understand that only the public SSH key should be copied to GitHub.

### 3. Challenge the AI

**One AI-generated question I challenged:**

“True or False: `git commit` creates a saved version in the local repository.”

**Why?**

- [ ] Ambiguous
- [ ] Oversimplified
- [ ] Technically questionable
- [x] Too easy
- [ ] Other

**Brief explanation:**

The lecture directly showed that `git commit` belongs to the local repository step, so the answer was pretty obvious.

### 4. One-Minute Reflection

**One thing I am still unsure about:**

I am still not completely sure what to do when my local repo and the GitHub repo both have changes and a pull causes a conflict.

## Part B: LeetCode-style Lecture Code Transfer

### 1. Today’s Challenge

**Core concept from today’s OCW lecture:**

Using Git in the correct order: check changes, stage them, commit them locally, connect to a remote repository, and push them to GitHub.

**AI-generated coding challenge title:**

Repair the Git Workflow

### Problem statement

You are working in a local Git repository and have edited three files:

```text
intro.md
notes.md
test.txt
```

You only want to upload `intro.md` and `notes.md` to GitHub. `test.txt` is unfinished and should stay only in the working directory.

Your repository already has a remote named `origin`, and the branch is `main`.

Your task is to give the correct Git command sequence that:

1. checks the current repository status,
2. stages only `intro.md` and `notes.md`,
3. creates one local commit with the message `update intro and notes`,
4. checks the configured remote,
5. pushes the commit to GitHub,
6. leaves `test.txt` uncommitted.

### Input/output specification

There is no program input.

The expected output is a correct sequence of Git commands that completes the required workflow.

### Constraints

- Do not stage `test.txt`.
- Do not use `git add .`.
- Do not use destructive commands such as `git reset --hard`.
- Use only Git commands covered in the lecture.
- Assume `origin` is already configured and the current branch is `main`.

### Example 1

```text
Changed files:
intro.md
notes.md
test.txt

Files that should be committed:
intro.md
notes.md
```

Expected result:

```text
One new commit is created and pushed.
test.txt remains uncommitted.
```

### Example 2

```text
Remote name: origin
Branch: main
```

Expected result:

```text
The new commit is pushed to origin/main.
```

### 2. My Initial Approach — Before AI Help

I planned to check the repo with `git status`, then add only the two files I wanted. After that I would commit them, check the remote with `git remote -v`, and push to `main`.

### 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

- [ ] No — I solved it independently
- [x] Yes — I received one or more hints

**The most useful hint/question from AI was:**

“If one file should stay uncommitted, is `git add .` still a good choice?”

**It helped me realize that:**

I should add the files by name instead of staging everything in the folder.

### 4. My Revision

**Did you change your approach or code after interacting with AI?**

- [ ] No
- [x] Yes

**What did you change, and why?**

I changed from using `git add .` to adding `intro.md` and `notes.md` separately so the unfinished file would not be included in the commit.

### 5. Verification

My final command sequence:

```bash
git status
git add intro.md notes.md
git commit -m "update intro and notes"
git remote -v
git push origin main
```

- [x] Staged only the requested files
- [x] Created a local commit
- [x] Checked the remote
- [x] Pushed the commit
- [x] Left `test.txt` uncommitted

**One edge case I checked:**

Input:

```text
test.txt is modified but should not be committed
```

Expected result:

```text
test.txt remains unstaged and uncommitted
```

Actual result:

```text
test.txt remains unstaged and uncommitted
```

### 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**

I used the same Git workflow from the lecture: check the working directory, stage selected files, commit locally, and then push to the remote repository.

**One thing I understand better now:**

I understand the difference between `git add`, `git commit`, and `git push`. They move changes through different stages instead of all doing the same thing.

**One thing I am still unsure about:**

I am still unsure about the best way to recover if I accidentally commit the wrong file.
