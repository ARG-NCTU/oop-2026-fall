import pytest

from calculator import add, divide


def test_add_two_numbers():
    assert add(2, 3) == 5


def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError):
        divide(10, 0)
