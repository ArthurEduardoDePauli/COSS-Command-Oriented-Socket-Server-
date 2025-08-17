from os import system
import socket
import platform
from functions import colors,write_on_txt

CLEAR_COMMAND = 'cls' if platform.system() == 'Windows' else 'clear'

HOSTNAME = socket.gethostname()
IP = socket.gethostbyname(HOSTNAME)

HOST = '0.0.0.0'
PORT = 5000

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:

    server.bind((HOST,PORT))

    server.listen(1)

    write_on_txt('< Server ONLINE >','others/logs.txt')

    system(CLEAR_COMMAND)

    print(f'{colors["Green"]}<< Server avaliable! IP: {colors["Purple"]}{IP} {colors["Green"]}PORT: {colors["Purple"]}{PORT}{colors["Green"]} >>{colors["Close"]}')

    while 1:
        print(f'{colors["Cyan"]}<< Waiting for clients.. >>{colors["Close"]}')
        conn, addr = server.accept()

        with conn:
            write_on_txt(text=f'<< A client has connected to the server! IP: {addr[0]} PORT: {addr[1]} >>',path='others/logs.txt')

            print(f'{colors["Yellow"]}<< A client has connected to the server! {colors['Green']}IP: {colors["Yellow"]}{addr[0]} {colors["Green"]}PORT: {colors["Yellow"]}{addr[1]} >>{colors["Close"]}')

            while 1:
                try:
                    solicitation = conn.recv(1024).decode()
                except ConnectionResetError:
                    print(f'{colors["Red"]}<< The client abruptly disconnected from the server. IP: {addr[0]} PORT: {addr[1]} >>{colors["Close"]}')
                    write_on_txt(text=f'The client abruptly disconnected from the server. IP: {addr[0]} PORT: {addr[1]}',path='others/logs.txt')
                    break
                else:
                    if solicitation == 'exit':
                        write_on_txt(text=f'The client from IP "{addr[0]}" has been disconnected from the server.',path='others/logs.txt')
                        print(f'{colors['Red']}<< The client from IP "{addr[0]}" has been disconnected from the server. >>{colors['Close']}')
                        break
                    elif solicitation == 'hi':
                        print(f'{colors["Cyan"]}<< The client send hi :D >>{colors["Close"]}')                        
                    

    write_on_txt('< Server OFFLINE >','others/logs.txt')