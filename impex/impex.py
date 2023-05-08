import csv
import xmltodict

with open("./data/utilisateurs.csv") as csvfile :
    reader1 = csv.DictReader(csvfile)

with open('./data/chalets.csv') as csvfile :
    reader2 = csv.DictReader(csvfile)

with open('./data/reservations.xml', 'r') :
    xml_string = file.read()