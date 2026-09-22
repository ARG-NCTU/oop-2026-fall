def letter_grade(x):
    if x > 100 or x < 0:
        raise ValueError
    if x >= 90:
        return 'A'
    elif x >= 80:
        return 'B'
    elif x >= 70:
        return 'C'
    elif x >= 60:
        return 'D'
    return 'F'


def average_scores(x):
    if len(x) == 0:
        raise ValueError
    s = 0
    for i in x:
        # if i < 0 or i > 100:
        #     raise ValueError
        s += i
    return s / len(x)
