"""
    4️⃣ Using else block

Write a program that divides two numbers. Print "Division successful" only if no exception occurs.

Expected concepts: try–except–else


    """

def division():
    try:
        a=int(input("Enter the Numerator :"))
        b=int(input("Enter the Denominator :"))
        c=a/b
        

    except ValueError as e:
        print(f"Value Error occured in the program {e}")

    except ZeroDivisionError as e:
        print(f"Cannot divide by 0 ")

    else:
        print(f"Divison is : {c}")

division()