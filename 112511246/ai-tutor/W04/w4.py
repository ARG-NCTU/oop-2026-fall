class Duration:
    def __init__(self, minutes, seconds):
        self.minutes = minutes
        self.seconds = seconds

    def to_seconds(self):
        return self.minutes * 60 + self.seconds 

    def __str__(self):
        return f"{self.minutes}:{self.seconds:02d}"

    def __add__(self, other):
        total_sec = self.to_seconds() + other.to_seconds()
        sum_min = total_sec // 60
        sum_sec = total_sec % 60
        return Duration(sum_min, sum_sec)

    def __eq__(self, other):
        return self.to_seconds() == other.to_seconds()


if __name__ == "__main__":
    a = Duration(3, 5)
    print(a)
    print(a.to_seconds())

    b = Duration(1, 58)
    print(a + b)
    print(a)

    print(a + b == Duration(5, 3))
    print(a == b)
