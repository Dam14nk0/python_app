# Day Detail View Example (UI copy)

## Day 42 — Practical retry logic for pentest API workflows

**Difficulty:** Advanced  
**Estimated time:** 40 min  
**Module:** Web Requests & APIs

### Lesson intro
Today you build resilient API calls for hostile network conditions. You will add timeout strategy, bounded retries, and normalized output objects so the next parsing stage can consume data safely.

### Content blocks
1. Model real-world API instability (timeouts, 500s, malformed JSON).
2. Implement defensive request wrapper with timeout + retry budget.
3. Normalize all responses into one schema: `target`, `status`, `service`, `error`.

### Step-by-step path
1. Create `fetch_target(target)` with explicit timeout.
2. Wrap request call in retry loop (`max_attempts=3`) with backoff.
3. Parse JSON defensively, fallback to defaults when keys are missing.
4. Emit deterministic result list and write summary to `reports/day42.json`.

### Tasks checklist (2/5)
- ✅ Define request function and timeout constants.
- ✅ Add retry loop and last-error capture.
- ⬜ Handle non-JSON responses gracefully.
- ⬜ Normalize output schema for all branches.
- ⬜ Run Check and compare with expected behavior.

### Challenge
**Description:** Call multiple host APIs safely and aggregate only valid service records.  
**Starter code:**
```python
import requests

hosts = ["10.10.10.1", "10.10.10.2"]
# TODO: implement timeout + retries + normalization
```

**Expected behavior:**
- Script never crashes on timeout or bad response.
- Returns normalized records list.
- Prints summary: `processed`, `failed`, `retried`.

### Mini project deliverable
Submit `api_collector.py` + `reports/day42.json` where collector supports retries, defensive parsing, and clean summary output ready for integration into the final OOP CLI tool.
