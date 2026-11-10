def first_at_least(L, x):
    low = 0
    high = len(L)
    while low < high:
        mid = (low + high) // 2
        if L[mid] >= x:
            high = mid
        else:
            low = mid + 1
    return low


def count_pass(L, limit):
    return len(L) - first_at_least(L, limit)


if __name__ == "__main__":
    scores = [45, 60, 60, 72, 90]
    print(first_at_least(scores, 60))
    print(first_at_least(scores, 61))
    print(first_at_least(scores, 0))
    print(first_at_least(scores, 100))
    print(first_at_least([], 60))
    print(count_pass(scores, 60))
