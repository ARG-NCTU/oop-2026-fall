from playlist_challenge import edit_playlist


def test_edit_playlist():
    original = ["A", "B", "A"]
    commands = [
        ("remove", "A"),
        ("append", "C"),
        ("remove", "missing"),
    ]

    edited, log = edit_playlist(original, commands)

    assert edited == ["B", "A", "C"]
    assert original == ["A", "B", "A"]
    assert log == [
        ("remove", "A", True),
        ("append", "C", True),
        ("remove", "missing", False),
    ]


def test_empty_playlist():
    original = []

    edited, log = edit_playlist(
        original,
        [("remove", "A"), ("append", "B")],
    )

    assert edited == ["B"]
    assert original == []
    assert log == [
        ("remove", "A", False),
        ("append", "B", True),
    ]
