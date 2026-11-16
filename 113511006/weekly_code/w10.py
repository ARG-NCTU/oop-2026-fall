"""Week 10 | Dynamic Programming: minimum coins for an exact payment."""


def min_coins(coins, amount):
    """Return minimum number of unlimited coins, or -1 if impossible."""
    if amount < 0 or any(coin <= 0 for coin in coins):
        raise ValueError("amount must be nonnegative and coins positive")

    impossible = amount + 1
    dp = [impossible] * (amount + 1)
    dp[0] = 0
    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value:
                dp[value] = min(dp[value], dp[value - coin] + 1)
    return -1 if dp[amount] == impossible else dp[amount]


if __name__ == "__main__":
    assert min_coins([1, 3, 4], 6) == 2  # 3 + 3 beats greedy 4 + 1 + 1
    assert min_coins([2, 4], 7) == -1
    assert min_coins([5], 0) == 0
    assert min_coins([7], 7) == 1
    assert min_coins([], 3) == -1
    print("Week 10: 5 tests passed")
