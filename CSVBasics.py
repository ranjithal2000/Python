import csv
with open('C:\\Users\\Ranjitha.l\\Documents\\Example.csv','w') as file:
    writer1 = csv.writer(file)
    writer1.writerow(["SN", "Movie", "Protagonist"])
    writer1.writerow([1, "Paramatma", "Puneeth Rajkumar"])
    writer1.writerow([2, "KGF", "Yash"])



import csv
with open('C:\\Users\\Ranjitha.l\\Documents\\Book1.csv','r') as csvfile:
 data = csv.reader(csvfile, delimiter=' ')
 for row in data:
   print(' '.join(row))



import csv
csv_rowlist = [["SN", "Movie", "Protagonist"], [1, "Paramatma", "Appu"],
               [2, "KGF", "Yash"],[3, "Badava Rascal", "Dhananjay"],[4, "Kotigobba2", "Sudeep"]]
with open('C:\\Users\\Ranjitha.l\\Documents\\Example.csv', 'w',newline='') as file:
    writer1 = csv.writer(file)
    writer1.writerows(csv_rowlist)


import csv
with open("example.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(dict(row))



import csv
with open('C:\\Users\\Ranjitha.l\\Documents\\Example1.csv', 'w', newline='') as file:
 fieldnames = ['name', 'rating']
 writer1 = csv.DictWriter(file, fieldnames=fieldnames)
 writer1.writeheader()
 writer1.writerow({'name': 'Ranju', 'rating': 1001})
 writer1.writerow({'name': 'Bae', 'rating': 2002})
 writer1.writerow({'name': 'Bee', 'rating': 3003})
