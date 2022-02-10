#read
import json
f = open('data.json','r')
data = json.load(f)
for i in data['employee']:
 print(i)
f.close()


#write
import json
a={
    "details" : {
        "name":"ranju",
        "age":"22"
    }
}
with open("abc.json","w") as b:
    json.dump(a,b,indent=2)

#append
import json
c={
    "additional" :
        {
            "college":"citech",
            "course":"cse"
        }
}
with open("abc.json","a") as b:
    json.dump(c,b,indent=2)
