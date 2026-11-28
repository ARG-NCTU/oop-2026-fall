# W8 AI Tutor Part B: Count Inversions (OCW Lec 12: Searching and Sorting)
#
# An inversion is a pair (i, j) with i < j and L[i] > L[j].
# count_inversions_slow(L) -> O(n^2), check every pair
# sort_and_count(L)        -> (sorted copy, inversions), O(n log n), merge sort idea from lecture


def count_inversions_slow(L):
    count = 0
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            if L[i] > L[j]:
                count += 1
    return count


def merge_and_count(left, right):
    result = []
    i, j, count = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:              # <= keeps equal values from counting
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += len(left) - i           # every remaining left item is bigger
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result, count


def sort_and_count(L):
    if len(L) < 2:
        return L[:], 0
    mid = len(L) // 2
    left, a = sort_and_count(L[:mid])
    right, b = sort_and_count(L[mid:])
    merged, c = merge_and_count(left, right)
    return merged, a + b + c


if __name__ == "__main__":
    # provided examples
    assert sort_and_count([2, 4, 1, 3, 5]) == ([1, 2, 3, 4, 5], 3)
    assert count_inversions_slow([2, 4, 1, 3, 5]) == 3

    # edge cases
    assert sort_and_count([]) == ([], 0)
    assert sort_and_count([7]) == ([7], 0)
    assert sort_and_count([1, 2, 3]) == ([1, 2, 3], 0)         # already sorted
    assert sort_and_count([3, 2, 1])[1] == 3                    # reversed: n(n-1)/2
    assert sort_and_count([2, 2, 2])[1] == 0                    # equal values
    original = [3, 1, 2]
    sort_and_count(original)
    assert original == [3, 1, 2]                                # input not mutated

    import random
    for _ in range(300):
        L = [random.randint(0, 9) for _ in range(random.randint(0, 12))]
        s, c = sort_and_count(L)
        assert s == sorted(L) and c == count_inversions_slow(L)

    print("all tests passed")
