#default constructor
class Constructors:
    def __init__(self):
        self.name="Ranjitha"
    def print(self):
        print(self.name)
obj= Constructors()
obj.print()


#parameterizes constructor
class Add:
    num1=0
    num2=0
    ans=0
    def __init__(self,f,s):
        self.num1=f
        self.num2=s
    def print(self):
        print("first number="+str(self.num1))
        print("second number=" + str(self.num2))
        print("answer=" + str(self.ans))
    def cal(self):
        self.ans=self.num1+self.num2
obj=Add(20,30)
obj.cal()
obj.print()


#destructors
class Destructor:
    def __init__(self):
        print("class created")
    def __del__(self):
        print("class deleted")
obj=Destructor()
del obj
