class InvalidAgeException(Exception):
    """
    Raise an custom exception
    
    """

def check_customer(customer_id):
        age=21
        if age:
            if age>=18:
                print("GOOD TO GO")

        else:
            raise InvalidAgeException("Not a valid age")

check_customer(22)