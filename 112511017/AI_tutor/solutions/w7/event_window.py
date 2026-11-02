"""Count events in a half-open time window without scanning a sorted log."""


def _first_at_least(timestamps, target):
    low = 0
    high = len(timestamps)
    while low < high:
        mid = (low + high) // 2
        if timestamps[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low


def count_events(timestamps, start, end):
    """Return the number of sorted integer timestamps in [start, end).

    The input must be in nondecreasing order. Equal timestamps are separate
    events. Empty or reversed windows contain no events. Input is unchanged.
    """
    if start >= end:
        return 0
    return _first_at_least(timestamps, end) - _first_at_least(timestamps, start)
