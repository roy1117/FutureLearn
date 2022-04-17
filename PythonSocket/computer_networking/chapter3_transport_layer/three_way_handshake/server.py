import socket
import time
IP_ADDRESS = '127.0.0.1'
PORT = 7777

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP_ADDRESS, PORT))
server.listen()
connection_socket,_ = server.accept()