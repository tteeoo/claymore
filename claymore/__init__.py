from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from sys import argv, stderr
from time import sleep

from .transmit import convert, hashpass
from .server import server_init

def prompt():
    global CLIENT
    sleep(0.5)
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
        argv[1]
    except IndexError:
        print("Error: Invalid arguments", file=stderr)
        HOST, PORT = input("Enter ip and port (colon seperated): ").split(":")
        PORT = int(PORT)
        PASS = input("Enter password: ")
    else:
        HOST, PORT = argv[1].split(":")
        PORT = int(PORT)
        try:
            argv[2]
        except IndexError:
            print("Error: Invalid arguments", file=stderr)
            PASS = input("Enter password: ")
        else:
            PASS = argv[2]

    CLIENT = socket(AF_INET, SOCK_STREAM)

    PASS = hashpass(PASS)

    server_init(PORT, PASS)

    print("[CLIENT Thread] Waiting for connection...")

    while True:
        try:
            CLIENT.connect((HOST, PORT))
            break
        except ConnectionRefusedError:
            pass

    print("[CLIENT Thread] Connected!")

    prompt()
