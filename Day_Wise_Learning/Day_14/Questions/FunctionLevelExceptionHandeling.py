"""
    7️⃣ Function-level exception handling

Create a function safe_divide(a, b) that:

Returns division result if valid
Returns None if an exception occurs
Prints the error message

    """

def safe_divide(a,b):
    try:
        return a/b

    except ZeroDivisionError as e:
        print(f"Error : {e}")
        return None

print(safe_divide(2,0))