"""New AI-assisted Lecture 6 transfer exercise prepared on 2026-10-05."""


def count_delivery_routes(rows, cols, blocked):
    blocked_lookup = {}
    for cell in blocked:
        blocked_lookup[cell] = True
    memo = {}

    def ways(row, col):
        if row >= rows or col >= cols or (row, col) in blocked_lookup:
            return 0
        if row == rows - 1 and col == cols - 1:
            return 1
        cell = (row, col)
        if cell not in memo:
            memo[cell] = ways(row + 1, col) + ways(row, col + 1)
        return memo[cell]

    return ways(0, 0)
