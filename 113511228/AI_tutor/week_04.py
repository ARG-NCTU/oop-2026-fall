"""AOOP Week 04: Study-Room Seat Booking.
Original educational exercise inspired by the course OCW topic.
This file is a worked-example solution; run it to execute its tests.
"""

class StudyRoom:
    def __init__(self, capacity):
        self.capacity = capacity
        self.booked = set()

    def reserve(self, name):
        if name in self.booked or len(self.booked) >= self.capacity:
            return False
        self.booked.add(name)
        return True

    def cancel(self, name):
        if name not in self.booked:
            return False
        self.booked.remove(name)
        return True

    def remaining(self):
        return self.capacity - len(self.booked)


def process_bookings(capacity, operations):
    room = StudyRoom(capacity)
    results = []
    for action, name in operations:
        if action == 'reserve':
            results.append(room.reserve(name))
        elif action == 'cancel':
            results.append(room.cancel(name))
        elif action == 'remaining':
            results.append(room.remaining())
    return results


def _run_self_tests():
    """Execute provided examples and additional edge cases."""
    import copy
    cases = [
        ((2, [('reserve', 'Amy'), ('reserve', 'Amy'), ('remaining', ''), ('cancel', 'Amy')]), [True, False, 1, True]),
        ((1, [('reserve', 'A'), ('reserve', 'B'), ('remaining', '')]), [True, False, 0]),
        ((0, [('remaining', ''), ('reserve', 'A')]), [0, False]),
        ((1, [('reserve', 'A'), ('reserve', 'A'), ('cancel', 'B'), ('remaining', '')]), [True, False, False, 0]),
    ]
    for number, (args, expected) in enumerate(cases, 1):
        given = copy.deepcopy(args)
        actual = process_bookings(*given)
        assert actual == expected, (number, actual, expected)
    print("Week 04: PASS ({} test cases)".format(len(cases)))


if __name__ == "__main__":
    _run_self_tests()
