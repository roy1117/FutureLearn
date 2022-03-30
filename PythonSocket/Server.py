import socket
import threading
import time

def send_text(socket, text):
    text = text + '\n'
    data = text.encode()
    socket.send(data)

def get_text(receiving_socket):
    buffer = ""

    socket_open = True
    while socket_open:
        data = receiving_socket.recv(1024) # Receive data

        if not data:
            socket_open = False # Repeat until there is no more data

        buffer = buffer + data.decode() # Store it in Buffer

        terminator_pos = buffer.find('\n')
        while terminator_pos > -1: #if there is special 'mark' exists
            message = buffer[:terminator_pos] #Move string until the mark to message
            buffer = buffer[terminator_pos + 1:]
            yield message
            terminator_pos = buffer.find('\n')


# Initial Stage
# socket.AF_INET : IP socket, socket.SOCK_STREAM : TCP_IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# IP 0,0,0,0 indiates that the server is going to answer to any ip addresses. 8081 is a port number
server_socket.bind(("0.0.0.0", 8081))
server_socket.listen()
print("waiting for a connection")
connection_socket, address = server_socket.accept()
print("connected")

# A sequence of research

# 1. Send message
# message1 = "Hello, Thanks for visiting1"
# send_text(connection_socket, message1)
# message2 = "Hello, Thanks for visiting2"
# send_text(connection_socket, message2)
#
# print('sent message')
t = threading.Thread(target = get_text(connection_socket))
t.start()
time.sleep(10)
message = 'Hello!'
connection_socket.send(message.encode())
print('sent message')
time.sleep(20)
# print('10 sec')
#
# # 2. get the message
# for answer in get_text(connection_socket):
#     print(answer)

# Closing Stage
print('closing')
server_socket.close()
connection_socket.close()