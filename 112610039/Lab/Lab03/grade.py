def letter_grade(score):
    if(score < 0 or score > 100):
        raise ValueError
    
    if(score >= 90):
        return "A";
    elif(score >= 80):
        return "B";
    elif(score >= 70):
        return "C";
    elif(score >= 60):
        return "D";
    else:
        return "F";

def average(scores):
    if(len(scores) == 0):
        raise ValueError

    sum = 0
    for score in scores:
        sum += score
    avg = sum / len(scores)

    return avg