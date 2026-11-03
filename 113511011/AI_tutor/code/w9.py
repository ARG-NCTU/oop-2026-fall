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
