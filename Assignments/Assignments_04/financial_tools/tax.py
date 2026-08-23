def calculate_tax():
    try:
        amount = float(input("Enter the amount to be taxed: "))

        if amount < 1000000:
            tax = amount * 0.01
        else:
            tax = amount * 0.10

        remaining_amount = amount - tax

    except ValueError:
        print("Please enter a valid number")

    else:
        print("The remaining balance is", remaining_amount)


if __name__=="__main__":
    calculate_tax()