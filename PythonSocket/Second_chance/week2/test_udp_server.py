import socket
import time
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(("0.0.0.0", 20001))
print("served is create")
print('server is waiting for a message to be arrived')
data, client_address = udp_server.recvfrom(1024)
print(data.decode())
response = input("type your response>>")
udp_server.sendto(response.encode(), client_address)
