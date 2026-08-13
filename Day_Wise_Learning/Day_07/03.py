#Encapsulation
                              
class Example:
    def __init__(self):
        self.public=1
        self.__private=2
        self._protected=3

    def public_method(self):
        print("Public Method")

    def _protected_method(self):
        print("Protected Method")

    def __private_method(self):
        print("Private Method")


obj=Example()
obj._protected
obj._protected_method()
# obj.__private
# obj.__private_method()


class SubClass(Example):
    def get_public(self):
        print(self.public)

    def get_protected(self):
        print(self._protected)

    # def get_private(self):
    #     print(self.__private)

s=SubClass()
s.get_public()
print(s.public)

    
