"""AI-assisted Week 6 challenge, prepared on 2026-10-12."""


def compress_events(events):
    """Return (message, count) for each consecutive run, preserving order."""
    runs = []
    index = 0
    while index < len(events):
        message = events[index]
        start = index
        while index < len(events) and events[index] == message:
            index += 1
        runs.append((message, index - start))
    return runs
