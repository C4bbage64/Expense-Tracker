class ExpenseTrackerError(Exception):
    """Base class for all expense tracker exceptions."""
    pass

class InvalidAmountError(ExpenseTrackerError):
    """Raised when an invalid (negative or zero) amount is provided."""
    def __init__(self, amount):
        super().__init__(f"Invalid amount: {amount}. Amount must be greater than zero.")

class ExpenseNotFoundError(ExpenseTrackerError):
    """Raised when the requested expense ID does not exist."""
    def __init__(self, expense_id):
        super().__init__(f"Expense with ID {expense_id} not found.")

class InvalidExpenseIDError(ExpenseTrackerError):
    """Raised when an invalid (non-integer or out-of-range) expense ID is provided."""
    def __init__(self, expense_id):
        super().__init__(f"Invalid expense ID: {expense_id}. It must be a positive integer.")

class InvalidCategoryError(ExpenseTrackerError):
    """Raised when an invalid category is provided."""
    def __init__(self, category):
        super().__init__(f"Invalid category: {category}. Please provide a valid category.")
