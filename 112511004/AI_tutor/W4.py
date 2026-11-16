"""Calculate the number of minutes two meetings overlap."""


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def overlap(self, other):
        overlap_start = max(self.start, other.start)
        overlap_end = min(self.end, other.end)
        return max(0, overlap_end - overlap_start)


if __name__ == "__main__":
    print(Meeting(60, 120).overlap(Meeting(90, 150)))

