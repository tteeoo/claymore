from socket import socket, AF_INET, SOCK_STREAM, gethostbyname
from threading import Thread
from sys import argv, stderr, exit
from time import sleep

from .transmit import convert, hashpass
from .server import server_init

def prompt():
    global CLIENT
    msg = input("claymore> ")
    if msg != "":
        CLIENT.send(convert(msg, PASS))
    else:
        prompt()
    prompt()

def main():
    global PASS
    global CLIENT

    try:
        HOST, PORT = (argv[1].split(":"))
        PORT = int(PORT)
        ADDR = (HOST, PORT)
        PASS = hashpass(argv[2])
    except (IndexError, ValueError):
        print("[CLIENT Thread] Error: Invalid arguments", file=stderr)
        exit(1)

    CLIENT = socket(AF_INET, SOCK_STREAM)
    server_init(ADDR[1], PASS, gethostbyname(ADDR[0]))

    print("[CLIENT Thread] Waiting for connection...")
    while True:
        try:
            CLIENT.connect(ADDR)
            break
        except ConnectionRefusedError:
            pass
    print("[CLIENT Thread] Connected!")

    prompt()
