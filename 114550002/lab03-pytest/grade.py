def letter_grade(score):

    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100")
    #put your code here
    elif score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    return 'F'
    
    #put your code here
def average(scores):
    if len(scores) == 0:
        raise ValueError("scores cannot be empty")

    return sum(scores) / len(scores)
