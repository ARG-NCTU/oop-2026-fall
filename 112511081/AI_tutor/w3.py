# W3 AI Tutor Part B: Robust Score Average (OCW Lec 7: Testing, Debugging, Exceptions, Assertions)
#
# raw is a list of strings typed in by a TA, e.g. ["90", "85.5", "abs", "70"].
# Return the average of the valid scores.
#   - an entry that cannot be converted to a number is skipped
#   - a number outside 0..100 is a real data error -> raise ValueError
#   - if no valid score is left, return None
# The function must not modify raw.


def average_score(raw):
    assert type(raw) == list, 'raw must be a list'

    total = 0.0
    count = 0
    for entry in raw:
        try:
            score = float(entry)
        except (ValueError, TypeError):
            continue                      # not a number: skip this entry only
        if score != score:                # float("nan") is the only value != itself
            continue
        if score < 0 or score > 100:
            raise ValueError('score out of range: ' + str(entry))
        total += score
        count += 1

    if count == 0:
        return None
    return total / count


if __name__ == "__main__":
    # provided examples
    assert average_score(["90", "80", "70"]) == 80.0
    assert average_score(["90", "abs", "70"]) == 80.0
    assert average_score(["100", " 50 "]) == 75.0       # float() ignores spaces

    # boundary values
    assert average_score(["0", "100"]) == 50.0
    assert average_score(["100"]) == 100.0

    # nothing valid left
    assert average_score([]) is None
    assert average_score(["abs", "", "n/a"]) is None
    assert average_score([None, "60"]) == 60.0          # float(None) is a TypeError
    assert average_score(["nan", "60"]) == 60.0         # float("nan") converts but is not a score

    # out-of-range must raise, not be skipped
    for bad in (["101"], ["90", "-1"]):
        try:
            average_score(bad)
        except ValueError:
            pass
        else:
            assert False, 'expected ValueError for ' + str(bad)

    # the input list is not modified
    data = ["90", "abs", "70"]
    average_score(data)
    assert data == ["90", "abs", "70"]

    print("all tests passed")
