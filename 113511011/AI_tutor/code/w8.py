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


def run_tests():
    from itertools import product

    fixed = [
        ([40, 60, 60, 20], [(1, 60, 1), (2, 60, 1), (0, 40, 2), (3, 20, 3)]),
        ([7, 7, 7], [(0, 7, 1), (1, 7, 1), (2, 7, 1)]),
        ([], []), ([8], [(0, 8, 1)]),
        ([1, 2, 3], [(2, 3, 1), (1, 2, 2), (0, 1, 3)]),
        ([3, 2, 1], [(0, 3, 1), (1, 2, 2), (2, 1, 3)]),
        ([-2, 0, -2], [(1, 0, 1), (0, -2, 2), (2, -2, 2)]),
        ([5, 1, 5, 1], [(0, 5, 1), (2, 5, 1), (1, 1, 2), (3, 1, 2)]),
        ([0, -1, 0, 1], [(3, 1, 1), (0, 0, 2), (2, 0, 2), (1, -1, 3)]),
        ([1000000, -1000000], [(0, 1000000, 1), (1, -1000000, 2)]),
    ]
    for scores, expected in fixed:
        before = scores[:]
        actual = rank_scores(scores)
        assert actual == expected, (scores, actual, expected)
        assert scores == before and actual is not scores

    count = 0
    for n in range(7):
        for values in product((-1, 0, 1), repeat=n):
            scores = list(values)
            ordered = sorted(enumerate(scores), key=lambda r: -r[1])
            distinct = sorted(set(scores), reverse=True)
            expected = [(i, v, distinct.index(v) + 1) for i, v in ordered]
            assert rank_scores(scores) == expected, values
            assert scores == list(values)
            count += 1
    scores = list(range(100000))
    actual = rank_scores(scores)
    assert actual == [(99999-i, 99999-i, i+1) for i in range(100000)]
    assert scores == list(range(100000))
    print(f"W8 PASS: {len(fixed)} fixed, {count} exhaustive, 1 large; input preserved.")


if __name__ == "__main__":
    run_tests()
