from statistics import mean
class Student:
    def __init__(self,name:str,p:int,c:int,m:int):
        self.name=name
        self.p=p
        self.c=c
        self.m=m

    def total(self):
        return sum([self.p, self.c, self.m])

    def average(self):
        return mean([self.p,self.c,self.m])

    def display(self):
        print(f"Name: {self.name}, Total: {self.total()}, Average: {self.average()}")
    
student1=Student("Alice", 5, 5, 5)
student1.display()
isinstance(student1, Student)