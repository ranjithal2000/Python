import pandas as pd
data=pd.read_csv("Pandascsv.csv")
print(pd)
print(data)


import pandas as pd
df = pd.DataFrame([[1,'Jack', 567], [2,'Rose', 222]], columns = ['Sno','Name', 'Age'])
df.to_csv('PandasCSV.csv')


import pandas
df = pandas.read_csv('Pandascsv.csv', index_col='Sno')
print(df)


import pandas
df = pandas.read_csv('Pandascsv.csv', header=0,names=['Serial no', 'Employee name', 'Employee age'])
print(df)


import csv
class Employee:
    def employeeDetails(self):
        with open('C:\\Users\\Ranjitha.l\\Documents\\Example1.csv', newline='') as csvfile:
            data = csv.reader(csvfile, delimiter=' ')
            for row in data:
                print(','.join(row))
class Department(Employee):
    def departmentDetails(self):
        super()
        with open('C:\\Users\\Ranjitha.l\\Documents\\Book1.csv', newline='') as csvfile:
            data = csv.reader(csvfile, delimiter=' ')
            for row in data:
                print(','.join(row))
obj = Department()
obj.employeeDetails()
obj.departmentDetails()
