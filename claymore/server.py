from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from sys import exit, stderr

from .transmit import unconvert

def main_loop(SERVER, PASS):
    print("[SERVER Thread] Main loop started")
    client, client_address = SERVER.accept()
    while True:
        msg = client.recv(1024)
        print("[SERVER Thread] Recieved from {}: {}".format(client_address, unconvert(msg, PASS)))

def server_init(PORT, PASS):
    SERVER = socket(AF_INET, SOCK_STREAM)
    try:
        SERVER.bind(("", PORT))
    except PermissionError:
        print("Error: Invalid permissions (run as root)", file=stderr)
        exit(1)

    SERVER.listen(1)
    Thread(target=main_loop, args=(SERVER,)).start()

