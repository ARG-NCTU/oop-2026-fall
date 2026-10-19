"""ReadingLog implementation supplied in the W4 tutoring conversation."""


class ReadingLog:
    def __init__(self, initial_pages):
        # Copy the caller's list; elements are immutable integers.
        self._pages = list(initial_pages)

    def add(self, pages):
        # Reject bool as well as other non-int values.
        if type(pages) is not int or pages < 0:
            raise ValueError("pages must be a non-negative integer")
        self._pages.append(pages)

    def total(self):
        return sum(self._pages)

    def snapshot(self):
        return list(self._pages)
