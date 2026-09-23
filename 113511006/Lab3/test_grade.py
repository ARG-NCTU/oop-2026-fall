import pytest
from grade import letter_grade, average


def test_letter_grade_normal():
    assert letter_grade(95) == "A"
    assert letter_grade(85) == "B"
    assert letter_grade(75) == "C"
    assert letter_grade(65) == "D"
    assert letter_grade(50) == "F"


def test_letter_grade_boundaries():
    assert letter_grade(90) == "A"
    assert letter_grade(89) == "B"
    assert letter_grade(80) == "B"
    assert letter_grade(79) == "C"
    assert letter_grade(70) == "C"
    assert letter_grade(69) == "D"
    assert letter_grade(60) == "D"
    assert letter_grade(59) == "F"


def test_letter_grade_invalid():
    with pytest.raises(ValueError):
        letter_grade(-1)

    with pytest.raises(ValueError):
        letter_grade(101)


def test_average():
    assert average([80, 90, 100]) == 90
    assert average([60, 70, 80, 90]) == 75


def test_average_empty_list():
    with pytest.raises(ValueError):
        average([])
