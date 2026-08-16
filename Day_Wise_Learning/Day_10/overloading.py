class Point:
    def __init__(self,x,y):
        self.x=x
        self .y=y

    def __str__(self):
        return f"({self.x},{self.y})"

    def __len__(self):
        a=len(str(self.x))
        b=len(str(self.y))
        return a+b

    def __add__(self,other):
        new_x= self.x+other.x
        new_y=self.y+other.y
        return Point(new_x,new_y)

    def __mul__(self,other):
        new_x= self.x * other.x
        new_y=self.y * other.y
        return Point(new_x,new_y)

p=Point(3,5)
p1=Point(3,6)

p3=p+p1
p4=p*p1
print(p3)
print(p4)
print(len(p))