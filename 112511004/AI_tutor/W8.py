"""Find the largest sum of two distinct activity costs within budget."""


def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort(values):
    if len(values) < 2:
        return values[:]
    middle = len(values) // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])
    return merge(left, right)


def best_pair_sum(costs, budget):
    """Return the greatest sum of two distinct entries <= budget, or -1.

    Equal prices at different positions are allowed. Input is not modified.
    Time: O(n log n). Extra space: O(n), including the sorting workspace.
    """
    prices = merge_sort(costs)
    best = -1

    for i in range(len(prices) - 1):
        limit = budget - prices[i]
        low = i + 1  # Only later positions: never reuse the same activity.
        high = len(prices) - 1

        while low <= high:
            mid = (low + high) // 2
            if prices[mid] <= limit:
                total = prices[i] + prices[mid]
                if total > best:
                    best = total
                # This partner fits; look for a more expensive one.
                low = mid + 1
            else:
                high = mid - 1

    return best


if __name__ == "__main__":
    print(best_pair_sum([8, 3, 5, 2], 10))
