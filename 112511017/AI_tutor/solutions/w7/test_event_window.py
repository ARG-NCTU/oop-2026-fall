from itertools import combinations_with_replacement

import pytest

from event_window import count_events


@pytest.mark.parametrize(
    "timestamps,start,end,expected",
    [
        ([2, 4, 4, 7, 10], 4, 8, 3),
        ([2, 4, 4, 7, 10], 4, 4, 0),
        ([2, 4, 4, 7, 10], 8, 12, 1),
        ([], -1, 1, 0),
        ([5], 5, 6, 1),
        ([5], 4, 5, 0),
        ([5], 6, 7, 0),
        ([3, 3, 3, 3], 3, 4, 4),
        ([3, 3, 3, 3], 2, 3, 0),
        ([-9, -3, -3, 0, 8], -3, 0, 2),
        ([1, 3, 5], 4, 2, 0),
        ([1, 3, 5], -100, 100, 3),
    ],
)
def test_examples_and_boundaries(timestamps, start, end, expected):
    before = timestamps.copy()
    assert count_events(timestamps, start, end) == expected
    assert timestamps == before


def test_exhaustive_small_sorted_logs():
    # Independent full-scan oracle, including every duplicate arrangement.
    for length in range(7):
        for values in combinations_with_replacement(range(4), length):
            timestamps = list(values)
            for start in range(-1, 6):
                for end in range(-1, 6):
                    expected = sum(start <= value < end for value in timestamps)
                    assert count_events(timestamps, start, end) == expected
            assert timestamps == list(values)


class IndexedLog:
    """Fail on slicing, iteration, or mutation; count indexed reads."""

    def __init__(self, values):
        self.values = values
        self.reads = 0

    def __len__(self):
        return len(self.values)

    def __getitem__(self, index):
        assert isinstance(index, int), "The search must not copy slices"
        self.reads += 1
        return self.values[index]

    def __iter__(self):
        raise AssertionError("The search must not scan the log")


def test_large_log_uses_logarithmic_number_of_reads():
    values = [index // 3 for index in range(100_000)]
    windows = [(0, 1), (100, 200), (-1, 100_000), (33_333, 33_334), (40_000, 50_000)]
    for start, end in windows:
        log = IndexedLog(values)
        assert count_events(log, start, end) == sum(start <= value < end for value in values)
        assert log.reads <= 2 * len(values).bit_length()


def test_empty_window_does_not_read_the_log():
    for start, end in [(5, 5), (7, 3)]:
        log = IndexedLog([1, 2, 3])
        assert count_events(log, start, end) == 0
        assert log.reads == 0
