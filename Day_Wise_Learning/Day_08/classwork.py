class Pet():
    def __init__(self,name,children = [],energy=50):
        self.name = name
        self.children = children
        self.__energy = energy
       
    def get_energy(self):
        return self.__energy
 
    def set_energy(self,val=50):
        
       
        if val > 100:
            self.__energy = 100
        elif val < 0 :
            self.__energy = 0
        else :
            self.__energy = val
   
    def add_child(self,*child):
       
        
        self.children.append(child)
           
    def display(self):
        print(f"My name is {self.name} with children {self.children} and energy {self.__energy}")
           
peet = Pet("Ruby")
print(peet.get_energy())
 
peet.set_energy()
print(peet.get_energy())
 
peet.add_child("ram","hari","sita")
peet.display()


class RoboPet(Pet):
    def set_energy(self, val=50):
        val=val+0.2*val
        print(val)

        if val > 100:
            a=self.Pet__energy=100
            print(a)
        elif val < 0 :
            b=self.Pet__energy = 0
            print(b)
        else :
            c=self.Pet__energy = val
            print(c)

r=RoboPet("one")
u=RoboPet("Two")
r.add_child(u,peet)
r.set_energy(90)

def get_total_family_energy():

    pass
    