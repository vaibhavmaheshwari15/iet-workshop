#!/usr/bin/env bash
# Idempotent Cloud Agent / local bootstrap for Google ADK.
# The venv lives outside /workspace so git checkout cleanup cannot delete it.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if ! python3 -c 'import venv, ensurepip' 2>/dev/null; then
  sudo apt-get update -qq
  sudo DEBIAN_FRONTEND=noninteractive apt-get install -y -qq python3.12-venv python3-pip
fi

VENV="${ADK_VENV:-$HOME/.venvs/adk}"
python3 -m venv "$VENV"
"$VENV/bin/pip" install -U pip
if [[ -f "$ROOT/requirements.txt" ]]; then
  "$VENV/bin/pip" install -r "$ROOT/requirements.txt"
else
  "$VENV/bin/pip" install 'google-adk>=1.2.0'
fi

mkdir -p "${HOME}/.adk"
python3 - <<'PY'
from pathlib import Path
import json
path = Path.home() / ".adk" / "config.json"
config = {}
if path.exists():
    try:
        config = json.loads(path.read_text())
        if not isinstance(config, dict):
            config = {}
    except Exception:
        config = {}
if "telemetry" not in config:
    config["telemetry"] = False
    path.write_text(json.dumps(config, indent=2) + "\n")
PY
