import pytest

from grade import letter_grade, average


def test_letter_grade_a():
    assert letter_grade(95) == "A"


def test_letter_grade_b():
    assert letter_grade(85) == "B"


def test_letter_grade_c():
    assert letter_grade(75) == "C"


def test_letter_grade_d():
    assert letter_grade(65) == "D"


def test_letter_grade_f():
    assert letter_grade(50) == "F"


def test_invalid_score_raises_error():
    with pytest.raises(ValueError):
        letter_grade(120)


def test_average():
    assert average([80, 90, 100]) == 90


def test_average_empty_list_raises_error():
    with pytest.raises(ValueError):
        average([])