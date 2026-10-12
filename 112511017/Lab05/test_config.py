"""Configuration regression checks. Run: python3 -m unittest -v test_config.py"""
import math
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parent


def blocks(filename, declaration):
    text = re.sub(r"//[^\n]*", "", (ROOT / filename).read_text())
    return re.findall(declaration + r"\s*=\s*(\w+)\s*\{([^}]+)\}", text)


def values(block, key):
    return re.findall(r"^\s*" + re.escape(key) + r"\s*=\s*(.*?)\s*$", block, re.M)


class Lab05ConfigTests(unittest.TestCase):
    def setUp(self):
        self.apps = dict(blocks("alpha.moos", "ProcessConfig"))
        self.behaviors = {
            values(body, "name")[0]: body
            for _, body in blocks("alpha.bhv", "Behavior")
        }

    def test_boat_colour(self):
        self.assertEqual(values(self.apps["pNodeReporter"], "platform_color"), ["orange"])

    def test_square(self):
        survey = self.behaviors["waypt_survey"]
        points = [tuple(map(float, p.split(","))) for p in values(survey, "points")[0].split(":")]
        self.assertEqual(len(points), 4)
        self.assertEqual(len(set(points)), 4)
        edges = [(points[(i + 1) % 4][0] - p[0], points[(i + 1) % 4][1] - p[1]) for i, p in enumerate(points)]
        for i, edge in enumerate(edges):
            self.assertAlmostEqual(math.hypot(*edge), 120)
            following = edges[(i + 1) % 4]
            self.assertAlmostEqual(edge[0] * following[0] + edge[1] * following[1], 0)
        self.assertEqual(values(survey, "repeat"), ["forever"])

    def test_buttons_and_update_channels(self):
        viewer = self.apps["pMarineViewer"]
        survey = self.behaviors["waypt_survey"]
        returning = self.behaviors["waypt_return"]
        self.assertEqual(values(survey, "updates"), ["WPT_UPDATE"])
        self.assertEqual(values(returning, "updates"), ["RETURN_UPDATE"])
        for key, label, speed in [("button_five", "MUCHSLO", "1.0"), ("button_six", "MUCHFST", "4.0")]:
            self.assertEqual(values(viewer, key), [f"{label} # WPT_UPDATE=speed={speed} # RETURN_UPDATE=speed={speed}"])
        self.assertEqual(values(survey, "use_alt_speed"), ["false"])
        self.assertEqual(values(self.apps["pHelmIvP"], "domain"), ["course:0:359:360", "speed:0:4:41"])

    def test_start_and_return_at_same_corner(self):
        self.assertIn("x=60, y=-40", values(self.apps["uSimMarineV22"], "start_pos")[0])
        self.assertEqual(values(self.behaviors["waypt_return"], "points"), ["60,-40"])
        self.assertEqual(values(self.behaviors["waypt_survey"], "condition"), ["RETURN = false", "DEPLOY = true"])
        self.assertEqual(values(self.behaviors["waypt_return"], "condition"), ["RETURN = true", "DEPLOY = true"])

    def test_required_apps_are_launched(self):
        runs = values(self.apps["ANTLER"], "Run")
        launched = {r.split("@")[0].strip() for r in runs}
        self.assertEqual(launched, (set(self.apps) - {"ANTLER"}) | {"MOOSDB"})


if __name__ == "__main__":
    unittest.main()
