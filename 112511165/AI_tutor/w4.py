class Interval(object):
    def __init__(self, start, end):
        if start > end:
            raise ValueError("start cannot be greater than end")
        self.start = start
        self.end = end

    def length(self):
        return self.end - self.start

    def overlaps(self, other):
        # 只要不是「完全在左邊」或「完全在右邊」，就是有重疊
        return not (self.end < other.start or self.start > other.end)

    def __add__(self, other):
        if not self.overlaps(other):
            raise ValueError("Intervals do not overlap")
        new_start = min(self.start, other.start)
        new_end = max(self.end, other.end)
        return Interval(new_start, new_end)

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __str__(self):
        return f"[{self.start},{self.end}]"
