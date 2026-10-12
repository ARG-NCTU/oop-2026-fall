#!/usr/bin/env python3
"""Exercise a real MOOSDB, helm, simulator and PID on a private port.

Needs built MOOS-IvP binaries on PATH. --gui also launches pMarineViewer
and requires an X display, e.g. xvfb-run -a python3 test_runtime.py --gui.
The original mission is never modified. Runtime logs remain in /tmp.
"""
import argparse
import json
import os
from pathlib import Path
import re
import shutil
import signal
import socket
import subprocess
import tempfile
import time

ROOT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gui", action="store_true")
    parser.add_argument("--screenshot", action="store_true", help="Save GUI evidence; requires Pillow")
    parser.add_argument("--port", type=int, default=19050)
    args = parser.parse_args()
    if args.screenshot and not args.gui:
        parser.error("--screenshot requires --gui")
    for app in ["pAntler", "uPokeDB", "uQueryDB"]:
        if not shutil.which(app):
            parser.error(f"{app} is missing from PATH")
    with socket.socket() as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("127.0.0.1", args.port))
    work = Path(tempfile.mkdtemp(prefix="aoop-lab05-"))
    config = (ROOT / "alpha.moos").read_text()
    config = re.sub(r"ServerPort\s*=\s*9000", f"ServerPort = {args.port}", config)
    config = re.sub(r"MOOSTimeWarp\s*=\s*1", "MOOSTimeWarp = 10", config)
    if not args.gui:
        config = re.sub(r"^\s*Run = pMarineViewer[^\n]*\n", "", config, flags=re.M)
    (work / "alpha.moos").write_text(config)
    shutil.copy2(ROOT / "alpha.bhv", work)
    results = {"runtime_directory": str(work), "gui": args.gui, "checks": []}

    def command(argv, timeout=120):
        result = subprocess.run(argv, cwd=work, text=True, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, timeout=timeout)
        with (work / "queries.log").open("a") as log:
            log.write("$ " + " ".join(argv) + "\n" + result.stdout + "\n")
        if result.returncode:
            raise RuntimeError(f"Command failed: {argv!r}\n{result.stdout}")
        return result.stdout

    def query(condition, wait=200):
        command(["uQueryDB", "alpha.moos", f"--condition={condition}", f"--wait={wait}"],
                timeout=wait / 10 + 30)
        results["checks"].append(condition)

    def poke(*assignments):
        command(["uPokeDB", "alpha.moos", *assignments], timeout=30)

    with (work / "mission.log").open("w") as log:
        mission = subprocess.Popen(["pAntler", "alpha.moos"],
                                   cwd=work, stdout=log, stderr=subprocess.STDOUT,
                                   start_new_session=True)
        try:
            query("DB_UPTIME > 5")
            # The helm iteration counter stays zero while parked. Wait for its
            # initialized behaviour variable instead of an active iteration.
            query("DEPLOY = false")
            poke("DEPLOY=true", "MOOS_MANUAL_OVERRIDE=false", "RETURN=false")
            query("DESIRED_SPEED = 3")
            # Use the exact assignments configured for each added viewer button.
            for button, target, low, high in [("button_five", 1.0, 0.85, 1.1),
                                               ("button_six", 4.0, 3.5, 4.1)]:
                line = re.search(r"^\s*" + button + r"\s*=\s*(.*)$", config, re.M)[1]
                assignments = [part.strip() for part in line.split("#")[1:]]
                poke(*assignments)
                query(f"DESIRED_SPEED = {target}")
                query(f"((NAV_SPEED > {low}) and (NAV_SPEED < {high}))")
                time.sleep(1)  # Record multiple fresh settled-speed samples.
            query("CYCLE_INDEX >= 2", wait=800)
            if args.screenshot:
                from PIL import ImageGrab
                screenshot = work / "viewer.png"
                ImageGrab.grab().save(screenshot)
                results["screenshot"] = str(screenshot)
            poke("RETURN=true")
            query("DESIRED_SPEED = 4")
            query("MISSION = complete", wait=500)
            query("DEPLOY = false")
            query("NAV_SPEED < 0.1")
            time.sleep(1)  # Let the asynchronous logger flush telemetry.
        finally:
            try:
                os.killpg(mission.pid, signal.SIGTERM)
            except ProcessLookupError:
                pass
            try:
                mission.wait(timeout=8)
            except subprocess.TimeoutExpired:
                os.killpg(mission.pid, signal.SIGKILL)
                mission.wait(timeout=5)
    alogs = list(work.glob("*/*.alog"))
    if not alogs:
        raise RuntimeError(f"No telemetry log in {work}")
    telemetry = "\n".join(p.read_text(errors="replace") for p in alogs)
    if not re.search(r"NODE_REPORT(?:_LOCAL)?\s+[^\n]*COLOR=orange", telemetry):
        raise AssertionError("Orange boat colour missing from node reports")
    indices = {int(float(m[1])) for m in re.finditer(r"^\S+\s+WPT_INDEX\s+\S+\s+(\S+)", telemetry, re.M)}
    if not {0, 1, 2, 3} <= indices:
        raise AssertionError(f"Square corners not all visited: {indices}")
    results["checks"].extend(["NODE_REPORT colour is orange", "WPT_INDEX selects all four corners"])
    records = []
    for line in telemetry.splitlines():
        parts = line.split(None, 3)
        if len(parts) == 4 and not line.startswith("%"):
            try:
                records.append((float(parts[0]), parts[1], parts[3].strip()))
            except ValueError:
                pass
    records.sort(key=lambda record: record[0])
    state = {}
    stable = {1.0: 0, 4.0: 0}
    stable_start = {1.0: None, 4.0: None}
    corners = [(60, -40), (60, -160), (180, -160), (180, -40), (60, -40)]
    visited = 0
    closing_midpoint = False
    for timestamp, variable, value in records:
        try:
            state[variable] = float(value)
        except ValueError:
            continue
        if variable == "NAV_SPEED":
            for target in stable:
                settled = (state.get("DESIRED_SPEED") == target
                           and abs(state.get("NAV_SPEED", -100) - target) < 0.12
                           and abs(state.get("DESIRED_RUDDER", 100)) < 5)
                if settled:
                    if stable_start[target] is None:
                        stable_start[target] = timestamp
                    stable[target] = max(stable[target], timestamp - stable_start[target])
                else:
                    stable_start[target] = None
        if variable == "NAV_Y" and "NAV_X" in state and visited < len(corners):
            x, y = state["NAV_X"], state["NAV_Y"]
            if visited == 4 and abs(x - 120) < 12 and abs(y + 40) < 12:
                closing_midpoint = True
            cx, cy = corners[visited]
            if (x - cx) ** 2 + (y - cy) ** 2 < 12 ** 2:
                visited += 1
    if any(duration < 2 for duration in stable.values()):
        raise AssertionError(f"Speeds did not settle for two simulated seconds: {stable}")
    if visited != len(corners) or not closing_midpoint:
        raise AssertionError(f"Missing ordered corner visits/closing leg: {visited}, {closing_midpoint}")
    results["settled_speed_seconds"] = stable
    results["checks"].extend(["Settled straight-leg speeds at 1.0 and 4.0 m/s",
                               "NAV positions visit A-B-C-D-A and closing-leg midpoint"])
    if args.gui and "pMarineViewer" not in telemetry:
        raise AssertionError("Viewer did not connect to MOOSDB")
    results["result"] = "PASS"
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
