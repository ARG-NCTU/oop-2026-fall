def filter_and_summarize(data: list[int], bound: tuple[int, int]) -> tuple[list[int], int, float]:
    lower_bound, upper_bound = bound

    result = []
    last = float("nan")
    for i in data:
        # only python can x <= i <= y, other languages need to use x <= i && i <= y
        if lower_bound <= i <= upper_bound and i != last:
            last = i
            result.append(i)

    # (filtered_list, count, average)
    count = len(result)
    average = sum(result) / count if count > 0 else 0.0
    return (result, count, average)
