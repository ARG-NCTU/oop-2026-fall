class Interval:
    def __init__(self, start: int, end: int):
        if start > end:
            raise ValueError("Start must be less than or equal to end")

        self.start = start
        self.end = end

    def __repr__(self):
        return f"<Interval [{self.start}, {self.end}]>"

    def __eq__(self, other):
        if isinstance(other, Interval):
            return self.start == other.start and self.end == other.end
        return False

    def length(self):
        return self.end - self.start

    def contains(self, value: int):
        return self.start <= value <= self.end

    def overlaps(self, other: "Interval"):
        return self.start <= other.end and other.start <= self.end

    def merge(self, other: "Interval"):
        if not self.overlaps(other):
            raise ValueError("Cannot merge disjoint intervals")
        return Interval(min(self.start, other.start), max(self.end, other.end))
