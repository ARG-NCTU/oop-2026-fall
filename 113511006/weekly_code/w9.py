"""Week 9 | Greedy: choose as many talks as possible with a cleanup gap."""


def schedule_talks(talks, cleanup):
    """Return chosen original indices in chronological finish order.

    Each talk is a (start, finish) pair with start < finish.
    A cleanup gap is required between consecutive talks.
    """
    if cleanup < 0:
        raise ValueError("cleanup must be nonnegative")

    ordered = sorted(enumerate(talks), key=lambda item: (item[1][1], item[1][0], item[0]))
    chosen = []
    available_at = float("-inf")
    for index, (start, finish) in ordered:
        if start >= available_at:
            chosen.append(index)
            available_at = finish + cleanup
    return chosen


if __name__ == "__main__":
    assert schedule_talks([(1, 3), (3, 5), (5, 7)], 0) == [0, 1, 2]
    assert schedule_talks([(1, 3), (3, 5), (5, 7)], 1) == [0, 2]
    assert schedule_talks([(2, 6), (1, 2), (3, 4), (4, 5)], 0) == [1, 2, 3]
    assert schedule_talks([], 2) == []
    print("Week 9: 4 tests passed")
