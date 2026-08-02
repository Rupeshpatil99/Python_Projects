# 🎓 Student Grade & Eligibility Calculator

A CLI project built to practice `if` / `elif` / `else` and logical operators (`and`, `or`).

## Concepts used
| Concept | Where it's used |
|---|---|
| **if / elif / else chain** | `get_grade()` assigns A–F based on marks, stopping at the first true condition |
| **Single condition (no logical operator)** | `is_pass()` — just one comparison, `marks >= 40` |
| **`and`** | `check_scholarship_eligibility()` — needs high marks **AND** high attendance |
| **`or`** | `check_re_exam_allowed()` — failing **OR** medical leave **OR** a sports event is enough |

## Features
- Calculates letter grade (A/B/C/D/F)
- Pass/Fail status
- Scholarship eligibility check
- Re-exam eligibility check (only asked if the student failed)

## Run it
```bash
python3 main.py
```

## Possible next steps
- Loop the program so it can grade a whole class and print a summary
- Add input validation (reject marks outside 0–100)
- Export results to a CSV file
