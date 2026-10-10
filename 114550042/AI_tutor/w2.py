def nested_depth_sum(d: dict[str, int | dict], depth: int = 1):
    total: int = 0
    for v in d.values():
        if isinstance(v, dict):
            total += nested_depth_sum(v, depth + 1)
        else:
            total += v * depth
    return total
