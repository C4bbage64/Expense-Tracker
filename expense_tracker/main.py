import argparse
from expense_tracker.expense_manager import add_expense, update_expense, delete_expense, list_expenses, summary_expenses

def main():
    parser = argparse.ArgumentParser(description="CLI Expense Tracker")

    # Define subcommands
    subparsers = parser.add_subparsers(dest="command")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--description", required=True, help="Description of the expense")
    add_parser.add_argument("--amount", type=float, required=True, help="Amount of the expense")
    add_parser.add_argument("--category", help="Category of the expense")

    # Update command
    update_parser = subparsers.add_parser("update", help="Update an existing expense")
    update_parser.add_argument("id", required=True, type=int, help="ID of the expense to update")
    update_parser.add_argument("--description", help="Updated description")
    update_parser.add_argument("--amount", type=float, help="Updated amount")
    update_parser.add_argument("--category", help="Updated category")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete an existing expense")
    delete_parser.add_argument("--id", required=True, type=int, help="ID of the expense to delete")

    # Summary 
    summary_parser = subparsers.add_parser("summary", help="Show a summary of expenses")
    summary_parser.add_argument("--month", type=int, help="Show summary for a specific month (format: YYYY-MM)")

    # Parse arguments
    args = parser.parse_args()

    # Handle commands
    if args.command == "add":
        add_expense(args.description, args.amount, args.category)
    elif args.command == "update":
        update_expense(args.id, args.description, args.amount, args.category)
    elif args.command == "delete":
        delete_expense(args.id)
    elif args.command = "list":
        list_expenses()
    elif args.command == "summary":
        summary_expenses(args.month)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()