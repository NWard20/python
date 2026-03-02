"""
-----------------------------------------------------------------------
ASSIGNMENT 7B: THE MAGIC 8 BALL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. RESPONSES is a tuple containing at least 8 string options.
[ ] 3. Program uses a 'while True' loop to keep the game running.
[ ] 4. random.choice() selects the answer from the tuple.
[ ] 5. Logic checks if "quit" is in the user input to break the loop.
-----------------------------------------------------------------------
"""
""""
ASSIGNMENT: Assignment 7B: Logic tools (Lists and strings)
DATE: [3/2/2026]
FILE: magic_8ball.py
"""
import random

# TODO: Create a tuple of at least 8 responses
RESPONSES = ("Yes", "No", "Maybe", "Ask again later")

print("Welcome to the Digital Oracle!")

# TODO: Create a while loop that keeps asking questions
# TODO: Use random.choice(RESPONSES) to answer
# TODO: If user types "quit", break the loop

# Tuple with 8 responses
RESPONSES = ("Yes", "No", "Ask again later", "Dont count on it", "As i see it, yes", "Concentrate and ask again", "It is certain", "My sources say no" )
print("Ask any question you would like:") # Prints question prompt and quit prompt
print("Type quit to leave") 

while True:
    question = input("Your Question: ") # 

    if "quit" in question.lower(): # If typed quit, system stops
        print("Goodbye")
        break

    answer = random.choice(RESPONSES) # Using random.choice() to randomize RESPONSES
    print("Magic 8 ball says:", answer) # What the magic 8 ball says
    print()