import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8888))
server.listen()
connection_socket, _ = server.accept()
print('connected')
message = connection_socket.recv(81, socket.MSG_WAITALL)
print(message.decode())
