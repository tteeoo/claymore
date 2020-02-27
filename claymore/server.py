from socket import socket, AF_INET, SOCK_STREAM, SO_REUSEADDR, SOL_SOCKET
from threading import Thread
from sys import exit, stderr

from .transmit import unconvert

def server_init(PORT, PASS, HOST):
    SERVER = socket(AF_INET, SOCK_STREAM)
    SERVER.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    try:
        SERVER.bind(("", PORT))
    except PermissionError:
        print("[SERVER Thread] Error: Invalid permissions (run as root)", file=stderr)
        exit(1)

    SERVER.listen(1)
    print("[SERVER Thread] Listening...")
    client, client_address = SERVER.accept()
    if client_address[0] != HOST:
        print("[SERVER Thread] Unauthorized host ({}) attempted to send data to this port".format(client_address[0]))
    else:
        while True:
            msg = unconvert(client.recv(1024), PASS)
            if msg == "/quit":
                print("[SERVER Thread] Remote host quit")
                exit(0)

            print("[SERVER Thread] Received from {}: {}".format(client_address[0], msg))

