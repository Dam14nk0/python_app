# 7️⃣ OUTPUT

## 1) Updated database structure

```text
categories
  - slug
  - title
  - description

tracks
  - slug
  - category_slug
  - title
  - description

courses
  - slug
  - track_slug
  - title
  - description
  - beginner_mode
  - final_goal

modules
  - course_slug
  - module_key
  - title
  - order
  - day_start
  - day_end

lessons
  - category_slug
  - track_slug
  - course_slug
  - module_key
  - day_number
  - title
  - difficulty (auto progression)
  - est_minutes
  - lesson_type (standard/checkpoint_lab/integrated_mini_project)
  - checkpoint_lab
  - integrated_mini_project_day
  - beginner_mode {assume_zero_knowledge, dependency_rule}
  - concept
  - allowed_concepts
  - content_blocks [{kind: what|why|real_example|common_mistake, text}]
  - step_by_step_path
  - tasks
  - challenge {description, starter_code, expected_behavior, used_concepts, pass_required_for_day_completion}
  - mini_project
  - learning_engine {unlock_rule, completion_rule, xp_rewards}
  - capstone_alignment
```

---

## 2) Updated folder structure

```text
python_app/
├─ backend/
│  ├─ app/
│  │  ├─ api/
│  │  ├─ models/
│  │  ├─ repositories/
│  │  ├─ services/
│  │  │  ├─ learning_engine_service.py
│  │  │  ├─ xp_service.py
│  │  │  └─ ide_service.py
│  │  └─ utils/
│  ├─ seeds/
│  │  ├─ generate_python_for_pentesters_seed.py
│  │  └─ python_for_pentesters_100_days.seed.json
│  ├─ tests/
│  │  ├─ test_health.py
│  │  ├─ test_learning_engine.py
│  │  └─ test_seed_content.py
│  ├─ requirements.txt
│  └─ run.py
├─ frontend/
│  ├─ src/
│  │  ├─ components/
│  │  ├─ pages/
│  │  ├─ services/
│  │  ├─ store/
│  │  └─ styles/
│  └─ package.json
├─ docs/
│  ├─ architecture.md
│  ├─ day_detail_view_example.md
│  └─ requested_output.md
└─ docker-compose.yml
```

---

## 3) Updated UI layout adjustments

- IDE-first rebalance:
  - app shell columns changed to give IDE most space.
  - center lesson constrained slightly narrower.
- Editor panel:
  - significantly increased min-height.
- Output panel:
  - higher min-height + stronger contrast + stronger border.
  - visually weighted as a critical panel.
- Sidebar hierarchy:
  - now displays `Programming / Python / Python for Pentesters` context.

---

## 4) Seeding script for 100 days

Use:

```bash
python backend/seeds/generate_python_for_pentesters_seed.py
```

This script generates:

- all 100 lessons
- checkpoint labs every 7th day
- integrated mini-projects every 14th day
- capstone milestone sequence (91–100)
- beginner-mode blocks for every lesson
- strict dependency metadata for challenge concept usage

---

## 5) Sample Day 1 (very detailed, beginner-friendly)

**Day 1: Basics — Python Syntax**

- **What it is:** Python syntax is the grammar of writing code (indentation, statements, variables, function calls).
- **Why it matters:** If syntax is wrong, your script will not run; automation reliability starts with valid syntax.
- **Real example:** Create a small script that prints target IPs from a list.
- **Common mistake:** Mixing tabs/spaces or forgetting `:` after `for`/`if` blocks.

**Step-by-step path**
1. Create `targets = ["10.0.0.1", "10.0.0.2"]`.
2. Print each target using a `for` loop.
3. Add one empty entry and skip it.
4. Print how many targets were processed.

**Tasks**
- Explain what syntax means in 1 sentence.
- Run the script and fix one syntax error intentionally.
- Add safe skip for empty item.
- Pass challenge check.

**Challenge constraints**
- Only use Day 1 concepts.
- No advanced libraries.
- Challenge pass required for completion.

**Mini project**
- Submit `day1_targets.py` that reads static list and prints clean processed output.

---

## 6) Sample Day 50 (mid-level)

**Day 50: Parsing & Regex — Structured Records**

- **What it is:** Converting unstructured scanner output into predictable dictionary/object records.
- **Why it matters:** Subsequent pipeline steps (storage/reporting) require stable schema.
- **Real example:** Parse lines like `host=10.0.0.5 port=443 service=https` into JSON entries.
- **Common mistake:** Regex that is too greedy and captures invalid tokens.

**Step-by-step path**
1. Define a regex pattern with named groups.
2. Parse each line and validate required fields.
3. Skip malformed rows with explicit reason.
4. Return final list of normalized records.

**Tasks**
- Parse at least 10 sample lines.
- Validate IP and port ranges.
- Log skipped lines.
- Pass challenge check.

**Mini project**
- Submit `parser_pipeline.py` + `normalized_output.json` with robust malformed-input handling.

---

## 7) Sample Day 95 (advanced, capstone building)

**Day 95: Capstone — Integrate parsing/normalization pipeline**

- **What it is:** Wiring parser module into the core OOP CLI execution flow.
- **Why it matters:** Raw HTTP/file output is useless unless normalized into reusable records.
- **Real example:** `tool scan --input hosts.txt --out findings.json` where parser normalizes each response.
- **Common mistake:** Tightly coupling parser with CLI argument parsing, making unit testing difficult.

**Step-by-step path**
1. Define parser interface accepted by core orchestrator.
2. Feed raw response objects into parser service.
3. Emit normalized finding model list.
4. Store normalized output for report/export modules.

**Tasks**
- Integrate parser class with orchestrator.
- Add error handling for malformed body.
- Add tests for parser integration path.
- Run full command flow and pass challenge.

**Mini project**
- Submit integrated capstone branch where parser module is fully connected to CLI command path with sample report output.
