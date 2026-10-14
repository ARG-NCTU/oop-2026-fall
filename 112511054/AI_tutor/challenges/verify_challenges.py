"""Run the weekly challenges in Python + pytest + g++ on Linux/WSL."""
from pathlib import Path
import json
import os
import random
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
ENV = dict(os.environ, PYTHONDONTWRITEBYTECODE="1",
           ASAN_OPTIONS="detect_leaks=1:halt_on_error=1",
           UBSAN_OPTIONS="halt_on_error=1")


def run_case(command, name, input_text, expected):
    result = subprocess.run(command, input=input_text, text=True,
                            capture_output=True, timeout=20, env=ENV)
    actual = result.stdout.strip()
    if result.returncode != 0 or actual != expected or result.stderr:
        raise AssertionError(f"{name}: expected={expected!r}, actual={actual!r}, "
                             f"exit={result.returncode}, stderr={result.stderr}")
    return {"name": name, "expected": expected, "actual": actual, "result": "PASS"}


def parking_oracle(kind, minutes):
    # Independent oracle: repeatedly consume a billing block instead of rounding.
    remaining = minutes if kind == 1 else max(0, minutes - 30)
    block, price, cap = (60, 20, 200) if kind == 1 else (30, 15, 180)
    fee = 0
    while remaining > 0:
        remaining -= block
        fee += price
    return min(fee, cap)


def mission_oracle(commands):
    # A label-based state model, independent of the C++ implementation's flags.
    phase, manual, speed = "PARK", True, 3
    for command in commands:
        parts = command.split()
        if parts[0] == "DEPLOY":
            phase, manual = "SURVEY", False
        elif parts[0] == "RETURN" and phase in ("SURVEY", "RETURN"):
            phase = "RETURN"
        elif parts[0] == "SPEED":
            speed = int(parts[1])
        elif parts[0] == "MANUAL":
            manual = parts[1] == "1"
        elif parts[0] == "REACHED" and not manual:
            if phase == "SURVEY":
                phase = "RETURN"
            elif phase == "RETURN":
                phase = "DONE"
    if phase in ("PARK", "DONE"):
        return f"{phase} 0"
    if manual:
        return "PARK 0"
    return "RETURN 2" if phase == "RETURN" else f"SURVEY {speed}"


def main():
    report = {"date": "2026-10-14", "python": sys.version.split()[0],
              "compiler": subprocess.check_output(["g++", "--version"], text=True).splitlines()[0],
              "sanitizers": ["AddressSanitizer", "UndefinedBehaviorSanitizer", "leak detection"],
              "weeks": {}}
    with tempfile.TemporaryDirectory(prefix="aoop-weekly-") as scratch_text:
        scratch = Path(scratch_text)
        for week in (2, 3):
            xml_path = scratch / f"w{week}.xml"
            result = subprocess.run(
                [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider",
                 f"--junitxml={xml_path}", str(ROOT / f"w{week}")],
                text=True, capture_output=True, env=ENV, timeout=40,
            )
            if result.returncode != 0:
                raise AssertionError(result.stdout + result.stderr)
            suites = ET.parse(xml_path).getroot().findall("testsuite")
            count = sum(int(s.attrib["tests"]) for s in suites)
            report["weeks"][f"w{week}"] = {"pytest_passed": count, "cli_cases": []}
            print(f"W{week}: {count} pytest cases PASS")

        python_cases = {
            2: [("staged snapshot", "5\nEDIT 10\nADD\nEDIT 20\nCOMMIT\nPUSH\n", "20 10 10 10"),
                ("not pushed", "4\nEDIT 7\nADD\nCOMMIT\nEDIT 9\n", "9 7 7 -1"),
                ("empty stream", "0\n", "-1 -1 -1 -1")],
            3: [("ordinary transfer", "100 20 30\n", "70 50"),
                ("full balance", "5 0 5\n", "0 5"),
                ("invalid transfer", "10 20 11\n", "INVALID")],
        }
        for week, cases in python_cases.items():
            filename = "git_snapshot.py" if week == 2 else "transfer.py"
            report["weeks"][f"w{week}"]["cli_cases"] = [
                run_case([sys.executable, str(ROOT / f"w{week}" / filename)], *case)
                for case in cases
            ]

        binaries = {}
        for week, filename in ((4, "parking_fees.cpp"), (6, "mission_state.cpp")):
            binary = scratch / f"w{week}"
            subprocess.run(["g++", "-std=c++11", "-Wall", "-Wextra", "-Werror", "-g",
                            "-fsanitize=address,undefined", "-fno-omit-frame-pointer", "-no-pie",
                            str(ROOT / f"w{week}" / filename), "-o", str(binary)], check=True)
            binaries[week] = str(binary)

        parking_cases = [
            ("example 1", "3\n1 61\n2 30\n2 31\n", "55"),
            ("example 2", "2\n1 1440\n2 1440\n", "380"),
            ("example 3", "0\n", "0"),
            ("zero minutes", "2\n1 0\n2 0\n", "0"),
            ("hour boundary", "2\n1 60\n1 61\n", "60"),
            ("free period boundary", "2\n2 30\n2 31\n", "15"),
            ("half-hour boundary", "2\n2 60\n2 61\n", "45"),
            ("regular cap boundary", "2\n1 600\n1 601\n", "400"),
            ("short-stay cap boundary", "2\n2 390\n2 391\n", "360"),
            ("maximum cars", "1000\n" + "1 1440\n" * 1000, "200000"),
        ]
        rng = random.Random(112511054)
        for i in range(20):
            cars = [(rng.randint(1, 2), rng.randint(0, 1440)) for _ in range(rng.randint(1, 30))]
            data = str(len(cars)) + "\n" + "".join(f"{kind} {minutes}\n" for kind, minutes in cars)
            expected = str(sum(parking_oracle(kind, minutes) for kind, minutes in cars))
            parking_cases.append((f"independent-oracle-{i + 1}", data, expected))
        report["weeks"]["w4"] = {"cases": [run_case([binaries[4]], *c) for c in parking_cases]}
        print(f"W4: {len(parking_cases)} C++ cases PASS; sanitizers clean")

        mission_cases = [
            ("example 1", ["DEPLOY", "SPEED 4", "REACHED"], "RETURN 2"),
            ("example 2", ["DEPLOY", "MANUAL 1", "REACHED", "MANUAL 0"], "SURVEY 3"),
            ("example 3", ["DEPLOY", "REACHED", "REACHED"], "DONE 0"),
            ("no events", [], "PARK 0"),
            ("inactive return", ["RETURN"], "PARK 0"),
            ("inactive reached", ["REACHED"], "PARK 0"),
            ("pending speed", ["SPEED 1", "DEPLOY"], "SURVEY 1"),
            ("zero survey speed", ["DEPLOY", "SPEED 0"], "SURVEY 0"),
            ("speed does not change return", ["DEPLOY", "RETURN", "SPEED 4"], "RETURN 2"),
            ("return while paused", ["DEPLOY", "MANUAL 1", "RETURN", "MANUAL 0"], "RETURN 2"),
            ("reached ignored in manual", ["DEPLOY", "RETURN", "MANUAL 1", "REACHED"], "PARK 0"),
            ("restart after done", ["DEPLOY", "REACHED", "REACHED", "DEPLOY"], "SURVEY 3"),
            ("duplicate return", ["DEPLOY", "RETURN", "RETURN"], "RETURN 2"),
            ("late reached after done", ["DEPLOY", "REACHED", "REACHED", "REACHED"], "DONE 0"),
            ("manual after done", ["DEPLOY", "REACHED", "REACHED", "MANUAL 1"], "DONE 0"),
        ]
        choices = ["DEPLOY", "RETURN", "REACHED", "MANUAL 0", "MANUAL 1", "SPEED 0", "SPEED 1", "SPEED 4"]
        for i in range(20):
            commands = [rng.choice(choices) for _ in range(rng.randint(1, 100))]
            mission_cases.append((f"independent-oracle-{i + 1}", commands, mission_oracle(commands)))
        mission_cases.append(("maximum events", ["DEPLOY"] + ["SPEED 4"] * 99999, "SURVEY 4"))
        report["weeks"]["w6"] = {"cases": [
            run_case([binaries[6]], name, str(len(commands)) + "\n" + "\n".join(commands) + "\n", expected)
            for name, commands, expected in mission_cases
        ]}
        print(f"W6: {len(mission_cases)} C++ cases PASS; sanitizers clean")

    (ROOT / "verification.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("ALL PASS; verification.json written")


if __name__ == "__main__":
    main()
