def merge_unique(a, b):
    result = []
    i, j = 0, 0
    len_a, len_b = len(a), len(b)

    while i < len_a and j < len_b:
        if a[i] < b[j]:
            val = a[i]
            i += 1
        elif a[i] > b[j]:
            val = b[j]
            j += 1
        else:
            val = a[i]
            i += 1
            j += 1

        if not result or result[-1] != val:
            result.append(val)

    while i < len_a:
        val = a[i]
        i += 1
        if not result or result[-1] != val:
            result.append(val)

    while j < len_b:
        val = b[j]
        j += 1
        if not result or result[-1] != val:
            result.append(val)

    return result
