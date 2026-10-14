"""Compile and verify the W5 reference solution in Ubuntu/WSL."""
from pathlib import Path
import os
import subprocess
import tempfile

folder = Path(__file__).resolve().parent
cases = [
    ("mixed tasks", "3 2\n1 5\n2 5\n1 1\n", "4"),
    ("zero rounds", "2 0\n1 3\n2 4\n", "7"),
    ("all completed", "2 3\n1 2\n2 3\n", "0"),
    ("empty task list", "0 5\n", "0"),
    ("zero initial work", "2 5\n1 0\n2 0\n", "0"),
    ("fast task with one unit", "1 1\n2 1\n", "0"),
    ("maximum constraints", "1000 1000\n" + "1 1000\n2 1000\n" * 500, "0"),
]

with tempfile.TemporaryDirectory(prefix="w5-scheduler-") as scratch:
    binary = Path(scratch) / "task_scheduler"
    subprocess.run([
        "g++", "-std=c++11", "-g", "-Wall", "-Wextra",
        "-Wsuggest-override", "-Werror=suggest-override",
        "-fsanitize=address", "-fno-omit-frame-pointer",
        str(folder / "task_scheduler.cpp"), "-o", str(binary),
    ], check=True)
    environment = dict(os.environ, ASAN_OPTIONS="detect_leaks=1")
    for name, input_text, expected in cases:
        result = subprocess.run(
            [str(binary)], input=input_text, capture_output=True,
            text=True, env=environment, timeout=10,
        )
        actual = result.stdout.strip()
        if result.returncode != 0 or actual != expected or result.stderr:
            raise AssertionError(
                f"{name}: expected={expected!r}, actual={actual!r}, "
                f"exit={result.returncode}, stderr={result.stderr}"
            )
        print(f"PASS: {name}; expected={expected}; actual={actual}")
    print(f"ALL PASS ({len(cases)}/{len(cases)})")
