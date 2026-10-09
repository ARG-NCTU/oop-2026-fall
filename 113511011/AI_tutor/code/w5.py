            + str(self.name)
            + ":"
            + str(self.borrowed)
        )


class StudentMember(Member):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major

    def get_borrow_limit(self):
        return 5

    def __str__(self):
        return (
            "student:"
            + str(self.id)
            + ":"
            + str(self.name)
            + ":"
            + str(self.major)
            + ":"
            + str(self.borrowed)
        )


if __name__ == "__main__":
    print("=== Example 1 ===")
    m = Member("Amy")
    print(m)
    print(m.get_borrow_limit())
    print(m.can_borrow())

    print("\n=== Example 2 ===")
    s = StudentMember("Bob", "CS")
    print(s)
    print(s.get_borrow_limit())

    print("\n=== Example 3 ===")
    c = StudentMember("Carol", "EE")
    c.borrow_book()
    c.borrow_book()
    c.borrow_book()
    c.borrow_book()
    c.borrow_book()

    print(c.can_borrow())

    c.return_book()

    print(c.can_borrow())

    print("\n=== Class variable test ===")
    x = Member("David")
    y = StudentMember("Eva", "ME")
    print(x.id)
    print(y.id)

