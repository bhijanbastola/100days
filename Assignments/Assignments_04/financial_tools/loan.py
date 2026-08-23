def calculate_emi():
    loan_amount=float(input("Enter the amount:"))
    emi=loan_amount *0.12

    print(f"Your Installmenrt Amount is : {emi}")


if __name__=="__main__":
    calculate_emi()
