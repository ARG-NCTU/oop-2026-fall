
"""
Week 10 - AI Tutor Coding Challenge
Topic: Optimization Problems and Dynamic Programming

Problem: Maximum Arcade Prize Value

You are at an arcade prize shop with a limited number of tickets.
Each prize has a ticket cost and a happiness value.

You can redeem each prize at most once.

Your goal is to maximize the total happiness value without
exceeding your available tickets.

Function:
    maxHappiness(prizes, tickets)

Input:
    prizes: A list of [ticketCost, happinessValue] pairs
    tickets: Total number of available tickets

Output:
    Maximum total happiness value (integer)

Constraints:
    1 <= len(prizes) <= 20
    1 <= ticketCost <= 100
    1 <= happinessValue <= 100
    0 <= tickets <= 500

Examples:
    Input: prizes = [[4, 10], [5, 12], [3, 7]], tickets = 8
    Output: 19

    Input: prizes = [[6, 15], [4, 9], [3, 8]], tickets = 7
    Output: 17

    Input: prizes = [[5, 20], [7, 30]], tickets = 3
    Output: 0
"""


# --------------------------------------------------
# Solution: Recursive Search Tree + Memoization
# --------------------------------------------------

def maxHappiness(prizes, tickets):

    # Dictionary to store previously calculated results
    memo = {}

    def solve(i, remaining):

        # Base case: No more prizes or tickets
        # No additional happiness can be earned
        if i == len(prizes) or remaining == 0:
            return 0

        # If already calculated, return stored result
        if (i, remaining) in memo:
            return memo[(i, remaining)]

        # Option 1: Skip the current prize
        skip = solve(i + 1, remaining)

        # Get current prize information
        cost = prizes[i][0]
        happiness = prizes[i][1]

        # Option 2: Take the current prize
        take = 0

        # Only take the prize if we have enough tickets
        if cost <= remaining:
            take = happiness + solve(i + 1, remaining - cost)

        # Choose the option with higher happiness
        best = max(skip, take)

        # Save the result to avoid repeated calculations
        memo[(i, remaining)] = best

        return best

    # Start from the first prize with all available tickets
    return solve(0, tickets)


# --------------------------------------------------
# Test Cases
# --------------------------------------------------

# Test 1: Normal case
prizes1 = [[4, 10], [5, 12], [3, 7]]
print("Test 1:", maxHappiness(prizes1, 8))
# Expected: 19


# Test 2: Different combinations
prizes2 = [[6, 15], [4, 9], [3, 8]]
print("Test 2:", maxHappiness(prizes2, 7))
# Expected: 17


# Test 3: Edge case - Not enough tickets
prizes3 = [[5, 20], [7, 30]]
print("Test 3:", maxHappiness(prizes3, 3))
# Expected: 0


# Test 4: Edge case - Zero tickets
prizes4 = [[2, 10], [3, 20]]
print("Test 4:", maxHappiness(prizes4, 0))
# Expected: 0


# Test 5: Edge case - Only one prize
prizes5 = [[3, 15]]
print("Test 5:", maxHappiness(prizes5, 5))
# Expected: 15


# Verify all test cases
assert maxHappiness(prizes1, 8) == 19
assert maxHappiness(prizes2, 7) == 17
assert maxHappiness(prizes3, 3) == 0
assert maxHappiness(prizes4, 0) == 0
assert maxHappiness(prizes5, 5) == 15

print("All tests passed!")


# --------------------------------------------------
# Complexity Analysis
# --------------------------------------------------

# n = Number of prizes
# W = Number of available tickets
#
# Time Complexity: O(n * W)
# Each (i, remaining) state is calculated at most once.
#
# Space Complexity: O(n * W)
# Memoization stores the results of subproblems.
# The recursion stack also uses O(n) space.
#
# Lecture Concepts:
# 1. Recursive Search Tree
# 2. 0/1 Knapsack Problem
# 3. Optimal Substructure
# 4. Overlapping Subproblems
# 5. Memoization (Dynamic Programming)


# def maxHappiness(prizes, tickets):
#     memo = {}

#     def solve(i, remaining):
#         # Base case
#         if i == len(prizes) or remaining == 0:
#             return 0

#         # Check memo
#         if (i, remaining) in memo:
#             return memo[(i, remaining)]

#         # Don't take the prize
#         skip = solve(i + 1, remaining)

#         # Take the prize if there are enough tickets
#         take = 0
#         if prizes[i][0] <= remaining:
#             take = prizes[i][1] + solve(i + 1, remaining - prizes[i][0])

#         # Choose the better option
#         best = max(skip, take)

#         # Store result
#         memo[(i, remaining)] = best

#         return best

#     return solve(0, tickets)

