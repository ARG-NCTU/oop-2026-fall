def min_coins_naive(coins, amount):
    if amount == 0:
        return 0
    best = -1
    for c in coins:
        if c <= amount:
            sub = min_coins_naive(coins, amount - c)
            if sub != -1 and (best == -1 or sub + 1 < best):
                best = sub + 1
    return best


def min_coins(coins, amount, memo=None):
    if memo is None:
        memo = {}
    if amount in memo:
        return memo[amount]
    if amount == 0:
        return 0
    best = -1
    for c in coins:
        if c <= amount:
            sub = min_coins(coins, amount - c, memo)
            if sub != -1 and (best == -1 or sub + 1 < best):
                best = sub + 1
    memo[amount] = best
    return best


if __name__ == "__main__":
    print(min_coins([1, 3, 4], 6))
    print(min_coins([1, 5, 10, 50], 68))
    print(min_coins([5, 10], 3))
    print(min_coins([2], 0))
    print(min_coins([1, 7, 10], 14))

    print(min_coins_naive([1, 3, 4], 6))
