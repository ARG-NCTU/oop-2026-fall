# W5 AI Tutor Part B: Library Items (OCW Lec 9: Python Classes and Inheritance)
#
# Item(title)                 every item gets a unique id: 1, 2, 3, ... (shared counter)
#   get_id()  -> "001"        zero padded to 3 digits
#   loan_days() -> 14
#   late_fee(days_late)       5 per day late
#   str(item) -> "Item 001: <title>"
# Book(Item)        (title, author)   loans for 21 days, same fee rule
# DVD(Item)         (title)           loans for 7 days, 20 per day, capped at 200
# ReferenceBook(Book)                 cannot be borrowed: loan_days() is 0, late_fee is 0


class Item(object):
    next_id = 1                              # class variable, shared by every item

    def __init__(self, title):
        self.title = title
        self.iid = Item.next_id
        Item.next_id += 1

    def get_id(self):
        return str(self.iid).zfill(3)

    def get_title(self):
        return self.title

    def loan_days(self):
        return 14

    def late_fee(self, days_late):
        assert days_late >= 0, "days_late cannot be negative"
        return 5 * days_late

    def __str__(self):
        return "Item " + self.get_id() + ": " + self.title


class Book(Item):
    def __init__(self, title, author):
        Item.__init__(self, title)           # let the parent set title and id
        self.author = author

    def loan_days(self):
        return 21

    def __str__(self):
        return "Book " + self.get_id() + ": " + self.title + " by " + self.author


class DVD(Item):
    def loan_days(self):
        return 7

    def late_fee(self, days_late):
        assert days_late >= 0, "days_late cannot be negative"
        return min(20 * days_late, 200)

    def __str__(self):
        return "DVD " + self.get_id() + ": " + self.title


class ReferenceBook(Book):
    def loan_days(self):
        return 0

    def late_fee(self, days_late):
        return 0

    def __str__(self):
        return "Reference" + Book.__str__(self)


def total_late_fee(items, days_late):
    """items: list of Item (any subclass). Same days_late for all of them."""
    total = 0
    for it in items:
        total += it.late_fee(days_late)      # each object uses its own class's rule
    return total


if __name__ == "__main__":
    a = Item("Campus Map")
    b = Book("SICP", "Abelson")
    c = DVD("Inception")
    d = ReferenceBook("Dictionary", "Oxford")

    # provided examples
    assert str(a) == "Item 001: Campus Map"
    assert str(b) == "Book 002: SICP by Abelson"
    assert str(c) == "DVD 003: Inception"
    assert [x.loan_days() for x in (a, b, c, d)] == [14, 21, 7, 0]
    assert b.late_fee(3) == 15               # inherited from Item
    assert c.late_fee(3) == 60               # overridden in DVD

    # edge cases
    assert str(d) == "ReferenceBook 004: Dictionary by Oxford"
    assert d.get_id() == "004"               # ids keep counting across subclasses
    assert c.late_fee(10) == 200 and c.late_fee(11) == 200   # cap
    assert a.late_fee(0) == 0 and c.late_fee(0) == 0
    assert d.late_fee(30) == 0
    assert total_late_fee([a, b, c, d], 2) == 10 + 10 + 40 + 0
    assert total_late_fee([], 5) == 0
    assert isinstance(d, Book) and isinstance(d, Item) and not isinstance(c, Book)
    assert Item.next_id == 5 and Book.next_id == 5   # one shared counter, not one per class
    try:
        a.late_fee(-1)
    except AssertionError:
        pass
    else:
        assert False, "expected AssertionError"

    print("all tests passed")
