def intersect_sorted(nums1: list[int], nums2: list[int]):
    i, j = 0, 0
    intersection: list[int] = []

    # two pointer merge
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            intersection.append(nums1[i])
            i += 1
            j += 1

    return intersection
