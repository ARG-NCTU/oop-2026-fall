def letter_grade(Score):
	if Score>100 or Score<0:
		raise ValueError
	elif Score<=100 and Score>=90:
		return "A"
	elif Score<90 and Score>=80:
                return "B"
	elif Score<80 and Score>=70:
                return "C"
	elif Score<70 and Score>=60:
                return "D"
	elif Score<60:
                return "F"

def average(scores):
    if len(scores) == 0:
        raise ValueError("scores cannot be empty")

    return sum(scores) / len(scores)
