import csv
from datetime import datetime
from expense_tracker.file_manager import load_expenses, save_expenses, get_next_id

def add_expense(description, amount, category=None):
    expenses = load_expenses()
    new_id = get_next_id(expenses)
    date = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "ID": new_id,
        "Date": date,
        "Description": description,
        "Amount": amount,
        "Category": category or "Uncategorized"
    }

    expenses.append(expense)
    save_expenses(expenses)
    print(f"Expense added: {description} (RM {amount})")

def update_expense(expense_id, description=None, amount=None, category=None):
    expenses = load_expenses()
    for expense in expenses:
        if expense["ID"] == expense_id:
            if description:
                expense["Description"] = description
            if amount:
                expense["Amount"] = amount
            if category:
                expense["Category"] = category
            save_expenses(expenses)
            print(f"Expense updated: ID {expense_id}")
            return
    print(f"Expense ID {expense_id} not found")

    def delete_expense(expense_id):
        expenses = load_expenses()
        filtered_expenses = [exp for exp in expenses if int(exp["ID"]) != expense_id]
        save_expenses(filtered_expenses)
        print(f"Deleted expense ID {expense_id}")

    def list_expenses():
        expenses = load_expenses()
        print("ID Date Description Amount Category")
        for expenses in expenses:
            print(f"{expenses['ID']} {expenses['Date']} {expenses['Description']} {expenses['Amount']} {expenses['Category']}")

    def summary_expenses(month=None):
        expenses = load_expenses()
        total = 0
        filtered_expenses = expenses

        if month:
            filtered_expenses = [exp for exp in expenses if datetime.strptime(exp["Date"], "%Y-%m-%d").month == month]

        for expense in filtered_expenses:
            total += float(expense["Amount"])

        if month:
            print(f"Total for month {month}: ${total}")
        else:
            print(f"Total expenses: ${total}")
            