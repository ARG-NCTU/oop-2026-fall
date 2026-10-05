def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("b cannot be zero")
    return a / b
