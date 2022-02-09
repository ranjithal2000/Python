#any length of arguements(overloading)
class Calculate:
    def add(self, *args):
        result=0
        for abc in args:
            result+=abc
        print("result:{}".format(result))
c=Calculate()
c.add(15,20,25,89)
c.add(50,50)

#overloading(fixed length of arguements)
class Calculate:
    def add(self,a,b,c=0):
        if c>0:
            print("a+b+c={}".format(a+b+c))
        else:
            print("a+b={}".format(a+b))
c=Calculate()
c.add(5,10,15)
c.add(10,15)



#overriding
class one:
    def fun1(self):
        print("function one")
    def fun2(self):
        print("function two")
class two(one):
    def fun1(self):
        print("altered function one")
    def fun3(self):
        print("function three")
obj=two()
obj.fun1()
