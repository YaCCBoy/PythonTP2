import json
from http.server import HTTPServer, BaseHTTPRequestHandler

class ReservationRequestHandler(BaseHTTPRequestHandler) : 
    
    def __init__(self) : 
        