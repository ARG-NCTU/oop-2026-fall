**Name:** 廖顯祐  
**Date:** 2026/11/27  
**Topic:** Searching and Sorting

### 1. Today’s Challenge

**Core concept from today’s OCW lecture:**

Merge sort, divide-and-conquer, recursion, and algorithm efficiency.

**AI-generated coding challenge title:**

Count Out-of-Order Transactions

### 2. My Initial Approach — Before AI Help

**My approach:**

I planned to modify merge sort to count inversions while sorting the timestamps. I divided the input into smaller sublists recursively and counted inversions within each half and across the two halves during merging. By utilizing the sorted property of each sublist, I avoided comparing every possible pair individually.

### 3. AI Tutor Help

**Did you ask the AI Tutor for help?**

☑ No — I solved it independently  
☐ Yes — I received one or more hints

**The most useful hint/question from AI was:**

Why does list slicing not increase the overall time complexity of merge sort beyond O(n log n)?

**It helped me realize that:**

Although list slicing introduces additional computational costs, the total slicing and merging costs at each recursion level remain O(n). I also learned to distinguish cumulative memory allocation from peak auxiliary space.

### 4. My Revision

**Did you change your approach or code after interacting with AI?**

☑ No  
☐ Yes

**What did you change, and why?**

No code changes were necessary because my original implementation satisfied both the correctness and efficiency requirements. The AI's feedback helped me further understand inversion counting, duplicate handling, and recursive complexity analysis.

### 5. Verification

**My final program:**

☑ Passed the provided examples  
☑ Passed additional edge cases  
☐ Still has unresolved problems

**One edge case I tested through manual tracing:**

Input: `timestamps = [2, 2, 1, 1]`

Expected output: `(4, [1, 1, 2, 2])`

Actual output (manual tracing): `(4, [1, 1, 2, 2])`

### 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**

I applied the divide-and-conquer strategy of merge sort to count inversions during the merging process. By utilizing the ordering of the sublists, I reduced the time complexity from O(n²) to O(n log n) while maintaining O(n) auxiliary space.

**One thing I understand better now:**

I better understand how sorting can provide additional information that reduces unnecessary computations. I also understand why handling equal elements correctly is important for both sorting stability and inversion counting.

**One thing I am still unsure about:**

I am still unsure how to systematically analyze peak auxiliary space in complex recursive algorithms, especially when multiple temporary lists are created and released at different recursion levels.