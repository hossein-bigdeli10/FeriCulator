import math


def get_history():
    open("CalHistory.txt", "a").close()
    with open("CalHistory.txt", "r") as file:
        return [line.strip() for line in file.readlines()]


def clear_history():
    open("CalHistory.txt", "w").close()
    pass


def show_menu():
    print("\n--- Main Menu ---")
    print("1. Standard Calculator")
    print("2. View History")
    print("3. Clear History")
    print("4. Exit")
    choice = input("Select an option (1-4): ")
    return choice


def calculate(num1, operator, num2=None):
    if operator == "sqrt":
        if num1 < 0:
            return "ERROR!"
        return math.sqrt(num1)

    if num2 is None:
        return "error (missing second number)"

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "%":
        return num1 % num2 if num2 != 0 else "DIVISION_BY_ZERO!"
    elif operator == "//":
        return num1 // num2 if num2 != 0 else "DIVISION_BY_ZERO!"
    elif operator == "**":
        return num1 ** num2
    elif operator == "/":
        return num1 / num2 if num2 != 0 else "DIVISION_BY_ZERO!"


print("Welcome to Fericulate!")


while True:
    choice = show_menu()

    if choice == "4":
        print("Thank you for using Fericulate. Goodbye!")
        break

    if choice == "3":
        print("do you want to clear calculation history? (y/n): ")
        confirm = input().strip().lower()
        if confirm != "y":
            print("Operation cancelled. History not cleared.")
            continue
        else:
            print("\nClearing calculation history...")
            clear_history()
            print("History cleared.")

    elif choice == "2":
        print("\n--- Calculation History ---")
        history = get_history()
        if not history:
            print("No history found.")
        else:
            for item in history:
                print(f"- {item}")

    elif choice == "1":
        try:
            n1 = float(input("please enter your first number: "))

            while True:
                op = input(
                    "select one of those opereator. (+, -, *, /, **, %, //, sqrt): ").strip().lower()

                if op not in ["+", "-", "*", "/", "**", "%", "//", "sqrt"]:
                    print("select an operator from the list.")
                    print("invalid operator. please try again.")
                    continue

                if op == "sqrt":
                    result = calculate(n1, op)
                    full_record = f"sqrt {n1} = {result}"
                    print(f"sqrt {n1} = {result}")

                else:
                    n2 = float(input("enter your sec number: "))
                    result = calculate(n1, op, n2)
                    print(f"{n1} {op} {n2} = {result}")
                    full_record = f"{n1} {op} {n2} = {result}"

                print(f"\n result = {full_record}")

                with open("CalHistory.txt", "a") as file:
                    file.write(full_record + "\n")

                break

        except ValueError:
            print("please enter a valid number or operator.")
    else:
        print("invalid menu option.")
