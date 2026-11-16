"""Find the cheapest route through toll stations with fee-waiver coupons."""


def minimum_toll(fees, k):
    """Start before the first station and move one or two spaces at a time.

    Each coupon waives the fee at one station. The exit has no fee.
    """
    exit_position = len(fees)
    start = (-1, min(k, exit_position))
    memo = {}
    pending = [start]

    # Use a stack to evaluate the memoized search without recursive calls.
    while pending:
        state = pending[-1]
        position, coupons = state
        if position == exit_position:
            memo[state] = 0
            pending.pop()
            continue

        choices = []
        for next_position in range(position + 1, min(position + 2, exit_position) + 1):
            if next_position == exit_position:
                choices.append(((next_position, coupons), 0))
            else:
                choices.append(((next_position, coupons), fees[next_position]))
                if coupons > 0:
                    choices.append(((next_position, coupons - 1), 0))

        for next_state, fee in choices:
            if next_state not in memo:
                pending.append(next_state)
                break
        else:
            memo[state] = min(fee + memo[next_state] for next_state, fee in choices)
            pending.pop()

    return memo[start]


if __name__ == "__main__":
    print(minimum_toll([7], 0))
