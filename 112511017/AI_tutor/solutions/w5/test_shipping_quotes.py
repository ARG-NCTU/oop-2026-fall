import pytest

from shipping_quotes import ExpressParcel, Parcel, StandardParcel, shipping_quotes


@pytest.fixture(autouse=True)
def independent_scenario():
    Parcel.next_tracking = 1
    yield
    Parcel.next_tracking = 1


def test_mixed_example():
    assert shipping_quotes([("S", 2), ("E", 2), ("S", 1)]) == (
        ["001:9", "002:16", "003:7"], 32
    )


def test_empty_example():
    assert shipping_quotes([]) == ([], 0)
    assert Parcel.next_tracking == 1


def test_duplicate_express_example():
    assert shipping_quotes([("E", 1), ("E", 1)]) == (["001:13", "002:13"], 26)


def test_duplicate_standard_edge_case():
    assert shipping_quotes([("S", 1), ("S", 1)]) == (["001:7", "002:7"], 14)


def test_counter_continues_across_calls():
    assert shipping_quotes([("S", 1)]) == (["001:7"], 7)
    assert shipping_quotes([("E", 1)]) == (["002:13"], 13)


def test_stored_identifiers_remain_unchanged():
    first = StandardParcel(1)
    second = ExpressParcel(1)
    third = StandardParcel(1)
    assert (first.tracking, second.tracking, third.tracking) == (1, 2, 3)
    assert str(first) == "001:7"
    assert str(second) == "002:13"


def test_maximum_weight():
    assert shipping_quotes([("S", 1000), ("E", 1000)]) == (
        ["001:2005", "002:3010"], 5015
    )


def test_maximum_parcel_count():
    labels, total = shipping_quotes([("S", 1)] * 100)
    assert labels == [f"{number:03d}:7" for number in range(1, 101)]
    assert total == 700
