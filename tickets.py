"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[ ] 1. Create a list of 20 seats (numbered 1-20).
[ ] 2. Display the list of available seats.
[ ] 3. Ask user for a seat number (0 to quit).
[ ] 4. Remove the selected seat from the list.
[ ] 5. Handle invalid inputs (seat taken or doesn't exist).
[ ] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
"""
"""Assignment Name: Assignment 6A: Lists & Indexing
Date: 2/16/2026
File Name: tickets.py
"""

#---List of seats (1-21)---
seats = list(range(1, 21))

#---List of avalible seats---
sold_seats = []

#---Ask for seat number---
while len(seats) > 0:   

    print("\nWhich seat would you like?:", seats)
    print("Seats left:", len(seats))

    user_input = input("Pick a seat (0 to quit): ")

#---Remove selected seat---
    if not user_input.isdigit():
        print("That’s not a number.")
        continue

    choice = int(user_input)

    if choice == 0:
        print("Stopping ticket sales.")
        break
#---Handles invalid inputs---
    if choice in seats:
        seats.remove(choice)
        sold_seats.append(choice)
        print("Seat", choice, "is now sold.")
    else:
        print("That seat is already taken.")

#---Last seat sold/ no more seats---
if len(sold_seats) > 0:
    print("\nLast seat sold was:", sold_seats.pop())

if len(seats) == 0:
    print("Sorry, all seats are already taken.")