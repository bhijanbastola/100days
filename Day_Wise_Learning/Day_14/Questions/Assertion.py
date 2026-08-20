""" 
1️⃣6️⃣ Using assertions

Write a function that checks if a number is positive using assert. Handle the AssertionError.
"""
def check_positive(number):
    assert number > 0, "Number must be positive"
    print("Number is positive")


try:
    check_positive(-5)

except AssertionError as e:
    print("Error:", e)