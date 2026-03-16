"""
ASSIGNMENT 9B: SPRINT 2 - FUNCTIONAL STUBS
Project: Instant IPhones
Developer: Nick Ward
"""

# GLOBAL CONSTANTS (Product File)
PRODUCT_FILE = "products.txt"


def get_customer_info():
    """Asks for customer name and shipping address."""
    # TODO: Ask user for name and shipping address
    return "Nick Ward", "2112 Verizon Lane"


def take_order():
    """Collects model, storage, color, and add-ons. Returns order data."""
    # TODO: Capture model (Standard/Plus/Pro/Pro Max)
    # TODO: Capture storage (128GB/256GB/512GB/1TB)
    # TODO: Capture color choice
    # TODO: Capture add-ons (AppleCare+, Fast Charger, Case)

    order = {
        "model": "Pro",
        "storage": "256GB",
        "color": "Blue",
        "applecare": "Yes",
        "charger": "Yes",
        "case": "No"
    }

    return order


def calculate_total(order_data):
    """Calculates total price based on selections."""
    # TODO: Load base prices and add-on prices from products.txt
    return 1328


def save_data_and_label(customer, address, order_data, total):
    """Saves order to file and prints a customer receipt."""

    # TODO: Append computer-readable data to order_history.txt


def main():

    # 1. Identity Phase
    name, address = get_customer_info()
    print(f"Customer: {name} | Ship To: {address}")

    # 2. Data Collection Phase
    current_order = take_order()

    # 3. Calculation Phase
    final_price = calculate_total(current_order)

    # 4. Handoff Phase
    save_data_and_label(name, address, current_order, final_price)


main()