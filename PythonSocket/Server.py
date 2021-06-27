import socket

def send_text(socket, text):
    text = text + '\n'
    data = text.encode()
    socket.send(data)

def get_text(receiving_socket):
    buffer = ""

    socket_open = True
    while socket_open:
        data = receiving_socket.recv(2)

        if not data:
            socket_open = False

        buffer = buffer + data.decode()

        terminator_pos = buffer.find('\n')
        while terminator_pos > -1:
            message = buffer[:terminator_pos]
            buffer = buffer[terminator_pos + 1:]
            yield message
            terminator_pos = buffer.find('\n')



# socket.AF_INET : IP socket, socket.SOCK_STREAM : TCP_IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# IP 0,0,0,0 indiates that the server is going to answer to any ip addresses. 8081 is a port number
server_socket.bind(("0.0.0.0", 8081))
server_socket.listen()
print("waiting for a connection")
connection_socket, address = server_socket.accept()
print("connected")
message = "Hello, Thanks for visiting"
data = message.encode()
print(data)
connection_socket.send(data)

# for answer in get_text(connection_socket):
#     print(answer)

answer = next(get_text(connection_socket))
print(answer)

# answer = connection_socket.recv(2)
# answer = answer.decode()
# print(answer)

server_socket.close()
connection_socket.close()