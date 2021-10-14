import socket
import pickle

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("0.0.0.0", 20001))
print('server is created')
client_list = []
while True:
    print('waiting for a message')
    data = server_socket.recv(1024)
    deserialized_data = pickle.loads(data)
    # data_parts = data.split(",")
    # complete_data = [data_parts[0], data_parts[1], (data_parts[2],data_parts[3],data_parts[4])]
    client_list.append(deserialized_data)
    print(client_list)
