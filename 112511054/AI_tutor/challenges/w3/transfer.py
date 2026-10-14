"""Return the balances after one transfer without changing input state."""


def transfer(source, destination, amount):
    if not (0 <= source <= 10000 and 0 <= destination <= 10000
            and 0 <= amount <= 10000):
        raise ValueError("values must be between 0 and 10000")
    if amount > source:
        raise ValueError("insufficient balance")
    if destination + amount > 10000:
        raise ValueError("destination balance exceeds limit")
    return source - amount, destination + amount


if __name__ == "__main__":
    source, destination, amount = map(int, input().split())
    try:
        print(*transfer(source, destination, amount))
    except ValueError:
        print("INVALID")
