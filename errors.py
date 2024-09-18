class ExpenseTrackerError(Exception):
    """Base class for other exceptions"""
    pass

class ExpenseNotFoundError(ExpenseTrackerError):
    """Raised when the expense ID is not found"""
    pass
