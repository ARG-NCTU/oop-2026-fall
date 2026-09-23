def safe_average(scores):
    if len(scores) == 0:
        raise ValueError("scores cannot be empty")

    total = 0

    for score in scores:
        if not isinstance(score, (int, float)):
            raise TypeError("score must be a number")

        if score < 0 or score > 100:
            raise ValueError("score must be between 0 and 100")

        total += score

    return total / len(scores)


# Normal cases
print(safe_average([80, 90, 100]))
print(safe_average([60, 70, 80, 90]))

# Edge case
try:
    print(safe_average([80, 90, 101]))
except ValueError as error:
    print(type(error).__name__)