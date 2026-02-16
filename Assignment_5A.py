"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. All 4 inputs have 'while' loop validation.
[ ] 3. The Chaperone loop uses .upper() and correct Boolean logic.
[ ] 4. I have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
"""
"""Assignment Name: Assignment 5A: Input Validation & Error Checking
Date: 2/16/2026
File Name: Assignment_5A.txt
"""

# ---First and Last Name (Cannot be blank)---
while True:
    full_name = input("What is your First and Last name? ")
    if full_name != "":
        break
    else:
        print("❌ Error: Name cannot be blank.")

print(f"\n✅ Registration Complete for {full_name}!")

# ---Determine if someone is a chaperone (Y/N)---
while True:
    chaperone = input("Parent Volunteering to be a chaperone? (Y/N): ").upper()
    if chaperone == "Y" or chaperone == "N":
        break
    else:
        print("Please enter Y or N")

print(f"\n✅ You said {chaperone} to become a chaperone!")

# ---Entering phone number (Cannot be blank)---
while True:
    phone_number = input("Please enter your phone number: ")
    if phone_number != "":
        break
    else:
        print("Please enter a full phone number: ")

print(f"\n✅ Registration Complete for {phone_number}!")

# ---Ticket Count (Must be integer > 0 and crash-proof)---
tickets = 0
while True:
    try:
        tickets = int(input("How many tickets? "))
        if tickets > 0:
            break # Valid number! Escape the loop!
        print("❌ Error: Must be at least 1 ticket.")
    except ValueError:
        print("❌ Error: Please enter a NUMBER (e.g., 5, not 'five').")

print(f"✅ Ordered {tickets} tickets.")