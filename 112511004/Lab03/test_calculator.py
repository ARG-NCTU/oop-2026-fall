import pytest

from calculator import add, divide


@pytest.mark.parametrize(
    "a, b, expected",
    [(2, 3, 5), (-2, 3, 1), (0, 0, 0)],
)
def test_add_two_numbers(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [(10, 2, 5), (1, 3, 1 / 3), (-6, 2, -3), (0, 5, 0)],
)
def test_divide_valid_numbers(a, b, expected):
    assert divide(a, b) == pytest.approx(expected)


def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError):
        divide(10, 0)
