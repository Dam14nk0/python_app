# Kali Workspace Upgrade Output

## 1) Python 100-day completeness
- **Yes**: `Programming → Python → Python for Pentesters` has all **100 days** seeded.
- Module spans confirmed:
  - 1–14 Basics
  - 15–30 Files & Automation
  - 31–45 Web Requests & APIs
  - 46–60 Parsing & Regex
  - 61–75 OOP & Architecture
  - 76–90 CLI & Tooling
  - 91–100 Capstone
- Missing items fixed: fixture/tool-format dependency gating, explicit Day 46 fixture challenge requirements, and schema fields for workspace workflows.

## 2) Updated DB structure additions

### `fixtures`
- `name`
- `tool`
- `format`
- `difficulty`
- `content`
- `tags`

### `user_files`
- `user_id`
- `course_slug`
- `files: [{ path, content, updated_at }]`
- `last_modified`

### Lesson schema additions
- `fixtures_used: [fixture_name]`
- `workspace_tasks: [string]`
- `challenge.file_requirements`

## 3) Kali Workspace page structure
- Left: File Explorer + plain-text editor
- Center: Terminal Output Viewer (read-only fixture blocks)
  - Copy block
  - Save block to file
  - Search output
- Right: Notes/Tasks + required output files

## 4) Example lesson updates

### Python Day 46
- Fixtures: `nmap_basic_scan`, `gobuster_dirs_small`, `ffuf_api_probe`
- Tasks: save fixture blocks into `outputs/*.txt`, extract ports/endpoints, write summary.
- Challenge checks:
  - files exist: `outputs/ports.json`, `outputs/endpoints.csv`, `outputs/report.md`
  - JSON keys and CSV columns
  - required values present

### Bash Day 12
- Fixtures: `gobuster_dirs_small`, `app_log_success_error`
- Tasks: parse with `grep/awk/sed` and produce `outputs/report.txt`
- Challenge checks required extracted lines and totals.

## 5) Seed summary counts
- Categories: **1**
- Tracks: **2**
- Courses: **2**
- Modules: **10**
- Lessons: **130**
- Fixture library entries: **21**
- Fixture instances attached across lessons: **187**

## 6) Kali Linux run instructions

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv nodejs npm docker.io docker-compose-plugin
```

```bash
cd /workspace/python_app
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
python backend/seeds/generate_python_for_pentesters_seed.py
pytest backend/tests -q
python backend/run.py
```

```bash
cd /workspace/python_app/frontend
npm install
npm run dev -- --host 0.0.0.0 --port 5173
```
Open: `http://127.0.0.1:5173`

Optional Docker:
```bash
cd /workspace/python_app
docker compose up --build
```
