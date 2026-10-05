"""Week 5: non-mutating list processing and copying a 2-D integer list."""

def clean_scores(scores):
    """Return (valid unique sorted scores, invalid count).

    Input: a list of integers. Valid scores are inclusively between 0 and 100.
    Repeated valid scores appear once; duplicates are not counted as invalid.
    The input is not mutated.
    """
    valid = []
    invalid_count = 0
    for score in scores:
        if 0 <= score <= 100:
            if score not in valid:
                valid.append(score)
        else:
            invalid_count += 1
    return (sorted(valid), invalid_count)

def remove_blocked(items, blocked):
    """Return items absent from blocked; retain order/duplicates; mutate neither input."""
    result = []
    for item in items:
        if item not in blocked:
            result.append(item)
    return result

def copy_score_rows(rows):
    """Copy each row of a 2-D list of integers. Not a general deep copy."""
    result = []
    for row in rows:
        result.append(row[:])
    return result

if __name__ == "__main__":
    scores = [80, -5, 60, 80, 105, 100, 0]
    print("Clean scores:", clean_scores(scores))
    print("Remove blocked:", remove_blocked([1, 2, 2, 3, 4], [1, 2]))
    original = [[80, 90], [60, 70]]
    backup = copy_score_rows(original)
    backup[0][0] = 100
    print("Original rows:", original)
    print("Backup rows:", backup)

    assert clean_scores(scores) == ([0, 60, 80, 100], 2)
    assert scores == [80, -5, 60, 80, 105, 100, 0]
    assert clean_scores([0, 100, -1, 101, 100]) == ([0, 100], 2)
    assert clean_scores([]) == ([], 0)
    assert clean_scores([-1, 101, -1]) == ([], 3)
    assert clean_scores([60, 60, 60]) == ([60], 0)
    assert remove_blocked([1, 2, 2, 3, 4], [1, 2]) == [3, 4]
    assert remove_blocked([3, 3, 2, 1], [2]) == [3, 3, 1]
    assert remove_blocked([], [1]) == []
    assert remove_blocked([1, 1], [1]) == []
    items = [1, 2, 3]
    blocked = [1, 2]
    remaining = remove_blocked(items, blocked)
    assert remaining == [3]
    assert items == [1, 2, 3] and blocked == [1, 2]
    assert remaining is not items
    assert original == [[80, 90], [60, 70]]
    assert backup is not original
    assert backup[0] is not original[0]
    assert backup[1] is not original[1]
    empty = []
    empty_copy = copy_score_rows(empty)
    assert empty_copy == [] and empty_copy is not empty
    rows = [[]]
    row_copy = copy_score_rows(rows)
    assert row_copy == [[]] and row_copy[0] is not rows[0]
    print("All checks passed!")

