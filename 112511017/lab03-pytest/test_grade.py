import pytest

from grade import letter_grade


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
