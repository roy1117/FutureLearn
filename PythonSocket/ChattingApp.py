import socket


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
        while terminator_pos > -1: # if there is special 'mark' exists
            message = buffer[:terminator_pos] # Move string until the mark to message
            buffer = buffer[terminator_pos + 1:]
            yield message
            terminator_pos = buffer.find('\n')


while True:
    init_choice = input('choose service between 1.server 2.client')
    if init_choice == '1':
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # IP 0,0,0,0 indiates that the server is going to answer to any ip addresses. 8081 is a port number
        server_socket.bind(("0.0.0.0", 8081))
        server_socket.listen()
        print("A server socket is created, waiting for a connection")
        connection_socket, address = server_socket.accept()
        print("connected")
        continue
    elif init_choice == '2':
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_ip = input('Type server ip address')
        client_socket.connect((server_ip, 8081))
        print("connected")
        continue
    else:
        print('Entered wrong choice')

if init_choice == '1' :
    for message in get_text(connection_socket):
        print(message)
else :
    while True :
        message = input('type the message you want to send (type exit to quit)')
        if message == 'exit':
            continue
        else :
            send_text(client_socket, message)

try :
    server_socket.close()
    connection_socket.close()
    client_socket.close()
except :
    print('Finished abrupptly')

