import socket
import time

my_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_client.connect(("192.168.35.73", 8181))
print("connected")
time.sleep(5)
data = my_client.recv(1024)
print(data.decode())