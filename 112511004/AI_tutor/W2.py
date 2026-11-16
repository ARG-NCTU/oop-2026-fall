"""Find the first event ID that occurs exactly once."""


def first_unique_event(events):
    counts = {}
    for event in events:
        counts[event] = counts.get(event, 0) + 1

    for event in events:
        if counts[event] == 1:
            return event

    return -1


if __name__ == "__main__":
    print(first_unique_event([4, 4, 4, 2]))

