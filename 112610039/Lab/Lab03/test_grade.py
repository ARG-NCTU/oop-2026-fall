import pytest

from grade import letter_grade, average

@pytest.mark.parametrize(
    "score, expected",
    [
        (95, "A"),
        (80, "B"),
        (60, "D"),
        (59, "F"),
        (-1, ValueError),
        (101, ValueError)
    ]
)

def test_letter_grade(score, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            letter_grade(score)
    else:
        assert letter_grade(score) == expected

@pytest.mark.parametrize(
    "scores, expected",
    [
        ([80, 90, 100], 90),
        ([], ValueError)
    ]
)

def test_average(scores, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            average(scores)
    else:
        assert average(scores) == expected