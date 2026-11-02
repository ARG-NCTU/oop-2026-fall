import pytest

from locker import Locker, locker_report


def test_duplicates_and_capacity_example():
    operations = [
        ("add", "pen"), ("add", "pen"), ("add", "book"),
        ("remove", "pen"), ("add", "book"),
    ]
    assert locker_report(2, operations) == (
        [True, True, False, True, True], "2/2:pen|book"
    )


def test_missing_removal_example():
    operations = [("remove", "pen"), ("add", "eraser"), ("remove", "eraser")]
    assert locker_report(1, operations) == ([False, True, True], "0/1:")


def test_empty_example():
    assert locker_report(3, []) == ([], "0/3:")


def test_independent_instances():
    first, second = Locker(2), Locker(2)
    first.add("pen")
    assert first.snapshot() == ["pen"]
    assert second.snapshot() == []


def test_snapshot_does_not_expose_internal_list():
    locker = Locker(2)
    locker.add("pen")
    copy = locker.snapshot()
    copy.append("book")
    assert locker.snapshot() == ["pen"]


def test_missing_remove_raises_without_mutation():
    locker = Locker(2)
    locker.add("pen")
    with pytest.raises(ValueError):
        locker.remove("book")
    assert locker.snapshot() == ["pen"]


def test_remove_only_first_duplicate():
    locker = Locker(3)
    locker.add("pen")
    locker.add("book")
    locker.add("pen")
    locker.remove("pen")
    assert locker.snapshot() == ["book", "pen"]


def test_full_add_preserves_state():
    locker = Locker(1)
    assert locker.add("pen") is True
    assert locker.add("book") is False
    assert str(locker) == "1/1:pen"


def test_maximum_operation_count():
    operations = [("add", "pen"), ("remove", "pen")] * 500
    results, final = locker_report(10, operations)
    assert results == [True] * 1000
    assert final == "0/10:"
