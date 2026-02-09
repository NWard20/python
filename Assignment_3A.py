"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Ask user for Monthly Income (float).
[ ] 3. Ask user for 5 DIFFERENT expense amounts (float).
[ ] 4. Calculate Total Expenses and Remaining Balance.
[ ] 5. Calculate Percentage of Income Spent.
[ ] 6. Output formatted to 2 decimal places (:,.2f or :.2%).
-----------------------------------------------------------------------
"""

# --- Monthly Income ---
income = float(input("Enter your monthly income: "))

# --- 5 Different Expenses ---
expense_1 = float(input("Enter expense 1: "))
expense_2 = float(input("Enter expense 2: "))
expense_3 = float(input("Enter expense 3: "))
expense_4 = float(input("Enter expense 4: "))
expense_5 = float(input("Enter expense 5: "))

# --- Calculations ---
total_expenses = expense_1 + expense_2 + expense_3 + expense_4 + expense_5
remaining_balance = income - total_expenses
percent_spent = total_expenses / income

# --- Formatted Output ---
print(f"Total Expenses: ${total_expenses:,.2f}")
print(f"Remaining Balance: ${remaining_balance:,.2f}")
print(f"Percentage of Income Spent: {percent_spent:.2%}")
