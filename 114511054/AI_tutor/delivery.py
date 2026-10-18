"""Delivery implementation supplied in the W5 tutoring conversation."""


class Delivery:
    def __init__(self, weight):
        if weight < 0:
            raise ValueError("weight must be non-negative")
        self.weight = weight

    def fee(self):
        return 0


class StandardDelivery(Delivery):
    def fee(self):
        return 40 + 8 * self.weight


class ExpressDelivery(Delivery):
    def fee(self):
        return 90 + 15 * self.weight


def total_fee(deliveries):
    total = 0
    for d in deliveries:
        total += d.fee()
    return total
