from itertools import combinations, product

import pytest

from upgrade_cost import min_upgrade_cost


@pytest.mark.parametrize(
    "options,target,expected",
    [
        ([(5, 8), (4, 5), (4, 5)], 10, 8),
        ([], 0, 0),
        ([], 1, None),
        ([(3, 4)], 4, 3),
        ([(3, 4)], 8, None),
        ([(9, 20)], 10, 9),
        ([(2, 3), (2, 3)], 6, 4),
        ([(5, 5), (2, 3), (2, 2)], 5, 4),
        ([(1, 1)], 0, 0),
        ([(2, 1), (3, 1)], 3, None),
    ],
)
def test_minimum_cost_reachability_and_single_use(options, target, expected):
    before = options.copy()
    assert min_upgrade_cost(options, target) == expected
    assert options == before


def test_memo_does_not_leak_between_calls():
    assert min_upgrade_cost([(2, 3)], 3) == 2
    assert min_upgrade_cost([(9, 3)], 3) == 9
    assert min_upgrade_cost([(2, 1)], 3) is None


def test_exhaustive_small_instances_against_all_subsets():
    choices = [(1, 1), (2, 3), (4, 2)]
    for size in range(6):
        for options in product(choices, repeat=size):
            subsets = [
                (sum(options[i][0] for i in indices),
                 sum(options[i][1] for i in indices))
                for count in range(size + 1)
                for indices in combinations(range(size), count)
            ]
            for target in range(10):
                feasible = [cost for cost, gain in subsets if gain >= target]
                expected = min(feasible) if feasible else None
                assert min_upgrade_cost(list(options), target) == expected


def test_maximum_option_count_and_target():
    assert min_upgrade_cost([(1, 10)] * 100, 1000) == 100
    assert min_upgrade_cost([(1, 9)] * 100, 1000) is None
