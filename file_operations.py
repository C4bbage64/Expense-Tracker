# file_operations.py
import csv

FILE_NAME = "expenses.csv"

def init_file():
    try:
        with open(FILE_NAME, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])
    except FileExistsError:
        pass  # File already exists

def read_expenses():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip the header
        return list(reader)

def write_expenses(expenses):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Description", "Amount"])
        writer.writerows(expenses)
