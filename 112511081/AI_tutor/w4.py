# W4 AI Tutor Part B: Clock Time (OCW Lec 8: Object Oriented Programming)
#
# Design a class Time that represents a time of day on a 24-hour clock.
#   Time(h, m)      h in 0..23, m in 0..59, both ints
#   str(t)          "HH:MM", zero padded
#   t + minutes     a new Time, minutes is an int (may be negative), wraps past midnight
#   t1 - t2         int, minutes from t2 forward to t1 (0..1439)
#   float(t)        hours as a float, e.g. 08:30 -> 8.5
#   t1 == t2        True when both show the same time


class Time(object):
    def __init__(self, hour, minute):
        assert type(hour) == int and type(minute) == int, "ints not used"
        assert 0 <= hour <= 23 and 0 <= minute <= 59, "time out of range"
        self.total = hour * 60 + minute       # minutes since 00:00

    def get_hour(self):
        return self.total // 60

    def get_minute(self):
        return self.total % 60

    def __str__(self):
        return "%02d:%02d" % (self.get_hour(), self.get_minute())

    def __add__(self, minutes):
        new_total = (self.total + minutes) % (24 * 60)
        return Time(new_total // 60, new_total % 60)

    def __sub__(self, other):
        return (self.total - other.total) % (24 * 60)

    def __float__(self):
        return self.total / 60

    def __eq__(self, other):
        return self.total == other.total


if __name__ == "__main__":
    # provided examples
    t = Time(8, 30)
    assert str(t) == "08:30"
    assert str(t + 45) == "09:15"
    assert Time(10, 0) - Time(8, 30) == 90
    assert float(t) == 8.5

    # edge cases
    assert str(Time(0, 0)) == "00:00"
    assert str(Time(23, 50) + 20) == "00:10"          # wraps past midnight
    assert str(Time(0, 10) + (-20)) == "23:50"        # negative minutes wrap backwards
    assert str(Time(12, 0) + 24 * 60 * 3) == "12:00"  # whole days change nothing
    assert Time(0, 10) - Time(23, 50) == 20           # crossing midnight
    assert Time(7, 5) - Time(7, 5) == 0
    assert Time(8, 30) + 30 == Time(9, 0)
    assert str(t) == "08:30"                          # + returns a new object, t is unchanged

    for bad in ((24, 0), (10, 60), (-1, 0), (8.5, 0)):
        try:
            Time(bad[0], bad[1])
        except AssertionError:
            pass
        else:
            assert False, "expected AssertionError for " + str(bad)

    print("all tests passed")
