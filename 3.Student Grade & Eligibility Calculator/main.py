"""
Student Grade & Eligibility Calculator
----------------------------------------
A small project built to practice conditional statements:
  - if / elif / else
  - comparison operators (>=, ==, etc.)
  - logical operators (and, or)

Run it with:  python3 main.py
"""


def get_grade(marks):
    """if / elif / else chain -- stops at the first True condition."""
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"


def is_pass(marks):
    """A single condition, no logical operator needed."""
    return marks >= 40


def check_scholarship_eligibility(marks, attendance_percent):
    """
    Uses 'and' -- BOTH conditions must be True.
    Real-life analogy from the notes: boarding a flight needs a ticket AND an ID.
    """
    return marks >= 85 and attendance_percent >= 90


def check_re_exam_allowed(marks, medical_leave, sports_event):
    """
    Uses 'or' -- only ONE condition needs to be True.
    Real-life analogy from the notes: entering a club with membership OR a guest pass.
    """
    return marks < 40 or medical_leave or sports_event


def main():
    print("🎓 Student Grade & Eligibility Calculator\n")

    name = input("Student name: ").strip()
    marks = float(input("Marks obtained (out of 100): "))
    attendance = float(input("Attendance percentage: "))

    grade = get_grade(marks)
    passed = is_pass(marks)

    print(f"\n--- Result for {name} ---")
    print(f"Marks   : {marks}")
    print(f"Grade   : {grade}")
    print(f"Status  : {'PASS ✅' if passed else 'FAIL ❌'}")

    if check_scholarship_eligibility(marks, attendance):
        print("🏆 Eligible for a scholarship! (marks >= 85 AND attendance >= 90)")
    else:
        print("Not eligible for a scholarship this term.")

    if not passed:
        medical_leave = input("Did the student have medical leave? (y/n): ").strip().lower() == "y"
        sports_event = input("Did the student attend a sports event? (y/n): ").strip().lower() == "y"

        if check_re_exam_allowed(marks, medical_leave, sports_event):
            print("📝 Re-exam allowed (failed OR had medical leave OR sports event).")
        else:
            print("Re-exam not applicable.")


if __name__ == "__main__":
    main()
