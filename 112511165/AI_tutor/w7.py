def lower_bound(L, e):
    low = 0
    high = len(L)

    while low < high:
        mid = (low + high) // 2
        if L[mid] >= e:
            high = mid
        else:
            low = mid + 1

    return low
