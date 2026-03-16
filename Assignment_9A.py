"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global Constants BASES and FRUITS defined as Tuples.
[ ] 3. Professional function get_price(size) returns a float.
[ ] 4. Professional function blend(size, base, fruit, scoops) for output.
[ ] 5. main() function handles try/except for scoops (int).
[ ] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""
"""Assignment Name: Assignment 9A: Introducing Functions
Date: 3/16/2026
File Name: Assignment_9A.py
"""

# GLOBAL CONSTANTS (The Pantry)
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")
PROTEIN = ("Chocolate", "Vanilla", "Whey")

# TODO: Define get_price(size)

# TODO: Define blend(size, base, fruit, scoops)

# TODO: Define main() to collect input and call your logic


def get_price(size):  # Price of specific size
    if size == "Small":
        price = 5.00
    elif size == "Medium":
        price = 8.00
    elif size == "Large":
        price = 10.00
    else:
        price = 5.00
    return price


def blend(size, base, fruit, protein, scoops):  # Smoothie Preparation
    print("\n--- Smoothie Order ---")
    print("Size:", size)
    print("Base:", base)
    print("Fruit:", fruit)
    print("Protein:", protein)
    print("Protein Scoops:", scoops)


def main():
    print("Welcome in, What type of smoothie can I get you?\n") #Final visual display

    size = input("Choose a size (Small, Medium, Large): ").title().strip()

    print("\nAvailable Bases:", BASES)
    base = input("Pick a base: ")

    print("\nAvailable Fruits:", FRUITS)
    fruit = input("Pick a fruit: ")

    print("\nAvailable Proteins:", PROTEIN)
    protein = input("Pick a protein: ")

    try:
        scoops = int(input("How many protein scoops? "))
    except ValueError:
        print("Invalid input. Scoops set to 0.")
        scoops = 0

    total = get_price(size) # Adding pricing for extra scoops of protein
    total += scoops * 1.50

    blend(size, base, fruit, protein, scoops)

    print(f"\nTotal Price: ${total:.2f}") # Total pricing


main()