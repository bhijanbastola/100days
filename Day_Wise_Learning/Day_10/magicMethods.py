class Person:
    """
    Leave it
    """
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name}-{self.age}"

    def __repr__(self):
        return f"Person({self.name}-{self.age})"

    def __len__(self):
        return self.age

    def __call__(self,gender="male"):
        return f"{self.name} is a {gender}"

person=Person("Bhijan",20)
print(person)
print(person.__doc__)




