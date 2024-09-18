# main.py
import expense_operations
import file_operations

def main():
    file_operations.init_file()
    
    while True:
        print("\nExpense Tracker")
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. Update an expense")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            description = input("Enter description: ")
            amount = input("Enter amount: ")
            expense_operations.add_expense(date, category, description, amount)
        elif choice == '2':
            expense_operations.view_expenses()
        elif choice == '3':
            expense_operations.update_expense()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
