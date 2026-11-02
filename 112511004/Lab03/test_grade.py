import pytest

from grade import average, letter_grade


@pytest.mark.parametrize(
    "score, expected",
    [(95, "A"), (85, "B"), (75, "C"), (65, "D"), (50, "F")],
)
def test_letter_grade_valid_scores(score, expected):
    assert letter_grade(score) == expected


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


@pytest.mark.parametrize(
    "scores, expected",
    [([80, 90, 100], 90), ([75], 75), ([0, 100], 50), ([0, 0], 0), ([1, 2, 2], 5 / 3)],
)
def test_average_scores(scores, expected):
    assert average(scores) == pytest.approx(expected)


def test_average_empty_list_raises_error():
    with pytest.raises(ValueError):
        average([])
