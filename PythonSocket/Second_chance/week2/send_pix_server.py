import pickle
import socket
import time
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1', 20001))
print('waiting for a message')
counter = 0
while True:
    counter = counter + 1
    print(counter)
    time.sleep(1)
    message, _ = server_socket.recvfrom(1024)
    message = pickle.loads(message)
    print(message)
