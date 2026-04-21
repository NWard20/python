"""
-----------------------------------------------------------------------
ASSIGNMENT 14A: Object practice
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Define a class for a part of your project using PascalCase.
[ ] 3. Use __init__ to set private attributes (__variable).
[ ] 4. Write Setters and Getters for the attributes.
[ ] 5. Write a summary function that returns a formatted description.
[ ] 6. Instantiate two distinct objects and print their summaries.
-----------------------------------------------------------------------
"""
"""Assignment Name: Lesson 12A: Working with Files
Date: 4/14/2026
File Name: Assignment_12A.txt
"""
class Pizza:
    def __init__(self, size, dough, topping, price):
        # basic pizza details
        self.__size = size
        self.__dough = dough
        self.__topping = topping
        self.__price = price

    # getters
    def get_size(self):
        return self.__size

    def get_price(self):
        return self.__price

    # setter
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price

    # summary
    def summary(self):
        return f"{self.__size} {self.__dough} pizza with {self.__topping} - ${self.__price}"

# create pizzas
pizza1 = Pizza("Large", "Thin Crust", "Pepperoni", 12)
pizza2 = Pizza("Medium", "DeepDish", "Cheese", 16)

# update one price
pizza2.set_price(14)

# print summaries
print(pizza1.summary())
print(pizza2.summary())