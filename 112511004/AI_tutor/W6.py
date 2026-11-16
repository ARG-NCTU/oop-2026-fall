"""Find all event indices that overlap another event."""


def conflicting_events(events):
    result = []

    for i in range(len(events)):
        for j in range(len(events)):
            if i == j:
                continue

            start_i, end_i = events[i]
            start_j, end_j = events[j]

            if start_i < end_j and start_j < end_i:
                result.append(i)
                break

    return result


if __name__ == "__main__":
    print(conflicting_events([[9, 11], [10, 12], [12, 13], [14, 16]]))
