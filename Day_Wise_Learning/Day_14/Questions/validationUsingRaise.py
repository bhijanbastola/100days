"""
    9️⃣ Manual validation using raise

Write a function check_age(age) that:

Raises ValueError if age is negative
Prints "Valid age" otherwise
    """

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")

    print("Valid age")


check_age(-5)