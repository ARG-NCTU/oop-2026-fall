import pytest

from grade import average, letter_grade


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


@pytest.mark.parametrize("score", [-1, 101])
def test_letter_grade_invalid_scores(score):
    with pytest.raises(ValueError):
        letter_grade(score)


def test_average_scores():
    assert average([80, 90, 100]) == 90


def test_average_empty_list_raises_error():
    with pytest.raises(ValueError):
        average([])