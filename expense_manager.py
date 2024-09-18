from file_manager import load_expenses, save_expenses, get_next_id
from datetime import datetime

# Function to add an expense
def add_expense(description, amount, category=None):
    date = datetime.now().strftime("%Y-%m-%d")
    next_id = get_next_id()

    expenses = load_expenses()

    expenses.append({
        "ID": next_id,
        "Date": date,
        "Description": description,
        "Amount": amount,
        "Category": category or "Uncategorized"
    })

    save_expenses(expenses)
    print(f"Expense added successfully (ID: {next_id})")

# Function to update an expense
def update_expense(expense_id, description=None, amount=None, category=None):
    expenses = load_expenses()
    found = False
    for expense in expenses:
        if expense["ID"] == str(expense_id):
            found = True
            if description:
                expense["Description"] = description
            if amount:
                expense["Amount"] = str(amount)
            if category:
                expense["Category"] = category
            break
    if found:
        save_expenses(expenses)
        print(f"Expense with ID {expense_id} updated successfully")
    else:
        print(f"Expense with ID {expense_id} not found")

# Function to delete an expense
def delete_expense(expense_id):
    expenses = load_expenses()
    filtered_expenses = [e for e in expenses if e["ID"] != str(expense_id)]
    if len(filtered_expenses) != len(expenses):
        save_expenses(filtered_expenses)
        print(f"Expense with ID {expense_id} deleted successfully")
    else:
        print(f"Expense with ID {expense_id} not found")

# Function to list all expenses
def list_expenses():
    expenses = load_expenses()
    print("ID  Date       Description  Amount  Category")
    for expense in expenses:
        print(f"{expense['ID']}  {expense['Date']}  {expense['Description']}  {expense['Amount']}  {expense['Category']}")

# Function to show a summary of expenses
def summary_expenses(month=None):
    expenses = load_expenses()
    total = 0
    filtered_expenses = expenses
    if month:
        filtered_expenses = [e for e in expenses if datetime.strptime(e["Date"], "%Y-%m-%d").month == month]
    
    for expense in filtered_expenses:
        total += float(expense["Amount"])

    if month:
        print(f"Total expenses for month {month}: ${total}")
    else:
        print(f"Total expenses: ${total}")
