"""
1️⃣3️⃣ Create a custom exception

Create a custom exception class InvalidPasswordError. Raise it if the password length is less than 8 characters.    
    """

class InvalidPasswordError(Exception):
    """
    This error is generated when the length of the password is less than 8 .
    
    """
    pass

def check_password(password:str):
    if len(password)<8:
        raise InvalidPasswordError("Passsword must be greater than 8 digits")


check_password("1234567")