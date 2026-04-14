"""
-----------------------------------------------------------------------
ASSIGNMENT 12A: THE CONFIGURABLE MENU & AUDITOR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. PHASE 1: External menu_config.txt file created in workspace.
[ ] 3. Program reads and parses the .txt file into a Dictionary.
[ ] 4. PHASE 2: break the dictionary into individual variables.
[ ] 6. Print each category and its details
[ ] 7. try/except used to prevent crashes on FileNotFoundError.
-----------------------------------------------------------------------
"""
"""Assignment Name: Lesson 12A: Working with Files
Date: 4/14/2026
File Name: Assignment_12A.txt
"""

MENU_FILE = "menu_config.txt"


def load_menu():
    menu = {}

    try:
        file = open(MENU_FILE, "r")

        for line in file:
            line = line.strip()
            if line != "":
                parts = line.split(":")
                category = parts[0]
                items = parts[1].split(",")
                for i in range(len(items)):
                    items[i] = items[i].strip()
                menu[category] = items
        file.close()

    except FileNotFoundError:
        print("no menu file")
        return {}

    return menu


def main():
    menu = load_menu()

    if menu == {}:
        print("nothing is here")
        return

    drinks = menu.get("Drinks", [])
    entrees = menu.get("Entrees", [])
    sides = menu.get("Sides", [])
    desserts = menu.get("Desserts", [])

    print("\n--- MENU ---")

    print("Drinks:")
    for d in drinks:
        print(d)

    print("\nEntrees:")
    for e in entrees:
        print(e)

    print("\nSides:")
    for s in sides:
        print(s)

    print("\nDesserts:")
    for d in desserts:
        print(d)


main()