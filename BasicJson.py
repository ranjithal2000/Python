#program 1
import json
student = '{"name":"Ranju", "age": "22", "college":"CITech"}'
student_dict = json.loads(student)
print(student_dict)
print(type(student_dict))
print("\n")


#Program 2
employee='{"id":"1","name":"Ranju","dept":"IT"}'
employee_dict=json.loads(employee)
print(employee_dict)
print(type(employee_dict))
print(employee)
print(type(employee))


#example 3(python dict to json)
student='{"name":"ranju","dept":"cse","college":"citech"}'
student_dict=json.loads(student)
json_object = json.dumps(student_dict, indent=4)
print(json_object)
print(type(json_object))


#example4
employee='{"name":"ranju","id":"2","dept":"it"}'
employee_dict=json.loads(employee)
json_object=json.dumps(employee_dict,indent=2)
print(json_object)

#example5
a ={"name":"John",
    "age":31,
 "Salary":25000}
b = json.dumps(a)
print(b)
print(type(b))
