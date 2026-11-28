from collections import deque


def security_terminal_unlock(start: int, target: int, limit: int, forbidden: list[int]):
    """
    This function finds the minimum number of steps required to unlock a security terminal.
    """
    # convert to set for O(1) lookups
    forbidden_set = set(forbidden)

    # if the start or target is forbidden, return -1
    if start in forbidden_set or target in forbidden_set:
        return -1

    queue = deque([(start, 0)])  # (current number, steps taken)
    visited = set([start])

    while queue:
        current, steps = queue.popleft()

        if current == target:
            return steps

        # possible next moves
        for next_num in (current + 1, current - 1, current * 2):
            # check if the next number is within limits and not forbidden or visited
            if 0 <= next_num <= limit and next_num not in forbidden_set and next_num not in visited:
                visited.add(next_num)
                queue.append((next_num, steps + 1))

    return -1
