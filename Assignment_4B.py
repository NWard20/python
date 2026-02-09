"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[ ] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[ ] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""
"""Assignment Name: Assignment 4B: Loops (While, For, Recursion)
Date: 2/9/2026
File Name: Assignment_4B.txt
"""
#---Repeats Are we there yet? until user types yes---
are_we_there = False

while not are_we_there:
    answer = input("Are we there yet? (yes/no): ")
    if answer == "yes":
        are_we_there = True

#---Range(start, stop, step)---
for bottles in range(99, 0, -1):
    print(f"{bottles} bottles of beer on the wall!")
