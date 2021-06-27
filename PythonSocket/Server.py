import socket
# socket.AF_INET : IP socket, socket.SOCK_STREAM : TCP_IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# IP 0,0,0,0 indiates that the server is going to answer to any ip addresses. 8081 is a port number
server_socket.bind(("0.0.0.0", 8081))
server_socket.listen()
print("waiting for a connection")
connection_socket, address = server_socket.accept()
print("connected")
