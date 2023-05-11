import requests

class ClientServeurChalet:

    # Constructeur
    def __init__(self, url_base):
        self.__url_base = url_base
        self.__post_headers = {'Content-Type': 'application/json'}

    # Méthode pour obtenir les infos pour les réservations
    def get_reservation(self, reservation):
        req = requests.get(self.__url_base + '/reservation/' + reservation)
        print(req.status_code)
        print(req.content)

    # Méthode pour retourner les reservations de l'utilisateur
    def get_reservations_utilisateur(self, reservations_c):
        req = requests.get(self.__url_base + '/reservations_utilisateur/' + reservations_c)
        print(req.status_code)
        print(req.content)

    # Méthode pour ajouter une réservation
    def post_reservation(self, info_reservation):
        json_body = info_reservation
        req = requests.post(self.__url_base + '/reservation', data=json_body, headers=self.__post_headers)
        print(req.status_code)
        print(req.content)

    # Méthode pour remplacer la réservation
    def put_reservation(self, data_reservations, reservation):
        json_body = '{"reservation": "' + reservation + '" }'
        req = requests.put(self.__url_base + '/reservations/' + data_reservations, data=json_body, headers=self.__post_headers)
        print(req.status_code)
        print(req.content)

    # Méthode pour supprimer une réservation
    def delete_reservation(self, reservation):
        req = requests.delete(self.__url_base + '/reservation/' + reservation)
        print(req.status_code)
        print(req.content)

    # Méthode pour ajouter un utilisateur
    def post_utilisateur(self, utilisateur):
        json_body = utilisateur
        req = requests.post(self.__url_base + '/utilisateur', data=json_body, headers=self.__post_headers)
        print(req.status_code)
        print(req.content)

    # Méthode pour retourner les réservations en ordre croissant d'ID (NE FONCTIONNE PAS)
    def get_reservations_liste(self, liste_reservations_ord):
        req = requests.get(self.__url_base + '/liste_reservations/' + liste_reservations_ord)
        print(req.status_code)
        print(req.content)

    # Méthode pour ajouter un chalet
    def post_chalet(self, chalets):
        json_body = chalets
        req = requests.post(self.__url_base + '/chalets', data=json_body, headers=self.__post_headers)
        print(req.status_code)
        print(req.content)

    # Méthode pour retourner les informations sur un chalet
    def get_chalet(self, info_chalets):
        req = requests.get(self.__url_base + '/chalet/' + info_chalets)
        print(req.status_code)
        print(req.content)

    # Méthode pour créer une plage de disponinbilitées
    def post_plage(self, plage):
        json_body = plage
        req = requests.post(self.__url_base + '/plages', data=json_body, headers=self.__post_headers)
        print(req.status_code)
        print(req.content)

