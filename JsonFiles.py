#files1
import json
def write_json(new_data, filename='data.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data["employee"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4, sort_keys=True)
y = {
         "id": "05",
         "name": "JKTECH",
         "department": "HR"
      }
write_json(y)



#file2
import json
data = {
 "user": {
    "name": "John",
    "age": 21,
    "Place": "Bangalore",
    "Blood group": "O+"
 }
}
with open( "datafile.json" , "w" ) as write:
 json.dump( data , write )
