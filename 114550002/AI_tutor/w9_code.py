def find_first_missing(L):
    if len(L) == 0:
        return 0
    l = 0
    r = len(L) - 1
    while l <= r:
        mid = (l + r) // 2
        if L[mid] == mid:
            l = mid + 1
        else:
            r = mid - 1
    return l

print(find_first_missing([0, 1, 2, 4, 5, 6, 7]))
print(find_first_missing([1, 2, 3, 4]))
print(find_first_missing([0, 1, 2, 3]))
print(find_first_missing([]))
print(find_first_missing([0, 1000, 2000]))