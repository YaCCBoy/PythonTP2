import json
from http.server import HTTPServer, BaseHTTPRequestHandler


class Truc() :

    def __init__(self):
        self.__reservations = {}

    @property
    def reservations(self):
        return self.reservations

    def post_reservations(self, info_reservation):
        if info_reservation in self.__reservations.keys():
            raise ValueError('Reservation deja existante ? ')
        self.__reservations[info_reservation] = []

    def put_reservations(self, ):
    def get_reservations(self):
        pass