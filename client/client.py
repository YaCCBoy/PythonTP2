import requests

class ClientServeurChalet:

    def __init__(self, url_base):
        self.__url_base = url_base
        self.__post_headers = {'Content-Type': 'text/json'}

    def get_reservation(self, reservations):
        req = requests.get(self.__url_base + '/reservation/' + reservations)
        print(req.status_code)
        print(req.content)

    def get_reservations_utilisateur(self):
        pass
    def post_reservation(self):
        pass
    def put_reservation(self):
        pass
    def delete_reservation(self):
        pass
    def post_utilisateur(self):
        pass
    def get_reservations_liste(self):
        pass
    def post_chalet(self):
        pass
    def get_chalet(self):
        pass
    def post_plage(self):
        pass