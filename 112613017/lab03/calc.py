def add(x, y):
    return x + y


def div(x, y):
    if y == 0:
        raise ValueError
    return x / y
