"""Week 6: recursive route counting with dictionary memoization."""


def count_routes(n, blocked):
    """Count 1/2-step routes from 0 to n; never land on a blocked key.

    Preconditions: 0 <= n <= 30, blocked is a dictionary with keys
    in 1..n and values True. The input dictionary is not modified.
    """
    memo = {}

    def routes(position):
        if position > n or position in blocked:
            return 0
        if position == n:
            return 1
        if position in memo:
            return memo[position]
        result = routes(position + 1) + routes(position + 2)
        memo[position] = result
        return result

    return routes(0)


if __name__ == "__main__":
    print(count_routes(4, {}))
    print(count_routes(4, {2: True}))
    print(count_routes(0, {}))
