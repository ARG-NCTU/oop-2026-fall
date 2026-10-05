"""AI-assisted checks of examples, rounding, state, and input limits."""
import os
from pathlib import Path
import subprocess
import unittest


class DeviceDispatcherTests(unittest.TestCase):
    def check_case(self, input_text, expected):
        environment = dict(os.environ, ASAN_OPTIONS="detect_leaks=1")
        result = subprocess.run(
            [str(Path(__file__).with_name("device_dispatcher"))],
            input=input_text,
            text=True,
            capture_output=True,
            env=environment,
            timeout=10,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        self.assertEqual(result.stdout, expected)

    def test_example_one(self):
        self.check_case(
            "2 4\nS 10\nE 10\n0 7\n1 7\n0 4\n1 12\n",
            "ACCEPT 3\nACCEPT 6\nREJECT 3\nACCEPT 0\n",
        )

    def test_example_two(self):
        self.check_case("1 2\nS 0\n0 0\n0 1\n", "ACCEPT 0\nREJECT 0\n")

    def test_example_three(self):
        self.check_case(
            "1 3\nE 2\n0 3\n0 1\n0 0\n",
            "ACCEPT 0\nREJECT 0\nACCEPT 0\n",
        )

    def test_rejected_request_preserves_energy(self):
        self.check_case("1 2\nE 1\n0 3\n0 1\n", "REJECT 1\nACCEPT 0\n")

    def test_no_requests(self):
        self.check_case("2 0\nS 100\nE 0\n", "")

    def test_maximum_counts_and_independent_devices(self):
        devices = "".join("S 100\n" if i % 2 == 0 else "E 100\n" for i in range(100))
        requests = "".join(f"{i % 100} 1\n" for i in range(1000))
        expected = "".join(f"ACCEPT {99 - i // 100}\n" for i in range(1000))
        self.check_case("100 1000\n" + devices + requests, expected)


if __name__ == "__main__":
    unittest.main()
