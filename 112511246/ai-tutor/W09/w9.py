def greedy_coins(coins, amount):
    used = []
    for c in sorted(coins, reverse=True):
        while amount >= c:
            used.append(c)
            amount -= c
    if amount != 0:
        return None
    return used


def best_coins_brute(coins, amount):
    if amount == 0:
        return []
    best = None
    for c in coins:
        if c <= amount:
            rest = best_coins_brute(coins, amount - c)
            if rest is not None and (best is None or len(rest) + 1 < len(best)):
                best = [c] + rest
    return best


if __name__ == "__main__":
    print(greedy_coins([1, 5, 10, 50], 68))
    print(greedy_coins([1, 3, 4], 6))
    print(greedy_coins([5, 10], 3))
    print(greedy_coins([1, 5, 10], 0))

    print(sorted(best_coins_brute([1, 3, 4], 6), reverse=True))
    print(sorted(best_coins_brute([1, 5, 10], 18), reverse=True))
