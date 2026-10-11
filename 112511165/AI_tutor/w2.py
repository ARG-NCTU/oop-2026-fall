def count_nums(nested):
    result = {}

    def helper(item):
        if isinstance(item, int):
            result[item] = result.get(item, 0) + 1
        elif isinstance(item, list):
            for elem in item:
                helper(elem)

    helper(nested)
    return result
