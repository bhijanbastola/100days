try:
    num=int(input("Enter the number"))
    print(6/num)


except ValueError as e:
    print(e)
    print(0)

except ZeroDivisionError as e:
    print("Cannot be divivded by 0")
    print(0)

except Exception as e:
    print("Error has occured")


value="abc"
try:
    print(int(value))

except (ValueError,TypeError) as e:
    print(f"{value} -> cannot be converted to int :->{e}")