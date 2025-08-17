from os import system
import socket
from time import sleep
from functions import colors
import platform

CLEAR_COMMAND = 'cls' if platform.system() == 'Windows' else 'clear'

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client:
    system(CLEAR_COMMAND)

    IP = input(f'{colors["Blue"]}SERVER IP: {colors["Close"]}')
    PORT = int(input(f'{colors["Blue"]}SERVER PORT: {colors["Close"]}'))

    system(CLEAR_COMMAND)

    try:
        client.connect((IP, PORT))
    except ConnectionRefusedError:
        print(f'{colors["Red"]}Connection refused. The server may be offline or not accepting connections.{colors["Close"]}')
        exit()
    except TimeoutError:
        print(f'{colors["Red"]}Connection timed out. Please check the server address and port.{colors["Close"]}')
        exit()
    except socket.gaierror:
        print(f'{colors["Red"]}Invalid server address.{colors["Close"]}')
        exit()
    except OSError as e:
        print(f'{colors["Red"]}OS error occurred: {e}{colors["Close"]}')
        exit()
    except Exception as e:
        print(f'{colors["Red"]}An unexpected error occurred: {e}{colors["Close"]}')
        exit()
    else:
        print(f'{colors["Green"]}WELCOME TO C.O.L.S{colors["Close"]}')

    while 1:
        command = input(f'{colors["Yellow"]}>>>{colors["Cyan"]}')
        if command == '':
            continue
        elif command == 'clr':
            system(CLEAR_COMMAND)
            continue
        elif command == 'exit':
            client.sendall(command.encode())
            exit()
        else:
            client.sendall(command.encode())