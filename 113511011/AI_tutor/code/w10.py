"""Lecture 2 transfer: exact workshop selection and memoization audit."""


def maxVal(items, budget, stats=None):
    """Return (value, ascending indices); equal values prefer skipping early."""
    if stats is None:
        stats = {}
    stats.update(calls=0)

    def search(i, remaining):
        stats['calls'] += 1
        if i == len(items) or remaining == 0:
            return 0, ()
        skipped = search(i + 1, remaining)
        value, cost = items[i]
        if cost > remaining:
            return skipped
        value_after, indices = search(i + 1, remaining - cost)
        if value + value_after > skipped[0]:
            return value + value_after, (i,) + indices
        return skipped

    return search(0, budget)


def fastMaxVal(items, budget, stats=None):
    """Same contract as maxVal, with a fresh per-solve suffix/capacity memo."""
    memo = {}
    if stats is None:
        stats = {}
    stats.update(calls=0, hits=0, states=0)

    def search(i, remaining):
        stats['calls'] += 1
        key = (i, remaining)
        if key in memo:
            stats['hits'] += 1
            return memo[key]
        if i == len(items) or remaining == 0:
            result = (0, ())
        else:
            result = search(i + 1, remaining)
            value, cost = items[i]
            if cost <= remaining:
                value_after, indices = search(i + 1, remaining - cost)
                if value + value_after > result[0]:
                    result = (value + value_after, (i,) + indices)
        memo[key] = result
        stats['states'] += 1
        return result

    return search(0, budget)


def subset_oracle(items, budget):
    """Independent brute-force oracle; compare full inclusion vectors."""
    from itertools import product

    best_value, best_bits = -1, None
    for bits in product((0, 1), repeat=len(items)):
        cost = sum(bit * item[1] for bit, item in zip(bits, items))
        value = sum(bit * item[0] for bit, item in zip(bits, items))
        if cost <= budget and (value > best_value or
                               (value == best_value and bits < best_bits)):
            best_value, best_bits = value, bits
    return best_value, tuple(i for i, bit in enumerate(best_bits) if bit)


def run_tests():
    from itertools import product

    fixed = [
        ([(6, 2), (10, 4), (12, 5)], 9, (22, (1, 2))),
        ([(5, 2), (5, 2)], 2, (5, (1,))),
        ([], 0, (0, ())),
        ([(8, 3)], 3, (8, (0,))),
        ([(8, 3)], 2, (0, ())),
        ([(8, 3)], 0, (0, ())),
        ([(0, 1), (4, 2)], 3, (4, (1,))),
        ([(100, 9), (4, 2)], 2, (4, (1,))),
        ([(3, 2), (4, 2), (8, 3)], 4, (8, (2,))),
        ([(17, 9), (10, 3), (14, 3), (7, 5), (16, 5)], 10, (30, (2, 4))),
    ]

    def check(items, budget):
        before = items[:]
        expected = subset_oracle(items, budget)
        for solver in (maxVal, fastMaxVal):
            stats = {}
            actual = solver(items, budget, stats)
            assert actual == expected, (items, budget, solver.__name__, actual, expected)
            value, chosen = actual
            assert chosen == tuple(sorted(set(chosen)))
            assert sum(items[i][1] for i in chosen) <= budget
            assert sum(items[i][0] for i in chosen) == value
            assert items == before
            if solver is fastMaxVal:
                assert stats['states'] <= (len(items) + 1) * (budget + 1)
                assert stats['calls'] == stats['states'] + stats['hits']
        return expected

    for items, budget, expected in fixed:
        assert check(items, budget) == expected
    count = 0
    for n in range(5):
        for sequence in product(((0, 1), (2, 1), (2, 2), (3, 3)), repeat=n):
            for budget in range(7):
                check(list(sequence), budget)
                count += 1
    # Same-shaped but different inputs must not share cached results.
    assert fastMaxVal([(9, 2)], 2) == (9, (0,))
    assert fastMaxVal([(1, 2)], 2) == (1, (0,))
    large = [(1, 1)] * 200
    assert fastMaxVal(large, 100) == (100, tuple(range(100, 200)))
    assert large == [(1, 1)] * 200
    print(f'W10 PASS: {len(fixed)} fixed, {count} exhaustive audits, cache isolation, 1 large.')
    print('n budget value plain_calls memo_calls memo_hits memo_states')
    for n in (6, 12, 18):
        items, budget = [(1, 1)] * n, n // 2
        plain, memo = {}, {}
        assert maxVal(items, budget, plain) == fastMaxVal(items, budget, memo)
        assert memo['calls'] < plain['calls']
        print(n, budget, budget, plain['calls'], memo['calls'], memo['hits'], memo['states'])


if __name__ == '__main__':
    run_tests()
