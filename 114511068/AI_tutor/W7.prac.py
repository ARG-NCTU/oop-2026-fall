
def common_participants(L1, L2):
    result = []

    for student in L1:
        if student in L2 and student not in result:
            result.append(student)

    return result


# Example 1
L1 = [12, 5, 8, 5, 20, 12]
L2 = [5, 12, 30, 8]
print(common_participants(L1, L2))

# Example 2
L1 = [3, 7, 9]
L2 = [2, 4, 6]
print(common_participants(L1, L2))

# Example 3
L1 = [4, 4, 2, 4, 6]
L2 = [4, 2, 2]
print(common_participants(L1, L2))

# Edge case: empty list
L1 = []
L2 = [1, 2, 3]
print(common_participants(L1, L2))
