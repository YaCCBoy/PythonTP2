import csv

with open("utilisateurs.csv") as csvfile :
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['first_name'], row['last_name'])

print("Hallo world ouais ouais mon cul")