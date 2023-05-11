import csv
import xmltodict
from client import client_2


# Fonction pour lire le fichier utilisateurs
def data_utilisateurs() :
    with open("./data/utilisateurs.csv") as csvfile :
        reader1 = csv.DictReader(csvfile)
        return reader1

# Fonction pour lire le fichier chalets
def data_chalets() :
    with open('./data/chalets.csv') as csvfile :
        reader2 = csv.DictReader(csvfile)
        return reader2

# Fonction pour lire le fichier reservations
def data_reservations() :
    file1 = open('./data/reservations.xml', 'r')
    xml_string = file1.read()
    reservation_dict = xmltodict.parse(xml_string)
    print(reservation_dict)
    return reservation_dict

# Fonction pour lire le fichier disponibilitées
def data_dipos() :
    file2 = open('./data/disponibilites.xml', 'r')
    xml_string = file2.read()
    dispos_dict = xmltodict.parse(xml_string)
    print(dispos_dict)
    return dispos_dict


# Associe a des variables les différentes données

utilisateurs = data_utilisateurs()
chalets = data_chalets()
reservations = data_reservations()
plages = data_dipos()

