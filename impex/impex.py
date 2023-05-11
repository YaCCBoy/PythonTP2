import csv
import xmltodict
from client import client_2

class Utilisateur:
    def __init__(self, email, mdp, nom, prenom, type, adresse_no, adresse_rue, adresse_ville, adresse_prov, adresse_pays, adresse_cp):
        self.__email = email
        self.__mdp = mdp
        self.__nom = nom
        self.__prenom = prenom
        self.__type = type
        self.__adresse_no = adresse_no
        self.__adresse_rue = adresse_rue
        self.__adresse_ville = adresse_ville
        self.__adresse_prov = adresse_prov
        self.__adresse_pays = adresse_pays
        self.__adresse_cp = adresse_cp

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valeur):
        self.__email = valeur

    @property
    def mdp(self):
        return self.__mdp

    @mdp.setter
    def mdp(self, valeur):
        self.__mdp = valeur

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, valeur):
        self.__nom = valeur

    @property
    def prenom(self):
        return self.__prenom

    @prenom.setter
    def prenom(self, valeur):
        self.__prenom = valeur

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, valeur):
        self.__type = valeur

    @property
    def adresse_no(self):
        return self.__adresse_no

    @adresse_no.setter
    def adresse_no(self, valeur):
        self.__adresse_no = valeur

    @property
    def adresse_rue(self):
        return self.__adresse_rue

    @adresse_rue.setter
    def adresse_rue(self, valeur):
        self.__adresse_rue = valeur

    @property
    def adresse_ville(self):
        return self.__adresse_ville

    @adresse_ville.setter
    def adresse_ville(self, valeur):
        self.__adresse_ville = valeur

    @property
    def adresse_prov(self):
        return self.__adresse_prov

    @adresse_prov.setter
    def adresse_prov(self, valeur):
        self.__adresse_prov = valeur

    @property
    def adresse_pays(self):
        return self.__adresse_pays

    @adresse_pays.setter
    def adresse_pays(self, valeur):
        self.__adresse_pays = valeur

    @property
    def adresse_cp(self):
        return self.__adresse_cp

    @adresse_cp.setter
    def adresse_cp(self, valeur):
        self.__adresse_cp = valeur

class Chalet:
    def __init__(self, id, nom, url_image):
        self.__id = id
        self.__nom = nom
        self.__url_image = url_image

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, valeur):
        self.__id = valeur

    @property
    def nom(self, nom):
        return self.__nom

    @nom.setter
    def nom(self, valeur):
        self.__nom = valeur

    @property
    def url_image(self):
        return self.__url_image

    @url_image.setter
    def url_image(self, valeur):
        self.__url_image = valeur

def data_utilisateurs() :
    with open("./data/utilisateurs.csv") as csvfile :
        reader1 = csv.DictReader(csvfile)
        print(reader1)


def data_chalets() :
    with open('./data/chalets.csv') as csvfile :
        reader2 = csv.DictReader(csvfile)
        print(reader2)

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

utilisateurs = data_utilisateurs()
chalets = data_chalets()
reservations = data_reservations()
plages = data_dipos()

client_2.ClientServeurChalet.post_reservation(reservations)
client_2.ClientServeurChalet.post_chalet(chalets)
client_2.ClientServeurChalet.post_utilisateur(utilisateurs)
client_2.ClientServeurChalet.post_plage(plages)