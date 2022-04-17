import socket

IP_ADDRESS = '127.0.0.1'
PORT = 7777
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP_ADDRESS, PORT))
message = 'Hello, World'
client.send(message.encode())