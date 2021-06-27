import socket

def send_text(socket, text):
    text = text + '\n'
    data = text.encode()
    socket.send(data)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8081))
print("connected")
data = client_socket.recv(1024)
message = data.decode()
print(message)

answer1 = 'I received your \n message well, thanks'
send_text(client_socket, answer1)
answer2 = 'This is second answer'
send_text(client_socket, answer2)
client_socket.close()
