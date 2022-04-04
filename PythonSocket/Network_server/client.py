# echo_client.py

import socket, sys
import time

HOST, PORT = "127.0.0.1", 9999
data = "".join(sys.argv[1:])
print('data = %s' %data)

# create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # connect to server
    sock.connect((HOST, PORT))
    while True:
        # send data
        data = data +"\n"
        sock.sendall(data.encode(encoding='ascii'))

        # receive data back from the server
        received = str(sock.recv(1024).decode())
        time.sleep(1)
finally:
    # shut down
    sock.close()

print("Sent:     {}".format(data))
print("Received: {}".format(received))