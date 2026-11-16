"""Find the minimum daily capacity for deliveries in the original order."""


def minimum_capacity(weights, days):
    """Assume nonempty positive integer weights and 1 <= days <= len(weights)."""
    low = weights[0]
    high = 0
    for weight in weights:
        if weight > low:
            low = weight
        high += weight

    while low < high:
        mid = (low + high) // 2
        used_days = 1
        current_load = 0

        for weight in weights:
            if current_load + weight > mid:
                used_days += 1
                current_load = weight
            else:
                current_load += weight

        if used_days <= days:
            high = mid
        else:
            low = mid + 1

    return low


if __name__ == "__main__":
    print(minimum_capacity([2, 5, 3], 1))
