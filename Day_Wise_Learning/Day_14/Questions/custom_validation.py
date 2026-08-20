"""
    1️⃣4️⃣ Custom exception in real scenario

Create a program for login validation:

Raise InvalidUserError if username is incorrect
Raise InvalidPasswordError if password is incorrect
    """

class InvalidUserError(Exception):
    """
    This gives an Invalid User Id Error
    
    """
    pass

class InValidPassWordError(Exception):
    """ 
    This gives an Invalid Password Error
    """

    pass

class LoginValidation:
    def login_validation(self,username:str,password:str):
        if username!="bhijan":
            raise InvalidUserError("Not a valid user")

        if password!="bastola":
            raise InValidPassWordError("Not a valid Password")

        print("Login Successful")

l=LoginValidation()
l.login_validation("bhijan","bastola")
