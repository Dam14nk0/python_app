$ErrorActionPreference = "Stop"

$Root = (Resolve-Path "$PSScriptRoot\..").Path
Set-Location $Root

Write-Host "[1/5] Preparing Python virtual environment"
if (-Not (Test-Path ".venv")) {
  py -3 -m venv .venv
}

Write-Host "[2/5] Installing backend dependencies"
& .\.venv\Scripts\python.exe -m pip install -r backend\requirements.txt

Write-Host "[3/5] Generating seed dataset"
& .\.venv\Scripts\python.exe backend\seeds\generate_python_for_pentesters_seed.py

Write-Host "[4/5] Installing frontend dependencies"
Push-Location frontend
npm install
Pop-Location

Write-Host "[5/5] Starting backend (:5000) and frontend (:5173) in separate windows"
Start-Process powershell -ArgumentList "-NoExit", "-Command", "Set-Location '$Root'; .\.venv\Scripts\python.exe backend\run.py"
Start-Process powershell -ArgumentList "-NoExit", "-Command", "Set-Location '$Root\frontend'; npm run dev -- --host 0.0.0.0 --port 5173"

Write-Host "Done. Open http://localhost:5173"
