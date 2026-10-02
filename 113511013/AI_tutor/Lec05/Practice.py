def clean_playlist(playlist, blocked):
    """
    Remove every song from playlist if its name appears in blocked.
    Modify playlist in place.
    Return a clone of the cleaned playlist.
    """
    playlist_copy = playlist[:]

    for song in playlist_copy:
        if song in blocked:
            playlist.remove(song)

    return playlist[:]


# Test 1: normal case
playlist1 = ["A", "B", "C", "B", "D"]
result1 = clean_playlist(playlist1, ["B"])

print("playlist1:", playlist1)
print("result1:", result1)

assert playlist1 == ["A", "C", "D"]
assert result1 == ["A", "C", "D"]


# Test 2: make sure the returned list is not an alias
result1.append("X")

print("result1 after append:", result1)
print("playlist1 should be unchanged:", playlist1)

assert playlist1 == ["A", "C", "D"]


# Test 3: nothing is blocked
playlist2 = ["A", "B"]
result2 = clean_playlist(playlist2, [])

assert playlist2 == ["A", "B"]
assert result2 == ["A", "B"]


# Test 4: all songs are blocked, including duplicates
playlist3 = ["A", "A", "B"]
result3 = clean_playlist(playlist3, ["A", "B"])

assert playlist3 == []
assert result3 == []


# Test 5: empty playlist
playlist4 = []
result4 = clean_playlist(playlist4, ["A"])

assert playlist4 == []
assert result4 == []

print("All tests passed!")