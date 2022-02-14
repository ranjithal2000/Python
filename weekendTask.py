# JSON
import json
class Image:
    def ImageDetails(self):
        with open('image.json') as file:
            data=json.load(file)
            for row in data:
                print(data)
class Imagefile(Image):
    def ImagefileDetails(self):
        super()
        with open('img.json') as f:
            data=json.load(f)
            for row in data:
                print(data)
obj=Imagefile()
print("-----Image1 Details-----")
obj.ImageDetails()
print("-----Image2 Details-----")
obj.ImagefileDetails()



# import module
import csv
class Image:
    def imageDetails(self):
        with open('C:\\Users\\Ranjitha.l\\Documents\\task.csv', newline='') as csvfile:
            data = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in data:
                print(', '.join(row))
class Images(Image):
    def imagesDetails(self):
        super()
        with open('C:\\Users\\Ranjitha.l\\Documents\\task1.csv', newline='') as csvfile:
            data = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in data:
                print(', '.join(row))
obj = Images()
print("-----Image1 Detail-----")
obj.imageDetails()
print("-----Image2 Detail-----")
obj.imagesDetails()




#xml
import xmltodict
import pprint
with open('image.xml', 'r') as file:
   my_xml = file.read()
print(my_xml)
my_dict = xmltodict.parse(my_xml)
pprint.pprint(my_dict, indent=4)
