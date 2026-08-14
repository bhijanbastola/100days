#Abstraction in python (Inheritance)

from abc import ABC,abstractmethod
import math

class Shape(ABC):
    def __init__(self,length,breadth=0,height=0):
        self.length=length
        self.breadth=breadth
        self.height=height

    
    @abstractmethod
    def area(self):
        pass

    def volume(self):
        return "Not Applicable of given shape."

class Rectangle(Shape):
    def area(self):
        return self.length*self.breadth

rect=Rectangle(50,60)
# print(rect.area())

class Circle(Shape):
    def __init__(self,radius):
        self.r=radius

    def area(self):
        return math.pi *(self.r**2)


c=Circle(45)

print(c.area())