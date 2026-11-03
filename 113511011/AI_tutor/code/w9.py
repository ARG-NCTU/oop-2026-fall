"""Lecture 1 transfer: compare three feasible workshop-selection policies."""


class Workshop:
    def __init__(self, index, value, duration):
        self.index = index
        self.value = value
        self.duration = duration

    def density(self):
        return self.value / self.duration


def greedy_plan(items, budget, key_function):
    """Return accepted indices, total value and used time; keep inputs intact."""
    ordered = sorted(items, key=key_function, reverse=True)
    chosen = []
    total_value = used_time = 0
    for item in ordered:
        if used_time + item.duration <= budget:
            chosen.append(item.index)
            total_value += item.value
            used_time += item.duration
    return chosen, total_value, used_time


def plan_workshops(workshops, budget):
    """Choose the first maximum-value plan among value, cost and density.

    Preconditions: nonnegative integer values and budget; positive durations.
    This is a best-of-three heuristic, not an exact knapsack solver.
    """
    items = [Workshop(i, value, duration)
             for i, (value, duration) in enumerate(workshops)]
    policies = [
        ("value", lambda item: item.value),
        ("cost", lambda item: -item.duration),
        ("density", lambda item: item.density()),
    ]
    best = None
    for name, key in policies:
        chosen, value, used = greedy_plan(items, budget, key)
        if best is None or value > best[1]:
            best = (chosen, value, used, name)
    return best


def exact_value(workshops, budget):
    """Tiny test oracle only: enumerate subsets without retaining them."""
    best = 0
    for mask in range(1 << len(workshops)):
        value = cost = 0
        for i, (v, c) in enumerate(workshops):
            if mask & (1 << i):
                value += v
                cost += c
        if cost <= budget:
            best = max(best, value)
    return best


def reference_plan(workshops, budget):
    """Independent repeated-maximum simulation with exact rational keys."""
    from fractions import Fraction

    keys = [lambda p: p[0], lambda p: -p[1],
            lambda p: Fraction(p[0], p[1])]
    best = None
    for name, key in zip(("value", "cost", "density"), keys):
        remaining = list(range(len(workshops)))
        chosen, value, used = [], 0, 0
        while remaining:
            # -i explicitly enforces earliest original index on equal keys.
            i = max(remaining, key=lambda i: (key(workshops[i]), -i))
            remaining.remove(i)
            v, c = workshops[i]
            if used + c <= budget:
                chosen.append(i)
                value += v
                used += c
        candidate = (chosen, value, used, name)
        if best is None or value > best[1]:
            best = candidate
    return best


def run_tests():
    from itertools import product

    counter = [(17, 9), (10, 3), (14, 3), (7, 5), (16, 5)]
    fixed = [
        ([(60, 10), (100, 20), (120, 30)], 50, ([2, 1], 220, 50, "value")),
        ([(9, 6), (8, 4), (7, 3)], 7, ([2, 1], 15, 7, "cost")),
        ([], 0, ([], 0, 0, "value")),
        ([(8, 3)], 3, ([0], 8, 3, "value")),
        ([(8, 3)], 2, ([], 0, 0, "value")),
        ([(10, 3), (9, 2)], 5, ([0, 1], 19, 5, "value")),
        ([(10, 9), (6, 3), (6, 3)], 6, ([1, 2], 12, 6, "value")),
        ([(5, 2), (5, 2), (5, 2)], 4, ([0, 1], 10, 4, "value")),
        ([(0, 1), (4, 2)], 3, ([1, 0], 4, 3, "value")),
        ([(4, 1)], 0, ([], 0, 0, "value")),
        (counter, 10, ([1, 2], 24, 6, "cost")),
        ([(100, 9), (4, 2)], 2, ([1], 4, 2, "value")),
    ]
    def check(workshops, budget):
        before = workshops[:]
        actual = plan_workshops(workshops, budget)
        assert actual == reference_plan(workshops, budget), (workshops, budget, actual)
        indices, value, used, _ = actual
        assert len(set(indices)) == len(indices)
        assert all(0 <= i < len(workshops) for i in indices)
        assert used == sum(workshops[i][1] for i in indices) <= budget
        assert value == sum(workshops[i][0] for i in indices)
        assert value <= exact_value(workshops, budget)
        assert workshops == before
        return actual

    for workshops, budget, expected in fixed:
        assert check(workshops, budget) == expected
    count = 0
    alphabet = [(1, 1), (2, 1), (2, 2), (3, 3)]
    for n in range(5):
        for values in product(alphabet, repeat=n):
            for budget in range(7):
                check(list(values), budget)
                count += 1
    assert exact_value(counter, 10) == 30
    assert plan_workshops(counter, 10)[1] == 24
    large = [(1, 1)] * 10000
    assert plan_workshops(large, 10000) == (list(range(10000)), 10000, 10000, "value")
    assert large == [(1, 1)] * 10000
    print(f"W9 PASS: {len(fixed)} fixed, {count} exhaustive audits, 1 large; heuristic gap 6 verified.")


if __name__ == "__main__":
    run_tests()
