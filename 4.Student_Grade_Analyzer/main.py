"""
Student Grade Analyzer
------------------------
A beginner Python project that practices:
- Data types: int, float, str, bool
- Data structures: list, tuple, dict, set
- range()
- for loops
- functions
- if / elif / else conditional statements
"""

# DATA STRUCTURE 1: List of tuples 
# Each tuple is an immutable (name, score) pair.
students = [
    ("Aarav", 55),
    ("Priya", 78),
    ("Rohan", 92),
    ("Sneha", 40),
    ("Kabir", 65),
    ("Isha", 88),
    ("Dev", 73),
    ("Meera", 100),
    ("Yusuf", 60),
    ("Anaya", 34),
]

def get_grade(score):
    """Return a letter grade based on a numeric score, using conditionals."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# Function: check if a student passed 
def passed(score, pass_mark=60):
    """Return True/False depending on whether the score meets the pass mark."""
    return score >= pass_mark


#  Main function: builds data structures + analyzes scores ----
def analyze_scores(students):
    #  DATA STRUCTURE 2: Dictionary 
    # Maps each student's name -> a record dict {score, grade, status}
    records = {}

    #  DATA STRUCTURE 3: Set 
    # Sets auto-remove duplicates -> perfect for "which unique grades appeared"
    unique_grades = set()

    # ---- DATA STRUCTURE 4: Dictionary used as a counter ----
    grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    total = 0
    pass_count = 0
    fail_count = 0

    print(f"{'Student':<10}{'Score':<8}{'Grade':<8}{'Status'}")
    print("-" * 40)

    # loop using range() over the list of tuples
    for i in range(len(students)):
        name, score = students[i]          # tuple unpacking
        grade = get_grade(score)           # function call
        total += score

        if passed(score):                  # conditional statement
            status = "Pass"
            pass_count += 1
        else:
            status = "Fail"
            fail_count += 1

        # store this student's full record in the dictionary
        records[name] = {"score": score, "grade": grade, "status": status}

        # track unique grades seen so far
        unique_grades.add(grade)

        # update the grade counter dictionary
        grade_counts[grade] += 1

        print(f"{name:<10}{score:<8}{grade:<8}{status}")

    average = total / len(students)

    print("-" * 40)
    print(f"Class Average : {average:.2f}")
    print(f"Passed        : {pass_count}")
    print(f"Failed        : {fail_count}")

    if average >= 75:
        print("Overall class performance: Excellent 🎉")
    elif average >= 60:
        print("Overall class performance: Satisfactory 👍")
    else:
        print("Overall class performance: Needs improvement 📉")

    return records, unique_grades, grade_counts


# ---- Function: find top and bottom scorer using the dict of records ----
def top_and_bottom(records):
    # dict.items() -> loop over (name, record) pairs
    top_name = max(records, key=lambda n: records[n]["score"])
    bottom_name = min(records, key=lambda n: records[n]["score"])
    return top_name, bottom_name


if __name__ == "__main__":
    records, unique_grades, grade_counts = analyze_scores(students)

    print("\n--- DATA STRUCTURE DEMO ---")

    # Using the SET: unique grades earned by the class
    print(f"Unique grades earned (set)   : {unique_grades}")

    # Using the DICT counter: how many students got each grade
    print("Grade distribution (dict)   :")
    for grade in ("A", "B", "C", "D", "F"):     # loop over a tuple of grade labels
        print(f"   {grade}: {grade_counts[grade]}")

    # Using the DICT of records: look up any student directly by name (fast lookup)
    lookup_name = "Rohan"
    print(f"\nLookup '{lookup_name}' in records dict -> {records[lookup_name]}")

    # Top / bottom scorer
    top_name, bottom_name = top_and_bottom(records)
    print(f"\nTop scorer    : {top_name} ({records[top_name]['score']})")
    print(f"Bottom scorer : {bottom_name} ({records[bottom_name]['score']})")

    # Using a LIST comprehension: names of everyone who failed
    failed_students = [name for name, r in records.items() if r["status"] == "Fail"]
    print(f"\nStudents who failed (list)  : {failed_students}")
