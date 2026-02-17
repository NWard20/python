"""Assignment Name: Assignment 5B: The ATM (Boss Level)
Date: 2/916/2026
File Name: Assignment_5B.txt
"""

# ---Starting Balance---
account_balance = 5000.00

# ---While Loop---4
while True:
    print("1.) Check Balance")
    print("2.) Deposit")
    print("3.) Withdraw")
    print("4.) Transfer")
    print("5.) Exit")

    menu_choice = input("Enter option (1-5): ")

#---Case 1, Formatted Balance---

    match menu_choice:

        case "1":
            print(f"Current Balance: ${account_balance:.2f}")

#---Case 2, Deposit and Add to Balance---

        case "2":
            user_amount = input("Enter deposit amount: ")

            if user_amount.isdigit():
                user_amount = float(user_amount)

                if user_amount > 0:
                    account_balance += user_amount
                    print(f"Deposited: ${user_amount:.2f}")

                    print(f"New Balance: ${account_balance:.2f}")
                else:
                    print("Deposit must be greater than 0.")
            else:
                print("Invalid amount. Please enter numbers only.")

#---Case 3, Withdraw and Subtract Balance---

        case "3":
            user_amount = input("Enter withdrawal amount: ")

            if user_amount.isdigit():
                user_amount = float(user_amount)

                if user_amount <= 0:
                    print("Withdrawal must be greater than 0.")
                elif user_amount > account_balance:
                    print("Insufficient funds. No overdrafts allowed.")
                else:
                    account_balance -= user_amount
                    print(f"Withdrew: ${user_amount:.2f}")

                    print(f"New Balance: ${account_balance:.2f}")
            else:
                print("Invalid amount. Please enter numbers only.")

#---Case 4, Transfer and Subtract from Balance---

        case "4":
            user_amount = input("Enter transfer amount: ")

            if user_amount.isdigit():
                user_amount = float(user_amount)

                if user_amount <= 0:
                    print("Transfer must be greater than 0.")
                elif user_amount > account_balance:
                    print("Insufficient funds. Transfer canceled.")
                else:
                    account_balance -= user_amount
                    print(f"Transferred: ${user_amount:.2f}")
                    print(f"New Balance: ${account_balance:.2f}")
            else:
                print("Invalid amount. Please enter numbers only.")

#---Case 5, Print "Goodbye"---

        case "5":
            print("Goodbye")
            break

#---Case _, Print, Invalid Selection---

        case _:
            print("Invalid selection.")