"""
    1️⃣5️⃣ Exception chaining

Write a program that:

Catches a ValueError
Raises a RuntimeError using raise ... from ...
    """

try:
    age = int(input("Enter your age: "))

except ValueError as e:
    raise RuntimeError("Invalid age entered") from e