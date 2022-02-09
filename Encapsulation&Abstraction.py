#encapsulation
class One:#base class
    def __init__(self):
        self.a=2
class Two(One):#derived class
    def __init__(self):
        One.__init__(self)
        print("calling the member of class One:",self.a)
        self.a=3
        print("calling altered member of class One:", self.a)
obj1=Two()
obj2=One()
print("members of obj1",obj1.a)
print("members of obj2",obj2.a)

#abstraction
import abc
class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,x,y):
        self.l=x
        self.b=y
    def area(self):
        return self.l*self.b
r=Rectangle(20,30)
print('area:',r.area())
