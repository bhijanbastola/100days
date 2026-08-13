#Abstraction in python (Inheritance)

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def volume(self):
        return "Not Applicable of given shape."

