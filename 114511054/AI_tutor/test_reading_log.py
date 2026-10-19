"""Independent checks reconstructed by Codex, not the student's original test file."""

import unittest

from reading_log import ReadingLog


class ReadingLogTests(unittest.TestCase):
    def assert_rejected_without_change(self, value):
        log = ReadingLog([5])
        with self.assertRaises(ValueError):
            log.add(value)
        self.assertEqual(log.snapshot(), [5])
        self.assertEqual(log.total(), 5)

    def test_total_after_add(self):
        log = ReadingLog([5, 8])
        log.add(3)
        self.assertEqual(log.total(), 16)

    def test_snapshot_after_add(self):
        log = ReadingLog([5, 8])
        log.add(3)
        self.assertEqual(log.snapshot(), [5, 8, 3])

    def test_empty_total(self):
        self.assertEqual(ReadingLog([]).total(), 0)

    def test_empty_snapshot(self):
        self.assertEqual(ReadingLog([]).snapshot(), [])

    def test_negative_rejected(self):
        self.assert_rejected_without_change(-1)

    def test_float_rejected(self):
        self.assert_rejected_without_change(1.5)

    def test_string_rejected(self):
        self.assert_rejected_without_change("3")

    def test_none_rejected(self):
        self.assert_rejected_without_change(None)

    def test_true_rejected(self):
        self.assert_rejected_without_change(True)

    def test_false_rejected(self):
        self.assert_rejected_without_change(False)

    def test_initial_append_isolated(self):
        source = [1, 2, 3]
        log = ReadingLog(source)
        source.append(99)
        self.assertEqual(log.snapshot(), [1, 2, 3])
        self.assertEqual(log.total(), 6)

    def test_initial_replacement_isolated(self):
        source = [1, 2, 3]
        log = ReadingLog(source)
        source[0] = 100
        self.assertEqual(log.snapshot(), [1, 2, 3])
        self.assertEqual(log.total(), 6)

    def test_snapshot_append_isolated(self):
        log = ReadingLog([1, 2, 3])
        snapshot = log.snapshot()
        snapshot.append(50)
        self.assertEqual(log.snapshot(), [1, 2, 3])
        self.assertEqual(log.total(), 6)

    def test_snapshot_replacement_isolated(self):
        log = ReadingLog([1, 2, 3])
        snapshot = log.snapshot()
        snapshot[0] = 0
        self.assertEqual(log.snapshot(), [1, 2, 3])
        self.assertEqual(log.total(), 6)

    def test_instances_from_same_source_are_independent(self):
        source = [1]
        a = ReadingLog(source)
        b = ReadingLog(source)
        a.add(10)
        self.assertEqual(a.snapshot(), [1, 10])
        self.assertEqual(b.snapshot(), [1])
        self.assertEqual(b.total(), 1)
        self.assertEqual(source, [1])

    def test_zero_accepted(self):
        log = ReadingLog([])
        log.add(0)
        self.assertEqual(log.snapshot(), [0])
        self.assertEqual(log.total(), 0)

    def test_each_snapshot_is_a_distinct_list(self):
        log = ReadingLog([1, 2, 3])
        first = log.snapshot()
        second = log.snapshot()
        self.assertIsNot(first, second)
        first.clear()
        self.assertEqual(second, [1, 2, 3])
        self.assertEqual(log.snapshot(), [1, 2, 3])

    def test_later_add_does_not_change_previous_snapshot(self):
        log = ReadingLog([1, 2, 3])
        snapshot = log.snapshot()
        log.add(4)
        self.assertEqual(snapshot, [1, 2, 3])
        self.assertEqual(log.snapshot(), [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main(verbosity=2)
