def first_unsafe_window(readings, k, limit):
    if k > len(readings):
        return -1

    for start in range(len(readings) - k + 1):
        total = 0
        for offset in range(k):
            total += readings[start + offset]

        if total > limit:
            return start

    return -1
