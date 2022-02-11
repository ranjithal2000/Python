from bs4 import BeautifulSoup
with open('sample.xml', 'r') as f:
   data = f.read()
   print(data)
bs_data = BeautifulSoup(data, 'xml')
for tag in bs_data.find_all('Product', {'name':'TV'}):tag["price"]="...!!!"
print(bs_data.prettify())



import xmltodict
import pprint
with open('sample.xml', 'r') as file:
   my_xml = file.read()
my_dict = xmltodict.parse(my_xml)
pprint.pprint(my_dict, indent=4)


# Program to convert an xml
# file to json file

import json
import xmltodict
with open("sample.xml") as xml_file:
     data_dict = xmltodict.parse(xml_file.read()) #XML TO DICT
     xml_file.close()
     json_data = json.dumps(data_dict) #DICT TO JSON
     with open("data1.json", "w") as json_file: #JSON->DATA1.JSON
         json_file.write(json_data)
         json_file.close()

