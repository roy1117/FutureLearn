import socket

my_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_server.bind(("0.0.0.0", 8181))
my_server.listen()
connection_socket, address = my_server.accept()
print("connected")
first_message = "first message"
second_message = "second message"
connection_socket.send(first_message.encode())
connection_socket.send(second_message.encode())
