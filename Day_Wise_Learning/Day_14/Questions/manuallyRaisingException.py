"""
    1️⃣2️⃣ Raise TypeError manually

Write a function add_numbers(a, b):

Raise TypeError if inputs are not integers
Return sum otherwise
    """

def add_number(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError ("Please only enter the Integer")

    return a+b

result=add_number(2,3.5)
print(result)
