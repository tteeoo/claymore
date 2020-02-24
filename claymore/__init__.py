from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from sys import argv
from .transmit import convert
from .server import server_init

def prompt():
    global CLIENT
    msg = input("> ")
    CLIENT.send(convert(msg, PASS))
    prompt()

def main():
    try:
        argv[1]
    except NameError:
        print("Error: Invalid arguments")
        HOST, int(PORT) = input("Enter ip and port (colon seperated): ").split(":")
        PASS = input("Enter password: ")
    else:
        HOST, int(PORT) = argv[1].split(":")
        try:
            argv[2]
        except NameError:
            print("Error: Invalid arguments")
            PASS = input("Enter password: ")
        else:
            PASS = argv[2]

    CLIENT = socket(AF_INET, SOCK_STREAM)

    server_init(PORT)

    print("[CLIENT Thread] Waiting for connection...")

    while True:
        try:
            CLIENT.connect((HOST, PORT))
            break
        except:
            pass

    print("[CLIENT Thread] Connected!")

    prompt()
