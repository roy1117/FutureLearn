import socket
from threading import Thread
import time

# socket.AF_INET means Internet Protocol version 4
# SOCK_STREAM is used to make TCP/IP socket
class Server(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.buffer = ''
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("127.0.0.1", 8082))

    def run(self):
        while True:
            self.server.listen()
            print("Waiting for a connection")
            connection_socket, connection_address = self.server.accept()
            print("client connected")
            for i in range(100):
                i = Thread(target=self.handler, args=(connection_socket,))
                i.daemon = False
                i.start()

    def send_message(self, connection_socket, message):
        message = message + '\n'
        message = message.replace('\\n', '\n')
        print('send back data : {0}'.format(message))
        data = message.encode()
        connection_socket.send(data)

    def receive_message(self, connection_socket):
        # recv takes integer which is maximum number of bytes
        data = connection_socket.recv(2000)
        self.buffer = self.buffer + data.decode()
        terminate_pos = self.buffer.find('\n')
        message = ''
        while terminate_pos > -1:
            message = self.buffer[:terminate_pos]
            self.buffer = self.buffer[terminate_pos+1:]
            terminate_pos = self.buffer.find('\n')
        self.send_message(connection_socket, message)

    def handler(self, connection_socket):
        while True:
            self.receive_message(connection_socket)


if __name__ == "__main__":
    try:
        my_server = Server()
        my_server.start()

    except NameError:
            print("server is not even made")
