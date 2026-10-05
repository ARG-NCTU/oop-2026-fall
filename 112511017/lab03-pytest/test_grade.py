import pytest

from grade import average, letter_grade


@pytest.mark.parametrize(
    "score, expected",
    [
        (100, "A"),
        (90, "A"),
        (89, "B"),
        (80, "B"),
        (79, "C"),
        (70, "C"),
        (69, "D"),
        (60, "D"),
        (59, "F"),
        (0, "F"),
    ],
)
def test_letter_grade_boundaries(score, expected):
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
