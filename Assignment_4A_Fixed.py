"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with your name.
[ ] 2. Ask user for two integers (num1 and num2).
[ ] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[ ] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""
"""Assignment Name: Assignment 4A: Boolean Logic (And/Or/Not)
Date: 2/9/2026
File Name: Assignment_4A.txt
"""
# ---Asking for integer---
print("Enter First integer")
num1 = int(input())
print("Enter Second integer")
num2 = int(input())

#---Checks Both numbers are greater or less than 0---
if num1 > 0 and num2 > 0:
    print(f"{num1} and {num2} are both greater than 0")
else:
    print(f"{num1} and {num2} are both not greater than 0")

#---Checks Both numbers are greater or less than 100---
if num1 > 100 and num2 > 100:
    print(f"{num1} and {num2} are both greater than 100")
else:
    print(f"{num1} and {num2} are both not greater than 100")

#---Checks Greater or less than 100---
if num1 > 100 or num2 > 100:
    print(f"{num1} is greater than 100")
else:
    print(f"{num1} is less than 100")

#---Checks Odd or Even---
if num1 % 2 == 0 or num2 % 2 == 0:
    print("The number is even!")
else:
    print("The number is odd!")

#---Checks Equal---
if num1 == num2:
    print(f"{num1} and {num2} are equal")
else:
    print(f"{num1} and {num2} are not equal")

#---Checks to see if num1 and num2 is equal to 0---
if num1 != 0 and num2 != 0:
    print(f"{num1} is equal to 0")
else:
    print(f"{num1} is not equal to 0")

#---Categhorize num1---
if num1 > 0:
    print("num1 is Positive")
elif num1 < 0:
    print("num1 is Negative")
else:
    print("num1 is Zero")