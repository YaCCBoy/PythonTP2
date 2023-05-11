import requests

class ClientServeurChalet:

    def __init__(self, url_base):
        self.__url_base = url_base
        self.__post_headers = {'Content-Type': 'application/json'}

    def get_reservation(self, reservation):
        req = requests.get(self.__url_base + '/reservation/' + reservation)
        print(req.status_code)
        print(req.content)

    def get_reservations_utilisateur(self, reservations_c):
        req = requests.get(self.__url_base + '/reservations_utilisateur/' + reservations_c)
        print(req.status_code)
        print(req.content)

    def post_reservation(self, info_reservation):
        json_body = '{"reservation": "' + info_reservation + '"}'
        req = requests.post(self.__url_base + '/reservation', data=json_body, headers=self.__post_headers)
        print(req.status_code)
        print(req.content)

    def put_reservation(self, data_reservations, reservation):
        json_body = '{"reservation": "' + reservation + '" }'
        req = requests.put(self.__url_base + '/reservations/' + data_reservations, data=json_body, headers=self.__post_headers)
        print(req.status_code)
        print(req.content)

    def delete_reservation(self, reservation):
        req = requests.delete(self.__url_base + '/reservation/' + reservation)
        print(req.status_code)
        print(req.content)

    def post_utilisateur(self, utilisateur):
        json_body = '{"utilisateur": "' + utilisateur + '"}'
        req = requests.post(self.__url_base + '/utilisateur', data=json_body, headers=self.__post_headers)
        print(req.status_code)
        print(req.content)

    def get_reservations_liste(self, liste_reservations_ord):
        req = requests.get(self.__url_base + '/liste_reservations/' + liste_reservations_ord)
        print(req.status_code)
        print(req.content)

    def post_chalet(self, chalets):
        json_body = '{"chalets": "' + chalets + '"}'
        req = requests.post(self.__url_base + '/chalets', data=json_body, headers=self.__post_headers)
        print(req.status_code)
        print(req.content)

    def get_chalet(self, info_chalets):
        req = requests.get(self.__url_base + '/chalet/' + info_chalets)
        print(req.status_code)
        print(req.content)

    def post_plage(self, plage):
        json_body = '{"plages": "' + plage + '"}'
        req = requests.post(self.__url_base + '/plages', data=json_body, headers=self.__post_headers)
        print(req.status_code)
        print(req.content)

