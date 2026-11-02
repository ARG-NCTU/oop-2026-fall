
"""
Problem: Maximum Non-Overlapping Study Sessions

You are organizing study sessions in a classroom.
Each session has a starting time and an ending time.

Only one session can take place at a time.

Find the maximum number of non-overlapping sessions
that can be attended.

If one session ends exactly when another begins,
both sessions can be attended.

Input:
    sessions: List of [start, end] pairs

Output:
    Maximum number of non-overlapping sessions

Example 1:
    Input: [[1, 3], [2, 5], [3, 4], [4, 7]]
    Output: 3

Example 2:
    Input: [[1, 4], [2, 5], [3, 6]]
    Output: 1

Example 3:
    Input: [[1, 2], [2, 3], [3, 4], [1, 4]]
    Output: 3
"""


def maxSessions(sessions):

    # Step 1: Sort sessions by their ending time
    sessions = sorted(sessions, key=lambda x: x[1])

    # Step 2: Initialize variables
    count = 0
    lastEnd = float('-inf')

    # Step 3: Check every session
    for start, end in sessions:

        # Choose the session if it does not overlap
        if start >= lastEnd:
            count += 1
            lastEnd = end

    # Step 4: Return maximum number of sessions
    return count


# Test cases
sessions1 = [[1, 3], [2, 5], [3, 4], [4, 7]]
sessions2 = [[1, 4], [2, 5], [3, 6]]
sessions3 = [[1, 2], [2, 3], [3, 4], [1, 4]]

print(maxSessions(sessions1))  # 3
print(maxSessions(sessions2))  # 1
print(maxSessions(sessions3))  # 3
