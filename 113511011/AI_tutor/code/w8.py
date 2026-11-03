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

    # Verify helper contracts separately: descending merge, ties, no aliasing.
    left, right = [(0, 9), (1, 5)], [(2, 9), (3, 5), (4, 1)]
    merged = merge_records(left, right)
    assert merged == [(0, 9), (2, 9), (1, 5), (3, 5), (4, 1)]
    assert left == [(0, 9), (1, 5)] and right == [(2, 9), (3, 5), (4, 1)]
    for records in ([], [(0, 3)], [(0, 3), (1, 3), (2, -1)]):
        output = sort_records(records)
        assert output == records and output is not records
    print("W8 helper contracts PASS.")

    # Reproducible non-power-of-two inputs with many cross-half ties.
    from random import Random
    rng = Random(20261103)
    for _ in range(200):
        values = [rng.randint(-50, 50) for _ in range(rng.randrange(300))]
        output = rank_scores(values)
        expected_order = sorted(range(len(values)), key=lambda i: -values[i])
        assert [row[0] for row in output] == expected_order
        unique = sorted(set(values), reverse=True)
        assert [row[2] for row in output] == [unique.index(values[i])+1 for i in expected_order]
        assert all(values[i] == score for i, score, _ in output)
    print("W8 randomized oracle PASS: 200 seeded cases.")

    # Instrument actual score comparisons, rather than timing a noisy machine.
    class CountedScore(int):
        comparisons = 0

        def __ge__(self, other):
            type(self).comparisons += 1
            return super().__ge__(other)

    for exponent in range(1, 11):
        size = 2 ** exponent
        values = [CountedScore((i * 37) % size) for i in range(size)]
        CountedScore.comparisons = 0
        ordered = sort_records(list(enumerate(values)))
        assert [int(score) for _, score in ordered] == list(range(size-1, -1, -1))
        assert CountedScore.comparisons <= size * exponent - size + 1
    print("W8 comparison bounds PASS: powers of two through 1024.")


if __name__ == "__main__":
    run_tests()
