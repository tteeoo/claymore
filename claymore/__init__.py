from socket import socket, AF_INET, SOCK_STREAM, gethostbyname
from threading import Thread
from sys import argv, stderr, exit
from time import sleep

from .transmit import convert, hashpass
from .server import server_init

def prompt():
    try:
        msg = input("claymore> ")
    except (KeyboardInterrupt, SystemExit):
        quit()
    if msg == "/quit":
        quit()
    elif msg != "":
        CLIENT.send(convert(msg, PASS))
    else:
        prompt()
    prompt()

def quit():
    CLIENT.send(convert("/quit", PASS))
    CLIENT.close()
    print("Quitting...")
    exit(0)

def main():
    global PASS
    global CLIENT

    try:
        if argv[1] == "-h" or argv[1] == "--help":
            print("""
Usage: claymore [<host>:<port> <password>] | [FLAG]

Flags:
    -V, --version: Displays version information

    -h, --help: Displays usage information
    
claymore must be ran as root

Repository hosted on GitHub: https://github.com/tteeoo/claymore
Copyright (c) 2020 Theo Henson, MIT License
""")
            exit(0)
        elif argv[1] == "-V" or argv[1] == "--version":
            print("""
                   \.          claymore 0.1.0
  -===============-{]###=<>    encrypted p2p chat client
                   /'          by Theo Henson      
""")
            exit(0)
        else:
            HOST, PORT = (argv[1].split(":"))
            PORT = int(PORT)
            ADDR = (HOST, PORT)
            PASS = hashpass(argv[2])
    except (IndexError, ValueError):
        print("Error: Invalid arguments, run \"claymore --help\" for usage", file=stderr)
        exit(1)

    CLIENT = socket(AF_INET, SOCK_STREAM)

    SERVER_THREAD = Thread(target=server_init,daemon=True,args=(ADDR[1], PASS, gethostbyname(ADDR[0]),))
    try:
        SERVER_THREAD.start()
    except (KeyboardInterrupt, SystemExit):
        quit()

    print("Waiting for connection...")
    while True:
        try:
            CLIENT.connect(ADDR)
            break
        except ConnectionRefusedError:
            pass
    print("Connected!")

    prompt()
