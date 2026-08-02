"""
Random Password Generator
--------------------------
A tiny beginner project built to practice core Python basics:
  - variables & data types
  - functions
  - importing and USING a library (random + string) -- exactly like
    "pip install" -> "import" -> "use" described in the Python basics notes
  - the Python interpreter running the file line by line, top to bottom

Run it with:  python3 main.py
"""

import random   # standard library -- no pip install needed, it ships with Python
import string   # gives us ready-made character sets (like renting a tool, see notes!)


def build_character_pool(use_upper, use_lower, use_digits, use_symbols):
    """Combine the character sets the user asked for into one pool."""
    pool = ""
    if use_upper:
        pool += string.ascii_uppercase
    if use_lower:
        pool += string.ascii_lowercase
    if use_digits:
        pool += string.digits
    if use_symbols:
        pool += string.punctuation
    return pool


def generate_password(length, pool):
    """Pick `length` random characters from the pool using the random library."""
    if not pool:
        return None
    password = ""
    for _ in range(length):
        password += random.choice(pool)   # random.choice() -> library in action
    return password


def ask_yes_no(prompt):
    answer = input(prompt + " (y/n): ").strip().lower()
    return answer == "y"


def main():
    print("🔐 Welcome to the Random Password Generator!\n")

    length = int(input("How many characters should the password be? "))

    use_upper = ask_yes_no("Include UPPERCASE letters?")
    use_lower = ask_yes_no("Include lowercase letters?")
    use_digits = ask_yes_no("Include digits (0-9)?")
    use_symbols = ask_yes_no("Include symbols (!@#$...)?")

    pool = build_character_pool(use_upper, use_lower, use_digits, use_symbols)
    password = generate_password(length, pool)

    if password is None:
        print("\n❌ You must select at least one character type!")
        return

    print(f"\n✅ Your generated password: {password}")
    print(f"   Pool size used: {len(pool)} possible characters")


if __name__ == "__main__":
    main()
