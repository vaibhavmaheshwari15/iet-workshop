#!/usr/bin/env bash
# Start ADK Dev UI so it works through Cursor Cloud's HTTPS port proxy.
#
# Default `adk web` binds 127.0.0.1 and only allows loopback Origins.
# Opening https://p-8000-*.agent.cvm.dev/dev-ui/ then loads index.html
# (dark blank page) while module scripts/API calls are rejected with
# 403 "origin not allowed" / "host not allowed" — a black screen.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

mkdir -p "${HOME}/.adk"
if [[ ! -f "${HOME}/.adk/config.json" ]]; then
  printf '{\n  "telemetry": false\n}\n' > "${HOME}/.adk/config.json"
fi

VENV="${ADK_VENV:-$HOME/.venvs/adk}"
if [[ -x "$VENV/bin/adk" ]]; then
  ADK="$VENV/bin/adk"
elif [[ -x "$ROOT/.venv/bin/adk" ]]; then
  ADK="$ROOT/.venv/bin/adk"
elif command -v adk >/dev/null 2>&1; then
  ADK="$(command -v adk)"
else
  echo "google-adk is not installed. Run: ./scripts/install-adk.sh" >&2
  exit 1
fi

if [[ -f "$ROOT/my_agent/.env" ]]; then
  set -a
  # shellcheck disable=SC1091
  source "$ROOT/my_agent/.env"
  set +a
fi

# Bind all interfaces and allow any Origin so the Cloud Agent port proxy
# (https://p-<port>-*.agent.cvm.dev) can load the Angular Dev UI.
exec "$ADK" web \
  --host 0.0.0.0 \
  --port "${ADK_PORT:-8000}" \
  --allow_origins '*' \
  --no-reload \
  .
