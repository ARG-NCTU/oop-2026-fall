"""Run the lab cases in isolated temporary directories under WSL.

Uses the instructor's templates unchanged; scales weights or adds a speed
behavior only in temporary copies. Writes measured results, not predictions.
"""
import json
import os
from pathlib import Path
import signal
import statistics
import subprocess
import tempfile
import time
import zipfile

SOURCE = Path.home() / "moos-ivp/ivp/missions/exp1_tugofwar"
OUTPUT = Path(__file__).resolve().parent / "verification-results.json"
os.environ["PATH"] = str(Path.home() / "moos-ivp/bin") + ":" + os.environ["PATH"]
SPEED_BEHAVIOR = """
// Added solution: retain both original behavior weights.
Behavior = BHV_ConstantSpeed
{
  name = keep_moving
  pwt = 200
  condition = DEPLOY = true
  duration = no-time-limit
  speed = 2.0
  peakwidth = 0
  basewidth = 0.4
  summitdelta = 100
}
"""


def run_case(case, scale=1, fix=False):
    with tempfile.TemporaryDirectory(prefix="aoop-tug-") as folder:
        work = Path(folder)
        # Use the archived instructor templates even after the installed
        # Case 3 has been updated to the moving version.
        with zipfile.ZipFile(OUTPUT.parent / "Lab06.zip") as archive:
            moos = archive.read("exp1_tugofwar/meta_tug.moos").decode("utf-8")
            original_bhv = archive.read("exp1_tugofwar/meta_tug.bhv").decode("utf-8")
        moos = moos.replace("$(WARP)", "5").replace("$(CASE)", str(case))
        (work / "meta_tug.moos").write_text(moos)
        (work / "meta_tug.bhv").write_text(original_bhv)
        subprocess.run(["nsplug", "meta_tug.moos", "targ_tug.moos", "-f", "--strict", "GUI=no"], cwd=work, check=True, stdout=subprocess.DEVNULL)
        subprocess.run(["nsplug", "meta_tug.bhv", "targ_tug.bhv", "-f", "--strict", f"CASE={case}"], cwd=work, check=True, stdout=subprocess.DEVNULL)
        bhv = (work / "targ_tug.bhv").read_text()
        if scale != 1:
            import re
            bhv = re.sub(r"(pwt\s*=\s*)(\d+)", lambda m: m[1] + str(int(m[2]) * scale), bhv)
        if fix:
            bhv += SPEED_BEHAVIOR
        (work / "targ_tug.bhv").write_text(bhv)
        with (work / "console.log").open("w") as console:
            process = subprocess.Popen(["pAntler", "targ_tug.moos"], cwd=work, stdout=console, stderr=subprocess.STDOUT, start_new_session=True)
            try:
                time.sleep(3)
                if process.poll() is not None:
                    raise RuntimeError((work / "console.log").read_text()[-4000:])
                subprocess.run(["uPokeDB", "targ_tug.moos", "DEPLOY=true", "MOOS_MANUAL_OVERRIDE=false"], cwd=work, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                time.sleep(12)
            finally:
                os.killpg(process.pid, signal.SIGINT)
                try:
                    process.wait(timeout=8)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
        logs = list(work.glob("**/*.alog"))
        if len(logs) != 1:
            raise RuntimeError(f"Expected one log, got {logs}")
        keys = {"DESIRED_HEADING", "DESIRED_SPEED", "NAV_SPEED", "NAV_X", "NAV_Y", "BHV_WARNING", "BHV_ERROR", "IVPHELM_STATE"}
        rows = {key: [] for key in keys}
        for line in logs[0].read_text().splitlines():
            parts = line.split(None, 3)
            if len(parts) == 4 and parts[1] in rows:
                rows[parts[1]].append({"time": float(parts[0]), "value": parts[3]})
        result = {"case": case, "weight_scale": scale, "added_speed_behavior": fix}
        for key in ("DESIRED_HEADING", "DESIRED_SPEED", "NAV_SPEED"):
            if not rows[key]:
                raise RuntimeError(f"Missing {key}")
            result[key] = round(statistics.median(float(row["value"]) for row in rows[key][-20:]), 4)
        result["last_position"] = {key: rows[key][-1] for key in ("NAV_X", "NAV_Y")}
        result["warnings"] = rows["BHV_WARNING"]
        result["errors"] = rows["BHV_ERROR"]
        result["helm_state"] = rows["IVPHELM_STATE"][-1]
        print(json.dumps(result), flush=True)
        return result


if __name__ == "__main__":
    if subprocess.run(["pgrep", "-x", "MOOSDB"], stdout=subprocess.DEVNULL).returncode == 0:
        raise SystemExit("Stop the existing MOOS mission before running these tests.")
    results = []
    for case, scale, fix in [(1, 1, False), (2, 1, False), (3, 1, False), (4, 1, False), (1, 2, False), (3, 1, True)]:
        results.append(run_case(case, scale, fix))
        OUTPUT.write_text(json.dumps({"date": "2026-10-19", "warp": 5, "results": results}, ensure_ascii=False, indent=2) + "\n")
