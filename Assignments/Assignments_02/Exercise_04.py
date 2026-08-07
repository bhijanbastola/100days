"""
Question:

Write a Python program to check whether a given number is an Armstrong number or not.

Definition: An Armstrong number (also known as a narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits. For example:

153 is an Armstrong number because ( 1^3 + 5^3 + 3^3 = 153 ).
9474 is an Armstrong number because ( 9^4 + 4^4 + 7^4 + 4^4 = 9474 ).
Input:
An integer (e.g., 153).

Output:
Output "Yes, it's an Armstrong number." if the number is an Armstrong number. Otherwise, output "No, it's not an Armstrong number."

Constraints:

The input should be a positive integer.
"""
num = int(input("Enter a number: "))

temp = num
digits = len(str(num))
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10

if sum == num:
    print("Yes, it's an Armstrong number.")
else:
    print("No, it's not an Armstrong number.")






