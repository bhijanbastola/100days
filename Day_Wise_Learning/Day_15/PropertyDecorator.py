#Getter
import uuid
class Person:
    def __init__(self,name):
        self.name=name


    @property
    def user_id(self):
        print("Getting ID :")
        return f"{self.name[-5:]}_{str(uuid.uuid1())[:8]}"

    # Setter 

    @user_id.setter
    def user_id(self,value):
        print("Setting Name :")
        self.name=value

    #Deleter
    @user_id.deleter
    def name(self):
        print("Deleting Name :")
        self.name=" "



obj=Person("Bhijan")
obj.user_id
obj.user_id="Bastola"
del obj.user_id