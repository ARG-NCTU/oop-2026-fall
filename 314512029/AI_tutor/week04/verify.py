"""Verification runner for Week 4 classes and inheritance."""

import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent


def main():
    cases = json.loads((HERE / "cases.json").read_text(encoding="utf-8"))
    spec = importlib.util.spec_from_file_location("week04_solution", HERE / "solution.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    Vehicle = module.Vehicle
    SurveyVehicle = module.SurveyVehicle
    SurveyVehicle.next_id = 1
    failures = 0

    for case in cases:
        try:
            if case["kind"] == "Vehicle":
                obj = Vehicle(*case["args"])
            else:
                obj = SurveyVehicle(*case["args"])
                assert isinstance(obj, Vehicle), "SurveyVehicle must inherit Vehicle"
                assert obj.get_id() == case["expected_id"]
                for sensor, expected in case.get("survey_checks", []):
                    assert obj.can_survey(sensor) is expected
            assert obj.get_name() == case["args"][0]
            assert obj.get_max_speed() == case["args"][1]
            assert obj.travel_time(case["distance"]) == case["expected_time"]
            assert str(obj) == case["expected_str"]
        except Exception as error:
            failures += 1
            print(f"FAIL {case['name']}: {type(error).__name__}: {error}")
        else:
            print(f"PASS {case['name']}")

    inherited = (SurveyVehicle.get_name is Vehicle.get_name
                 and SurveyVehicle.travel_time is Vehicle.travel_time)
    if inherited:
        print("PASS inherited_methods")
    else:
        failures += 1
        print("FAIL inherited_methods: base behavior was duplicated or replaced")

    total = len(cases) + 1
    print(f"{total-failures}/{total} cases passed.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.dont_write_bytecode = True
    sys.exit(main())
