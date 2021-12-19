import socket
import pickle

SERVER_IP_ADDRESS = '127.0.0.1'
PORT = 2001
NUMBER_OF_PARTICIPANT = 1

waiting_list = []
joined_list = []
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_IP_ADDRESS, PORT))
server.listen()
print('server has been created and now is listening for a client connection')

client_connection, _ = server.accept()
waiting_list.append(client_connection)
print('a client was connected')

message = (1, "You are successfully connected")
data = pickle.dumps(message)
client_connection.send(data)

data = client_connection.recv(1024)
message = pickle.loads(data)
print(message)

if message[0] == 'JOIN':
    waiting_list.remove(client_connection)
    joined_list.append(client_connection)
    message = (2, 'Welcome joining')
    data = pickle.dumps(message)
    client_connection.send(data)

    message = (11, 'the number of people needed to start : {0}, the number of current people: {1}'.format(NUMBER_OF_PARTICIPANT, len(joined_list)))
    data = pickle.dumps(message)
    client_connection.send(data)
