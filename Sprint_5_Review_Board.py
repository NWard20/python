"""
ASSIGNMENT 12B: SPRINT 5 - Sprint 5 Review Board
Project: Instant IPhones 
Developer: Nick Ward
"""

import datetime

# GLOBAL CONSTANTS (Product Rules)
PRODUCT_FILE = "products.txt"
DATA_FILE = "order_history.txt"       
HUMAN_REPORT = "latest_receipt.txt"    
COLOR_OPTIONS = ("Black", "Silver", "Blue", "Gold", "Purple")


def get_customer_info():
    """Asks for name and shipping address."""
    name = input("Customer Name: ").title()
    address = input("Shipping Address: ")
    return name, address


def take_order():
    """Collects choices."""
    model = input("iPhone Model (Standard/Plus/Pro/Pro Max): ")
    storage = input("Storage (128GB/256GB/512GB/1TB): ")
    print(f"Available Colors: {COLOR_OPTIONS}")
    color = input("Choice of color: ")
    applecare = input("AppleCare+ (Yes/No): ")
    charger = input("Fast Charger (Yes/No): ")
    return {"model": model, "storage": storage, "color": color, "applecare": applecare, "charger": charger}


def calculate_total(order_data):
    """Calculates price based on model, storage, and add-ons."""
    base_price = 999  

    if order_data["model"] == "Standard":
        base_price = 799
    elif order_data["model"] == "Plus":
        base_price = 899
    elif order_data["model"] == "Pro":
        base_price = 999
    elif order_data["model"] == "Pro Max":
        base_price = 1199

    storage_cost = 0
    if order_data["storage"] == "256GB":
        storage_cost = 100
    elif order_data["storage"] == "512GB":
        storage_cost = 300
    elif order_data["storage"] == "1TB":
        storage_cost = 500

    total = base_price + storage_cost

    if order_data["applecare"] == "Yes":
        total += 199
    if order_data["charger"] == "Yes":
        total += 29

    return total


def save_data_and_label(customer, address, total, order_data):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # SAVE SIMPLE DATA
    with open(DATA_FILE, "a") as file:
        file.write(f"{customer},{address},{total:.2f}\n")

    # OVERWRITE PREVIOS RECIPT
    with open(HUMAN_REPORT, "w") as file:
        file.write(f"Receipt - {time}\n")
        file.write(f"{customer} | {address}\n")

        for key, value in order_data.items():
            file.write(f"{key}: {value}\n")

        file.write(f"Total: ${total:.2f}\n")
        file.write("------------------\n")

    print("Receipt saved.")



def review_orders():
    print("\nPast Orders:")

    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                print(line.strip())
    except:
        print("No orders yet.")

def main():
    # Ask if user wants to review orders first
    choice = input("Type 'review' to see past orders or press Enter to continue: ")

    if choice.lower() == "review":
        review_orders()

    # 1. Identity Phase
    name, address = get_customer_info()

    # 2. Data Collection Phase
    current_order = take_order()

    # 3. Calculation Phase
    final_price = calculate_total(current_order)

    # 4. Save + Print
    save_data_and_label(customer=name, address=address, total=final_price, order_data=current_order)


main()