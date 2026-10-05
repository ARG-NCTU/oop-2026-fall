def remove_blocked(values, blocked):
    values_copy = values[:]

    for e in values_copy:
        if e in blocked:
            values.remove(e)

    return values


# Test
values = [1, 2, 3, 2, 4]
blocked = [2, 4]

print(remove_blocked(values, blocked))
# Expected: [1, 3]


# Edge case
values = [2, 2, 2, 3]
blocked = [2]

print(remove_blocked(values, blocked))
# Expected: [3]