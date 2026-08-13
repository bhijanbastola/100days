# Method Overiding

class Animal:
    def sound(self):
        print ("Making sound")


class Dog(Animal):
    def sound(self):
        print("Dogesh vai makes woff sound")


dog= Dog()
dog.sound()