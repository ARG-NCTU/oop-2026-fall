#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"
export PATH="$PATH:$HOME/moos-ivp/bin"
for app in MOOSDB pAntler pHelmIvP pMarineViewer; do
  command -v "$app" >/dev/null || { echo "Missing $app: build ~/moos-ivp first."; exit 1; }
done
exec pAntler alpha.moos
