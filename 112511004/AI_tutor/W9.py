"""Schedule the maximum number of activities in one venue."""


def max_activities(intervals):
    # An earlier finish leaves at least as much time for later activities.
    ordered = sorted(intervals, key=lambda activity: activity[1])
    count = 0
    last_end = 0  # All start times are nonnegative by the specification.

    for start, end in ordered:
        if start >= last_end:
            count += 1
            last_end = end

    return count


if __name__ == "__main__":
    print(max_activities([[1, 4], [2, 3], [3, 5], [5, 6]]))
