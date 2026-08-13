#Polymorphism
class Example:
    def add(self,*args):
        return sum(args)

e=Example()
print(e.add(1,23.5))
print(e.add(1,23.5,4))
print(e.add(1.5,23.5,3.5))



