import csv
import os

# Path to store expenses
FILE_NAME = "expenses.csv"

# Function to initialize the csv file if it doesn't exist
def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])

# Function to add an expense
def add_expense(date, category, description, amount):
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

# Function to view all expenses
def view_expenses():
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Function to update an expense
def update_expense(expense_index, new_date, new_category, new_description, new_amount):
    expenses = []

    # Read all the current expenses
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        expenses = list(reader)

    # Check if the index is valid
    if 0 < expense_index < len(expenses):
        # Update the selected expense
        expenses[expense_index] = [new_date, new_category, new_description, new_amount]
        
        # Write the updated list of expenses back to the file
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(expenses)
        return True
    else:
        return False