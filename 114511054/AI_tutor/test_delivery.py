"""Independent checks reconstructed by Codex, not the student's original test file."""

import unittest

from delivery import Delivery, ExpressDelivery, StandardDelivery, total_fee


class DeliveryTests(unittest.TestCase):
    def test_standard_example(self):
        self.assertEqual(StandardDelivery(2).fee(), 56)

    def test_express_example(self):
        self.assertEqual(ExpressDelivery(2).fee(), 120)

    def test_base_example(self):
        self.assertEqual(Delivery(2).fee(), 0)

    def test_pair_total(self):
        self.assertEqual(total_fee([StandardDelivery(2), ExpressDelivery(2)]), 176)

    def test_empty_total(self):
        self.assertEqual(total_fee([]), 0)

    def test_base_zero(self):
        self.assertEqual(Delivery(0).fee(), 0)

    def test_standard_zero(self):
        self.assertEqual(StandardDelivery(0).fee(), 40)

    def test_express_zero(self):
        self.assertEqual(ExpressDelivery(0).fee(), 90)

    def test_base_upper_boundary(self):
        self.assertEqual(Delivery(100).fee(), 0)

    def test_standard_upper_boundary(self):
        self.assertEqual(StandardDelivery(100).fee(), 840)

    def test_express_upper_boundary(self):
        self.assertEqual(ExpressDelivery(100).fee(), 1590)

    def test_base_rejects_negative(self):
        with self.assertRaises(ValueError):
            Delivery(-1)

    def test_standard_rejects_negative(self):
        with self.assertRaises(ValueError):
            StandardDelivery(-1)

    def test_express_rejects_negative(self):
        with self.assertRaises(ValueError):
            ExpressDelivery(-1)

    def test_mixed_base_and_subclasses(self):
        deliveries = [Delivery(10), StandardDelivery(10), ExpressDelivery(10), Delivery(0)]
        self.assertEqual(total_fee(deliveries), 360)

    def test_instance_weights_are_independent(self):
        a = StandardDelivery(1)
        b = StandardDelivery(1)
        a.weight = 50
        self.assertEqual(a.fee(), 440)
        self.assertEqual(b.fee(), 48)
        self.assertEqual(b.weight, 1)

    def test_maximum_list_length(self):
        deliveries = [ExpressDelivery(100) for _ in range(100)]
        self.assertEqual(total_fee(deliveries), 159000)

    def test_new_subclass_without_changing_total_fee(self):
        class OvernightDelivery(Delivery):
            def fee(self):
                return 200 + 20 * self.weight

        self.assertEqual(total_fee([OvernightDelivery(2), StandardDelivery(2)]), 296)

    def test_total_does_not_change_input(self):
        deliveries = [StandardDelivery(2), ExpressDelivery(3)]
        originals = deliveries.copy()
        weights = [d.weight for d in deliveries]
        self.assertEqual(total_fee(deliveries), 191)
        self.assertEqual(deliveries, originals)
        self.assertEqual([d.weight for d in deliveries], weights)

    def test_repeated_object_is_counted_per_entry(self):
        delivery = StandardDelivery(2)
        self.assertEqual(total_fee([delivery, delivery]), 112)


if __name__ == "__main__":
    unittest.main(verbosity=2)
