from calc import add, div
import pytest


def test_add_two_numbers():
    assert add(2, 3) == 5


def test_div_zero():
    with pytest.raises(ValueError):
        div(10, 0)
