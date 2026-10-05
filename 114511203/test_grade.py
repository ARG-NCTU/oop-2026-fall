import pytest
from grade import letter_grade, average

def test_letter_grade():
    assert letter_grade(95) == "A"
    assert letter_grade(80) == "B"
    assert letter_grade(60) == "D"
    assert letter_grade(59) == "F"

def test_letter_grade_raises_value_error():
    with pytest.raises(ValueError):
        letter_grade(-1)
    with pytest.raises(ValueError):
        letter_grade(101)

def test_average():
    assert average([80, 90, 100]) == 90.0

def test_average_raises_value_error():
    with pytest.raises(ValueError):
        average([])
