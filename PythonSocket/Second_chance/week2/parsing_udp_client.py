import socket
from platform import node, python_version_tuple
from time import time
import pickle

SERVER_ADDRESS = ("127.0.0.1", 20001)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('client is created')
current_time = time()
network_name = node()
python_version = python_version_tuple()
# data = str(current_time) + ','
# data = data + network_name + ','
# data = data + python_version[0] + ',' + python_version[1] + ',' + python_version[2]

# serialization
data = [current_time, network_name, python_version]
serialized_data = pickle.dumps(data)
client_socket.sendto(serialized_data, SERVER_ADDRESS)