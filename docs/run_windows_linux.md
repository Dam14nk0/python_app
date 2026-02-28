# Run guide (Windows + Linux / Kali)

This project includes backend (Flask), frontend (Vite React), seed generator, and tests.

## Quick start (one command)

### Kali / Linux (recommended)
```bash
./scripts/run_app_linux.sh
```

What this script does automatically:
1. Checks required tools (`python3`, `pip3`, `npm`).
2. If missing, asks whether to install dependencies via `apt`.
3. Creates `.venv`.
4. Installs backend dependencies.
5. Generates seed data.
6. Runs backend tests.
7. Installs frontend dependencies and starts API + frontend.

### Windows (PowerShell)
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\run_app_windows.ps1
```

### Docker
```bash
./scripts/run_app_docker.sh
```

---

## Manual run (Kali/Linux)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
python backend/seeds/generate_python_for_pentesters_seed.py
pytest backend/tests -q
python backend/run.py
```

In second terminal:
```bash
cd frontend
npm install
npm run dev -- --host 0.0.0.0 --port 5173
```

Open:
- Frontend: http://localhost:5173
- API health: http://localhost:5000/api/health

---

## Manual run (Windows)

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r backend\requirements.txt
python backend\seeds\generate_python_for_pentesters_seed.py
pytest backend\tests -q
python backend\run.py
```

In second PowerShell window:
```powershell
cd frontend
npm install
npm run dev -- --host 0.0.0.0 --port 5173
```

---

## Troubleshooting (expected/common issues)

### 1) `python3: command not found` or `npm: command not found`
Install dependencies:
```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv nodejs npm
```

### 2) Port already in use (`5000` or `5173`)
Find and stop process:
```bash
lsof -i :5000
lsof -i :5173
kill -9 <PID>
```

### 3) Frontend says `vite: not found`
Reinstall node modules in `frontend`:
```bash
cd frontend
npm install
npm run build
```

### 4) Backend tests fail with missing Flask/PyMongo
Ensure virtualenv is active and install requirements:
```bash
source .venv/bin/activate
pip install -r backend/requirements.txt
pytest backend/tests -q
```

### 5) PowerShell blocks script execution (Windows)
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 6) Mongo connection issues
Current backend has fallback behavior for local dev in some features, but if you run full stack use Docker:
```bash
./scripts/run_app_docker.sh
```

---

## Notes
- Language selector supports **EN / SK**.
- Courses include Python and Bash tracks with fixture-based lessons and real-output parsing tasks.
