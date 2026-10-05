"""Week 4 AI Tutor B: Score Adjustment and Passing Counter.

Input scores are numbers between 0 and 100.
Each function returns a result; demonstration output is printed in main.
"""


def apply_adjustment(score, adjustment):
    """Apply the supplied adjustment function to one score."""
    return adjustment(score)


def add_bonus(score):
    """Add five points, keeping the adjusted score at most 100."""
    return min(score + 5, 100)


def is_passing(score):
    """Return True if the score is at least 60, otherwise False."""
    return score >= 60


def count_passing(scores, adjustment):
    """Count passing scores after adjustment without changing scores."""
    count = 0
    for score in scores:
        adjusted_score = apply_adjustment(score, adjustment)
        if is_passing(adjusted_score):
            count += 1
    return count


if __name__ == "__main__":
    scores = [50, 55, 60, 98]
    print("Original scores:", scores)
    print("Passing count after bonus:", count_passing(scores, add_bonus))
    print("Bonus for 98:", add_bonus(98))
    print("Passing count for empty list:", count_passing([], add_bonus))

    assert count_passing(scores, add_bonus) == 3
    assert count_passing([], add_bonus) == 0
    assert count_passing([54, 55], add_bonus) == 1
    assert apply_adjustment(98, add_bonus) == 100
    assert is_passing(59) is False
    assert is_passing(60) is True
    assert scores == [50, 55, 60, 98]
    print("All checks passed!")
