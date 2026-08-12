#MultiLevel Inheritance
class A:
    def method_a(self):
        print("This is methodn from CLass A")

class B(A):
    def method_b(self):
        print("This is a method of class B")

class C(B):
    def method_c(self):
        print("this is multilevel in heritance ")

c=C()
c.method_a()
c.method_b()
c.method_c()
print(isinstance(c,C))
print(dir(c))