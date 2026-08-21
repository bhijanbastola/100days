while True:
    try:
        a = int(input("Enter the integer: "))

    except ValueError:
        print("Please enter an integer")
        continue

    else:
        print("You entered the correct value")
        break

