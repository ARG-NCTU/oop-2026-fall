def greedy_coins(coins, amount):
    used = []
    for c in sorted(coins, reverse=True):
        while amount >= c:
            used.append(c)
            amount -= c
    if amount != 0:
        return None
    return used


if __name__ == "__main__":
    print(greedy_coins([1, 5, 10, 50], 68))
    print(greedy_coins([1, 3, 4], 6))
    print(greedy_coins([5, 10], 3))
    print(greedy_coins([1, 5, 10], 0))
