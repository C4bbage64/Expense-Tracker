import csv
import os

FILE_NAME = "expenses.csv"

# Function to load expenses from a CSV file
def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        return list(reader)

# Function to save expenses to a CSV file
def save_expenses(expenses):
    with open(FILE_NAME, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["ID", "Date", "Description", "Amount", "Category"])
        writer.writeheader()
        writer.writerows(expenses)

# Utility function to get the next available ID
def get_next_id():
    expenses = load_expenses()
    if not expenses:
        return 1
    return int(expenses[-1]["ID"]) + 1
