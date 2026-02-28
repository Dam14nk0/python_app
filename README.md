# CodePath – Python for Pentesters

Full-stack learning platform (Flask + MongoDB + React) upgraded from demo to product-oriented skeleton.

## Stack
- Backend: Flask + MongoDB + JWT
- Frontend: React + Vite
- API: REST
- Runtime: Docker

## Seeded learning content
- `backend/seeds/python_for_pentesters_100_days.seed.json`
  - includes hierarchy: categories, tracks, courses, modules, lessons
  - includes full 100-day curriculum with beginner-mode blocks
  - includes checkpoint labs (every 7th day) and integrated mini projects (every 14th day)
  - includes capstone day-by-day build plan (91–100)

## Learning engine integration (current baseline)
- unlock requires previous day completion
- challenge pass required for day completion
- XP scaling tuned for 100-day progression
- difficulty auto progression supported

## UI direction
- IDE-first workspace layout (IDE panel larger than lesson panel)
- stronger editor/output visual priority for coding workflow
- sidebar reflects hierarchy path (Programming → Python → course)

## Key docs
- `docs/architecture.md`
- `docs/day_detail_view_example.md`


## Quick run (Windows/Linux)

Detailed installation + troubleshooting guide is available in `docs/run_windows_linux.md`.

One-time scripts:
- Linux: `./scripts/run_app_linux.sh`
- Windows (PowerShell): `powershell -ExecutionPolicy Bypass -File .\scripts\run_app_windows.ps1`
- Docker: `./scripts/run_app_docker.sh`


## Kali/Linux one-command start

Use:
```bash
./scripts/run_app_linux.sh
```

The script checks dependencies, asks to install missing packages, runs seed/tests, and starts backend+frontend.
