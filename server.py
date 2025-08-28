from socket import *
import time

sock = socket(AF_INET, SOCK_STREAM)
sock.bind('localhost', 8080)

sock.listen(5)

players = {}

id_counter = 0

def handle_date():
    global id_counter 
    while True:
        time.sleep(0.01)
        player_data = {}
        to_remove = []

        
