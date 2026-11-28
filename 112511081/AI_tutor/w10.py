# W10 AI Tutor Part B: Fewest Coins (MIT 6.0002 Lec 2: Optimization Problems, DP and memoization)
#
# min_coins_greedy(coins, amount)  -> always take the biggest coin that fits (can be wrong / fail)
# min_coins(coins, amount, memo)   -> fewest coins to make amount, None if impossible
#                                     recursion + memo, O(amount * len(coins))


def min_coins_greedy(coins, amount):
    count = 0
    for c in sorted(coins, reverse=True):
        count += amount // c
        amount %= c
    return count if amount == 0 else None


def min_coins(coins, amount, memo=None):
    if memo is None:                         # fresh dict every top-level call
        memo = {}
    if amount == 0:
        return 0
    if amount < 0:
        return None
    if amount in memo:
        return memo[amount]
    best = None
    for c in coins:
        sub = min_coins(coins, amount - c, memo)
        if sub is not None and (best is None or sub + 1 < best):
            best = sub + 1
    memo[amount] = best
    return best


def min_coins_no_memo(coins, amount):
    """same recursion without memo, only for checking small inputs"""
    if amount == 0:
        return 0
    if amount < 0:
        return None
    best = None
    for c in coins:
        sub = min_coins_no_memo(coins, amount - c)
        if sub is not None and (best is None or sub + 1 < best):
            best = sub + 1
    return best


if __name__ == "__main__":
    # provided examples
    assert min_coins([1, 3, 4], 6) == 2              # 3 + 3
    assert min_coins_greedy([1, 3, 4], 6) == 3       # 4 + 1 + 1, greedy is wrong
    assert min_coins([1, 5, 10, 50], 68) == 6        # 50 + 10 + 5 + 1 + 1 + 1

    # edge cases
    assert min_coins([1, 3, 4], 0) == 0
    assert min_coins([2], 3) is None                 # impossible
    assert min_coins_greedy([5, 3], 9) is None and min_coins([5, 3], 9) == 3   # greedy gets stuck
    assert min_coins([7], 7) == 1
    assert min_coins([1, 3, 4], 500) == 125          # fast thanks to memo
    assert min_coins([2], 3) is None and min_coins([1], 3) == 3   # memo not shared between calls

    import random
    for _ in range(200):
        coins = random.sample(range(1, 10), random.randint(1, 3))
        amount = random.randint(0, 15)
        assert min_coins(coins, amount) == min_coins_no_memo(coins, amount)

    print("all tests passed")
