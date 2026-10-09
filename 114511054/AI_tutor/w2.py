"""W2 student solution with verification checks added by Codex."""

import copy
import sys


def count_supplies(tree):
    counts = {}

    def walk(node):
        for item in node:
            if isinstance(item, str):
                counts[item] = counts.get(item, 0) + 1
            else:
                walk(item)

    walk(tree)
    return counts


def run_checks():
    deep_tree = "bolt"
    for _ in range(20):
        deep_tree = [deep_tree]

    cases = [
        ("provided example 1", ["wire", ["bolt", "wire"], []], {"wire": 2, "bolt": 1}),
        ("provided example 2", [], {}),
        ("provided example 3", [["nut"], ["Nut", ["nut"]]], {"nut": 2, "Nut": 1}),
        ("20 nested lists", deep_tree, {"bolt": 1}),
        ("repeated names across branches", [["wire"], [["wire"], "nut"], "wire"], {"wire": 3, "nut": 1}),
    ]
    for name, tree, expected in cases:
        snapshot = copy.deepcopy(tree)
        actual = count_supplies(tree)
        assert actual == expected, (name, actual, expected)
        assert tree == snapshot, (name, "input changed")
        print(f"PASS: {name}; output={actual}; input unchanged")
    print("ALL 5 CHECKS PASSED")


if __name__ == "__main__":
    print(f"Python {sys.version.split()[0]}; recursion limit={sys.getrecursionlimit()}")
    run_checks()
