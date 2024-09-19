import csv
import os

CSV_FILE = "expenses.csv"

def load_expenses():
    if not os.path.exists(CSV_FILE):
        return []

    with open(CSV_FILE, "r") as file:
        reader = csv.DictReader(file)
        return list(reader)
    
def save_expenses(expenses):
    with open(CSV_FILE, "w", newline="") as file:
        fieldnames = ["ID", "Date", "Description", "Amount", "Category"]
        writer = csv.DictWriter(file, fieldnames=expenses[0].keys())
        writer.writeheader()
        writer.writerows(expenses)

def get_next_id(expenses):
    if not expenses:
        return 1
    return max(int(exp["ID"]) for exp in expenses) + 1