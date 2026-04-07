"""
ASSIGNMENT 11B: SPRINT 4 - Sprint 4 Review Board
Project: Instant IPhones
Developer: Nick Ward
"""
import datetime

# GLOBAL CONSTANTS (Product Rules)
PRODUCT_FILE = "products.txt"
COLOR_OPTIONS = ("Black", "Silver", "Blue", "Gold", "Purple")


def get_customer_info():
    """Asks for name and shipping address."""
    name = input("Customer Name: ").title()
    address = input("Shipping Address: ")
    return name, address

def take_order():
    """Collects choices. Notice the tuple usage for color options."""
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

def write_receipt(customer_name, order_data, total):
    """Stores the order with timestamp in the receipts file, including total."""
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("store_receipts.txt", "a") as file:
        file.write(f"\n[{current_time}] ORDER RECORD\n")
        file.write(f"Customer: {customer_name}\n")

        for key, value in order_data.items():
            file.write(f"{key.capitalize()}: {value}\n")

        file.write(f"Total: ${total:.2f}\n")
        file.write("-----------------------------\n")

    print("Printing Your Reciept")

def save_data_and_label(customer, address, total, order_data):
    """Prints order summary and logs it to the receipt file."""
    print(f"\nORDER SUMMARY")
    print(f"SHIP TO: {address} | Customer: {customer}")
    print(f"TOTAL: ${total:.2f}")

    # Log the order with total included
    write_receipt(customer_name=customer, order_data=order_data, total=total)

def main():
    # 1. Identity Phase
    name, address = get_customer_info()

    # 2. Data Collection Phase
    current_order = take_order()

    # 3. Calculation Phase
    final_price = calculate_total(current_order)

    # 4. Handoff Phase (Using KEYWORD ARGUMENTS)
    save_data_and_label(customer=name, address=address, total=final_price, order_data=current_order)

main()