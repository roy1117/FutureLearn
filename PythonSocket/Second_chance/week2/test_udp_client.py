import socket
import time
SERVER_ADDRESS = ("127.0.0.1", 20001)
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('client is created')
message = input('type message to send>>')
udp_client.sendto(message.encode(), SERVER_ADDRESS)
time.sleep(20)
print('client is waiting for response')
data, client_address = udp_client.recvfrom(1024)
print(data.decode())