import json
from http.server import HTTPServer, BaseHTTPRequestHandler


class Truc() :

    def __init__(self):
        self.__reservations = {}

    @property
    def reservations(self):
        return self.reservations

    def post_reservations(self, nouv_reservation):
        if nouv_reservation in self.__reservations.keys():
            raise ValueError('Reservation deja existante ? ')
        self.__reservations.append(nouv_reservation)

    def put_reservations(self, nouv_reservation, anc_reservation):
        if nouv_reservation == anc_reservation :
            raise ValueError('Aucun changement dans la reservation')
        self.reservations[anc_reservation] = nouv_reservation
    def get_reservation(self, ID_reservation):
        return self.__reservations[ID_reservation]

    def get_reservations(self, email):



        pass