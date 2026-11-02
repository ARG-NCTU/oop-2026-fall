def count_out_of_order(timestamps):
    """Count pairs i < j with timestamps[i] > timestamps[j], without mutation."""
    def sort_and_count(values):
        if len(values) < 2:
            return values[:], 0

        middle = len(values) // 2
        left, left_count = sort_and_count(values[:middle])
        right, right_count = sort_and_count(values[middle:])
        merged = []
        count = left_count + right_count
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                count += len(left) - i
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, count

    return sort_and_count(timestamps)[1]
