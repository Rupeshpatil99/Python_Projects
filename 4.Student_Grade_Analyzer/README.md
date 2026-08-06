# 📊 Student Grade Analyzer

A beginner-friendly Python project built to practice and demonstrate the core fundamentals of the language — all in one small, real-world-style script.

## 🧠 What This Project Covers

| Concept | Where it's used |
|---|---|
| **Data types** | `int`, `float`, `str`, `bool` |
| **Data structures** | `list`, `tuple`, `dict`, `set` |
| **Loops** | `for` loops, `range()` |
| **Functions** | `get_grade()`, `passed()`, `analyze_scores()`, `top_and_bottom()` |
| **Conditional statements** | `if` / `elif` / `else` |
| **List comprehensions** | building the failed-students list |
| **Lambda functions** | finding top/bottom scorer with `max()`/`min()` |

## 🚀 What It Does

The script simulates a class of students (name + score), then:

- ✅ Assigns each student a letter grade (A–F)
- 📈 Calculates the class average and pass/fail counts
- 🔎 Tracks all unique grades earned using a `set`
- 📋 Builds a dictionary of full student records for fast lookups
- 🏆 Identifies the top and bottom scorer
- 📉 Summarizes overall class performance
- 🎯 Lists every student who failed using a list comprehension

## 📁 Project Structure

```
.
├── grade_analyzer.py     # Main script
└── README.md             # Project documentation
```

## ▶️ How to Run

**Requirements:** Python 3.x (no external libraries needed)

1. Clone this repository:
   ```bash
   git clone https://github.com/Rupeshpatil99/Python_Projects.git
   cd "Python_Projects/5.Student Grade Analyzer"
   ```

2. Run the script:
   ```bash
   python grade_analyzer.py
   ```
   *(use `python3` instead of `python` on Mac/Linux if needed)*

## 📤 Sample Output

```
Student   Score   Grade   Status
----------------------------------------
Aarav     55      F       Fail
Priya     78      C       Pass
Rohan     92      A       Pass
...
----------------------------------------
Class Average : 68.50
Passed        : 7
Failed        : 3
Overall class performance: Satisfactory 👍

--- DATA STRUCTURE DEMO ---
Unique grades earned (set)   : {'B', 'D', 'A', 'C', 'F'}
Grade distribution (dict)   :
   A: 2
   B: 1
   C: 2
   D: 2
   F: 3

Top scorer    : Meera (100)
Bottom scorer : Anaya (34)
Students who failed (list)  : ['Aarav', 'Sneha', 'Anaya']
```

## 🔮 Planned Improvements

- [ ] Read student data from a CSV file instead of hardcoded values
- [ ] Add `while` loop-based interactive input
- [ ] Add string handling / formatting exercises
- [ ] Export results back to a CSV or JSON report

## 🙋 Author

Built as a hands-on learning project to strengthen Python fundamentals for data analytics.

## 📄 License

This project is open source and available for learning purposes.
