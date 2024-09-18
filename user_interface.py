import csv_operations

# Function to display the main menu and handle user input
def main_menu():
    while True:
        print("\nExpense Tracker")
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. Update an expense")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            handle_add_expense()
        elif choice == '2':
            print("All expenses:")
            csv_operations.view_expenses()
        elif choice == '3':
            handle_update_expense()
        elif choice == '4':
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

# Function to handle updating an expense
def handle_update_expense():
    print("Current Expenses:")
    csv_operations.view_expenses()

    # Ask user for the index of the expense they want to update
    try:
        expense_index = int(input("Enter the index of the expense to update (1 for the first expense): ")) - 1
        new_date = input("Enter the new date (DD-MM-YYYY): ")
        new_category = input("Enter the new category: ")
        new_description = input("Enter the new description: ")
        new_amount = input("Enter the new amount: ")

        # Attempt to update the expense
        if csv_operations.update_expense(expense_index, new_date, new_category, new_description, new_amount):
            print("Expense updated successfully.")
        else:
            print("Invalid index. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")