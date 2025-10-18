import socket
import threading
from sys import excepthook

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
name = input("Під яким іменем підключитись?")
client_socket.connect(("6.tcp.eu.ngrok.io", 19732))
client_socket.send(name.encode())

def send_message():
    while True:
        msg = input()

        if msg.lower() == "exit":
            client_socket.close()
            break
        client_socket.send(msg.encode())

threading.Thread(target=send_message).start()

while True:
    try:
        msg = client_socket.recv(1024).decode()
        if msg:
            print(msg)

    except:
        break


client_socket.close()



