class Person:
    count=0
    def __init__(self, name:str, age:int): 
        #initializer or constructor 
        self.name = name  #instance variable
        self.age = age
        Person.count+=1

    def greet(self): #<- instance method
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def get_full_name(first,last): #<- static method
        return f"{first} {last}"


student = Person("Alice", 30)
student.greet()  # Output: Hello, my name is Alice and I am 30
student.get_count()
student.get_full_name("Alice","Johnson")