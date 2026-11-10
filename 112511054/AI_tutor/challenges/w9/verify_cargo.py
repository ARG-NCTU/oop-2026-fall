"""Build a real pybind11 extension and check its Python interface."""
import importlib
import json
from pathlib import Path
import platform
import random
import subprocess
import sys
import sysconfig
import tempfile


def main():
    root = Path(__file__).resolve().parent
    results = []

    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        results.append({"name": name, "result": "PASS"})

    def rejects(name, action):
        try:
            action()
        except ValueError:
            check(name, True)
        else:
            raise AssertionError(name + ": ValueError expected")

    with tempfile.TemporaryDirectory(prefix="aoop-w9-") as build:
        includes = subprocess.check_output(
            [sys.executable, "-m", "pybind11", "--includes"], text=True
        ).split()
        output = Path(build) / ("cargocpp" + sysconfig.get_config_var("EXT_SUFFIX"))
        command = ["g++", "-O2", "-Wall", "-Wextra", "-Werror", "-shared",
                   "-std=c++17", "-fPIC", *includes,
                   str(root / "cargocpp.cpp"), "-o", str(output)]
        subprocess.run(command, check=True)
        sys.path.insert(0, build)
        module = importlib.import_module("cargocpp")
        loader = module.CargoLoader(10)
        check("example 1: skip oversized item", loader.add_batch([6, 5, 4]) == [0, 2]
              and (loader.load(), loader.remaining(), loader.count()) == (10, 0, 2))
        loader = module.CargoLoader(8)
        loader.add_batch([3])
        check("example 2: state across batches", loader.add_batch([6, 2, 3]) == [1, 2]
              and loader.load() == 8 and loader.count() == 3)
        loader = module.CargoLoader(5)
        rejects("example 3: invalid batch", lambda: loader.add_batch([2, 0, 1]))
        check("invalid batch leaves object unchanged", loader.load() == 0 and loader.count() == 0)
        for capacity in [0, -1, 1000000000001]:
            rejects(f"invalid capacity {capacity}", lambda c=capacity: module.CargoLoader(c))
        check("empty batch", loader.add_batch([]) == [] and loader.remaining() == 5)
        weights = [4, 3, 1]
        check("list/vector conversion", loader.add_batch(weights) == [0, 2])
        check("Python input list unchanged", weights == [4, 3, 1])
        loader.clear()
        check("clear resets both counters", (loader.load(), loader.count(), loader.remaining()) == (0, 0, 5))
        other = module.CargoLoader(5)
        loader.add_batch([1])
        check("separate objects own separate state", other.load() == 0 and loader.load() == 1)
        for bad in [-2, 0, 1000000000001]:
            before = loader.load(), loader.count()
            rejects(f"invalid weight {bad}", lambda b=bad: loader.add_batch([1, b]))
            check(f"rollback for {bad}", before == (loader.load(), loader.count()))
        rejects("batch length limit", lambda: loader.add_batch([1] * 100001))
        loader = module.CargoLoader(1000000000000)
        check("64-bit capacity", loader.add_batch([999999999999, 2, 1]) == [0, 2]
              and loader.load() == 1000000000000)
        loader = module.CargoLoader(100000)
        check("100000 item batch", loader.add_batch([1] * 100000) == list(range(100000))
              and loader.load() == 100000 and loader.count() == 100000)

        rng = random.Random(20261110)
        for trial in range(200):
            capacity = rng.randint(1, 300)
            loader = module.CargoLoader(capacity)
            selected = []
            for _ in range(10):
                if rng.randrange(8) == 0:
                    selected = []
                    loader.clear()
                batch = [rng.randint(1, 150) for _ in range(rng.randrange(15))]
                expected = []
                for index, weight in enumerate(batch):
                    # Independent reference retains accepted cargo, rather than a running sum.
                    if sum(selected + [weight]) <= capacity:
                        selected.append(weight)
                        expected.append(index)
                actual = loader.add_batch(batch)
                if (actual != expected or loader.load() != sum(selected)
                        or loader.count() != len(selected)
                        or loader.remaining() != capacity - sum(selected)):
                    raise AssertionError(f"random trial {trial}")
            check(f"stateful random trial {trial}", True)

    report = {"date": "2026-11-10", "python": platform.python_version(),
              "platform": platform.platform(), "passed": len(results),
              "failed": 0, "random_seed": 20261110,
              "compiler_flags": "-O2 -Wall -Wextra -Werror -shared -std=c++17 -fPIC",
              "cases": results}
    (root / "verification.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"W9: {len(results)}/{len(results)} PASS")


if __name__ == "__main__":
    main()
