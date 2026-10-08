# W1 AI Tutor Part B: Purge the Roster (OCW Lec 5: Tuples, Lists, Aliasing, Mutability, Cloning)
#
# roster is a list of student names (names may repeat). dropped is a list of
# names that dropped the course. Remove every dropped name from roster IN PLACE
# and return a tuple (number_removed, number_remaining).
# dropped must not be modified.


def purge_roster(roster, dropped):
    removed = 0
    for name in roster[:]:          # iterate over a clone, mutate the original
        if name in dropped:
            roster.remove(name)
            removed += 1
    return (removed, len(roster))


if __name__ == "__main__":
    # provided examples
    r = ["amy", "bob", "cat", "dan"]
    assert purge_roster(r, ["bob"]) == (1, 3)
    assert r == ["amy", "cat", "dan"]

    r = ["amy", "bob", "cat"]
    assert purge_roster(r, ["zed"]) == (0, 3)
    assert r == ["amy", "bob", "cat"]

    # edge cases
    r = ["amy", "bob", "bob", "cat"]            # two dropped names next to each other
    assert purge_roster(r, ["bob"]) == (2, 2)
    assert r == ["amy", "cat"]

    r = ["bob", "amy", "bob", "amy"]            # everything is removed
    assert purge_roster(r, ["amy", "bob"]) == (4, 0)
    assert r == []

    r = []
    assert purge_roster(r, ["amy"]) == (0, 0)

    r = ["amy", "bob"]
    alias = r                                   # caller's other name sees the change
    d = ["amy"]
    purge_roster(r, d)
    assert alias == ["bob"] and alias is r
    assert d == ["amy"]                         # dropped is untouched

    print("all tests passed")
