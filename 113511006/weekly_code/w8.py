"""Week 8 | Sorting: count the number of out-of-order pairs."""


def count_inversions(numbers):
    """Return inversions without changing the caller's list; O(n log n)."""
    def merge_count(items):
        if len(items) < 2:
            return items, 0

        middle = len(items) // 2
        left, left_count = merge_count(items[:middle])
        right, right_count = merge_count(items[middle:])
        merged = []
        i = j = 0
        crossings = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                crossings += len(left) - i
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, left_count + right_count + crossings

    return merge_count(list(numbers))[1]


if __name__ == "__main__":
    cases = [([2, 4, 1, 3, 5], 3), ([1, 2, 3], 0),
             ([3, 2, 1], 3), ([2, 2, 1], 2), ([], 0)]
    for data, expected in cases:
        result = count_inversions(data)
        assert result == expected, (data, result, expected)
    print("Week 8: 5 tests passed")
