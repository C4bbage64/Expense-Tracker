# utils.py
def validate_amount(amount_str):
    try:
        return float(amount_str)
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return None
