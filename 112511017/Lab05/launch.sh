#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
# Override this if MOOS-IvP is installed elsewhere, e.g. ~/moos-ivp on WSL.
MOOS_IVP_ROOT="${MOOS_IVP_ROOT:-$(cd ../../.. && pwd)/moos-ivp}"
export PATH="$MOOS_IVP_ROOT/bin:$PATH"
# Optional user-local runtime libraries, used on the lab PC for FLTK 1.3.
if [[ -d "$MOOS_IVP_ROOT/lib-runtime" ]]; then
  export LD_LIBRARY_PATH="$MOOS_IVP_ROOT/lib-runtime${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
fi
if [[ -d "$MOOS_IVP_ROOT/build/MOOS/MOOSGeodesy/lib" ]]; then
  export LD_LIBRARY_PATH="$MOOS_IVP_ROOT/build/MOOS/MOOSGeodesy/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
fi
export IVP_IMAGE_DIRS="$MOOS_IVP_ROOT/ivp/data${IVP_IMAGE_DIRS:+:$IVP_IMAGE_DIRS}"
if [[ "${1:-}" == "--help" ]]; then
  printf 'Usage: ./launch.sh [positive_integer_time_warp]\nPress DEPLOY to start; Ctrl+C stops this mission.\n'
  exit 0
fi
warp="${1:-1}"
[[ $# -le 1 && "$warp" =~ ^[1-9][0-9]*$ ]] || { echo 'Invalid time warp' >&2; exit 2; }
command -v pAntler >/dev/null || { echo 'pAntler missing. Set MOOS_IVP_ROOT to your built MOOS-IvP checkout.' >&2; exit 1; }
command -v setsid >/dev/null || { echo 'setsid missing' >&2; exit 1; }
# Kill only the process group created for this mission, not other MOOS missions.
setsid pAntler alpha.moos --MOOSTimeWarp="$warp" &
mission_pid=$!
cleanup() {
  trap - EXIT INT TERM
  kill -TERM -- "-$mission_pid" 2>/dev/null || true
  for _ in {1..25}; do
    kill -0 -- "-$mission_pid" 2>/dev/null || break
    sleep 0.2
  done
  kill -KILL -- "-$mission_pid" 2>/dev/null || true
  wait "$mission_pid" 2>/dev/null || true
}
trap cleanup EXIT
trap 'exit 130' INT
trap 'exit 143' TERM
wait "$mission_pid"
