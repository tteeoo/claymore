from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from sys import argv
from .transmit import convert
from .server import server_init

def prompt(CLIENT):
    msg = input("> ")
    CLIENT.send(convert(msg, "hell"))
    prompt(CLIENT)

def main():
    CLIENT = socket(AF_INET, SOCK_STREAM)

    server_init()

    print("[CLIENT Thread] Waiting for connection...")

    while True:
        try:
            CLIENT.connect((argv[1], int(argv[2])))
            break
        except:
            pass

    print("[CLIENT Thread] Connected!")

    prompt(CLIENT)
