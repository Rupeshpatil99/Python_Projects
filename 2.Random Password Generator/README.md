# 🔐 Random Password Generator

A beginner CLI project built to practice the fundamentals from "Introduction to Python" — variables,
functions, and how to `import` and actually use a library.

## Concepts used
| Concept | Where it's used |
|---|---|
| **Importing a library** | `import random`, `import string` — exactly the 3-step pattern (install → import → use) from the notes, using two built-in libraries so no `pip install` is even needed |
| **Functions** | `build_character_pool()`, `generate_password()`, `ask_yes_no()` keep the code organized |
| **Variables** | `length`, `pool`, `password` hold the program's state |
| **The interpreter** | Python runs `main()` top to bottom, line by line, exactly like the "live UN translator" analogy in the notes |

## Features
- Choose password length
- Toggle uppercase, lowercase, digits, and symbols on/off
- Warns you if you deselect every character type

## Run it
```bash
python3 main.py
```

## Possible next steps
- Add a "password strength" rating
- Let the user generate multiple passwords at once and save them to a file
- Add a `--length` command-line flag using the `argparse` library
