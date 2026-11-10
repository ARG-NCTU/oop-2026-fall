"""Independent replay reference; compile and exercise the actual C++ CLI."""
import itertools
import json
from pathlib import Path
import platform
import random
import subprocess
import tempfile


def reference(capacity, initial, events):
    accepted = []

    def replay():
        energy, completed = initial, 0
        for kind, value in accepted:
            if kind == "CHARGE":
                energy = min(capacity, energy + value)
            else:
                energy -= value
                completed += 1
        return energy, completed

    for kind, value in events:
        energy, _ = replay()
        if kind == "UNDO":
            if accepted:
                accepted.pop()
        elif kind == "RUN":
            if value <= energy:
                accepted.append((kind, value))
        elif value > 0 and energy < capacity:
            accepted.append((kind, value))
    return (*replay(), len(accepted))


def main():
    root = Path(__file__).resolve().parent
    results = []
    flags = ["-std=c++11", "-O1", "-Wall", "-Wextra", "-Werror",
             "-fsanitize=undefined", "-fno-sanitize-recover=undefined"]
    with tempfile.TemporaryDirectory(prefix="aoop-w8-") as build:
        executable = Path(build) / "undo_mission"
        subprocess.run(["g++", *flags, str(root / "undo_mission.cpp"), "-o", str(executable)], check=True)

        def check(name, capacity, initial, events, expected=None):
            if expected is None:
                expected = reference(capacity, initial, events)
            lines = [f"{capacity} {initial} {len(events)}"]
            lines += [kind if kind == "UNDO" else f"{kind} {value}" for kind, value in events]
            run = subprocess.run([str(executable)], input="\n".join(lines) + "\n",
                                 text=True, capture_output=True, timeout=10, check=True)
            actual = tuple(map(int, run.stdout.split()))
            if actual != expected or run.stderr:
                raise AssertionError((name, actual, expected, run.stderr))
            results.append({"name": name, "result": "PASS", "actual": list(actual)})

        fixed = [
            ("example 1", 10, 4, [("CHARGE", 9), ("RUN", 6), ("UNDO", 0)], (10, 0, 1)),
            ("example 2", 5, 2, [("RUN", 3), ("CHARGE", 0), ("UNDO", 0)], (2, 0, 0)),
            ("example 3", 5, 0, [("RUN", 0), ("UNDO", 0)], (0, 0, 0)),
            ("no events", 1, 0, [], (0, 0, 0)),
            ("empty undo", 5, 2, [("UNDO", 0)] * 3, (2, 0, 0)),
            ("charge at full creates no history", 5, 5, [("CHARGE", 3), ("UNDO", 0)], (5, 0, 0)),
            ("zero-cost run changes count", 1, 0, [("RUN", 0)], (0, 1, 1)),
            ("undo restores completed count", 5, 5, [("RUN", 5), ("UNDO", 0)], (5, 0, 0)),
            ("failure does not consume history", 5, 2, [("CHARGE", 1), ("RUN", 5), ("UNDO", 0)], (2, 0, 0)),
            ("clamped charge undo restores original", 10, 4, [("CHARGE", 1000000000), ("UNDO", 0)], (4, 0, 0)),
            ("branch after undo", 10, 4, [("RUN", 2), ("UNDO", 0), ("CHARGE", 1), ("UNDO", 0)], (4, 0, 0)),
        ]
        for case in fixed:
            check(*case)
        alphabet = [("CHARGE", 0), ("CHARGE", 1), ("CHARGE", 3),
                    ("RUN", 0), ("RUN", 1), ("RUN", 3), ("UNDO", 0)]
        exhaustive = 0
        for length in range(4):
            for events in itertools.product(alphabet, repeat=length):
                check(f"exhaustive {exhaustive}", 3, 1, events)
                exhaustive += 1
        rng = random.Random(20261110)
        for trial in range(250):
            capacity = rng.randint(1, 100)
            initial = rng.randint(0, capacity)
            events = [(rng.choice(["CHARGE", "RUN", "UNDO"]), rng.randint(0, 150))
                      for _ in range(rng.randint(0, 80))]
            check(f"random {trial}", capacity, initial, events)
        check("100000 successful zero-cost runs", 1000000000, 0,
              [("RUN", 0)] * 100000, (0, 100000, 100000))
        check("50000 runs fully undone", 1000000000, 1000000000,
              [("RUN", 1)] * 50000 + [("UNDO", 0)] * 50000, (1000000000, 0, 0))
        check("100000 rejected runs", 1, 0,
              [("RUN", 1000000000)] * 100000, (0, 0, 0))
    report = {"date": "2026-11-10", "python": platform.python_version(),
              "passed": len(results), "failed": 0, "exhaustive_cases": exhaustive,
              "random_cases": 250, "random_seed": 20261110,
              "compiler_flags": " ".join(flags), "cases": results}
    (root / "verification.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"W8: {len(results)}/{len(results)} PASS")


if __name__ == "__main__":
    main()
