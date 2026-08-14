a=input("enter a string:").lower().strip()
reverse="".join(reversed(a))
#print(reverse)
if a==reverse:
    print("palindrome")
else:
    print("not a palindrome")

