"""
🔟 Raising exceptions in functions

Create a function withdraw(balance, amount):

Raise ValueError if amount is greater than balance
Return remaining balance otherwise    
    """

# from Day_13.Exceptional_handeling.atm import withdraw_balance

# print(withdraw_balance(2000,1000))


def withdraw_balance(balance,amount):
    

    if amount > balance:
        #raise InsufficientBalanceException("Not sufficient balance")
        raise ValueError("Insuiificent balance")

    return f"Remaining balance: {balance - amount}"

if __name__=="__main__":
    print(withdraw_balance(12000,10000))