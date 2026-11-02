from math import comb

from delivery_routes import count_delivery_routes


def test_blocked_center_example():
    assert count_delivery_routes(3, 3, [(1, 1)]) == 2


def test_rectangle_example():
    assert count_delivery_routes(2, 3, []) == 3


def test_blocked_single_cell_example():
    assert count_delivery_routes(1, 1, [(0, 0)]) == 0


def test_unblocked_single_cell():
    assert count_delivery_routes(1, 1, []) == 1


def test_blocked_endpoints():
    assert count_delivery_routes(2, 2, [(0, 0)]) == 0
    assert count_delivery_routes(2, 2, [(1, 1)]) == 0


def test_complete_barrier():
    assert count_delivery_routes(3, 3, [(1, 0), (1, 1), (1, 2)]) == 0


def test_single_row_and_column():
    assert count_delivery_routes(1, 5, []) == 1
    assert count_delivery_routes(5, 1, []) == 1
    assert count_delivery_routes(1, 5, [(0, 2)]) == 0


def test_input_is_unchanged():
    blocked = [(1, 1)]
    count_delivery_routes(3, 3, blocked)
    assert blocked == [(1, 1)]


def test_maximum_grid_against_combinatorial_count():
    assert count_delivery_routes(20, 20, []) == comb(38, 19)
