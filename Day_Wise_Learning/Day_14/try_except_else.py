try:
    x=float(input("Number:"))
    y=int(input("Number:"))
    result=x/y

except ValueError as e:
    print("Error occured",e)
    result=0

else:
    print("Final Result :",result)

finally :
    print("End of File")