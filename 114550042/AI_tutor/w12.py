import random


def coupon_collector_simulation(n: int, trials: int, seed: int = 0) -> float:
    """
    Simulates the coupon collector's problem.
    """
    random.seed(seed)

    coupons_needed = 0

    for _ in range(trials):
        collected = set()
        while len(collected) < n:
            new_coupon = random.randint(1, n)
            collected.add(new_coupon)
            coupons_needed += 1

    return coupons_needed / trials
