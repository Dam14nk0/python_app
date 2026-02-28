#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "[1/5] Preparing Python virtual environment"
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi
source .venv/bin/activate


echo "[2/5] Installing backend dependencies"
pip install -r backend/requirements.txt

echo "[3/5] Generating seed dataset"
python backend/seeds/generate_python_for_pentesters_seed.py

echo "[4/5] Installing frontend dependencies"
(cd frontend && npm install)

echo "[5/5] Starting backend (:5000) and frontend (:5173)"
trap 'kill 0' EXIT
python backend/run.py &
(cd frontend && npm run dev -- --host 0.0.0.0 --port 5173) &
wait
