import random
import string
import datetime

# Programmed to iterate random alphanumerical tables to use for authentication on communication channels.

# Please note that a random table will be generated upon each execution. Document immediately after generation.
print(f'\nAuthentication Code # <<{datetime.datetime.now()}>>\n')

def generate_random_value():
    """Generates a random alphanumeric value (letter + digit)."""
    letter = random.choice(string.ascii_uppercase)  # Random letter (A-Z)
    digit1 = random.choice(string.digits)  # Random digit (0-9)
    digit2 = random.choice(string.digits)  # Random Digit (0-9)
    return letter + digit1 + digit2


def create_auth_table():
    """Creates a 9x9 authentication table."""
    table = {}
    rows = string.ascii_uppercase[:9]  # First 9 letters (A-I)
    cols = [str(i) for i in range(1, 10)]  # Column numbers 1-9

    for row in rows:
        table[row] = []
        for _ in cols:
            table[row].append(generate_random_value())

    return table


def print_auth_table(table):
    """Prints the authentication table in a formatted way."""
    cols = [str(i) for i in range(1, 10)]
    print(f"{'':<5}", end="")  # For the top left corner
    for col in cols:
        print(f"{col:<5}", end="")
    print()

    for row in table:
        print(f"{row:<5}", end="")  # Row labels (A-I)
        for value in table[row]:
            print(f"{value:<5}", end="")
        print()


# Generate and print the authentication table
auth_table = create_auth_table()
print_auth_table(auth_table)


print("\nWARNING: Regenerate tables to prevent leakage of confirmation data\n")