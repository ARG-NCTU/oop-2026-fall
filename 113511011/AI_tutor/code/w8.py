"""Lecture 12 transfer: stable score ordering and dense ranks."""


def merge_records(left, right):
    """Merge descending-score records, choosing left on ties."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][1] >= right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def sort_records(records):
    """Return a fresh, stable list sorted by descending score."""
    if len(records) < 2:
        return records[:]
    mid = len(records) // 2
    return merge_records(sort_records(records[:mid]),
                         sort_records(records[mid:]))


def rank_scores(scores):
    """Return (original index, score, dense rank), preserving input."""
    records = sort_records(list(enumerate(scores)))
    result = []
    rank = 0
    previous = None
    for index, score in records:
        if rank == 0 or score != previous:
            rank += 1
        result.append((index, score, rank))
        previous = score
    return result
