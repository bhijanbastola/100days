"""
    1️⃣1️⃣ Re-raising exceptions

Write a program where:

An exception is caught
Logged using print
Re-raised using raise
    """
def divide(a, b):
    try:
        result = a / b
        return result

    except ZeroDivisionError as e:
        print("Error logged:", e)
        raise


try:
    print(divide(10, 0))

except ZeroDivisionError:
    print("Exception handled in after re-raise")