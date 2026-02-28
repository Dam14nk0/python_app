# Run guide (Windows + Linux)

This project includes backend (Flask), frontend (Vite React), seed generator, and tests.

## Quick start (one command)

### Linux
```bash
./scripts/run_app_linux.sh
```

### Windows (PowerShell)
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\run_app_windows.ps1
```

### Docker (Linux/macOS, and Windows with Docker Desktop)
```bash
./scripts/run_app_docker.sh
```

---

## Manual run (Linux)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
python backend/seeds/generate_python_for_pentesters_seed.py
pytest backend/tests -q
python backend/run.py
```

In a second terminal:
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

In a second PowerShell window:
```powershell
cd frontend
npm install
npm run dev -- --host 0.0.0.0 --port 5173
```

Open:
- Frontend: http://localhost:5173
- API health: http://localhost:5000/api/health

---

## Notes
- Language selector now supports **EN / SK / CZ** in the app shell.
- Courses include Python and Bash tracks with fixture-based lessons.
- If PowerShell blocks scripts, run once as admin:
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
