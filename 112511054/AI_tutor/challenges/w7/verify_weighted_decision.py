"""Compile and check the W7 finite weighted-decision challenge under Linux/WSL."""
from pathlib import Path
import json
import os
import random
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent


def serialize(weights, candidates):
    lines = [f"{len(candidates)} {len(weights)}", " ".join(map(str, weights))]
    lines.extend(" ".join(map(str, [heading, speed, allowed, *scores]))
                 for heading, speed, allowed, scores in candidates)
    return "\n".join(lines) + "\n"


def oracle(weights, candidates):
    ranked = []
    for heading, speed, allowed, utilities in candidates:
        if allowed:
            total = sum(w * u for w, u in zip(weights, utilities))
            ranked.append((total, -speed, -heading))
    if not ranked:
        return "-1"
    score, negative_speed, negative_heading = max(ranked)
    return f"{-negative_heading} {-negative_speed} {score}"


def main():
    cases = [
        ("example 1 - compromise", [2, 1],
         [(0, 20, 1, [100, 0]), (45, 20, 1, [90, 80]), (90, 20, 1, [0, 100])], "45 20 260"),
        ("example 2 - blocked maximum", [1, 1],
         [(0, 0, 0, [100, 100]), (90, 10, 1, [60, 60])], "90 10 120"),
        ("example 3 - zero weights", [0],
         [(90, 20, 1, [100]), (180, 10, 1, [50]), (0, 10, 1, [0])], "0 10 0"),
        ("empty candidates", [1], [], "-1"),
        ("all blocked", [5], [(0, 0, 0, [100]), (90, 10, 0, [100])], "-1"),
        ("speed tie-break first", [1], [(0, 20, 1, [50]), (180, 10, 1, [50])], "180 10 50"),
        ("heading tie-break second", [1], [(90, 10, 1, [50]), (0, 10, 1, [50])], "0 10 50"),
        ("64-bit product", [1000000000], [(359, 40, 1, [100])], "359 40 100000000000"),
        ("maximum weighted score", [1000000000] * 20, [(359, 40, 1, [100] * 20)], "359 40 2000000000000"),
        ("zero utilities", [100], [(300, 40, 1, [0]), (0, 0, 1, [0])], "0 0 0"),
        ("inactive zero-weight behavior", [0, 1], [(0, 10, 1, [100, 0]), (90, 20, 1, [0, 100])], "90 20 100"),
        ("stop is a valid candidate", [1], [(50, 0, 1, [1])], "50 0 1"),
        ("consume blocked score row", [1, 2], [(10, 5, 0, [99, 99]), (20, 10, 1, [1, 2]), (30, 20, 0, [100, 100])], "20 10 5"),
    ]
    rng = random.Random(1125110547)
    for i in range(40):
        m, n = rng.randint(1, 20), rng.randint(0, 80)
        weights = [rng.randint(0, 1000) for _ in range(m)]
        pairs = rng.sample([(h, s) for h in range(360) for s in range(41)], n)
        candidates = [(h, s, rng.randint(0, 1), [rng.randint(0, 100) for _ in range(m)]) for h, s in pairs]
        expected = oracle(weights, candidates)
        cases.append((f"independent-oracle-{i + 1}", weights, candidates, expected))

        scale = rng.randint(2, 7)
        if expected == "-1":
            scaled_expected = "-1"
        else:
            heading, speed, score = map(int, expected.split())
            scaled_expected = f"{heading} {speed} {score * scale}"
        cases.append((f"positive-weight-scaling-{i + 1}", [w * scale for w in weights], candidates, scaled_expected))
        if i < 20:
            shuffled = candidates[:]
            rng.shuffle(shuffled)
            cases.append((f"input-permutation-{i + 1}", weights, shuffled, expected))

    maximum_candidates = [(h, s, 1, [100] * 20) for h in range(360) for s in range(41)]
    cases.append(("full 14760-point domain", [1000000000] * 20, maximum_candidates, "0 0 2000000000000"))

    environment = dict(os.environ, ASAN_OPTIONS="detect_leaks=1:halt_on_error=1",
                       UBSAN_OPTIONS="halt_on_error=1")
    results = []
    with tempfile.TemporaryDirectory(prefix="aoop-w7-") as folder:
        binary = Path(folder) / "weighted_decision"
        subprocess.run(["g++", "-std=c++11", "-Wall", "-Wextra", "-Werror", "-g",
                        "-fsanitize=address,undefined", "-fno-omit-frame-pointer", "-no-pie",
                        str(ROOT / "weighted_decision.cpp"), "-o", str(binary)], check=True)
        for name, weights, candidates, expected in cases:
            result = subprocess.run([str(binary)], input=serialize(weights, candidates),
                                    capture_output=True, text=True, timeout=20, env=environment)
            actual = result.stdout.strip()
            if result.returncode or actual != expected or result.stderr:
                raise AssertionError(f"{name}: expected={expected!r}, actual={actual!r}, "
                                     f"exit={result.returncode}, stderr={result.stderr}")
            results.append({"name": name, "expected": expected, "actual": actual, "result": "PASS"})

    report = {"date": "2026-10-20", "seed": 1125110547,
              "compiler": subprocess.check_output(["g++", "--version"], text=True).splitlines()[0],
              "sanitizers": ["AddressSanitizer", "UndefinedBehaviorSanitizer", "leak detection"],
              "passed": len(results), "cases": results}
    (ROOT / "verification.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"ALL PASS ({len(results)}/{len(results)}); sanitizers clean; verification.json written")


if __name__ == "__main__":
    main()
