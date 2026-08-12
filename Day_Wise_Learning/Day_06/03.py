#Inheritance
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def intro(self):
        print(f"hello, I am {self.name}")

class Cat(Animal):
    def __init__(self,name,age,color):

        super().__init__(name,age)
        self.color=color

    def details(self):
        print(f"Name:{self.name}-Age:{self.age}-color:{self.color}")
    

cat=Cat('milo',22,'red')
cat.intro()
cat.details()