class Interval:
    def __init__(self, _start, _end):
        if type(_start) != int or type(_end) != int:
            raise AssertionError("Endpoints must be integers")
        if _start > _end:
            raise ValueError("Start must be <= End")
        self.start = _start
        self.end = _end
    def __str__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]"
    def overlaps(self, other):
        if self.start <= other.start:
            return other.start <= self.end
        return self.start <= other.end
    def merge(self, other):
        if not self.overlaps(other):
            if self.start - other.end == 1 or other.start - self.end == 1:
                return Interval(min(self.start, other.start), max(self.end, other.end))
            raise ValueError("Cannot merge disjoint intervals")
        return Interval(min(self.start, other.start), max(self.end, other.end))

i1 = Interval(1, 3)
i3 = Interval(7, 10)
# i1.merge(i3)          # Raises ValueError: Cannot merge disjoint intervals

# Interval(5, 2)        # Raises ValueError: Start must be <= End
# Interval(1.5, 3)      # Raises AssertionError: Endpoints must be integers