class Employee:
    name=""
    age=0
    def emp(self):
        print(self.name)
        print(self.age)

class Department(Employee):
    id=0
    place=""
    def dep(self):
        print(self.id)
        print(self.place)

class Admin(Department, Employee):
    def adm(self):
        print("employee details:")
        print("employee name:", self.name)
        print("employee age:", self.age)
        print("department details:")
        print("department id:", self.id)
        print("department place:", self.place)

object = Admin()
object.name="Ranju"
object.age=22
object.id=1
object.place="Bengalore"
object.adm()

class Emp():
    name=""
    def emp(self):
        print(self.name)

class Dep(Emp):
    location=""
    def dep(self):
        print(self.location)

class Adm(Dep):
    def adm(self):
        print("Name:", self.name)
        print("Location:", self.location)
obj=Adm()
obj.name="Ranju"
obj.location="Bengalore"
obj.adm()
