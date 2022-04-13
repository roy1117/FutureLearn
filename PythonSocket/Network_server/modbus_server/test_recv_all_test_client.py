import socket
import time
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8888))
message = 'Hello, world! Hello, world! Hello,'

message = message.encode()
client_socket.send(message)

time.sleep(1)

message = ' world! Hello, world! Hello, world! And the end'
message = message.encode()
client_socket.send(message)