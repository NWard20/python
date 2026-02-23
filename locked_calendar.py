"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE LOCKED CALENDAR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. MONTHS is defined as a constant tuple ().
[ ] 3. Program uses a for loop to display each month.
[ ] 4. 'try' and 'except' blocks catch a TypeError.
[ ] 5. Comments explain why the modification failed.
-----------------------------------------------------------------------
"""
"""Assignment Name: Assignment 6B: Data Integrity & Resilience
Date: 2/23/2026
File Name: locked_calendar.txt
"""

#---Constant tuple of MONTHS---
MONTHS = ("January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" )

#---Print all the months---
print("Months:")
for month in MONTHS:
    print(month)

print("\nAttempting illegal modification...")

#---Trying to change January to Smarch---
try:
    MONTHS[0] = "Smarch"   

#The code failed because once a tuple is created, its value cannot be changed. No matter what!
except TypeError:
    print("YOU CANT CHANGE THAT MONTH!")