class Person:
    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age

class Employee(Person):
    def __init__(self,name:str,age:int,emp_id:int):
        super().__init__(name,age)
        self.emp_id=emp_id

class Manager(Employee):
    def __init__(self,name:str,age:int,emp_id:int,department:str):
        super().__init__(name,age,emp_id)
        self.department=department

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.emp_id}, Department: {self.department}")

m=Manager("bhijan",22,1,"it")
m.display()


