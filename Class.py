class Emp:
    name="Employee"
    city="Kolar"
    age=22
    def __init__(self,name,city,age):
        self.name=name
        self.city=city
        self.age=age
    def details(self):
        print("Employee name= {}".format(self.name))
        print("Employee city= {}".format(self.city))
        print("Employee age= {}".format(self.age))
A=Emp("Ranju","kolar",22)
print("Details of an {}:".format(A.__class__.name))
A.details()
