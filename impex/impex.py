import csv
import xmltodict

def data_utilisateurs() :
    with open("./data/utilisateurs.csv") as csvfile :
        reader1 = csv.DictReader(csvfile)


def data_chalets() :
    with open('./data/chalets.csv') as csvfile :
        reader2 = csv.DictReader(csvfile)

def data_reservations() :
    file1 = open('./data/reservations.xml', 'r')
    xml_string = file1.read()
    reservation_dict = xmltodict.parse(xml_string)
    print(reservation_dict)

def data_dipos() :
    file2 = open('./data/disponibilites.xml', 'r')
    xml_string = file2.read()
    dispos_dict = xmltodict.parse(xml_string)
    print(dispos_dict)

print('hallo world')