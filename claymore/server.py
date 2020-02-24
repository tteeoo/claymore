from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

from .transmit import unconvert

def main_loop(SERVER):
    print("[SERVER Thread] Main loop started")
    client, client_address = SERVER.accept()
    while True:
        msg = client.recv(1024)
        print("[SERVER Thread] Recieved from {}: {}".format(client_address, unconvert(msg, "hell")))

def server_init(PORT):
    SERVER = socket(AF_INET, SOCK_STREAM)
    SERVER.bind(("", PORT))
    SERVER.listen(1)
    Thread(target=main_loop, args=(SERVER,)).start()

