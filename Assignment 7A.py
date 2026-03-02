""""
ASSIGNMENT: Assignment 7A: String Mastery
DATE: [3/2/2026]
FILE: Assignment 7A.py
"""
""" Task 1: Basics (Length, Indexing, ASCII).
Task 2: Cleanup (Strip, Casing, Replace).
Task 3: Validation (isdigit check).
Task 4: The Ducky Loop (Using .join() and direct iteration).
Checklist Docstring present at the top.
"""
# Task 1
animal = "zebra"
print(animal[0]) # Output: Z Indexing
length = len(animal) # Length of string
print(length)

print(ord(animal[2])) # Used ord function to get the ASCII value of b in Zebra

# Task 2
text = "  the dog  "
print(text.strip()) #Strips out the white space
print(text.strip().upper()) # Strips out white space and capatializes all letters
print(text.strip().replace("dog", "cat")) # Strips out white space and replaces dog with cat

# Task 3
print ("223".isdigit()) # Checks to see if strings are all numbers, Output True
print ("556W".isdigit()) # Checks to see if strings are all numbers, Output False

# Task 4
word = input("\nEnter a word: ")

letters = []

for letter in word:   # direct iteration
    letters.append(letter.upper())

joined = "-".join(letters)   # using .join()

print("Ducky Loop Result:", joined)