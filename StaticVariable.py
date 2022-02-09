#static
class one:
    staticVariable=1
print(one.staticVariable)
instance=one()
print(instance.staticVariable)
instance.staticVariable=2
print(instance.staticVariable)
print(one.staticVariable)

#static variable
class Employee:
    dept="CSE"
    def __init__(self,name,id):
        self.name=name
        self.id=id
emp1=Employee('Ranju','C101')
emp2=Employee('Bee','C102')
print(emp1.dept)
print(emp2.dept)
print(emp1.name)
print(emp2.name)
print(emp1.id)
print(emp2.id)
print(Employee.dept)
emp1.dept="ISE"
print(emp1.dept)
print(emp2.dept)
Employee.dept="ECE"
print(emp1.dept)
print(emp2.dept)
