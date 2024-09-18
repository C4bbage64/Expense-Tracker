# expense_operations.py
import file_operations

def add_expense(date, category, description, amount):
    expenses = file_operations.read_expenses()
    expenses.append([date, category, description, amount])
    file_operations.write_expenses(expenses)

def view_expenses():
    expenses = file_operations.read_expenses()
    for idx, expense in enumerate(expenses):
        print(f"{idx}: Date: {expense[0]}, Category: {expense[1]}, Description: {expense[2]}, Amount: {expense[3]}")
    return expenses

def update_expense():
    expenses = view_expenses()
    expense_idx = int(input("Enter the index of the expense to update: "))
    if expense_idx < 0 or expense_idx >= len(expenses):
        print("Invalid index!")
        return

    # Get current expense details
    current_expense = expenses[expense_idx]
    print(f"Current: {current_expense}")

    # Get new details
    new_date = input(f"Enter new date (or press Enter to keep {current_expense[0]}): ") or current_expense[0]
    new_category = input(f"Enter new category (or press Enter to keep {current_expense[1]}): ") or current_expense[1]
    new_description = input(f"Enter new description (or press Enter to keep {current_expense[2]}): ") or current_expense[2]
    new_amount = input(f"Enter new amount (or press Enter to keep {current_expense[3]}): ") or current_expense[3]

    # Update the expense and save it
    expenses[expense_idx] = [new_date, new_category, new_description, new_amount]
    file_operations.write_expenses(expenses)
    print(f"Expense {expense_idx} updated!")
