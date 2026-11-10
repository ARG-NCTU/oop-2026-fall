import itertools
import json
from pathlib import Path
import platform
import random
import subprocess
import sys

from edited_brackets import balanced_after_edits


def reference(text):
    # Deliberately slow independent model: string edits and repeated pair deletion.
    retained = ""
    for char in text:
        retained = retained[:-1] if char == "#" else retained + char
    while True:
        reduced = retained.replace("()", "").replace("[]", "").replace("{}", "")
        if reduced == retained:
            return not reduced
        retained = reduced


def main():
    root = Path(__file__).resolve().parent
    results = []

    def check(name, text, expected):
        actual = balanced_after_edits(text)
        if actual != expected:
            raise AssertionError((name, text, actual, expected))
        results.append({"name": name, "result": "PASS"})

    fixed = [("example 1", "([#)", True), ("example 2", "([)]", False),
             ("example 3", "#[]", True), ("empty", "", True),
             ("erased error", "]#", True), ("erase opener", "(#[", False),
             ("erase everything", "([])####", True), ("excess edits", "######", True),
             ("unclosed", "((", False), ("nested", "{[()]}", True),
             ("wrong close", "(]", False), ("close first", ")(", False)]
    for name, text, expected in fixed:
        check(name, text, expected)
    exhaustive_count = 0
    for length in range(5):
        for chars in itertools.product("()[]{}#", repeat=length):
            text = "".join(chars)
            check(f"exhaustive {exhaustive_count}", text, reference(text))
            exhaustive_count += 1
    rng = random.Random(20261110)
    for trial in range(250):
        text = "".join(rng.choices("()[]{}#", k=rng.randint(0, 150)))
        check(f"random {trial}", text, reference(text))
    for name, text, expected in [
            ("maximum nested", "(" * 100000 + ")" * 100000, True),
            ("maximum erased", "]" * 100000 + "#" * 100000, True),
            ("maximum unclosed", "(" * 200000, False),
            ("maximum edits", "#" * 200000, True)]:
        check(name, text, expected)
    for name, text, expected in fixed[:3]:
        actual = subprocess.check_output([sys.executable, str(root / "edited_brackets.py")],
                                         input=text + "\n", text=True).strip()
        if actual != str(expected).lower():
            raise AssertionError("CLI " + name)
        results.append({"name": "CLI " + name, "result": "PASS"})
    report = {"date": "2026-11-10", "python": platform.python_version(),
              "passed": len(results), "failed": 0, "exhaustive_cases": exhaustive_count,
              "random_cases": 250, "random_seed": 20261110, "cases": results}
    (root / "verification.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"W10: {len(results)}/{len(results)} PASS")


if __name__ == "__main__":
    main()
