import socket
import pickle

SERVER_IP_ADDRESS = '127.0.0.1'
PORT = 2001

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP_ADDRESS, PORT))
print('connection is made with server')

data = client.recv(1024)
message = pickle.loads(data)
print(message)

if message[0] == 1:
    message = ('JOIN', )
    data = pickle.dumps(message)
    client.send(data)

data = client.recv(1024)
message = pickle.loads(data)
print(message)

data = client.recv(1024)
message = pickle.loads(data)
print(message)