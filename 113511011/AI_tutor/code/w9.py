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
