from socket import socket, AF_INET, SOCK_STREAM
from .transmit import unconvert
from threading import Thread
from sys import argv

def main_loop(SERVER):
    print("[SERVER Thread] Main loop started")
    client, client_address = SERVER.accept()
    while True:
        msg = client.recv(1024)
        print("[SERVER Thread] Recieved from {}: {}".format(client_address, unconvert(msg, "hell")))

def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

def server_init():
    HOST = ""
    PORT = int(argv[2])
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    SERVER = socket(AF_INET, SOCK_STREAM)
    SERVER.bind(ADDR)
    SERVER.listen(1)
    Thread(target=main_loop, args=(SERVER,)).start()

