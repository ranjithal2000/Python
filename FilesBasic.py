#Python JSON to dict
import json
details='{"Name":"Ranjitha","Languages":["Kannada","English"]}'
details_dict=json.loads(details)
print(details_dict)
print(details_dict['Languages'])


#Convert dict to JSON
import json
details_dict={"Name":"Ran",
      "Id":"1"}
details_json=json.dumps(details_dict)
print(details_dict)


#Writing JSON to a file
import json
sample_dict = {"name": "Bob",
"languages": ["English", "French"],
"married": True,
"age": 32
}
with open('sample.txt', 'w') as json_file:
  json.dump(sample_dict, json_file)


#updateJSON
import json
x='{"Name":"Ranju","City":"Kolar","State":"Karnataka"}'
y={"pin":563133}
z=json.loads(x)
z.update(y)
print(json.dumps(z))
