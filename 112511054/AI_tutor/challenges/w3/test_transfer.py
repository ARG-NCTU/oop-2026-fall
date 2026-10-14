import pytest
from transfer import transfer


@pytest.mark.parametrize("source, destination, amount, expected", [
    (100, 20, 30, (70, 50)),
    (5, 0, 5, (0, 5)),
    (0, 0, 0, (0, 0)),
    (10000, 0, 10000, (0, 10000)),
    (1, 9999, 1, (0, 10000)),
    (10000, 10000, 0, (10000, 10000)),
])
def test_normal_and_boundaries(source, destination, amount, expected):
    result = transfer(source, destination, amount)
    assert result == expected
    assert sum(result) == source + destination


@pytest.mark.parametrize("source, destination, amount", [
    (10, 20, 11), (5, 10000, 1),
    (-1, 0, 0), (0, -1, 0), (0, 0, -1),
    (10001, 0, 0), (0, 10001, 0), (10000, 0, 10001),
])
def test_invalid_values(source, destination, amount):
    with pytest.raises(ValueError):
        transfer(source, destination, amount)


def test_balance_conservation_over_many_transfers():
    source, destination = 1000, 0
    for amount in (1, 2, 7, 10, 80, 100, 300, 500):
        source, destination = transfer(source, destination, amount)
        assert source + destination == 1000
    assert (source, destination) == (0, 1000)
