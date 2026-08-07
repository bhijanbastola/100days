"""
Control Flow with Nested Loops and Complex Logic

Write a Python program that simulates a number guessing game:

The program should generate a random number between 1 and 100 and give the user 7 attempts to guess it.

After each wrong guess, the program should provide a hint whether the guess was too high or too low.

If the user fails to guess the number within the attempts, the program should reveal the number and ask if they would like to play again.
"""

import random
b=random.randint(1,100)
counter =0
while counter<=7:
    
    a=int(input("Enter the number (1-100): "))
    if a==b:
        print("Congrats you escaped the matrix")
        break
    else:
        if a>b:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
    counter+=1

print("The number was ",b)

