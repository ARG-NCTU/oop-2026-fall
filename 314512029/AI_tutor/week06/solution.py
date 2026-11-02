def first_event_at_or_after(times, target):
    """Return the first index whose timestamp is at least target, or -1."""
    low = 0
    high = len(times)

    while low < high:
        mid = (low + high) // 2
        if times[mid] < target:
            low = mid + 1
        else:
            high = mid

    if low == len(times):
        return -1
    return low
