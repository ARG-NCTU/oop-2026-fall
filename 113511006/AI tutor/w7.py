"""Week 7: explicit input errors and a checked balance invariant."""


def process_withdrawals(balance, withdrawals):
    """Return the final balance; never modify the withdrawal list.

    Balance and amounts must be nonnegative integers (bool excluded).
    Validate all types/signs before checking funds in order.
    TypeError: invalid types. ValueError: negative values/insufficient funds.
    """
    if not isinstance(balance, int) or isinstance(balance, bool):
        raise TypeError("balance must be an integer, not bool")
    if balance < 0:
        raise ValueError("balance must be nonnegative")
    if not isinstance(withdrawals, list):
        raise TypeError("withdrawals must be a list")
    for amount in withdrawals:
        if not isinstance(amount, int) or isinstance(amount, bool):
            raise TypeError("each withdrawal must be an integer, not bool")
        if amount < 0:
            raise ValueError("withdrawals must be nonnegative")

    remaining = balance
    for amount in withdrawals:
        if amount > remaining:
            raise ValueError("insufficient funds")
        remaining = remaining - amount
        assert remaining >= 0, "internal balance invariant violated"
    return remaining


if __name__ == "__main__":
    print(process_withdrawals(100, [20, 30]))
    print(process_withdrawals(50, [50]))
    try:
        process_withdrawals(50, [30, 30])
    except ValueError as error:
        print("ValueError:", error)
