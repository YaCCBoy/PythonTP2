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

class TPBaseHTTPRequestHandler(BaseHTTPRequestHandler) :


    truc = Truc()

    def do_GET(self):
        path = self.path
        print(path)

        if path.startswith('/reservation/') :
            reservation = path.split('/')[2]
            content = 'Reservation : ' + reservation + '-> ' + str(self.truc.get_reservation[reservation])
            self.send_response(200)
            self.send_header()
            self.wfile.write(bytes(content, 'utf-8'))

        else :
            self.send_response(500, 'ERREUR')
            self.end_headers()

class ServeurTest:
    @staticmethod
    def run(serveur_class=HTTPServer, serveur_port=8000, handler_class=TPBaseHTTPRequestHandler):
        # le serveur va écouter sur localhost sur le port passé en paramètre
        serveur_adresse = ('localhost', serveur_port)
        # Les requêtes vont être gérées par handler_class passé en paramètre (notre class TPBaseHTTPRequestHandler
        # par défaut)
        httpd = serveur_class(serveur_adresse, handler_class)
        # Écoute pour des requêtes jusqu'à ce qu'on arrête le serveur
        httpd.serve_forever()


ServeurTest.run()