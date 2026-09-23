import pytest

from grade import average, letter_grade


@pytest.mark.parametrize(
    "score, expected",
    [
        (95, "A"),
        (85, "B"),
        (75, "C"),
        (65, "D"),
        (55, "F"),
        (90, "A"),
        (80, "B"),
        (70, "C"),
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


@pytest.mark.parametrize(
    "scores, expected",
    [
        ([90, 80, 70], 80),
        ([100, 90, 80], 90),
        ([60, 50, 40], 50),
    ],
)
def test_average_scores(scores, expected):
    assert average(scores) == expected


def test_average_empty_list_raises_error():
    with pytest.raises(ValueError):
        average([])


@pytest.mark.parametrize(
    "scores",
    [
        [90, -10, 80],
        [100, 110, 90],
    ],
)
def test_average_invalid_scores(scores):
    with pytest.raises(ValueError):
        average(scores)