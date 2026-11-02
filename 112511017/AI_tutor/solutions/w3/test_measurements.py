from measurements import parse_measurements


def test_mixed_example():
    assert parse_measurements(["A,20", "bad", "B,x", "A,35"]) == (
        {"A": 55}, [(1, "format"), (2, "number")]
    )


def test_boundaries_example():
    assert parse_measurements(["A,0", "B,100", "B,101", "A,-1"]) == (
        {"A": 0, "B": 100}, [(2, "range"), (3, "range")]
    )


def test_empty_example():
    assert parse_measurements([]) == ({}, [])


def test_blank_name_and_extra_separator():
    assert parse_measurements([" ,2", "S,1,2"]) == (
        {}, [(0, "format"), (1, "format")]
    )


def test_numeric_conversion_errors():
    assert parse_measurements(["A,", "A,2.5", "A,no"]) == (
        {}, [(0, "number"), (1, "number"), (2, "number")]
    )


def test_whitespace_and_signed_integer():
    assert parse_measurements([" A , +5 ", "A,005"]) == ({"A": 10}, [])


def test_invalid_reading_does_not_change_total():
    assert parse_measurements(["A,40", "A,101", "A,60"]) == (
        {"A": 100}, [(1, "range")]
    )


def test_input_is_unchanged():
    lines = ["A,20", "bad"]
    parse_measurements(lines)
    assert lines == ["A,20", "bad"]


def test_maximum_line_count():
    assert parse_measurements(["A,100"] * 1000) == ({"A": 100000}, [])
