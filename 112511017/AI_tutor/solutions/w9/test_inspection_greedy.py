import pytest

from inspection_greedy import greedy_inspections


@pytest.mark.parametrize(
    "jobs,budget,expected",
    [
        ([(10, 60), (20, 100), (30, 120)], 50, ([0, 1], 160)),
        ([], 20, ([], 0)),
        ([(1, 5)], 0, ([], 0)),
        ([(10, 100), (2, 4)], 2, ([1], 4)),
        ([(2, 6), (1, 3), (3, 6)], 3, ([0, 1], 9)),
        ([(3, 10), (2, 5), (1, 1)], 3, ([0], 10)),
        ([(2, 3), (2, 3)], 4, ([0, 1], 6)),
        ([(2, 5)], 2, ([0], 5)),
        ([(3, 2), (2, 3), (1, 4)], 6, ([2, 1, 0], 9)),
    ],
)
def test_density_order_ties_capacity_and_skipping(jobs, budget, expected):
    before = jobs.copy()
    assert greedy_inspections(jobs, budget) == expected
    assert jobs == before
    assert greedy_inspections(jobs, budget) == expected


def test_density_heuristic_is_not_an_optimum_claim():
    jobs = [(10, 60), (20, 100), (30, 120)]
    assert greedy_inspections(jobs, 50) == ([0, 1], 160)
    assert jobs[1][0] + jobs[2][0] == 50
    assert jobs[1][1] + jobs[2][1] == 220


def test_maximum_job_count():
    jobs = [(1, 1)] * 10_000
    assert greedy_inspections(jobs, 10_000) == (list(range(10_000)), 10_000)
