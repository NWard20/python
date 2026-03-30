"""
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[ ] 3. Function 'make_pizza' defines 4 specific parameters.
[ ] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[ ] 5. main() displays the Global Pantry list to the user.
[ ] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
"""
"""Assignment Name:  Assignment 10A: The Smart Blueprint
Date: 3/30/2026
File Name: pizza_engine.py
"""
# The Global Pantry
TOPPINGS = ("Pepperoni", "Sausage", "Cheese", "Peppers","Onions")


# The Architect Function
def make_pizza(customer, size, topping, is_delivery=False):
    print(f"Customer Name: {customer}")
    print(f"Pizza Size: {size}")
    print(f"Topping: {topping}")
    
    if is_delivery:
        print("Delivery: Yes ")
    else:
        print("Delivery: No ")
    


# The Interaction
def main():
    print("Welcome to Nicks Pizza!\n")
    
    # Display Global Pantry
    print("Toppings:")
    for item in TOPPINGS:
        print(f"- {item}")
    
    # User input
    customer_name = input("\nEnter your name: ")
    size = input("Enter pizza size (Small/Medium/Large): ")
    topping = input("Choose a topping: ")
    delivery_choice = input("Delivery? (yes/no): ").lower()
    
    # The Saftey Net
    is_delivery = True if delivery_choice == "yes" else False
    
    # The Professional Call
    make_pizza(
        customer=customer_name,
        size=size,
        topping=topping,
        is_delivery=is_delivery
    )


# Run program
if __name__ == "__main__":
    main()