import json
from http.server import HTTPServer, BaseHTTPRequestHandler

class Chalet:
      def __init__(self, chalet_id, nom, url_image, latitude, longitude, plages):
            self.__chalet_id = chalet_id
            self.__nom = nom
            self.__url_image = url_image
            self.__geolocalisation = [latitude, longitude]
            self.__plages = plages

      @property
      def chalet_id(self):
            return self.__chalet_id

      @chalet_id.setter
      def chalet_id(self, valeur):
            self.__chalet_id = valeur

      @property
      def nom(self):
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

      @property
      def geolocalisation(self):
            return self.__geolocalisation

      @geolocalisation.setter
      def geolocalisation(self, latitude, longitude):
            self.__geolocalisation = []
            self.__geolocalisation.append(latitude)
            self.__geolocalisation.append(longitude)

      @property
      def plages(self):
            return self.__plages

      @plages.setter
      def plages(self, valeur):
            self.__plages = valeur

class Utilisateur: