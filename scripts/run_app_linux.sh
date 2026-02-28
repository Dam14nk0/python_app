#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

ask_yes_no() {
  local prompt="$1"
  local default="${2:-Y}"
  local answer
  if [[ "$default" == "Y" ]]; then
    read -r -p "$prompt [Y/n]: " answer || true
    answer="${answer:-Y}"
  else
    read -r -p "$prompt [y/N]: " answer || true
    answer="${answer:-N}"
  fi
  [[ "$answer" =~ ^[Yy]$ ]]
}

need_cmds=(python3 pip3 npm)
missing=()
for c in "${need_cmds[@]}"; do
  command -v "$c" >/dev/null 2>&1 || missing+=("$c")
done

if (( ${#missing[@]} > 0 )); then
  echo "Missing commands: ${missing[*]}"
  if ask_yes_no "Install required packages with apt (Kali/Debian)?" "Y"; then
    sudo apt update
    sudo apt install -y python3 python3-pip python3-venv nodejs npm
  else
    echo "Please install missing dependencies and rerun the script."
    exit 1
  fi
fi

echo "[1/7] Preparing Python virtual environment"
if [[ ! -d ".venv" ]]; then
  python3 -m venv .venv
fi
# shellcheck disable=SC1091
source .venv/bin/activate

echo "[2/7] Upgrading pip"
python -m pip install --upgrade pip

echo "[3/7] Installing backend dependencies"
pip install -r backend/requirements.txt

echo "[4/7] Generating seed dataset"
python backend/seeds/generate_python_for_pentesters_seed.py

echo "[5/7] Running backend tests"
pytest backend/tests -q

echo "[6/7] Installing frontend dependencies"
(cd frontend && npm install)

echo "[7/7] Starting backend (:5000) and frontend (:5173)"
trap 'echo "Stopping services..."; kill 0' EXIT INT TERM
python backend/run.py &
(cd frontend && npm run dev -- --host 0.0.0.0 --port 5173) &

cat <<'MSG'

✅ App is starting.
Open:
- Frontend: http://localhost:5173
- API health: http://localhost:5000/api/health

Press Ctrl+C to stop both services.
MSG

wait
