import requests

class ClientServeurChalet:

    def __init__(self, url_base):
        self.__url_base = url_base
        self.__post_headers = {'Content-Type': 'text/json'}

    def get_reservation(self, reservations):
        req = requests.get(self.__url_base + '/reservation/' + reservations)
        print(req.status_code)
        print(req.content)

    def get_reservations_utilisateur(self, reservations_c):
        req = requests.get(self.__url_base + '/reservation du client/' + reservations_c)
        print(req.status_code)
        print(req.content)
    def post_reservation(self, reservation):
        json_body = '{"reservation": "' + reservation + '"}'
        req = requests.post(self.__url_base + '/reservation', data=json_body)
        print(req.status_code)
        print(req.content)
    def put_reservation(self, data_reservations, reservation):
        json_body = '{"reservation": "' + reservation + '" }'
        req = requests.post(self.__url_base + '/data_reservations/' + data_reservations, data=json_body)
        print(req.status_code)
        print(req.content)
    def delete_reservation(self):
        pass
    def post_utilisateur(self, utilisateur):
        json_body = '{"utilisateur": "' + utilisateur + '"}'
        req = requests.post(self.__url_base + '/utilisateur', data=json_body)
        print(req.status_code)
        print(req.content)
    def get_reservations_liste(self):
        pass
    def post_chalet(self):
        pass
    def get_chalet(self):
        pass
    def post_plage(self):
        pass

print('hallo world')