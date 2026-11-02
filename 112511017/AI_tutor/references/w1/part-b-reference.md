# Week 1 coding challenge: Playlist edit history

AI-generated reference challenge, algorithm, and solution.

## Part B: Programming challenge

### Playlist Edit History

Write a function:

```python
edit_playlist(original, commands)
```

`original` is a list of song names. Each command is a tuple:

```python
("append", song_name)
("remove", song_name)
```

Apply the commands to a cloned playlist without modifying `original`.

For every command, record:

```python
(action, song_name, changed)
```

For `remove`, remove only the first occurrence. If the song is absent, do nothing and record `False`.

### Examples

```python
original = ["A", "B", "A"]
commands = [("remove", "A"), ("append", "C")]
```

Result:

```python
(
    ["B", "A", "C"],
    [
        ("remove", "A", True),
        ("append", "C", True),
    ],
)
```

The original remains:

```python
["A", "B", "A"]
```

Missing song:

```python
edit_playlist(["A"], [("remove", "B")])
```

Result:

```python
(["A"], [("remove", "B", False)])
```

## Proposed algorithm

1. Clone `original` using slicing.
2. Create an empty change log.
3. Iterate through the command tuples.
4. Append songs for `append`.
5. For `remove`, check whether the song exists before removing it.
6. Record whether each command changed the playlist.
7. Return the edited playlist and log as a tuple.

## Reference implementation and validation

- [Reference implementation](../../solutions/w1/playlist_challenge.py)
- [Example and edge-case tests](../../solutions/w1/test_playlist_challenge.py)

The reference uses a shallow list copy, which is sufficient for this challenge's song-name strings. Commands are assumed to be `append` or `remove`.

With `n` initial songs and `m` commands, the edited list can grow to `n + m`. Under unit-cost string comparison, cloning costs O(n), and scans and removals can cost O(n + m) per command. The general worst-case time bound is O(n + m(n + m)); auxiliary space is O(n + m). The earlier answer's O(mn) bound omitted growth from append commands.

Student initial approach, actual hints, revisions, and personal reflection remain to be recorded if this material is used as a completed learning record.
