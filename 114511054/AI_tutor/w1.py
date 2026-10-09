"""W1 coding challenge: student's solution and executable verification.

The clean_batches algorithm and isolation checks were supplied by the student
in the 2026-10-09 tutoring conversation. The tutor formatted the code and added
the three published examples plus an all-filtered batch check.
"""

import copy


def clean_batches(batches, minimum):
    return [[x for x in batch if x >= minimum] for batch in batches]


def run_checks():
    examples = [
        ([[1, 5, 3], [8, 2]], 3, [[5, 3], [8]]),
        ([[], [-3, -1, 0]], -1, [[], [-1, 0]]),
        ([], 10, []),
    ]
    for batches, minimum, expected in examples:
        assert clean_batches(batches, minimum) == expected
    print("PASS: 3 provided examples")

    assert clean_batches([[1, 2]], 3) == [[]]
    print("PASS: all-filtered batch retains its empty position")

    data = [[1, 5, 3], [8, 2], [], [9, 10]]
    snapshot = copy.deepcopy(data)
    result = clean_batches(data, 3)
    assert result == [[5, 3], [8], [], [9, 10]]
    assert data == snapshot
    assert result is not data
    assert all(r is not b for r, b in zip(result, data))

    result[0].append(99)
    result[2].append(0)
    result.append([7])
    assert data == snapshot
    print("PASS: input unchanged; outer and inner lists are distinct")
    print("PASS: output mutation does not change input, including empty batch")
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    run_checks()