import re
from datetime import datetime

# You can add utility functions here, like validation, date formatting, etc.
def validate_date(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        raise ValueError("Invalid email address")

# Example: Validate that the amount is positive
def validate_amount(amount):
    if amount <= 0:
        raise ValueError("Amount must be greater than zero")
