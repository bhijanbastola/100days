"""  
1️⃣8️⃣ Banking system simulation

Create a mini banking system:

Custom exceptions:

InsufficientBalanceError
InvalidAmountError
Handle deposits and withdrawals

Ensure program never crashes

"""
class InsufficientBalanceError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

class Bank:
    def transaction(self,balance,amount):

        if not isinstance(amount,(int,float)):
            raise InvalidAmountError("Please enter a valid amount")
        
        if amount>balance:
            raise InsufficientBalanceError("Insufficient Balance")

       

        print(f"Amount Withdrawn Successfully . The remaining balance is {balance-amount}")
            
b=Bank()
b.transaction(1000,'5000')
