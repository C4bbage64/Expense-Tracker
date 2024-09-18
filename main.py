import argparse
from expense_manager import add_expense, update_expense, delete_expense, list_expenses, summary_expenses
import sys

def main():
    parser = argparse.ArgumentParser(description="Simple CLI Expense Tracker")

    # Commands
    subparsers = parser.add_subparsers(dest="command", help="commands")

    # Add expense
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--description", required=True, help="Description of the expense")
    add_parser.add_argument("--amount", required=True, type=float, help="Amount of the expense")
    add_parser.add_argument("--category", required=False, help="Category of the expense")

    # Update expense
    update_parser = subparsers.add_parser("update", help="Update an existing expense")
    update_parser.add_argument("--id", required=True, type=int, help="ID of the expense to update")
    update_parser.add_argument("--description", help="Updated description of the expense")
    update_parser.add_argument("--amount", type=float, help="Updated amount of the expense")
    update_parser.add_argument("--category", help="Updated category of the expense")

    # Delete expense
    delete_parser = subparsers.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument("--id", required=True, type=int, help="ID of the expense to delete")

    # List all expenses
    list_parser = subparsers.add_parser("list", help="List all expenses")

    # Summary of expenses
    summary_parser = subparsers.add_parser("summary", help="Show a summary of expenses")
    summary_parser.add_argument("--month", required=False, type=int, help="Month to filter by")

    # Parse arguments
    args = parser.parse_args()

    # Handle commands
    if args.command == "add":
        add_expense(args.description, args.amount, args.category)
    elif args.command == "update":
        update_expense(args.id, args.description, args.amount, args.category)
    elif args.command == "delete":
        delete_expense(args.id)
    elif args.command == "list":
        list_expenses()
    elif args.command == "summary":
        summary_expenses(args.month)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
