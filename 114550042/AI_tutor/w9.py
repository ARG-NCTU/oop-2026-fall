def optimal_task_exec_order(tasks: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Return the optimal order of task execution based on their duration and weight."""
    return sorted(
        tasks, key=lambda x: x[1] / x[0], reverse=True
    )  # Sort by weight/duration ratio in descending order


def optimal_task_punishment(tasks: list[tuple[int, int]]) -> int:
    """Calculate the total punishment for executing tasks in the optimal order."""
    ordered_tasks = optimal_task_exec_order(tasks)
    total_punishment = 0
    current_time = 0

    for duration, weight in ordered_tasks:
        current_time += duration
        total_punishment += current_time * weight

    return total_punishment


# wBtA, wAtB
# wB/tB, wA/tA
