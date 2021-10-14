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
        self.server.bind(("0.0.0.0", 8082))
        self.server.listen()
        print("Waiting for a connection")
        self.connection_socket, self.connection_address = self.server.accept()
        print("client connected")

    def run(self):
        while True:
            self.receive_message()

    def send_message(self):
        message = input("enter some message>>") + '\n'
        message = message.replace('\\n', '\n')
        data = message.encode()
        self.connection_socket.send(data)

    def receive_message(self):
        # recv takes integer which is maximum number of bytes
        data = self.connection_socket.recv(10)
        self.buffer = self.buffer + data.decode()
        terminate_pos = self.buffer.find('\n')
        print(terminate_pos)
        while terminate_pos > -1:
            message = self.buffer[:terminate_pos]
            self.buffer = self.buffer[terminate_pos+1:]
            print(message)
            terminate_pos = self.buffer.find('\n')


if __name__ == "__main__":
    try:
        my_server = Server()
        my_server.start()
        while True:
            my_server.send_message()
    except:
        try:
            my_server.close()
            print("server closed due to exception")
        except NameError:
            print("server is not even made")
