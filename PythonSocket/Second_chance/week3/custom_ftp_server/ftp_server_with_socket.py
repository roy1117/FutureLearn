import socket

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 2122))
    print('server is created')
    server.listen()
    control_connection, _ = server.accept()
    print('control connection was made')
    message = '220 pyftpdlib based ftp ready\r\n'.encode(encoding='ascii')
    control_connection.send(message)
    user_name = control_connection.recv(1024)
    user_name = user_name.decode(encoding='ascii')
    print(user_name)
    if not user_name == 'USER edwards\r\n':
        print('user name is wrong')
        return
    message = '331 user name ok,send password\r\n'.encode(encoding='ascii')
    control_connection.send(message)
    password = control_connection.recv(1024)
    password = password.decode(encoding='ascii')
    print(password)

main()



