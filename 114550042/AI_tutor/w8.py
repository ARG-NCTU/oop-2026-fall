def merge_two_sorted(list1: list[int], list2: list[int]):
    # two pointer merging
    i, j = 0, 0
    merged: list[int] = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged


def merge_k_sorted(lists: list[list[int]]) -> list[int]:
    n = len(lists)
    if n == 0:
        return []
    if n == 1:
        return lists[0]
    mid = n // 2
    left = merge_k_sorted(lists[:mid])
    right = merge_k_sorted(lists[mid:])
    return merge_two_sorted(left, right)
