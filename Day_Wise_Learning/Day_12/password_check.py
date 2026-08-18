import re
class PassCheck:

  
    def __init__(self,password):
        self.password=password
        

    def check(self):
   
        pattern=r"^(?=.*[A-Za-z])(?=.*\d).{9,}$"
        if re.match(pattern,self.password):
            print("Strong password")
        else :
            print("weak password")

p=PassCheck("123")
p.check()