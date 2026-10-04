"""
Lec08 Practice
Challenge: Reading Progress Tracker

Concepts practiced:
- defining a class
- creating object instances
- __init__
- instance attributes
- methods
- self
- __str__
"""

class BookProgress(object):
    def __init__(self, title, total_pages):
        self.title = title
        self.total_pages = total_pages
        self.pages_read = 0

    def read(self, pages):
        """
        Adds pages to the reading progress.
        Progress cannot go beyond total_pages.
        """
        self.pages_read += pages

        if self.pages_read > self.total_pages:
            self.pages_read = self.total_pages

    def remaining(self):
        """
        Returns the number of pages that have not been read yet.
        """
        return self.total_pages - self.pages_read

    def __str__(self):
        return self.title + ": " + str(self.pages_read) + "/" + str(self.total_pages) + " pages"


# -------------------------------------------------
# Tests
# -------------------------------------------------

# Normal case
book1 = BookProgress("Python", 100)

assert book1.pages_read == 0
assert book1.remaining() == 100

book1.read(30)

assert book1.pages_read == 30
assert book1.remaining() == 70

print(book1)
# Expected:
# Python: 30/100 pages


# Read more pages
book1.read(20)

assert book1.pages_read == 50
assert book1.remaining() == 50


# Edge case: try to read beyond the end of the book
book1.read(100)

assert book1.pages_read == 100
assert book1.remaining() == 0


# Another object should keep its own instance data
book2 = BookProgress("Algorithms", 80)

assert book2.pages_read == 0
assert book2.remaining() == 80

book2.read(25)

assert book2.pages_read == 25
assert book2.remaining() == 55

# book1 should be unchanged
assert book1.pages_read == 100


# Check __str__
assert str(book2) == "Algorithms: 25/80 pages"

print(book2)
print("All tests passed!")