import csv_operations

# Function to display the main menu and handle user input
def main_menu():
    while True:
        print("\nExpense Tracker")
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            handle_add_expense()
        elif choice == '2':
            print("All expenses:")
            csv_operations.view_expenses()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Function to handle adding an expense
def handle_add_expense():
    date = input("Enter the date (DD-MM-YYYY): ")
    category = input("Enter the category: ")
    description = input("Enter the description: ")
    amount = input("Enter the amount: ")

    csv_operations.add_expense(date, category, description, amount)
    print("Expense added.")
