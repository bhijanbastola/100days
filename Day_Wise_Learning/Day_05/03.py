#impleementing a simple calculator class with basic arithmetic operations using classes

class Calculator:

    def __init__(self,num1=0,num2=0):
        self.num1=num1
        self.num2=num2


        
    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero")


calc = Calculator(2,4)
print(calc.add())        # Output: 6
print(calc.subtract())   # Output: -2   
print(calc.multiply(10, 5))   # Output: 50
print(calc.divide(10, 5))     # Output: 2.0 

