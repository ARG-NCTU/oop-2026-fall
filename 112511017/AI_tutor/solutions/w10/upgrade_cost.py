def min_upgrade_cost(options, target):
    """Minimum cost to reach at least target gain using each option once."""
    memo = {}

    def best(index, remaining):
        if remaining <= 0:
            return 0
        if index == len(options):
            return None
        state = (index, remaining)
        if state not in memo:
            skip = best(index + 1, remaining)
            cost, gain = options[index]
            take_rest = best(index + 1, remaining - gain)
            take = None if take_rest is None else cost + take_rest
            if skip is None:
                memo[state] = take
            elif take is None:
                memo[state] = skip
            else:
                memo[state] = min(skip, take)
        return memo[state]

    return best(0, target)
