# ============================
# ATM Banking System
# Author: Rupesh Patil
# ============================

balance = 5000
pin = "1234"
transactions = []


# -----------------------------
# Functions
# -----------------------------
def check_balance():
    print(f"\nCurrent Balance: ₹{balance}")


def deposit():
    global balance

    amount = float(input("Enter deposit amount: ₹"))

    if amount > 0:
        balance += amount
        transactions.append(f"Deposited ₹{amount}")
        print("Deposit Successful.")
    else:
        print("Invalid Amount.")


def withdraw():
    global balance

    amount = float(input("Enter withdrawal amount: ₹"))

    if amount <= 0:
        print("Invalid Amount.")

    elif amount <= balance:
        balance -= amount
        transactions.append(f"Withdraw ₹{amount}")
        print("Please collect your cash.")

    else:
        print("Insufficient Balance.")


def transaction_history():

    if len(transactions) == 0:
        print("\nNo Transactions Yet.")

    else:
        print("\nTransaction History")

        for i in range(len(transactions)):
            print(f"{i+1}. {transactions[i]}")


def change_pin():
    global pin

    old = input("Enter Current PIN: ")

    if old == pin:

        new = input("Enter New PIN: ")

        pin = new

        print("PIN Changed Successfully.")

    else:
        print("Wrong PIN.")


# -----------------------------
# Login
# -----------------------------

print("=" * 35)
print("      Welcome To Python ATM")
print("=" * 35)

entered_pin = input("Enter 4-digit PIN: ")

if entered_pin != pin:
    print("Incorrect PIN")
    print("Program End")

else:

    while True:

        print("\n====== ATM MENU ======")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Change PIN")
        print("6. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            transaction_history()

        elif choice == "5":
            change_pin()

        elif choice == "6":
            print("\nThank You For Using Our ATM.")
            break

        else:
            print("Invalid Choice.")