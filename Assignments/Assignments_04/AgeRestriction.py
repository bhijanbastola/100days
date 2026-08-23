""" 
Exception Handling Scenario: Online Age-Restricted Service

Scenario: You’re building a sign-up system for an online movie rental platform. Some movies are age-restricted (18+). You need to ensure proper validation and error handling during user registration.

Task:

Create a custom exception class called UnderageError that inherits from Exception.

Write a function register_user() that:

Takes a user’s name and age as input.
Raises UnderageError if the user is under 18.
Otherwise, prints a welcome message.
Wrap the function call in a try block and handle the exception.

Use else to confirm successful registration and finally to always print “Thank you for using MovieTime!” regardless of outcome.

Also try to validate if the age input is numeric. Raise a ValueError if not, and handle it separately.
"""

class UnderAgeError(Exception):

    pass

def register_user():
    name=input("Enter your Name :")
    age=int(input("Enter your age"))

    if age<18:
        raise UnderAgeError("You must be above 18 to watch the movie")

    else :
        print(f"Welcome {name}")





try:
    register_user()

except UnderAgeError as e:
    print(e)

except ValueError as e:
    print("Please enter an integer")

else:
    print("Registred Successfully")

finally:
    print("Thank you for using MovieTime!")

