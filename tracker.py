import csv
import os

# Path to store expenses
FILE_NAME = "expenses.csv"

# Function to initialize the csv file if it doesn't exist
def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writenow(["Date", "Category", "Description", "Amount"])

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

# Main application loop
def main():
    init_file()  # Ensure the file is initialized
    while True:
        print("\nExpense Tracker")
        print("1. Add an expense")
        print("2. view all expenses")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            date = input("Enter the date (DD-MM-YYYY): ")
            category = input("Choose an option: ")
            description = input("Enter the description: ")
            amount = input("Enter the amount: ")
            add_expense(date, category, description, amount)
            print("Expense added.")
        elif choice == '2':
            print("Expense added.")
            view_expenses()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
