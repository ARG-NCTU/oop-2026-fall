def common_students(A, B):
    result = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            result.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return result


if __name__ == "__main__":
    print(common_students([3, 5, 8, 10], [1, 5, 6, 10, 12]))
    print(common_students([1, 2, 3], [4, 5]))
    print(common_students([], [1, 2]))
    print(common_students([2, 4, 6], [2, 4, 6]))
