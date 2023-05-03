import json
from http.server import HTTPServer, BaseHTTPRequestHandler

class Chalet:
      def __init__(self, chalet_id, nom, url_image, latitude, longitude, plages):
            self.__id = chalet_id
            self.__nom = nom
            self.__url_image = url_image
            self.__geolocalisation = [latitude, longitude]
            self.__plages = plages

class Utilisateur: