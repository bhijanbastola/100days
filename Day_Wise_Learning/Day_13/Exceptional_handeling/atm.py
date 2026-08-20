class InsufficientBalanceException(Exception):
    """Custom exception for insufficient balance."""
    pass


def withdraw_balance(balance,amount):
    

    if amount > balance:
        #raise InsufficientBalanceException("Not sufficient balance")
        raise ValueError("Insuiificent balance")

    return f"Remaining balance: {balance - amount}"

if __name__=="__main__":
    withdraw_balance(12000,10000)