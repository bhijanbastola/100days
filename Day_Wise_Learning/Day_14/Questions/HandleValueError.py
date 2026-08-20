"""
2️⃣ Handle ValueError

Ask the user to enter an integer. If the user enters a non-integer value, print a friendly error message.

Expected concepts: ValueError
    """

try:
    a = int(input("Enter an integer: "))
    print("You entered a correct value")

except ValueError:
    print("Please enter a valid integer.")