#multiple inheritance
class Parent1:
    def func1(self):
        print("parent1")
class Parent2:
    def func1(self):
        print("parent2")
class Parent3:
    def func1(self):
        print("parent3")

class Child(Parent1,Parent2,Parent3):
    def func4(self):
        print('child')

child=Child()
child.func1()
child.func4()