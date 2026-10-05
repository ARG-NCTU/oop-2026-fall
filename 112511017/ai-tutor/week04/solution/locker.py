"""New AI-assisted Lecture 8 transfer exercise prepared on 2026-10-05."""


class Locker:
    def __init__(self, capacity):
        self.capacity = capacity
        self._items = []

    def add(self, label):
        if len(self._items) == self.capacity:
            return False
        self._items.append(label)
        return True

    def remove(self, label):
        self._items.remove(label)

    def snapshot(self):
        return self._items[:]

    def __str__(self):
        return f"{len(self._items)}/{self.capacity}:" + "|".join(self._items)


def locker_report(capacity, operations):
    locker = Locker(capacity)
    results = []
    for action, label in operations:
        if action == "add":
            results.append(locker.add(label))
        else:
            try:
                locker.remove(label)
            except ValueError:
                results.append(False)
            else:
                results.append(True)
    return results, str(locker)
