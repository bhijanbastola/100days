"""
1️⃣ Handle ZeroDivisionError

Write a program that takes two numbers from the user and prints their division. Handle the error when the denominator is zero.

Expected concepts: try, except ZeroDivisionError
"""

def division():
    try:
        a=int(input("Enter the Numerator :"))
        b=int(input("Enter the Denominator :"))

        print(f"Divison is : {a/b}")

    except ValueError as e:
        print(f"Value Error occured in the program {e}")

    except ZeroDivisionError as e:
        print(f"Cannot divide by 0 ")

if __name__=="__main__":
    division()