import pytest
from grade import letter_grade, average

@pytest.mark.parametrize(
    "score, expected",
    [
        (95, "A"),
        (80, "B"),
        (60, "D"),
        (59, "F"),
    ],
)
def test_letter_grade_valid_scores(score, expected):
    assert letter_grade(score) == expected

def test_letter_grade_invalid_scores():
    with pytest.raises(ValueError):
        letter_grade(-1)
    with pytest.raises(ValueError):
        letter_grade(101)

def test_average_scores():
    assert average([80, 90, 100]) == 90

def test_average_empty_list():
    with pytest.raises(ValueError):
        average([])
