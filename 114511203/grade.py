def letter_grade(score):
    if not (0 <= score <= 100):
        raise ValueError("Score must be between 0 and 100")
    
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def average(scores):
    if not scores:
        raise ValueError("Scores list cannot be empty")
    return sum(scores) / len(scores)
