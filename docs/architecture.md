# CodePath – Architecture Proposal (Upgraded)

## Product hierarchy (scalable)

```text
Category -> Track -> Course -> Module -> Lesson
Programming -> Python -> Python for Pentesters -> 7 modules -> Day 1..100
```

Collections:
- `categories`
- `tracks`
- `courses`
- `modules`
- `lessons`
- `progress`
- `submissions`

This enables future language expansion while reusing the same learning engine.

## Learning engine rules

- Day unlock rule: `day N` unlocks only after `day N-1` completion.
- Day completion rule: challenge must pass.
- Difficulty is auto-assigned by progression (1–35 Beginner, 36–75 Intermediate, 76–100 Advanced).
- XP scaling for 100-day journey:
  - task completion: +15 XP
  - challenge pass: +60 XP
  - day completion: +120 XP

## Course structure

Modules and day ranges:
- 1–14 Basics
- 15–30 Files & Automation
- 31–45 Web Requests & APIs
- 46–60 Parsing & Regex
- 61–75 OOP & Architecture
- 76–90 CLI & Tooling
- 91–100 Capstone

Pacing rules:
- every 7th day = checkpoint lab
- every 14th day = integrated mini project
- days 91–100 = final large OOP CLI tool implementation milestones

## Beginner mode enforcement

Each lesson includes explicit blocks:
- `what`
- `why`
- `real_example`
- `common_mistake`

Challenge payload includes `used_concepts`, and seed stores `allowed_concepts` to enforce strict concept dependency chain.

## Capstone final tool (days 91–100)

The final deliverable is a large modular OOP CLI pentesting utility containing:
- HTTP requests
- file input/output
- response parsing
- structured logging
- argument parsing
- config loader
- reusable services/components
- robust error handling
