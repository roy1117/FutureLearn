import socket
import time

def send_text(socket, text):
    text = text + '\n'
    data = text.encode()
    socket.send(data)

def get_text(receiving_socket):
    buffer = ""

    socket_open = True
    while socket_open :
        data = receiving_socket.recv(2) # Receive data
        if not data :
            socket_open = False # Repeat until there is no more data

        buffer = buffer + data.decode() # Store it in Buffer

        terminator_pos = buffer.find('\n')
        while terminator_pos > -1: #if there is special 'mark' exists
            message = buffer[:terminator_pos] #Move string until the mark to message
            buffer = buffer[terminator_pos + 1:]
            yield message
            terminator_pos = buffer.find('\n')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8081))
client_socket.settimeout(5)
print("connected")

# for recv_text in get_text(client_socket):
#     print(recv_text)
message = client_socket.recv(1024)
print(message)
# print(message.decode())
# print('Got message')
# time.sleep(10)
# print('10 sec')
#
# answer1 = 'I received your \n message well, thanks'
# client_socket.send(answer1.encode())
# answer2 = 'This is second answer'
# send_text(client_socket, answer2)
#
print('closing')
client_socket.close()
