from itertools import groupby, product

import pytest

from compress_events import compress_events


@pytest.mark.parametrize("events, expected", [
    (["idle", "idle", "move", "move", "move", "idle"],
     [("idle", 2), ("move", 3), ("idle", 1)]),
    ([], []),
    (["alarm"], [("alarm", 1)]),
    (["a", "b", "a"], [("a", 1), ("b", 1), ("a", 1)]),
    (["ok", "ok", "ok"], [("ok", 3)]),
    (["x" * 20, "x" * 20, "y" * 20], [("x" * 20, 2), ("y" * 20, 1)]),
])
def test_examples_and_boundaries(events, expected):
    assert compress_events(events) == expected


def test_input_and_result_are_independent():
    events = ["idle", "idle", "move"]
    result = compress_events(events)
    assert events == ["idle", "idle", "move"]
    events[0] = "alarm"
    result.append(("other", 4))
    assert result[:2] == [("idle", 2), ("move", 1)]
    assert events == ["alarm", "idle", "move"]


def test_exhaustive_short_sequences():
    for length in range(7):
        for sequence in product(["a", "b"], repeat=length):
            events = list(sequence)
            expected = [(label, len(list(group))) for label, group in groupby(events)]
            assert compress_events(events) == expected
            assert [label for label, count in compress_events(events)
                    for _ in range(count)] == events


def test_maximum_uniform_input():
    assert compress_events(["alarm"] * 10000) == [("alarm", 10000)]


def test_maximum_alternating_input():
    events = ["a", "b"] * 5000
    assert compress_events(events) == [(event, 1) for event in events]
