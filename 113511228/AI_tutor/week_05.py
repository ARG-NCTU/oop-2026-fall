"""AOOP Week 05: Polymorphic Shipping Calculator.
Original educational exercise inspired by the course OCW topic.
This file is a worked-example solution; run it to execute its tests.
"""

class ShippingMethod:
    def cost(self, weight):
        raise NotImplementedError


class Standard(ShippingMethod):
    def cost(self, weight):
        return 5 + 2 * weight


class Express(ShippingMethod):
    def cost(self, weight):
        return 12 + 4 * weight


class Pickup(ShippingMethod):
    def cost(self, weight):
        return 0


def calculate_shipping(requests):
    methods = {'Standard': Standard(),
               'Express': Express(),
               'Pickup': Pickup()}
    return [methods[mode].cost(weight) for mode, weight in requests]


def _run_self_tests():
    """Execute provided examples and additional edge cases."""
    import copy
    cases = [
        (([('Standard', 3), ('Express', 2), ('Pickup', 9)],), [11, 20, 0]),
        (([('Standard', 0)],), [5]),
        (([],), []),
    ]
    for number, (args, expected) in enumerate(cases, 1):
        given = copy.deepcopy(args)
        actual = calculate_shipping(*given)
        assert actual == expected, (number, actual, expected)
    print("Week 05: PASS ({} test cases)".format(len(cases)))


if __name__ == "__main__":
    _run_self_tests()
