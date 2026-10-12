# Lab05: MOOS-IvP

Yu-Liang Tan 譚羽良, 112511017

Based on [the Lab05 slides](https://docs.google.com/presentation/d/1x8wc8snRqeBkyieUpvco9AnM9ukjIADRn-8jp79Byxg/edit), especially the four demo tasks on slide 18. The mission is adapted from `ivp/missions/s1_alpha` in MOOS-IvP v24.8.1.

## Run on Linux

After building MOOS-IvP, launch from this directory:

```bash
MOOS_IVP_ROOT=/path/to/moos-ivp ./launch.sh
```

The default checkout location is `~/Workspace/AOOP/moos-ivp`. A graphical desktop is required for `pMarineViewer`. No WSL is needed on Linux.

On the lab PC, v24.8.1 is built at that default location. The launcher loads the missing FLTK 1.3 libraries from the checkout's `lib-runtime/` directory. No host packages or shell configuration were changed. A Debian container was used for compilation and a virtual-display GUI check; the native simulation test ran directly on the Arch Linux host.

1. Press `DEPLOY` to enable the helm and start the square survey.
2. Press `MUCHSLO` for a target speed of 1.0 m/s.
3. Press `MUCHFST` for a target speed of 4.0 m/s.
4. Press `RETURN` to return to the starting corner and stop.
5. Press Ctrl+C in the launch terminal to stop this mission's processes.

Use `./launch.sh 10` for ten-times simulation speed. It changes the time scale, not the commanded speed in m/s. Port 9000 must be free.

## Boat colour

In `alpha.moos`, `pNodeReporter` has:

```text
platform_color = orange
```

The reporter includes this colour in its node reports. `pMarineViewer` uses those reports to draw the boat. Changing the waypoint colour would change the route markers, not the boat.

## Square route

The survey in `alpha.bhv` uses these local coordinates in metres:

```text
points = 60,-40:60,-160:180,-160:180,-40
repeat = forever
```

The four vertices are A = 60,-40, B = 60,-160, C = 180,-160 and D = 180,-40. Every edge is 120 m long, and adjacent edges are perpendicular. Repeating the route adds the closing edge D to A.

The simulator starts at A, facing south. The return waypoint is also A. This avoids an extra approach leg outside the square. The target route is square; the simulated boat rounds its corners because it has finite turning response and a 5 m waypoint capture radius.

## Added speed buttons

In `alpha.moos`:

```text
button_five = MUCHSLO # WPT_UPDATE=speed=1.0 # RETURN_UPDATE=speed=1.0
button_six = MUCHFST # WPT_UPDATE=speed=4.0 # RETURN_UPDATE=speed=4.0
```

Each click publishes a behaviour update through MOOSDB. The survey subscribes through `updates = WPT_UPDATE`; the return behaviour uses `updates = RETURN_UPDATE`. Both buttons therefore work during survey and return. The original `SLOWER` and `FASTER` buttons remain available for survey at 1.5 and 3.5 m/s.

The upstream survey enables `use_alt_speed = true` with `speed_alt = 1.2`. That alternate speed takes precedence over `speed`. This mission explicitly sets `use_alt_speed = false` so the new buttons actually change the helm's target speed. The helm's speed domain includes 4.0 m/s.

`DESIRED_SPEED` is the target, while `NAV_SPEED` is the simulated measured speed. They need not match during acceleration or turns. With `speed_factor = 20`, the PID app requests thrust 20 for 1 m/s and thrust 80 for 4 m/s. These agree with the simulator's configured thrust map on straight legs.

## How to change steering response

The command chain is:

```text
BHV_Waypoint -> pHelmIvP -> DESIRED_HEADING
            -> pMarinePIDV22 -> DESIRED_RUDDER
            -> uSimMarineV22 -> NAV_HEADING
```

The waypoint behaviour chooses a course; the PID controller turns heading error into a rudder command; the simulator determines how the boat moves. All communicate through MOOSDB. Separate responsibilities let us tune steering without changing the waypoint behaviour's C++ code.

### Simulator turning ability

`turn_rate = 95` in `uSimMarineV22` sets the full-speed turning-rate parameter. Reducing it, for example to 50, makes the boat turn more slowly for the same speed, thrust and rudder input. It is not a constant 95 degrees/s at every speed.

In v24.8.1, `SimEngine::propagateHeading` and `TurnSpeedMap` scale the turning rate with speed, reaching the configured full rate at 5 m/s. With the default speed map, no external rotation and forward motion:

```text
rate(v) = turn_rate * min(v / 5, 1)
heading_change = rudder * rate(v) / 100 * dt * thrust / 50
```

Rudder is clipped to -100 through 100. This model cannot turn with its rudder at zero speed. Its response depends on speed and thrust as well as `turn_rate`, so changing speed also changes cornering behaviour.

`turn_spd_loss = 0.4` separately models speed loss while turning. A larger value slows the boat more for the same rudder magnitude. It is not the turning-rate setting.

### Heading controller

In `pMarinePIDV22`, the starting gains are:

```text
yaw_pid_kp = 0.9
yaw_pid_kd = 0.3
yaw_pid_ki = 0.3
maxrudder = 100
```

Increasing the proportional gain usually commands stronger corrections, but excessive gain can produce overshoot or oscillation. The derivative term reacts to changes in heading error and can reduce oscillation. The integral term addresses persistent error, but excessive integral action can also cause overshoot. The integral limit bounds accumulation; `maxrudder` bounds the commanded rudder.

To compare responses, change one parameter at a time and run the same square at the same speed. Inspect `DESIRED_HEADING`, `NAV_HEADING` and `DESIRED_RUDDER`, and compare overshoot and corner-cutting. Do not attribute differences caused by changing speed to a PID gain change.

The waypoint `lead` and `capture_radius` settings affect the guidance path and when the next corner is selected. Smaller capture radii can keep the boat closer to corners but may make waypoint capture harder. They change guidance, not the physical turning ability.

## Tests

Configuration checks require only Python:

```bash
python3 -m unittest -v test_config.py
```

The integration test launches the real MOOSDB, helm, PID and simulator on a separate port, checks both speed commands, waits for two route cycles, returns home and verifies stopping. It reads the telemetry log to check the orange node-report colour, at least two simulated seconds of settled straight-leg speed near each target, ordered position samples within 12 m of A-B-C-D-A, and the closing-leg midpoint. It uses a temporary mission copy and does not edit the submitted files.

```bash
export PATH="$MOOS_IVP_ROOT/bin:$PATH"
export IVP_IMAGE_DIRS="$MOOS_IVP_ROOT/ivp/data"
python3 test_runtime.py
# Also launch the viewer on a virtual display:
xvfb-run -a python3 test_runtime.py --gui
```

The scripted test sends the exact button assignments through `uPokeDB`; by itself it does not prove that a mouse click invokes a GUI button. Runtime evidence is recorded under `evidence/`.

### Verified on 2026-10-12

- Five configuration tests passed; Python compilation and shell syntax checks passed.
- `evidence/native-runtime.json` records the passing native Linux simulation test.
- `evidence/gui-runtime.json` records the passing integration test with `pMarineViewer` on Xvfb.
- `evidence/viewer.png` shows the closed square, orange boat, both added button labels and a 4.0 m/s helm target.
- Both runs completed two waypoint cycles, returned home and stopped. Mission processes were cleaned up afterward.
- GUI button labels were visually inspected, and the test exercised their exact publication assignments. Automated mouse clicking was not tested.

## Sources

- Course slides, installation on slides 14–15 and demo requirements on slide 18.
- MOOS-IvP v24.8.1, commit `477be7e91`, upstream `s1_alpha` mission.
- `ivp/src/lib_behaviors-marine/BHV_Waypoint.cpp`, alternate-speed selection and behaviour updates.
- `ivp/src/uSimMarineV22/SimEngine.cpp` and `TurnSpeedMap.cpp`, heading propagation.
- `ivp/src/pMarineViewer/PMV_GUI.cpp`, button publications.

Final-project grouping in the announcement is a separate classroom task, not part of this mission.
