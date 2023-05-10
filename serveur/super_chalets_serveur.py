import json
from http.server import HTTPServer, BaseHTTPRequestHandler


class Truc() :

    def __init__(self):
        self.__reservations = {}
        self.__utilisateurs = {}
        self.__chalets = {}

    @property
    def reservations(self):
        return self.reservations

    def post_reservations(self,reservations, nouv_reservation):
        if nouv_reservation in self.__reservations.keys():
            raise ValueError('Reservation deja existante ? ')
        self.__reservations[reservations].append(nouv_reservation)

    def put_reservations(self, nouv_reservation, anc_reservation):
        if nouv_reservation == anc_reservation :
            raise ValueError('Aucun changement dans la reservation')
        self.reservations[anc_reservation] = nouv_reservation
    def get_reservation(self, ID_reservation):
        if ID_reservation in self.__reservations.keys() :
            return self.reservations[ID_reservation]
        else :
            raise ValueError('ID inexistant')

    def get_reservations(self, email):
        if email in self.__reservations.keys() :
            return self.__reservations[email]

    def post_utilisateur(self, reservations, utilisateur):
        if utilisateur in self.__reservations.keys():
            raise ValueError('Utilisateur deja existant')
        self.__reservations[reservations].append(utilisateur)


    def post_chalet(self, chalets, chalet) :
        if chalet in self.__chalets.keys() :
            raise ValueError('Chalet deja existant')
        self.__chalets[chalets].append(chalet)
    def get_chalet(self, ID_chalet):
        if ID_chalet in self.__chalets.keys() :
            return self.__chalets[ID_chalet]

    def post_chalet(self, reservations, ID_chalet, plage) :
        if ID_chalet in self.__reservations.keys() :
            self.__reservations[reservations].append(plage)
        else :
            raise ValueError('ID de chalet inexistante')
