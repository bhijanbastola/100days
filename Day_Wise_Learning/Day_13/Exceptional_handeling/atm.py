class InsufficientBalanceException(Exception):
    """Custom exception for insufficient balance."""
    pass


def withdraw_balance(amount):
    balance = 10000

    if amount > balance:
        raise InsufficientBalanceException("Not sufficient balance")

    return f"Remaining balance: {balance - amount}"


withdraw_balance(12000)