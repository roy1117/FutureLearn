import socket
import time

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(("127.0.0.1", 8000))
socket.listen()
connection_socket, address = socket.accept()
print("{0} is connected, read after 5 sec".format(address))
time.sleep(5)
message = connection_socket.recv(100)
message = message.decode()
print(message)