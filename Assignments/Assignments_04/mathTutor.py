
"""
    
    Math Tutor Using Random, Arithmetic Operators, and OOP

Scenario: Create a MathTutor class that generates random math questions using random and math operators.

Track correct and incorrect answers.
Provide a score at the end.
Handle invalid input using exception handling.
Concepts: Random, Math, Exception Handling, Classes
    """

import random
import operator


class MathTutor:

    def __init__(self):
        self.operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }

    def generate_question(self):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)

        symbol = random.choice(list(self.operators.keys()))

        # Avoid division by zero
        if symbol == "/":
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 20)

        answer = self.operators[symbol](num1, num2)

        return f"{num1} {symbol} {num2}", answer

    def start(self):
        score = 0

        for i in range(5):
            question, answer = self.generate_question()

            print(f"\nQuestion {i + 1}: {question}")

            try:
                user_answer = float(input("Your answer: "))

                if user_answer == answer:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong! The correct answer is {answer}")

            except ValueError:
                print(f"Invalid input! The correct answer is {answer}")

        print(f"\nYour score: {score}/5")


tutor = MathTutor()
tutor.start()

