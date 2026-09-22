import pytest
from grade import letter_grade, average_scores
from statistics import mean 

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


def test_letter_grade_score_bounds_l():
    with pytest.raises(ValueError):
        letter_grade(-1)


def test_letter_grade_score_bounds_h():
    with pytest.raises(ValueError):
        letter_grade(101)


def test_average():
    l = [80, 90, 100]
    # I use the average to test the average
    # Could actually blow up in my face due to floating point error
    assert average_scores(l) == mean(l)


def test_average_error():
    with pytest.raises(ValueError):
        average_scores([])


# def test_average_e2():
#     with pytest.raises(ValueError):
#         average_scores([114, 51, 4])
