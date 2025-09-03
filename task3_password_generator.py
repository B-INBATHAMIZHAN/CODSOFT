import random
import string
import os
from datetime import datetime

def generate_password(length, use_digits=True, use_symbols=True):
    """
    Generate a secure random password.
    """
    chars = string.ascii_letters  # a-z + A-Z
    
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        raise ValueError("No characters selected to generate password!")

    return ''.join(random.choice(chars) for _ in range(length))


def save_passwords(passwords):
    """
    Save generated passwords to a text file in same directory.
    Each run will be stored with a timestamp header.
    """
    filename = os.path.join(os.path.dirname(__file__), "codsoft_passwords.txt")
    with open(filename, "a", encoding="utf-8") as file:
        file.write("\n=== Passwords Generated at {} ===\n".format(datetime.now()))
        for pwd in passwords:
            file.write(pwd + "\n")
    print(f"\n Passwords saved successfully to {filename}")


def main():
    print(" Welcome to CodSoft Internship Password Generator ")
    try:
        count = int(input(" How many passwords do you want to generate? "))
        length = int(input(" Enter password length: "))

        # Options for digits & symbols
        use_digits = input(" Include digits? (y/n): ").strip().lower() == "y"
        use_symbols = input(" Include symbols? (y/n): ").strip().lower() == "y"

        passwords = []
        for i in range(count):
            pwd = generate_password(length, use_digits, use_symbols)
            passwords.append(pwd)
            print(f"Password {i+1}: {pwd}")

        # Save all passwords in file
        save_passwords(passwords)

    except ValueError:
        print(" Invalid input! Please enter numbers for count and length.")

if __name__ == "__main__":
    main()
