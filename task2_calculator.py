import math
import json
from datetime import datetime
import os

# Save history function
def save_history(entry):
    """Save each calculation to a JSON file with timestamp."""
    history_file = os.path.join(os.path.dirname(__file__), "calculator_history.json")

    # Load existing history
    if os.path.exists(history_file):
        with open(history_file, "r", encoding="utf-8") as f:
            history = json.load(f)
    else:
        history = []

    # Add new entry
    history.append(entry)

    # Save back
    with open(history_file, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4)

def calculator():
    print("Welcome to CodSoft Scientific Calculator")

    # Mapping operation numbers to names
    operations_map = {
        "1": "Addition",
        "2": "Subtraction",
        "3": "Multiplication",
        "4": "Division",
        "5": "Power",
        "6": "Modulus",
        "7": "Square Root",
        "8": "Factorial",
        "9": "Logarithm",
        "10": "Trigonometry"
    }

    while True:
        print("\nChoose Operation:")
        for key, value in operations_map.items():
            print(f"{key}. {value}")
        print("0. Exit")

        choice = input("\nEnter choice: ")

        if choice == "0":
            print("Exiting calculator. Goodbye!")
            break

        try:
            if choice in ["1", "2", "3", "4", "5", "6"]:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    result = num1 + num2
                    print(f"Result: {num1} + {num2} = {result}")
                elif choice == "2":
                    result = num1 - num2
                    print(f"Result: {num1} - {num2} = {result}")
                elif choice == "3":
                    result = num1 * num2
                    print(f"Result: {num1} * {num2} = {result}")
                elif choice == "4":
                    if num2 == 0:
                        print("Cannot divide by zero!")
                        continue
                    result = num1 / num2
                    print(f"Result: {num1} / {num2} = {result}")
                elif choice == "5":
                    result = num1 ** num2
                    print(f"Result: {num1} ^ {num2} = {result}")
                elif choice == "6":
                    result = num1 % num2
                    print(f"Result: {num1} % {num2} = {result}")

            elif choice == "7":
                num = float(input("Enter number: "))
                result = math.sqrt(num)
                print(f"Result: √{num} = {result}")

            elif choice == "8":
                num = int(input("Enter integer: "))
                result = math.factorial(num)
                print(f"Result: {num}! = {result}")

            elif choice == "9":
                num = float(input("Enter number: "))
                result = math.log10(num)
                print(f"Result: log10({num}) = {result}")

            elif choice == "10":
                num = math.radians(float(input("Enter angle in degrees: ")))
                result = {
                    "sin": round(math.sin(num), 4),
                    "cos": round(math.cos(num), 4),
                    "tan": round(math.tan(num), 4) if math.cos(num) != 0 else "undefined"
                }
                print(f"Result: sin = {result['sin']}, cos = {result['cos']}, tan = {result['tan']}")

            else:
                print("Invalid choice!")
                continue

            # Save to history with operation name
            entry = {
                "time": str(datetime.now()),
                "operation": operations_map.get(choice, "Unknown"),
                "result": str(result)
            }
            save_history(entry)

        except ValueError:
            print("Invalid input, please enter valid numbers.")

if __name__ == "__main__":
    calculator()
