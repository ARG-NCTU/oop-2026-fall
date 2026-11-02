from itertools import product

import pytest

from event_order import count_out_of_order


@pytest.mark.parametrize(
    "values,expected",
    [
        ([2, 4, 1, 3, 5], 3),
        ([3, 2, 1], 3),
        ([2, 2, 1], 2),
        ([], 0),
        ([9], 0),
        ([1, 2, 3], 0),
        ([5, 5, 5], 0),
        ([-1, -3, -2], 2),
        ([0, -1, 0, -1], 3),
    ],
)
def test_counts_strictly_reversed_pairs_without_mutation(values, expected):
    before = values.copy()
    assert count_out_of_order(values) == expected
    assert values == before


def test_exhaustive_small_logs_against_pair_enumeration():
    for size in range(8):
        for values in product(range(3), repeat=size):
            expected = sum(
                values[i] > values[j]
                for i in range(size)
                for j in range(i + 1, size)
            )
            assert count_out_of_order(list(values)) == expected


def test_maximum_reverse_log():
    size = 100_000
    values = list(range(size, 0, -1))
    assert count_out_of_order(values) == size * (size - 1) // 2
    assert values[0] == size and values[-1] == 1
